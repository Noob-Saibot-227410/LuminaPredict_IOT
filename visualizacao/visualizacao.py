import pandas as pd
import plotly.express as px

def gerar_grafico(dados):
    fig = px.line(dados, x='timestamp', y=['luminosidade', 'luminosidade_prevista'], title='Luminosidade x Tempo')
    return fig
