import yfinance as yf
import pandas as pd

def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Baixa dados históricos do ativo com yfinance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data[['Close']]
    data.rename(columns={'Close': 'close'}, inplace=True)
    data.dropna(inplace=True)
    return data
