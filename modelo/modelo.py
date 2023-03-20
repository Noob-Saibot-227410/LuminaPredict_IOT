from sklearn.linear_model import LinearRegression

def treinar_modelo(dados):
    X = dados[['temperatura', 'humidade']]
    y = dados['luminosidade']
    
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    return modelo
