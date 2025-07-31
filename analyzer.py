import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def get_stock_data(ticker, start, end):
    try:
        data = yf.download(ticker, start=start, end=end)
        data['MA20'] = data['Close'].rolling(window=20).mean()
        data['MA50'] = data['Close'].rolling(window=50).mean()
        return data
    except:
        return None

def plot_stock_data(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Close Price"))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA20'], name="20-day MA"))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA50'], name="50-day MA"))
    fig.update_layout(title=f"{ticker.upper()} Stock Price", xaxis_title="Date", yaxis_title="Price")
    fig.show()