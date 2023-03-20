<h1>LuminaPredict</h1>

<p>LuminaPredict é um projeto de IoT com aprendizado de máquina para previsão de luminosidade. Ele usa dados de luminosidade, temperatura e umidade coletados por um dispositivo IoT para prever a luminosidade futura com base nas condições ambientais.</p>

<h1>Como funciona</h1>

<p>O projeto é dividido em três partes principais:</p>

<p>Pre-processamento: os dados brutos coletados pelo dispositivo IoT são normalizados e preparados para o treinamento do modelo.
Treinamento do modelo: um modelo de regressão linear é treinado para prever a luminosidade futura com base na temperatura e umidade dos dados normalizados.
Visualização: os resultados são visualizados em um gráfico interativo que mostra a previsão de luminosidade em relação ao tempo.</p>

<h1>Como usar</h1>

<p>Para utilizar o projeto, siga os seguintes passos:</p>

Clone o repositório para sua máquina local.
Instale as dependências necessárias usando pip install -r requirements.txt.
Coloque os dados coletados pelo seu dispositivo IoT em um arquivo CSV na pasta dados.
Execute o arquivo main.py para rodar o projeto.
Os resultados da previsão serão salvos em um arquivo CSV na pasta visualizacao e uma página HTML interativa será gerada na pasta visualizacao para visualizar os resultados.

<h1>Tecnologias utilizadas</h1>
<p>O projeto foi desenvolvido utilizando as seguintes tecnologias:</p>

<img src="https://img.icons8.com/color/48/000000/python.png">
<img src="https://img.icons8.com/color/48/000000/html.png">

Dependencias Python:
Pandas
Scikit-learn
Jinja2
Como contribuir
Se você gostaria de contribuir com este projeto, sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias.

Créditos
Este projeto foi desenvolvido por Davi Silva como parte [adicione qualquer informação adicional sobre a motivação por trás do projeto].

Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE.md para mais detalhes.
