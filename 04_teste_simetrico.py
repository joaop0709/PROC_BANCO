import csv
import os
import importlib

calculador = importlib.import_module("03_calculador_saldo")
calcular_saldo_diario = calculador.calcular_saldo_diario

def testar_massa_simetrica():
    arquivo_teste_entrada = "teste_transacoes_simetricas.csv"
    arquivo_teste_saida = "teste_saldo_simetrico.csv"

    # Criando 4 datas com lançamentos simétricos exatos (R$ 100 crédito e R$ 100 débito)
    dados_teste = [
        ["Data_Hora", "Tipo_Transacao", "Valor"],
        ["2026-08-01 10:00:00", "Credito", "100.00"],
        ["2026-08-01 11:00:00", "Debito", "100.00"],
        ["2026-08-02 10:00:00", "Credito", "100.00"],
        ["2026-08-02 11:00:00", "Debito", "100.00"],
        ["2026-08-03 10:00:00", "Credito", "100.00"],
        ["2026-08-03 11:00:00", "Debito", "100.00"],
        ["2026-08-04 10:00:00", "Credito", "100.00"],
        ["2026-08-04 11:00:00", "Debito", "100.00"],
    ]

    # Salva a massa de teste temporária
    with open(arquivo_teste_entrada, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(dados_teste)

    # Executa a função do calculador de saldo sobre a massa de teste
    calcular_saldo_diario(arquivo_entrada=arquivo_teste_entrada, arquivo_saida=arquivo_teste_saida)

    # Validação determinística
    sucesso = True
    with open(arquivo_teste_saida, mode="r", encoding="utf-8") as f:
        leitor = list(csv.DictReader(f))
        
        if len(leitor) != 4:
            print(f"[-] Erro: Esperado 4 datas, mas foram encontradas {len(leitor)}.")
            sucesso = False

        for linha in leitor:
            saldo = float(linha["Saldo_Diario"])
            if saldo != 0.0:
                print(f"[-] Erro na data {linha['Data']}: Saldo esperado 0.00, obtido {saldo}")
                sucesso = False

    if sucesso:
        print("[+] SUCESSO: Todos os saldos diários das 4 datas resultaram exatamente em 0.00!")
    else:
        print("[-] FALHA no teste automatizado.")

if __name__ == "__main__":
    testar_massa_simetrica()