import os
from transformers import pipeline

# 1. Configuração de Caminhos
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
path_repo = os.path.join(raiz_projeto, 'Scrapegraph-ai')
pasta_resultados = os.path.join(raiz_projeto, 'Resultados')
arquivo_saida = os.path.join(pasta_resultados, 'resultado_qa_RoBERTa.txt')

MODEL_NAME = 'deepset/roberta-base-squad2'

print(f'Carregando {MODEL_NAME}...')
qa_pipeline = pipeline('question-answering', model=MODEL_NAME)

# 2. Ler contexto
arquivo_contributing = os.path.join(path_repo, 'CONTRIBUTING.md')
arquivo_changelog = os.path.join(path_repo, 'CHANGELOG.md')

contexto = ''

for arquivo in [arquivo_contributing, arquivo_changelog]:
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            contexto += f'\n\n===== {os.path.basename(arquivo)} =====\n\n'
            contexto += f.read()

if not contexto.strip():
    print('ERRO: Documentação não encontrada.')
    exit()

def dividir_texto(texto, tamanho=400):
    palavras = texto.split()
    return [
        ' '.join(palavras[i:i + tamanho])
        for i in range(0, len(palavras), tamanho)
    ]

chunks = dividir_texto(contexto)

def responder_qa(pergunta, chunks, pipeline):
    melhor = {'answer': '', 'score': 0.0}

    for c in chunks:
        res = pipeline(question=pergunta, context=c)
        if res['score'] > melhor['score']:
            melhor = res

    return melhor

perguntas = [
    'What is the main branch name?',
    'How do I submit a contribution?',
    'Is there a release schedule?'
]

# 3. Salvar
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

with open(arquivo_saida, 'w', encoding='utf-8') as f:
    f.write('=== RESULTADO MODELO 2 (QA) ===\n')
    f.write(f'Contexto: CONTRIBUTING.md + CHANGELOG.md\n\n')

    for p in perguntas:
        print(f'Perguntando: {p}...')
        res = responder_qa(p, chunks, qa_pipeline)

        f.write(f'P: {p}\n')
        f.write(f'R: {res["answer"]}\n')
        f.write(f'Score: {res["score"]:.4f}\n')
        f.write('-' * 30 + '\n')

print(f'Sucesso! Salvo em: {arquivo_saida}')
