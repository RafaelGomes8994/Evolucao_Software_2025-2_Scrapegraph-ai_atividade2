# 🚀 Atividade 2: Análise de Governança e Fluxo de Trabalho com LLMs

**Repositório da Atividade:** `Evolucao_Software_2025-2_Scrapegraph-ai_atividade2`
**Projeto Alvo:** `Scrapegraph-ai` (Mesmo da Atividade 1)

Esta atividade foca na identificação da **Governança do Projeto**, especificamente:
1.  **Modelo de Fluxo de Trabalho (Branching Model):** O "sistema circulatório" (como o código é organizado).
2.  **Estratégia de Releases (Release Strategy):** O "ritmo cardíaco" (como e quando o software é entregue).

---

## 👥 Componentes da Equipe

| Nome | Matrícula | Contribuição na Atividade 2 |
| :--- | :--- | :--- |
| Maria Eduarda M. da Silva | 202300038860 | Validação Manual da Governança e Relatório |
| Rafael Gomes Oliveira Santos | 202300095730 | Validação Manual e Edição de Vídeo |
| Cauan Teixeira Machado | 202300038627 | Script e Análise com Modelo 1 (BART - Classificação) |
| Pedro Joaquim Silva Silveira | 202300038897 | Script e Análise com Modelo 1 (BART - Classificação) |
| Breno Silva do Nascimento | 202300038968 | Script e Análise com Modelo 2 (RoBERTa - QA) |
| José Gabriel R. G. de Almeida | 202300095599 | Script e Análise com Modelo 2 (RoBERTa - QA) |
| José Victor Ribeiro de Jesus | 202300038799 | Script e Análise com Modelo 3 (Flan-T5 - Geração) |
| Mateus da Silva Barreto | 202300038879 | Script e Análise com Modelo 3 (Flan-T5 - Geração) |

---

## 🎯 1. Objetivo e Metodologia

O objetivo desta etapa foi utilizar **Inteligência Artificial (Processamento de Linguagem Natural)** para ler a documentação do projeto (`CONTRIBUTING.md`, `README.md`) e inferir automaticamente suas estratégias de governança.

### 1.1. A "Verdade" Manual (Gabarito)
Antes de executar as IAs, realizamos uma auditoria manual no repositório para estabelecer a verdade:
* **Branching Model:** Identificamos como **GitHub Flow**. O projeto utiliza uma branch `main` estável e recebe contribuições via Pull Requests diretos. Não existe branch `develop` (característica do Gitflow).
* **Estratégia de Releases:** Identificamos como **Rapid Releases**. O projeto utiliza Semantic Versioning (v0.x.x) com lançamentos frequentes baseados em features, sem janelas de suporte de longo prazo (LTS) explícitas.

### 1.2. Modelos de IA Selecionados (Hugging Face)
Selecionamos 3 modelos distintos, focados em interpretação de texto, para validar se eles conseguiam chegar à mesma conclusão que nós:

1.  **`facebook/bart-large-mnli` (Zero-Shot Classification):**
    * *Estratégia:* Classificar o texto em categorias pré-definidas (ex: "Gitflow" vs "GitHub Flow") sem treinamento prévio.
2.  **`deepset/roberta-base-squad2` (Question Answering):**
    * *Estratégia:* "Entrevistar" a documentação fazendo perguntas específicas (ex: "Qual é a branch principal?").
3.  **`google/flan-t5-large` (Text2Text Generation):**
    * *Estratégia:* Pedir para a IA ler o arquivo de contribuição e gerar um resumo explicativo sobre o processo.

---

## 🛠️ 2. Tutorial de Execução

### 2.1. Estrutura de Pastas
A estrutura do projeto para esta atividade é a seguinte:
. ├── reports/ # Logs de execução e resultados (.txt) │ ├── resultado_classificacao_BART.txt │ ├── resultado_qa_RoBERTa.txt │ └── resultado_geracao_FlanT5.txt │ ├── scripts/ # Scripts Python desenvolvidos pela equipe │ ├── analise_classificacao.py (Modelo 1) │ ├── analise_qa.py (Modelo 2) │ └── analise_geracao.py (Modelo 3) │ ├── Scrapegraph-ai/ # O repositório alvo (apenas documentação necessária) ├── venv/ # Ambiente Virtual │ ├── README.md # Este documento └── requirements.txt # Dependências (transformers, torch, etc.)


### 2.2. Instalação e Configuração

1.  **Clone este repositório** e navegue para a pasta raiz.
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### 2.3. Execução dos Scripts

Execute os scripts a partir da raiz do projeto para gerar os relatórios na pasta `reports/`:

* **Modelo 1 (Classificação):**
    ```bash
    python scripts/analise_classificacao.py
    ```
* **Modelo 2 (Perguntas e Respostas):**
    ```bash
    python scripts/analise_qa.py
    ```
* **Modelo 3 (Geração de Resumo):**
    ```bash
    python scripts/analise_geracao.py
    ```

---

## 📊 3. Resultados e Comparação

Abaixo apresentamos a comparação entre o que os modelos encontraram e a realidade do projeto.

| Modelo | Tarefa NLP | Branching Identificado | Estratégia Release Identificada | Efetividade |
| :--- | :--- | :--- | :--- | :--- |
| **`facebook/bart-large-mnli`** | Classificação (Zero-Shot) | **GitHub Flow** (Score Alto) | **Rapid Releases** (Score Médio) | **Alta** (Vencedor) |
| **`deepset/roberta-base-squad2`** | Question Answering | Identificou "main branch" e "pull requests". | Inconclusivo (Respostas vagas). | **Média** |
| **`google/flan-t5-large`** | Text Generation | Resumiu o uso de PRs corretamente. | Mencionou versionamento semântico. | **Alta** |

### 3.1. Análise Detalhada e Justificativa

* **Vencedor (Mais Efetivo): `facebook/bart-large-mnli`**
    * **Justificativa:** Para identificar governança, muitas vezes precisamos classificar o projeto em "caixas" conceituais (ex: é Gitflow ou não?). O modelo Zero-Shot foi capaz de ler o texto ambíguo do `CONTRIBUTING.md` e atribuir corretamente a probabilidade mais alta para **GitHub Flow** e **Rapid Releases**, alinhando-se perfeitamente com nossa análise manual.

* **O Papel do `roberta-base-squad2`:**
    * Embora não tenha dado o "nome" da estratégia, ele foi excelente para extrair fatos. Quando perguntado *"What is the main branch?"*, ele respondeu corretamente `main` (e não `master` ou `develop`), o que ajudou a descartar o Gitflow.

* **O Papel do `flan-t5-large`:**
    * Gerou um resumo textual que confirmou o entendimento, explicando que "developers should submit changes via Pull Requests", reforçando o modelo de colaboração distribuída.

---

## 🔗 4. Links da Atividade

* **Tutorial em PDF:** [Link para o PDF no Google Drive/Classroom]
* **Vídeo de Relato (YouTube):** [Link para o Vídeo]

## 🖥️ 5. Infraestrutura Utilizada

* **Ambiente:** Execução Local
* **CPU:** [PREENCHA AQUI]
* **RAM:** [PREENCHA AQUI]
* **Python:** 3.10
