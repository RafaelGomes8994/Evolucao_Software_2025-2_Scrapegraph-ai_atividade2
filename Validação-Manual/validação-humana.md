# 🕵️‍♂️ Auditoria Manual de Governança

**Data da Análise:** 18/12/2025
**Responsáveis:** Equipe do Projeto

## 1. Branching Model (Fluxo de Trabalho)
**Veredito:** GitHub Flow

**Evidências:**
1.  Ao analisar a aba "Branches" no GitHub, constatamos apenas a existência da branch `main` (default) e uma branch `pre/beta`.
2.  Não existe branch `develop` ou branches de `release/x.y`, o que descarta o Gitflow.
3.  O fluxo de contribuição descrito no `CONTRIBUTING.md` foca em Pull Requests diretos.

## 2. Release Strategy (Estratégia de Lançamento)
**Veredito:** Rapid Releases

**Evidências:**
1.  Na aba "Releases/Tags", o projeto apresenta lançamentos frequentes (ex: v1.66.0 há 4 dias, v1.65.0 há uma semana).
2.  Não há menção a versões LTS (Long Term Support) com suporte estendido de anos. O foco é estar sempre na versão mais recente ("Current").