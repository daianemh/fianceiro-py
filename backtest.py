import pandas as pd

def backtest_strategy(data: pd.DataFrame, predictions: pd.Series) -> pd.DataFrame:
    """
    Estratégia simples: compra se previsão > preço atual, vende caso contrário.
    Calcula retorno diário da estratégia.
    """
    data = data.iloc[:-1].copy()
    data['predicted_close'] = predictions
    data['signal'] = (data['predicted_close'] > data['close']).astype(int)  # 1 = compra, 0 = vende
    data['return'] = data['close'].pct_change().shift(-1)  # Retorno no próximo dia
    data['strategy_return'] = data['signal'] * data['return']
    data['cumulative_return'] = (1 + data['strategy_return']).cumprod() - 1
    return data
