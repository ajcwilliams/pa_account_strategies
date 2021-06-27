import config
import pandas as pd

datalocation = config.datalocation

#Calculate the $US volatility for each instrument currently in the traded portfolio.
#EWM Span is EWM Span Decay: alpha = 2(span + 1)
#Volatility is output as a CSV
def all_intr_dollar_vol(ewm_span):
    instr_param = pd.read_csv(datalocation + 'instrument_parameters.csv', delimiter = ',', index_col = 0)
    instr_list = instr_param.index.tolist()
    ticker_list = pd.read_csv(datalocation + 'ticker_list.csv', delimiter = ',', index_col = 0)
    ticker_list = ticker_list[(ticker_list['Symbol'].isin(instr_list)) & (ticker_list['Rule'] == 'EB')]
    for ticker in ticker_list.index:
        prc = pd.read_csv(datalocation + ticker + '.csv', delimiter = ',', index_col = 0)
        prc = prc.set_index('date')
        vol = pd.DataFrame(index =prc.index, columns = ['stdev', 'multi', 'usdstdev'] )
        vol['stdev'] = prc['settle'].ewm(span = ewm_span).std()
        cc = ticker_list['Symbol'].loc[ticker]
        vol['multi'] = instr_param['Multiplier'].loc[cc]
        vol['usdstdev'] = vol['multi'] * vol['stdev']
        vol.to_csv(datalocation + ticker + '_vols.csv')

#Calculate the momentum for each instrument currently in the traded portfolio
#A few defninitions of momentum are used
#Signals are output as a CSV
def momentum():
    instr_param = pd.read_csv(datalocation + 'instrument_parameters.csv', delimiter = ',', index_col = 0)
    instr_list = instr_param.index.tolist()
    ticker_list = pd.read_csv(datalocation + 'ticker_list.csv', delimiter = ',', index_col = 0)
    ticker_list = ticker_list[(ticker_list['Symbol'].isin(instr_list)) & (ticker_list['Rule'] == 'EB')]
    for ticker in ticker_list.index:
        prc = pd.read_csv(datalocation + ticker + '.csv', delimiter = ',', index_col = 0)
        prc = prc.set_index('date')
        prc = prc['settle']
        print(prc)

momentum()

