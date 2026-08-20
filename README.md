
# PROC_BANCO - Processamento de Transações Bancárias

Sistema automatizado desenvolvido em Python para ordenação cronológica de movimentações bancárias, apuração de saldos diários e contagem do volume de transações por data. O projeto conta com testes unitários automatizados determinísticos e controle de versão estruturado com Git/GitHub.

---

## 📋 Pré-requisitos

Para executar o projeto, você precisará apenas do **Python 3** instalado em sua máquina. Nenhuma biblioteca externa é necessária, pois todo o projeto utiliza módulos nativos da linguagem.

- Python 3.8 ou superior
- Git (opcional, para versionamento)

---

## 🚀 Funcionalidades

- **Ordenação de Transações:** Organização dos registros por data/hora e classificação do tipo de transação (Crédito/Débito).
- **Apuração de Saldo Diário:** Cálculo automático do saldo final por data (`Somatório Crédito - Somatório Débito`) e contagem do volume diário.
- **Testes Automatizados:** Script de teste com massa de dados simétrica para validação determinística dos saldos.

---

## 📁 Estrutura do Projeto

- `02_ordenador.py`: Ordena os lançamentos por data/hora e classifica a ordem de prioridade de Crédito/Débito.
- `03_calculador_saldo.py`: Apura o saldo diário (`Somatório Crédito - Somatório Débito`) e conta a quantidade de transações diárias.
- `04_teste_simetrico.py`: Script de teste de integração que gera uma massa simétrica de 4 datas e valida a acurácia dos cálculos.
- `transacoes_completas.csv`: Base inicial de dados brutos das transações.
- `transacoes_ordenadas.csv`: Base de dados gerada após a ordenação.
- `saldo_diario.csv`: Relatório consolidado gerado após a apuração dos saldos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Git & GitHub** (Versionamento de código utilizando fluxo de branches `feature/` e `test/`)

---

## ⚙️ Como Executar

Abra o terminal na pasta raiz do projeto e execute os passos na ordem abaixo:

### 1. Ordenar as Transações Brutas

Processa a base bruta (`transacoes_completas.csv`) e gera o arquivo ordenado (`transacoes_ordenadas.csv`):

```bash
python 02_ordenador.py
```

### 2. Calcular o Saldo Diário

Lê a base ordenada e gera o relatório consolidado de saldos (`saldo_diario.csv`):

```bash
python 03_calculador_saldo.py
```

### 3. Executar os Testes Automatizados

Roda os testes de integração para validar a acurácia dos cálculos do sistema:

```bash
python 04_teste_simetrico.py
```
