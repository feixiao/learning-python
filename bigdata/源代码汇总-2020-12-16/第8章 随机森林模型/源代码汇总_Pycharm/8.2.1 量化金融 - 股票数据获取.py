# # 8.2 量化金融 - 股票数据获取
# # 8.2.1 股票基本数据获取
# 1.Tushare库的基本介绍
# (1) 获得日线行情数据
import tushare as ts
df = ts.get_hist_data('000002', start='2018-01-01', end='2019-01-31')
df.head()

df = ts.get_hist_data('000002','2018-01-01', '2019-01-31')
df.head()

# **补充知识点：get_k_data()函数**
df = ts.get_k_data('000002', start='2000-01-01', end='2019-01-31')
df.head()

df = df.set_index('date')
# 或者写成：df.set_index('date', inplace=True)
df.head()

# (2) 获得分钟级别的数据
df = ts.get_hist_data('000002', ktype='5')
df.head()

# (3) 获得实时行情数据
df = ts.get_realtime_quotes('000002')
print(df)

df = df[['code','name','price','bid','ask','volume','amount','time']]
print(df)

df = ts.get_realtime_quotes(['000002','000980','000981'])
print(df)

# (4) 获得分笔数据
df = ts.get_tick_data('000002', date='2018-12-12', src='tt')
df.head()

# (5) 获得指数信息
df = ts.get_index()
df.head()
