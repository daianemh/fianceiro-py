Projeto IA para Mercado Financeiro
Descrição
Este projeto é uma aplicação simples de Inteligência Artificial para previsão de preços de ações e backtesting de uma estratégia de trading. Utiliza dados históricos financeiros, indicadores técnicos e um modelo de machine learning para prever o preço do próximo dia e simular uma estratégia de compra e venda baseada nessas previsões.

O projeto inclui uma interface web interativa feita com Streamlit para facilitar a análise e visualização dos resultados.

Funcionalidades
Download automático de dados históricos de ações via yfinance.

Cálculo de indicadores técnicos (média móvel simples).

Treinamento de modelo Random Forest para previsão do preço de fechamento.

Backtesting de estratégia simples baseada nas previsões do modelo.

Dashboard interativo para visualização dos resultados e gráficos.

Tecnologias e Bibliotecas
Python 3.10+

yfinance

pandas

numpy

scikit-learn

matplotlib

streamlit

Estrutura do Projeto
text
finance_ai_project/
│
├── data_fetch.py           # Coleta dados históricos
├── indicators.py           # Cálculo de indicadores técnicos
├── model.py                # Treinamento do modelo ML
├── backtest.py             # Backtesting da estratégia
├── dashboard.py            # Interface web com Streamlit
├── requirements.txt        # Dependências do projeto
└── main.py                 # Script principal para rodar o dashboard

Autora
Daiane Moreira Horbach
