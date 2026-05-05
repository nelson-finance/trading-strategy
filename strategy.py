import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Télécharger les données (Apple)
data = yf.download("AAPL", start="2020-01-01")

# Moyennes mobiles
data["MA50"] = data["Close"].rolling(50).mean()
data["MA200"] = data["Close"].rolling(200).mean()

# Signal (1 = acheter, 0 = vendre)
data["Signal"] = (data["MA50"] > data["MA200"]).astype(int)

# Rendements
data["Return"] = data["Close"].pct_change()
data["Strategy"] = data["Return"] * data["Signal"].shift(1)

# Performance cumulée
data["Market"] = (1 + data["Return"]).cumprod()
data["Strategy_cum"] = (1 + data["Strategy"]).cumprod()

# Graphique
plt.figure(figsize=(10,5))
plt.plot(data["Market"], label="Buy & Hold")
plt.plot(data["Strategy_cum"], label="Strategy")
plt.legend()
plt.title("Trading Strategy (AAPL)")
plt.show()
