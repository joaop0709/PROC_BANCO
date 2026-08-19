import csv

def calcular_saldo_diario(arquivo_entrada="transacoes_ordenadas.csv", arquivo_saida="saldo_diario.csv"):
    try:
        dados_diarios = {}

        with open(arquivo_entrada, mode="r", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)
            for linha in leitor:
                # Extrai apenas a data (formato DD/MM/AAAA ou AAAA-MM-DD)
                data_bruta = linha["Data_Hora"].strip()
                data = data_bruta.split(" ")[0] if " " in data_bruta else data_bruta.split("T")[0]
                
                # Tratamento do Valor
                valor_str = str(linha["Valor"]).replace("R$", "").replace(" ", "").replace(",", ".")
                valor = float(valor_str)
                
                # Normalização do Tipo de Transação
                tipo = linha["Tipo_Transacao"].strip().lower()

                if data not in dados_diarios:
                    dados_diarios[data] = {"num_operacoes": 0, "creditos": 0.0, "debitos": 0.0}

                dados_diarios[data]["num_operacoes"] += 1
                
                # Identificação flexível de Crédito vs Débito
                if "cred" in tipo or "deposito" in tipo or "entrada" in tipo:
                    dados_diarios[data]["creditos"] += valor
                elif "deb" in tipo or "saque" in tipo or "saida" in tipo or "pagamento" in tipo:
                    dados_diarios[data]["debitos"] += valor
                else:
                    # Caso não identifique o texto, assume valor positivo/negativo se houver sinal
                    if valor >= 0:
                        dados_diarios[data]["creditos"] += valor
                    else:
                        dados_diarios[data]["debitos"] += abs(valor)

        with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as arq_saida:
            campos = ["Data", "Num_Operacoes", "Saldo_Diario"]
            escritor = csv.DictWriter(arq_saida, fieldnames=campos)
            escritor.writeheader()

            for data, info in dados_diarios.items():
                saldo_diario = info["creditos"] - info["debitos"]
                
                escritor.writerow({
                    "Data": data,
                    "Num_Operacoes": info["num_operacoes"],
                    "Saldo_Diario": round(saldo_diario, 2)
                })

        print(f"Sucesso! Saldo diário apurado com valores em '{arquivo_saida}'.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")

if __name__ == "__main__":
    calcular_saldo_diario()