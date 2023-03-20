import pandas as pd
import pickle
from datetime import datetime
from pre_processamento.pre_processamento import pre_processamento
from modelo.modelo import treinar_modelo
from visualizacao.visualizacao import gerar_grafico
from jinja2 import Environment, FileSystemLoader

# Carregar os dados
dados = pd.read_csv('dados/dataset.csv', parse_dates=['timestamp'])

# Pre-processar os dados
dados_normalizados = pre_processamento(dados)
if 'luminosidade_prevista' in dados_normalizados.columns:
    dados['luminosidade_prevista'] = dados_normalizados['luminosidade_prevista']
else:
    print('Erro ao normalizar os dados: a coluna "luminosidade_prevista" não foi incluída!')

dados = dados.copy()
dados.dropna(inplace=True)
print(dados_normalizados.head())

# Treinar o modelo
modelo = treinar_modelo(dados_normalizados)

# Salvar o modelo
with open('modelo/modelo.pkl', 'wb') as f:
    pickle.dump(modelo, f)

# Carregar o modelo
with open('modelo/modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Verificar se o modelo foi carregado corretamente
if modelo is None:
    print('Erro ao carregar modelo!')
else:
    # Realizar a predição
    X = dados_normalizados[['temperatura', 'humidade']]
    dados['luminosidade_prevista'] = modelo.predict(X)

# Gerar a visualização dos resultados
grafico = gerar_grafico(dados)

# Salvar os resultados
dados[['timestamp', 'luminosidade_prevista']].to_csv('visualizacao/resultado.csv', index=False)

# Gerar a interface de visualização
env = Environment(loader=FileSystemLoader('visualizacao'))
template = env.get_template('index.html')
with open('visualizacao/index.html', 'w') as f:
    f.write(template.render(grafico=grafico.to_json()))
