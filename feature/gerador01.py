import csv
from datetime import datetime, timedelta

def processar_transacoes_csv(lista_transacoes, nome_arquivo="transacoes_completas.csv"):
    saldo = 0.0
    data_atual = datetime(2026, 8, 1, 9, 0)  # Data base fictícia para simulação

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)
        # Cabeçalho do arquivo
        escritor.writerow(["Data_Hora", "Tipo_Transacao", "Valor", "Saldo_Resultante"])

        # Processamento em lote de cada transação
        for tipo, valor in lista_transacoes:
            tipo = tipo.upper()
            if tipo == "C":
                saldo += valor
            elif tipo == "D":
                saldo -= valor

            data_str = data_atual.strftime("%d/%m/%Y %H:%M")
            escritor.writerow([data_str, tipo, f"{valor:.2f}", f"{saldo:.2f}"])

            # Avanca o tempo a cada transação
            data_atual += timedelta(days=1, hours=2, minutes=15)

# Lista de dados predefinida (Sem input de usuário)
transacoes = [
    ("C", 2500.00),  # Crédito
    ("D", 850.00),   # Débito
    ("D", 120.50),   # Débito
    ("D", 45.90),    # Débito
    ("D", 230.40),   # Débito
    ("C", 150.00),   # Crédito
    ("D", 35.00),    # Débito
    ("D", 15.00),    # Débito
    ("C", 500.00),   # Crédito
    ("D", 60.00),    # Débito
    ("D", 112.30),   # Débito
    ("D", 29.90),    # Débito
    ("C", 200.00),   # Crédito
    ("D", 89.90),    # Débito
    ("D", 14.50)     # Débito
]

# Executa o script
processar_transacoes_csv(transacoes)
print("CSV gerado com sucesso contendo 15 transações!")