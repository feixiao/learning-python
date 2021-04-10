import tushare as ts
import mplfinance as mpf
from pylab import mpl
import pandas as pd

pro = ts.pro_api('9d674d000f7c730dd3108701a1a1c534bf51bfb03a0ff169a9d11848')
# https://tushare.pro/user/token
df = pro.daily(ts_code='000001.SZ', start_date='20200101', end_date='20201103')

# df.sort_values(by='trade_date',ascending=False)
# 取所有行数据，后面取date列，open列等数据
data = df.loc[:, ['trade_date', 'open', 'close', 'high', 'low', 'vol']]
data = data.rename(columns={'trade_date': 'Date', 'open': 'Open', 'close': 'Close', 'high': 'High', 'low': 'Low',
                            'vol': 'Volume'})  # 更换列名，为后面函数变量做准备
# 设置date列为索引，覆盖原来索引,这个时候索引还是 object 类型，就是字符串类型。
data.set_index('Date', inplace=True)
# 将object类型转化成 DateIndex 类型，pd.DatetimeIndex 是把某一列进行转换，同时把该列的数据设置为索引 index。
data.index = pd.DatetimeIndex(data.index)

# 将时间顺序升序，符合时间序列
data = data.sort_index(ascending=True)

# pd.set_option()就是pycharm输出控制显示的设置，下面这几行代码其实没用上，暂时也留在这儿吧
pd.set_option('expand_frame_repr', False)  # True就是可以换行显示。设置成False的时候不允许换行
pd.set_option('display.max_columns', None)  # 显示所有列
# pd.set_option('display.max_rows', None)# 显示所有行
pd.set_option('colheader_justify', 'centre')  # 显示居中

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams["figure.figsize"] = [6.4, 4.8]
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

mpf.plot(data, type='candle', mav=(5, 10, 20), volume=True, show_nontrading=False)
