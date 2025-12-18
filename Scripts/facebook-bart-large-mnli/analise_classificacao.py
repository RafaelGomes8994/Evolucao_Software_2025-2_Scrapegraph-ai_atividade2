import os
from transformers import pipeline

# 1. Configuração de Caminhos
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

path_repo = os.path.join(raiz_projeto, "Scrapegraph-ai")
pasta_resultados = os.path.join(raiz_projeto, "Resultados")
arquivo_saida = os.path.join(pasta_resultados, "resultado_classificacao_BART.txt")

MODEL_NAME = "facebook/bart-large-mnli"

print(f"Carregando {MODEL_NAME}...")
classifier = pipeline("zero-shot-classification", model=MODEL_NAME)

# 2. Ler todos os arquivos .md
def ler_arquivos_combinados(caminho_repo):
    arquivos_md = []
    texto_combinado = ""
    
    # Buscar recursivamente todos os arquivos .md
    for root, dirs, files in os.walk(caminho_repo):
        for file in files:
            if file.endswith(".md"):
                arquivos_md.append(os.path.join(root, file))
    
    print(f"Encontrados {len(arquivos_md)} arquivos .md")
    
    for caminho in arquivos_md:
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()
                # Pegamos os primeiros 1000 chars de cada arquivo para ter variedade
                nome_relativo = os.path.relpath(caminho, caminho_repo)
                texto_combinado += f"--- Conteúdo de {nome_relativo} ---\n"
                texto_combinado += conteudo[:1500] + "\n\n"
        except Exception as e:
            print(f"Erro ao ler {caminho}: {e}")
                
    return texto_combinado

texto = ler_arquivos_combinados(path_repo)

# Truncagem de segurança (BART tem limite de tokens)
# Cortamos em 3000 caracteres para garantir que cabe um pouco de cada arquivo
if len(texto) > 3000:
    texto = texto[:3000]

if not texto:
    print("ERRO: Nenhum arquivo encontrado.")
    exit()

# 3. Análise
print("Analisando Governança (Branching e Release)...")

# Definição das classes
labels_branching = ["GitHub Flow", "Gitflow", "Trunk Based Development"]
labels_release = ["Rapid Releases", "Long Term Support (LTS)", "Release Train"]

# Execução
res_branch = classifier(texto, labels_branching)
res_release = classifier(texto, labels_release)

# 4. Salvar
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write(f"=== RESULTADO MODELO 1 (CLASSIFICACAO) ===\n")
    f.write(f"Arquivos analisados: Todos os arquivos .md encontrados no repositório\n\n")
    
    f.write(f"--- Branching Model ---\n")
    f.write(f"Vencedor: {res_branch['labels'][0]}\n")
    f.write(f"Score: {res_branch['scores'][0]:.4f}\n")
    f.write(f"2º Lugar: {res_branch['labels'][1]} ({res_branch['scores'][1]:.4f})\n\n")
    
    f.write(f"--- Release Strategy ---\n")
    f.write(f"Vencedor: {res_release['labels'][0]}\n")
    f.write(f"Score: {res_release['scores'][0]:.4f}\n")
    f.write(f"2º Lugar: {res_release['labels'][1]} ({res_release['scores'][1]:.4f})\n")

print(f"Sucesso! Salvo em: {arquivo_saida}")