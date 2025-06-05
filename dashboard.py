import streamlit as st
import matplotlib.pyplot as plt
from backtest import backtest_strategy
from data_fetch import fetch_data
from indicators import add_moving_average
from model import prepare_features, train_model

def run_dashboard():
    st.title("IA no Mercado Financeiro - Previsão e Backtest")

    ticker = st.text_input("Ticker da ação:", "PETR4.SA")
    start_date = st.date_input("Data início:", value=pd.to_datetime("2020-01-01"))
    end_date = st.date_input("Data fim:", value=pd.to_datetime("2023-01-01"))

    if st.button("Executar análise"):
        data = fetch_data(ticker, str(start_date), str(end_date))
        data = add_moving_average(data)
        X, y = prepare_features(data)
        model = train_model(X, y)
        predictions = model.predict(X)

        result = backtest_strategy(data, predictions)
        st.line_chart(result['cumulative_return'])

        st.write("Retorno acumulado da estratégia")
        st.dataframe(result.tail())

if __name__ == "__main__":
    run_dashboard()
