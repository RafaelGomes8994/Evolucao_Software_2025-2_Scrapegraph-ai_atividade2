# 🚀 Atividade 2: Análise de Governança de Software com LLMs

**Projeto Alvo:** `Scrapegraph-ai`
**Disciplina:** Evolução de Software (2025.2)

Este repositório contém os artefatos e a automação desenvolvida para a análise de **Governança de Projetos Open Source** utilizando Inteligência Artificial. O objetivo é identificar automaticamente, através de Modelos de Linguagem (LLMs), as regras de contribuição e lançamento de versões do projeto.

---

## 👥 Equipe

| Nome Completo | Matrícula | Contribuição na Atividade |
| :--- | :--- | :--- |
| Maria Eduarda M. da Silva | 202300038860 | |
| Rafael Gomes Oliveira Santos | 202300095730 | |
| Cauan Teixeira Machado | 202300038627 | |
| Pedro Joaquim Silva Silveira | 202300038897 | |
| Breno Silva do Nascimento | 202300038968 | |
| José Gabriel R. G. de Almeida | 202300095599 | |
| José Victor Ribeiro de Jesus | 202300038799 | |
| Mateus da Silva Barreto | 202300038879 | |

---

## 🎯 Metodologia e Objetivos

Nesta atividade, comparamos a análise humana (Auditoria Manual) com a análise automatizada por IAs para determinar:
1.  **Branching Model (Fluxo de Trabalho):** Como o código é integrado? (Ex: Gitflow, GitHub Flow, Trunk-Based).
2.  **Release Strategy (Estratégia de Lançamento):** Qual a frequência de lançamentos? (Ex: Rapid Releases, LTS, Release Train).

### 1. A "Verdade" (Auditoria Manual)
Após auditoria nas abas *Branches* e *Releases* do repositório `Scrapegraph-ai`, a equipe identificou:
* **Branching:** **GitHub Flow** (Apenas branch `main` ativa e branches de feature temporárias; ausência de branch `develop`).
* **Releases:** **Rapid Releases** (Lançamentos semanais frequentes, ex: v1.66, v1.65).

### 2. Os Modelos de IA Selecionados
Desenvolvemos scripts Python que utilizam a biblioteca `transformers` para ler arquivos de documentação (`CONTRIBUTING.md`, `CHANGELOG.md`, `README.md`).

* **Modelo 1: `facebook/bart-large-mnli` (Classificação Zero-Shot)**
    * *Estratégia:* Analisa o texto combinado do `CONTRIBUTING.md` e `CHANGELOG.md` para classificar o projeto em categorias pré-definidas.
* **Modelo 2: `deepset/roberta-base-squad2` (Question Answering)**
    * *Estratégia:* Realiza perguntas diretas ao texto (ex: "What is the main branch?") para extrair trechos específicos.
* **Modelo 3: (Modelo Generativo)**
    * *Estratégia:* Geração de resumo textual focado em governança.

---

## 🛠️ Instalação e Execução

### Pré-requisitos
* Python 3.10 ou superior
* Git

### Passo a Passo

1.  **Clone este repositório da atividade:**
    ```bash
    git clone https://github.com/RafaelGomes8994/Evolucao_Software_2025-2_Scrapegraph-ai_atividade2.git

    cd Evolucao_Software_2025-2_Scrapegraph-ai_atividade2
    ```

2.  **Clone o projeto alvo (Scrapegraph-ai) na raiz:**
    É necessário ter o código do projeto alvo para que os scripts possam ler a documentação.
    ```bash
    git clone https://github.com/ScrapeGraphAI/Scrapegraph-ai.git
    ```

3.  **Crie e Configure o Ambiente Virtual (venv):**
    Isso isola as dependências do projeto para evitar conflitos no seu sistema.
    ```bash
    # Cria o ambiente virtual chamado 'venv'
    python -m venv venv

    # Ativa o ambiente:
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
    ```

4.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute os Scripts de Análise:**
    Os resultados serão gerados na pasta `Resultados/`.

    ```bash
    # Modelo 1: Classificação (BART)
    python Scripts/facebook-bart-large-mnli/analise_classificacao.py

    # Modelo 2: Perguntas e Respostas (RoBERTa)
    python Scripts/deepset-roberta-base-squad2/analise_qa.py

    # Modelo 3: Geração de Texto
    python Scripts/google-flan-t5-large/analise_geracao.py
    ```

---

## 📊 Resultados e Discussão

| Modelo | Tarefa NLP | Branching Identificado | Estratégia Release Identificada | Análise da Equipe |
| :--- | :--- | :--- | :--- | :--- |
| **BART-Large-MNLI** | Classificação | **Trunk Based Development** (Score: 0.38) | **Long Term Support - LTS** (Score: 0.43) | **Parcialmente Correto.** O modelo acertou o fluxo ágil (Trunk Based ≈ GitHub Flow), mas a inclusão do `CHANGELOG.md` (com histórico antigo) confundiu o modelo, levando-o a classificar erroneamente como LTS. |
| **RoBERTa-SQuAD2** | QA (Extração) | Branch **`pre/beta`** | Inconclusivo | **Média.** O modelo foi eficaz em encontrar nomes de branches existentes no texto, mas falhou em interpretar o contexto global da estratégia. |
| **Modelo 3** | Geração | *Aguardando Definição* | *Aguardando Definição* | *Análise Pendente* |

### Principais Descobertas
1.  **O Efeito do Changelog no BART:** Ao adicionarmos o histórico de versões (`CHANGELOG.md`) ao contexto do BART, o modelo mudou sua classificação de *Rapid Releases* para *LTS*. Isso indica que o modelo interpretou a longa lista de versões passadas como um sinal de suporte estendido, ignorando a frequência semanal das datas.
2.  **Limitações de Modelos Extrativos (QA):** O modelo RoBERTa conseguiu identificar a existência da branch `pre/beta`, validando sua capacidade de extração, mas não conseguiu deduzir que a ausência de uma branch `develop` implicava no GitHub Flow.

---

## 📂 Estrutura do Projeto
```
.
├── Resultados/                  # Arquivos .txt com as saídas dos modelos
├── Scripts/                     # Códigos Python organizados por modelo
│   ├── deepset-roberta-base-squad2/
│   ├── facebook-bart-large-mnli/
│   └── [pasta_modelo_3]/
├── requirements.txt             # Dependências do Python
└── README.md                    # Este arquivo
```