import os
from transformers import pipeline, AutoTokenizer

# Configuração
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
path_repo = os.path.join(raiz_projeto, "Scrapegraph-ai")
pasta_resultados = os.path.join(raiz_projeto, "Resultados")
arquivo_saida = os.path.join(pasta_resultados, "resultado_geracao_DistilBART.txt")

# Modelo de Resumo (Notícias/Fatos)
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

print(f"Carregando {MODEL_NAME}...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    summarizer = pipeline("summarization", model=MODEL_NAME, tokenizer=tokenizer)
except Exception as e:
    print(f"Erro ao carregar: {e}")
    exit()

def limpar_ruido(texto):
    # Remove linhas de links e badges que atrapalham a IA
    linhas = [linha.strip() for linha in texto.split('\n')]
    return "\n".join([l for l in linhas if "http" not in l and len(l) > 20])

def carregar_contexto(caminho_repo):
    # Busca todos os arquivos .md recursivamente
    texto_full = ""
    arquivos_md = []
    
    for root, dirs, files in os.walk(caminho_repo):
        for file in files:
            if file.endswith(".md"):
                arquivos_md.append(os.path.join(root, file))
    
    print(f"Encontrados {len(arquivos_md)} arquivos .md")
    
    # Lê todos os arquivos encontrados
    for caminho in arquivos_md:
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                texto_full += f.read() + "\n"
        except Exception as e:
            print(f"Erro ao ler {caminho}: {e}")
    
    # Limpa e filtra parágrafos sobre releases/branches
    texto_limpo = limpar_ruido(texto_full)
    palavras_chave = ["branch", "main", "release", "version", "pull request", "workflow"]
    relevantes = [p for p in texto_limpo.split('\n') if any(k in p.lower() for k in palavras_chave)]
    
    return "\n".join(relevantes)[:3000] # Limite seguro

contexto = carregar_contexto(path_repo)
print("Gerando resumo...")

if contexto:
    # Gera o resumo
    res = summarizer(contexto, max_length=150, min_length=40, do_sample=False)
    texto_gerado = res[0]['summary_text']
    
    # Salva
    if not os.path.exists(pasta_resultados): os.makedirs(pasta_resultados)
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(f"=== RESUMO MODELO 3 ({MODEL_NAME}) ===\n\n{texto_gerado}")
    print("Sucesso!")
else:
    print("Erro: Contexto vazio.")