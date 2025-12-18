import os
from transformers import pipeline

# 1. Configuração de Caminhos
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
path_repo = os.path.join(raiz_projeto, "Scrapegraph-ai")
pasta_resultados = os.path.join(raiz_projeto, "Resultados")
arquivo_saida = os.path.join(pasta_resultados, "resultado_qa_RoBERTa.txt")

MODEL_NAME = "deepset/roberta-base-squad2"

print(f"Carregando {MODEL_NAME}...")
qa_pipeline = pipeline('question-answering', model=MODEL_NAME)

# 2. Ler contexto
arquivo_alvo = os.path.join(path_repo, "CONTRIBUTING.md", "CHANGELOG.md")
if not os.path.exists(arquivo_alvo):
    arquivo_alvo = os.path.join(path_repo, "README.md")

try:
    with open(arquivo_alvo, "r", encoding="utf-8") as f:
        contexto = f.read()
except FileNotFoundError:
    print("ERRO: Documentação não encontrada.")
    exit()

perguntas = [
    "What is the main branch name?",
    "How do I submit a contribution?",
    "Is there a release schedule?"
]

# 3. Salvar
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write(f"=== RESULTADO MODELO 2 (QA) ===\n")
    f.write(f"Contexto: {arquivo_alvo}\n\n")
    
    for p in perguntas:
        print(f"Perguntando: {p}...")
        res = qa_pipeline(question=p, context=contexto)
        
        f.write(f"P: {p}\n")
        f.write(f"R: {res['answer']}\n")
        f.write(f"Score: {res['score']:.4f}\n")
        f.write("-" * 30 + "\n")

print(f"Sucesso! Salvo em: {arquivo_saida}")