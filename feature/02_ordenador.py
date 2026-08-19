import csv

def ordenar_transacoes(arquivo_entrada="transacoes_completas.csv", arquivo_saida="transacoes_ordenadas.csv"):
    try:
        with open(arquivo_entrada, mode="r", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)
            transacoes = list(leitor)

        # Regra de ordenação: 
        # 1º por Data_Hora
        # 2º por Tipo_Transacao (prioriza Crédito em relação a Débito)
        def chave_ordenacao(t):
            tipo = t.get("Tipo_Transacao", "").strip().lower()
            # Prioridade 0 para crédito, 1 para débito e 2 para outros
            prioridade_tipo = 0 if "credito" in tipo or "crédito" in tipo else (1 if "debito" in tipo or "débito" in tipo else 2)
            return (t.get("Data_Hora", ""), prioridade_tipo)

        transacoes_ordenadas = sorted(transacoes, key=chave_ordenacao)

        with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as arq_saida:
            campos = ["Data_Hora", "Tipo_Transacao", "Valor", "Saldo_Resultante"]
            escritor = csv.DictWriter(arq_saida, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(transacoes_ordenadas)

        print(f"Sucesso! Arquivo '{arquivo_saida}' reordenado por data e por tipo (Crédito > Débito).")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")

if __name__ == "__main__":
    ordenar_transacoes()