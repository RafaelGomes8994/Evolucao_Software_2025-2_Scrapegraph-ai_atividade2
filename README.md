# 🚀 Evolução de Software - Análise de Governança de Software com LLMs

## .📋 Sumário

- [1. Sobre o Projeto](#-1-sobre-o-projeto)
- [2. Projeto Selecionado](#-2-projeto-selecionado--scrapegraph-ai)
- [3. Metodologia e Objetivos](#-3-metodologia-e-objetivos)
- [4. Identificação Manual da Arquitetura](#-4-identificação-manual-da-arquitetura)
- [5. Análise com Modelos de Linguagem](#-5-análise-com-modelos-de-linguagem)
- [6. Instalação e Execução](#-6-instalação-e-execução)
- [7. Configuração do Ambiente de Execução](#-7-Configuração-do-Ambiente-de-Execução)
- [8. Resultados e Discussão](#-8-resultados-e-discussão)
- [9. Conclusões](#-9-conclusões)

---

## 📌 1. Sobre o Projeto

Este repositório contém **toda a análise de governança** realizada pelo grupo sobre o projeto **Scrapegraph-ai**, incluindo:

* Identificação manual das estratégias de **Branching** e **Releases**.
* Análise automatizada utilizando **3 modelos de LLM** distintos.
* Comparação entre a auditoria humana e a inteligência artificial.
* Orquestração automatizada dos scripts de análise.

O objetivo central da atividade foi avaliar se modelos de IA conseguem identificar corretamente padrões de fluxo de trabalho (como *Gitflow* ou *GitHub Flow*) e frequência de lançamentos em documentações técnicas.

---

## 🧩 2. Projeto Selecionado – Scrapegraph-ai

O **Scrapegraph-ai** é uma biblioteca Python de *web scraping* que utiliza Grandes Modelos de Linguagem (LLMs) e lógica de grafos para criar pipelines de extração de dados flexíveis.

O projeto foi escolhido por possuir uma documentação rica (`CONTRIBUTING.md`, `CHANGELOG.md`) e um histórico ativo de lançamentos, sendo ideal para testar a capacidade de interpretação das IAs sobre regras de governança.

---

## 👥 Equipe

| Nome Completo | Matrícula | Contribuição na Atividade |
| :--- | :--- | :--- |
| Maria Eduarda M. da Silva | 202300038860 | Contextualização Teórica, Descrição da Metodologia, Teste, Tutorial e Revisão. |
| Rafael Gomes Oliveira Santos | 202300095730 | Validação Manual, Escolha dos LLMs e Implementação dos Scripts, Análise e Comparação dos Resultados |
| Cauan Teixeira Machado | 202300038627 | Análise do Modelo RoBERTa (QA) |
| Pedro Joaquim Silva Silveira | 202300038897 | Análise do Modelo RoBERTa (QA) |
| Breno Silva do Nascimento | 202300038968 | Análise do Modelo DistilBART (Sumarização) |
| José Gabriel R. G. de Almeida | 202300095599 | Análise do Modelo DistilBART (Sumarização) |
| José Victor Ribeiro de Jesus | 202300038799 | Análise do Modelo BART (Classificação) |
| Mateus da Silva Barreto | 202300038879 | Análise do Modelo BART (Classificação) |

**Estrutura de Trabalho:** O grupo atuou de forma colaborativa na auditoria manual e no desenvolvimento dos scripts de automação.

---

## 🎯 3. Metodologia e Objetivos

Nesta atividade, comparamos a análise humana (Auditoria Manual) com a análise automatizada por IAs para determinar:

1. **Branching Model (Fluxo de Trabalho):** Como o código é integrado? (Ex: Gitflow, GitHub Flow, Trunk-Based).
2. **Release Strategy (Estratégia de Lançamento):** Qual a frequência de lançamentos? (Ex: Rapid Releases, LTS, Release Train).

### A "Verdade" (Auditoria Manual)

Após auditoria nas abas *Branches* e *Releases* do repositório `Scrapegraph-ai`, a equipe identificou:
* **Branching:** **GitHub Flow** (Apenas branch `main` ativa e branches de feature temporárias; ausência de branch `develop`).
* **Releases:** **Rapid Releases** (Lançamentos semanais frequentes, ex: v1.66, v1.65).

### Os Modelos de IA Selecionados

Desenvolvemos scripts Python que utilizam a biblioteca `transformers` para ler arquivos de documentação (`CONTRIBUTING.md`, `CHANGELOG.md`, `README.md`).

* **Modelo 1: `facebook/bart-large-mnli` (Classificação Zero-Shot)**
    * *Estratégia:* Analisa o texto combinado do `CONTRIBUTING.md` e `CHANGELOG.md` para classificar o projeto em categorias pré-definidas.
* **Modelo 2: `deepset/roberta-base-squad2` (Question Answering)**
    * *Estratégia:* Realiza perguntas diretas ao texto (ex: "What is the main branch?") para extrair trechos específicos.
* **Modelo 3: `sshleifer/distilbart-cnn-12-6` (Sumarização)**
    * *Estratégia:* Gera um resumo textual focado em palavras-chave de governança, ignorando ruídos visuais (imagens/links).

---

## 🏗️ 4. Identificação Manual da Arquitetura

A análise manual (auditoria humana) concluiu que o Scrapegraph-ai segue:

### ✔ Branching Model: GitHub Flow

O projeto possui apenas a branch `main` como permanente e utiliza branches temporárias (ex: `pre/beta`) e Pull Requests diretos. Não há branch `develop` (característica do Gitflow).

### ✔ Release Strategy: Rapid Releases

O projeto realiza lançamentos frequentes (semanais ou quinzenais), focando sempre na versão atual ("Current") sem manter versões de Long Term Support (LTS).

Um documento completo com as evidências está na pasta `Validação-Manual/`.

---

## 🤖 5. Análise com Modelos de Linguagem

O projeto utilizou **3 abordagens de NLP** para tentar replicar a auditoria humana:

### 5.1 facebook/bart-large-mnli (Classificação Zero-Shot)

Utilizado para classificar o texto do projeto em categorias pré-definidas (*Gitflow* vs *GitHub Flow*, *LTS* vs *Rapid Releases*). Analisou o `CONTRIBUTING.md` e o `CHANGELOG.md`.

### 5.2 deepset/roberta-base-squad2 (Question Answering)

Modelo extrativo utilizado para responder perguntas pontuais, como "Qual é a branch principal?" e "Como contribuir?", buscando trechos exatos no texto.

### 5.3 sshleifer/distilbart-cnn-12-6 (Sumarização)

Modelo generativo utilizado para ler a documentação e criar um resumo focado nas regras de contribuição, ignorando ruídos visuais (badges e links).


```
.
├── Resultados/                  # Arquivos .txt com as saídas dos modelos
├── Validação-Manual/
├   └── validação-humana.md      # Documentação da auditoria manual
├── Scripts/                     # Códigos Python organizados por modelo
│   ├── deepset-roberta-base-squad2/
│   │   └── analise_qa.py
│   ├── facebook-bart-large-mnli/
│   │   └── analise_classificacao.py
│   └── sshleifer-distilbart-cnn-12-6/
│       └── analise_geracao.py
├── organizador.py               # Orquestrador principal
├── requirements.txt             # Dependências do Python
└── README.md                    # Este arquivo
```

---

## 🛠️ 6. Instalação e Execução

### Pré-requisitos
* Python 3.10 ou superior
* Git

### Passo a Passo

1. **Clone este repositório da atividade:**
    ```bash
    git clone https://github.com/RafaelGomes8994/Evolucao_Software_2025-2_Scrapegraph-ai_atividade2.git

    cd Evolucao_Software_2025-2_Scrapegraph-ai_atividade2
    ```

2. **Crie e Configure o Ambiente Virtual (venv):**
    ```bash
    # Cria o ambiente virtual
    python -m venv venv

    # Ativa o ambiente:
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
    ```

3. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    Dependências incluem: `transformers`, `torch`, `scipy`.

4. **Execute o Orquestrador:**
    ```bash
    python organizador.py
    ```
    Não é necessário rodar os scripts individualmente. O orquestrador executará o pipeline completo e os resultados serão gerados sequencialmente na pasta `Resultados/`.
   Ao final da execução, será exibida no terminal uma mensagem semelhante a:

```bash
✅ Sucesso: Modelo 3: DistilBART (Sumarização) finalizado.

🎉 TODAS AS ANÁLISES FORAM CONCLUÍDAS!
Verifique a pasta 'Resultados/' para ver os relatórios.
```

5. **Visualização dos resultados**

Após a conclusão do processo acesse a pasta Resultados/, criada automaticamente na raiz do projeto. Nessa pasta estarão disponíveis os arquivos gerados por cada etapa do pipeline, incluindo:
* Relatórios textuais
* Resultados das análises
* Saídas dos modelos de NLP (classificação, análise de sentimentos e sumarização)

> Os arquivos podem ser abertos em qualquer editor de texto ou IDE (por exemplo, VS Code, PyCharm ou Bloco de Notas).

---

## 7. 💻 Configuração do Ambiente de Execução

Os testes e a execução dos modelos de linguagem foram realizados em uma máquina local com as seguintes especificações. Esta documentação é relevante para justificar o tempo de inferência e a escolha de modelos otimizados (como versões `distil` ou `base`) em detrimento de modelos maiores.

| Componente | Especificação Utilizada |
| :--- | :--- |
| **Sistema Operacional** | Windows 10/11 (64-bit) |
| **Linguagem** | Python 3.10+ |
| **Processador (CPU)** | Ryzen 5 3400 G  |
| **Memória RAM** | 24 GB DDR4 3200 Mhz |
| **Aceleração (GPU)** | Veneida RX580 8 GB DDR5 AMD |
| **Bibliotecas Chave** | `transformers`, `torch`, `scipy` |


## 📊 8. Resultados e Discussão

### 8.1 Resultados: BART MNLI (Classificação)

* **Branching:** Com a expansão do contexto para todos os arquivos `.md`, o modelo refinou sua previsão e identificou corretamente o **GitHub Flow** (Score: 0.37), superando o *Trunk Based Development*.
* **Releases:** Manteve a confusão ao ler o `CHANGELOG.md`. A lista extensa de versões passadas fez o modelo classificar erroneamente como **LTS (Long Term Support)**.

### 8.2 Resultados: RoBERTa (QA)

O modelo conseguiu extrair o nome da branch de desenvolvimento **`pre/beta`**, provando que é capaz de encontrar entidades no texto. No entanto, falhou em entender o contexto global da estratégia, não conseguindo responder perguntas subjetivas sobre o processo de release.

### 8.3 Resultados: DistilBART (Sumarização)

Foi o modelo mais perspicaz tecnicamente. Além de validar o fluxo de PRs, ele encontrou a menção crítica: *"follow Conventional Commits format for **semantic-release compatibility**"*.
Isso é a "prova técnica" de que o projeto usa lançamentos automatizados (**Rapid Releases**), algo que o modelo de classificação não conseguiu deduzir.

### Tabela Comparativa

| Modelo | Tarefa NLP | Branching Identificado | Estratégia Release Identificada | Análise da Equipe |
| :--- | :--- | :--- | :--- | :--- |
| **BART-Large-MNLI** | Classificação | **GitHub Flow** (Score: 0.37) | **Long Term Support - LTS** (Score: 0.37) | **Alta Precisão no Fluxo.** Ao ler todos os arquivos de documentação, o modelo corrigiu sua previsão anterior e alinhou-se 100% com a auditoria manual (GitHub Flow). Porém, insistiu no erro de LTS para releases. |
| **RoBERTa-SQuAD2** | QA (Extração) | Branch **`pre/beta`** | Inconclusivo | **Média.** Útil para extrair nomes de branches específicas, mas sem capacidade de generalização sobre a estratégia. |
| **DistilBART-CNN** | Sumarização | **"Push & open a PR to the pre-beta branch"** | Identificou **"Semantic-Release Compatibility"** | **Excelente (Insight Técnico).** O modelo encontrou a menção à ferramenta *Semantic Release*. Isso valida tecnicamente a estratégia de **Rapid Releases** (automação de versões) via evidência textual direta. |

### Principais Descobertas

1. **A Vitória da Classificação (BART):** A estratégia de expandir o contexto para "todos os arquivos .md" foi decisiva para o modelo BART migrar de *Trunk Based* para **GitHub Flow**. Isso sugere que as regras de branch estavam dispersas em arquivos menores de documentação, e não apenas no CONTRIBUTING.md.

2. **O "Detetive" DistilBART:** Enquanto o BART tentou adivinhar a categoria (e errou dizendo LTS), o modelo generativo encontrou a evidência técnica: o uso de **Semantic Release**. Isso mostra que modelos generativos são melhores para auditoria técnica profunda, pois encontram as ferramentas que justificam a governança.

---

## 📌 9. Conclusões

A combinação das análises permitiu concluir que:

✅ **O Scrapegraph-ai adota GitHub Flow e Rapid Releases.**

✅ **Limitações e Forças dos Modelos:**

* **Classificação (BART):** Excelente para identificar o fluxo de trabalho quando alimentado com o contexto completo, mas suscetível a "ruídos" de dados históricos (confundindo histórico longo com suporte LTS).
* **Sumarização (DistilBART):** Superou os outros ao identificar ferramentas específicas (*Semantic Release*, *Conventional Commits*), provando ser a abordagem mais robusta para entender *como* a governança é implementada tecnicamente, e não apenas qual rótulo ela recebe.
