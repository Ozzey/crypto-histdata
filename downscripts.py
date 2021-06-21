import shrimpy
import pandas as pd
import ccxt
from datetime import datetime
#--------------------------------------------------------------------#
#CCXT DOWNLOADER FUNCTION
def ccxt_hist(symbol):
    df = pd.DataFrame()

    binance = ccxt.binance()
    trading_pair = f'{symbol}/USDT'
    candles = binance.fetch_ohlcv(trading_pair, '1d')

    dates = []
    open_data = []
    high_data = []
    low_data = []
    close_data = []
    volume= []
    # format the data
    for candle in candles:
        dates.append(datetime.fromtimestamp(candle[0] / 1000.0).strftime('%Y-%m-%d'))
        open_data.append(candle[1])
        high_data.append(candle[2])
        low_data.append(candle[3])
        close_data.append(candle[4])
        volume.append(candle[5])


    df['Date'] = pd.Series(dates)
    df['Open'] = pd.Series(open_data)
    df['High'] = pd.Series(high_data)
    df['Low'] = pd.Series(low_data)
    df['Close'] = pd.Series(close_data)
    df['Volume'] = pd.Series(volume)

    df.set_index('Date', inplace=True)
    df.dropna(axis='index', how='all', inplace=True)

    return df

#--------------------------------------------------------------------#
#SHRIMPY DOWNLOADER FUNCTION
def shrimpy_hist(symbol):

    public_key = '...'
    secret_key = '...'
    client = shrimpy.ShrimpyApiClient(public_key, secret_key)
    candles = client.get_candles(
        'binance', # exchange
        symbol,     # base_trading_symbol
        'USDT',     # quote_trading_symbol
        '1d'       # interval
    )

    df = pd.DataFrame()

    dates = []
    open_data = []
    high_data = []
    low_data = []
    close_data = []
    volume= []
    # format the data to match the plotting library
    for candle in candles:
        dates.append(datetime.strptime(candle['time'], '%Y-%m-%dT%H:%M:%S.%f%z').date())
        open_data.append(candle['open'])
        high_data.append(candle['high'])
        low_data.append(candle['low'])
        close_data.append(candle['close'])
        volume.append(candle['volume'])


    df['Date'] = pd.Series(dates)
    df['Open'] = pd.Series(open_data)
    df['High'] = pd.Series(high_data)
    df['Low'] = pd.Series(low_data)
    df['Close'] = pd.Series(close_data)
    df['Volume'] = pd.Series(volume)

    df.set_index('Date', inplace=True)
    df.dropna(axis='index', how='all', inplace=True)

    return df
#--------------------------------------------------------------------#
#--------------------------------------------------------------------#
#SHRIMPY API DOWNLOADER FUNCTION
api_public='...'
api_private='...'

def shrimpy_histpro(symbol):
    public_key = 'api_public'
    secret_key = 'api_private'
    client = shrimpy.ShrimpyApiClient(public_key, secret_key)
    candles = client.get_candles(
        'binance', # exchange
        symbol,     # base_trading_symbol
        'USDT',     # quote_trading_symbol
        '1d'       # interval
    )

    df = pd.DataFrame()

    dates = []
    open_data = []
    high_data = []
    low_data = []
    close_data = []
    volume= []
    # format the data to match the plotting library
    for candle in candles:
        dates.append(datetime.strptime(candle['time'], '%Y-%m-%dT%H:%M:%S.%f%z').date())
        open_data.append(candle['open'])
        high_data.append(candle['high'])
        low_data.append(candle['low'])
        close_data.append(candle['close'])
        volume.append(candle['volume'])


    df['Date'] = pd.Series(dates)
    df['Open'] = pd.Series(open_data)
    df['High'] = pd.Series(high_data)
    df['Low'] = pd.Series(low_data)
    df['Close'] = pd.Series(close_data)
    df['Volume'] = pd.Series(volume)

    df.set_index('Date', inplace=True)
    df.dropna(axis='index', how='all', inplace=True)

    return df
#--------------------------------------------------------------------#

#ccxt_hist('ETH').to_csv('datasets/tst.csv')
