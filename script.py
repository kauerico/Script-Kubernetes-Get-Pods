import subprocess
import argparse

def get_pods(namespace, cluster):
    try:
        # Define o comando kubectl get pods com os parâmetros fornecidos
        command = ["kubectl", "get", "pods", "--namespace", namespace, "--context", cluster]

        # Executa o comando kubectl e captura a saída
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Exibe a saída do comando
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando kubectl: {e.stderr}")

def main():
    # Configura os argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Obter pods de um namespace específico em um cluster Kubernetes.")
    parser.add_argument("namespace", type=str, help="Nome do namespace")
    parser.add_argument("cluster", type=str, help="Nome do cluster")

    # Analisa os argumentos fornecidos
    args = parser.parse_args()

    # Chama a função get_pods com os argumentos fornecidos
    get_pods(args.namespace, args.cluster)

if __name__ == "__main__":
    main()
