# PROC_BANCO - Processamento de Transações Bancárias

Este projeto foi desenvolvido em Python para automatizar o processamento, tratamento e apuração de saldos diários a partir de registros de transações bancárias.

## 🚀 Funcionalidades

- **Ordenação de Transações:** Organização dos registros por data/hora e classificação do tipo de transação (Crédito/Débito).
- **Apuração de Saldo Diário:** Cálculo automático do saldo final por data (`Somatório Crédito - Somatório Débito`) e contagem do volume de operações diárias.
- **Testes Automatizados:** Script de teste com massa de dados simétrica para validação determinística dos saldos.

## 📁 Estrutura do Projeto

- `02_ordenador.py`: Script responsável por ordenar as transações.
- `03_calculador_saldo.py`: Script que realiza a apuração dos saldos e contagem por dia.
- `04_teste_simetrico.py`: Validação automatizada da lógica do calculador.
- `*.csv`: Arquivos de dados de entrada, saída e relatórios apurados.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Git & GitHub** (Versionamento de código utilizando fluxo de branches `feature/` e `test/`)
  
