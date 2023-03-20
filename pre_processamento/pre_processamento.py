import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def pre_processamento(dados):
    # Selecionar as colunas de interesse
    dados = dados[['timestamp', 'temperatura', 'humidade', 'luminosidade']]
    
    # Tratar valores ausentes
    dados.dropna(inplace=True)

    # Normalizar os dados
    scaler = MinMaxScaler()
    dados_normalizados = pd.DataFrame(scaler.fit_transform(dados[['temperatura', 'humidade', 'luminosidade']]), 
                                       columns=['temperatura', 'humidade', 'luminosidade'])
    dados_normalizados['luminosidade_prevista'] = 0 # Adicionar esta linha
    dados_normalizados['timestamp'] = dados['timestamp']
    dados_normalizados.set_index('timestamp', inplace=True)
    
    return dados_normalizados
