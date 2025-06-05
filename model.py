import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def prepare_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Prepara features para o modelo: preço atual e média móvel.
    """
    data = data.dropna()
    X = data[['close', 'sma_14']]
    y = data['close'].shift(-1).dropna()
    X = X.iloc[:-1]  # Alinha com y
    return X, y

def train_model(X: pd.DataFrame, y: pd.Series):
    """
    Treina RandomForest para prever preço do próximo dia.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"R² no teste: {score:.4f}")
    return model
