import pandas as pd

def add_moving_average(data: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """
    Adiciona média móvel simples ao DataFrame.
    """
    data[f'sma_{window}'] = data['close'].rolling(window=window).mean()
    return data
