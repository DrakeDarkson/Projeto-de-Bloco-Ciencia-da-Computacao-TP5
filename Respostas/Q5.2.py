import subprocess
import sys

def varredura_nmap(host):
    try:
        resultado = subprocess.run(["nmap", "-sV", host], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except FileNotFoundError:
        print("Erro: O Nmap não está instalado. Instale-o e tente novamente.")
    except subprocess.CalledProcessError:
        print("Erro ao executar o Nmap.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <IP ou domínio>")
    else:
        varredura_nmap(sys.argv[1])
