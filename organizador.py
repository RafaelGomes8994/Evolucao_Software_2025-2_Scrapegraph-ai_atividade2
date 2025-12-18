import subprocess
import os
import sys

# Configuração de Cores para o Terminal ficarem bonitos
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def rodar_script(caminho_script, nome_modelo):
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{YELLOW}🚀 Iniciando Pipeline: {nome_modelo}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}")
    
    if not os.path.exists(caminho_script):
        print(f"❌ Erro: Script não encontrado em {caminho_script}")
        return

    # Executa o script python usando o mesmo ambiente virtual atual
    try:
        resultado = subprocess.run([sys.executable, caminho_script], check=True)
        if resultado.returncode == 0:
            print(f"{GREEN}✅ Sucesso: {nome_modelo} finalizado.{RESET}")
        else:
            print(f"❌ Erro ao rodar {nome_modelo}")
    except Exception as e:
        print(f"❌ Falha crítica na execução: {e}")

def main():
    print(f"{GREEN}🤖 INICIANDO ORGANIZADOR DE ANÁLISE {RESET}")
    
    # Lista dos seus scripts (Ajuste se os nomes das pastas forem diferentes)
    scripts = [
        {
            "nome": "Modelo 1: BART (Classificação)",
            "path": os.path.join("Scripts", "facebook-bart-large-mnli", "analise_classificacao.py")
        },
        {
            "nome": "Modelo 2: RoBERTa (QA)",
            "path": os.path.join("Scripts", "deepset-roberta-base-squad2", "analise_qa.py")
        },
        {
            "nome": "Modelo 3: DistilBART (Sumarização)",
            # Atenção: Certifique-se que o nome da pasta aqui é o que você criou
            "path": os.path.join("Scripts", "sshleifer-distilbart-cnn-12-6", "analise_geracao.py")
        }
    ]

    for item in scripts:
        rodar_script(item["path"], item["nome"])

    print(f"\n{CYAN}🎉 TODAS AS ANÁLISES FORAM CONCLUÍDAS!{RESET}")
    print(f"Verifique a pasta {YELLOW}'Resultados/'{RESET} para ver os relatórios.")

if __name__ == "__main__":
    main()