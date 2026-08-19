import csv

def ordenar_transacoes(arquivo_entrada="transacoes_completas.csv", arquivo_saida="transacoes_ordenadas.csv"):
    try:
        with open(arquivo_entrada, mode="r", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)
            transacoes = list(leitor)

        # Ordena pelo valor da transacao (da maior para a menor)
        transacoes_ordenadas = sorted(
            transacoes, 
            key=lambda t: float(t["Valor"]), 
            reverse=True
        )

        with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as arq_saida:
            campos = ["Data_Hora", "Tipo_Transacao", "Valor", "Saldo_Resultante"]
            escritor = csv.DictWriter(arq_saida, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(transacoes_ordenadas)

        print(f"Sucesso! Arquivo '{arquivo_saida}' gerado com as transações ordenadas.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")

if __name__ == "__main__":
    ordenar_transacoes()