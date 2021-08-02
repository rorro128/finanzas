import pyfolio as pf

import warnings
warnings.filterwarnings('ignore')

stock_rets = pf.utils.get_symbol_rets('AMZN')

pf.create_returns_tear_sheet(stock_rets, live_start_date='2015-12-1')