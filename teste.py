from pre_processamento.pre_processamento import pre_processamento
import pandas as pd

# Carregar dados
dados = pd.read_csv('dados/dataset.csv')

# Pré-processar dados
dados_preprocessados = pre_processamento(dados)

# Exibir dados pré-processados
print(dados_preprocessados)
