import config
import quandl
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

quandl.ApiConfig.api_key = config.quandl_apikey
tiingo_apikey = config.tiingo_apikey

datalocation = config.datalocation

tday = pd.datetime.today()
yday_func = pd.tseries.offsets.BusinessDay(-1)
yday = yday_func(tday).date()

def download_quandl_all_hist():
    #Downloads all data for every price series and roll type from quandl futures DB
    df = pd.read_csv(datalocation + 'ticker_list.csv',
                delimiter = ',', index_col=0)
    for i in df.index:
        print('Getting ' + i + '...')
        data = quandl.get_table('SCF/PRICES', quandl_code = i, paginate = True)    
        data.to_csv(datalocation + i + '.csv')

def download_quandl_rolled_hist():
    df = pd.read_csv('/Users/adamwilliams/OneDrive/Data/Personal/ticker_list.csv',
                delimiter = ',', index_col=0)
    df = df.loc[(df['Rule'] == 'EB')]
    for i in df.index:
        print('Getting ' + i + '...')
        data = quandl.get_table('SCF/PRICES', quandl_code = i, paginate = True)    
        data.to_csv(datalocation + i + '.csv')

def download_quandl_unrolled_hist():
    df = pd.read_csv('/Users/adamwilliams/OneDrive/Data/Personal/ticker_list.csv',
                delimiter = ',', index_col=0)
    df = df.loc[(df['Rule'] == 'EN')]
    for i in df.index:
        print('Getting ' + i + '...')
        data = quandl.get_table('SCF/PRICES', quandl_code = i, paginate = True)    
        data.to_csv(datalocation + i + '.csv')  

def update_quandl_all():
    #Downloads updates to all the listed quandl contracts for all roll types
    lst = pd.read_csv('/Users/adamwilliams/OneDrive/Data/Personal/ticker_list.csv',
                delimiter = ',', index_col=0)
    for i in lst.index:
        df = pd.read_csv(datalocation + i + '.csv', delimiter = ',', index_col=0).sort_values(by = 'date')
        df['date']= pd.to_datetime(df['date'])
        if df['date'].iloc[-1] < yday:
            print('Updating ' + i)
            data = quandl.get_table('SCF/PRICES', quandl_code = i, paginate = True, date = {'gte' : df['date'].iloc[-1], 'lte' : yday}) 
            data['date']= pd.to_datetime(data['date'])
            df = df.append(data).reset_index(drop=True)
            df = df.drop_duplicates(subset = 'date')
            df.to_csv(datalocation + i + '.csv')
        else:
            print(i + ' is up to date')

def update_quandl_rolled():
    #Downloads updates to all the listed quandl contracts for all roll types
    lst = pd.read_csv('/Users/adamwilliams/OneDrive/Data/Personal/ticker_list.csv',
                delimiter = ',', index_col=0)
    lst = lst.loc[(lst['Rule'] == 'EB')]
    for i in lst.index:
        df = pd.read_csv(datalocation + i + '.csv', delimiter = ',', index_col=0).sort_values(by = 'date')
        df['date']= pd.to_datetime(df['date'])
        if df['date'].iloc[-1] < yday:
            print('Updating ' + i)
            data = quandl.get_table('SCF/PRICES', quandl_code = i, paginate = True, date = {'gte' : df['date'].iloc[-1], 'lte' : yday}) 
            data['date']= pd.to_datetime(data['date'])
            df = df.append(data).reset_index(drop=True)
            df = df.drop_duplicates(subset = 'date')
            df.to_csv(datalocation + i + '.csv')
        else:
            print(i + ' is up to date')

def update_quandl_unrolled():
    #Downloads updates to all the listed quandl contracts for all roll types
    lst = pd.read_csv('/Users/adamwilliams/OneDrive/Data/Personal/ticker_list.csv',
                delimiter = ',', index_col=0)
    lst = lst.loc[(lst['Rule'] == 'EN')]
    for i in lst.index:
        df = pd.read_csv(datalocation + i + '.csv', delimiter = ',', index_col=0).sort_values(by = 'date')
        df['date']= pd.to_datetime(df['date'])
        if df['date'].iloc[-1] < yday:
            print('Updating ' + i)
            data = quandl.get_table('SCF/PRICES', quandl_code = i, paginate = True, date = {'gte' : df['date'].iloc[-1], 'lte' : yday}) 
            data['date']= pd.to_datetime(data['date'])
            df = df.append(data).reset_index(drop=True)
            df = df.drop_duplicates(subset = 'date')
            df.to_csv(datalocation + i + '.csv')
        else:
            print(i + ' is up to date')

# def download_spot_fx_hist():
#     headers = {'Content-Type' : 'application/json'}
#     requestResponse = requests.get('https://api.tiingo.com/tiingo/fx/' + ticker + '/prices?startDate=' + 
#     '2019-06-30' + 'resampleFreq=daily&token=' + tiingo_apikey + ', headers=headers')
#     print(requestResponse)

def beta_instr_waterfall():
    print('This is the method for calculation of the instrument allocation waterfall for the beta portfolio')

def alpha_instr_waterfall():
    print('This is the method for calculation of the instrument allocation waterfall for the alpha portfolio')

def market_beta_portfolio(account_size, vol_target):
    print('This is the method for calculation of the market beta positions')

def market_alpha_portfolio(account_size, vol_target):
    print('This is the method for calculation of the market alpha positions')   

#download_quandl_all_hist()
#update_quandl_all()