def cotar(ticker, start, end):
    import pandas_datareader.data as web
    import matplotlib.pyplot as plt
    import yfinance as yf
    yf.pdr_override()

    cotacao = web.get_data_yahoo(f'{ticker}', start=f"{start}", end=f"{end}")
    cotacao['Adj Close'].plot()
    plt.show()
