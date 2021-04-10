# # 8.2.2 股票衍生变量生成
# **1.生成股票基本数据**
df = ts.get_k_data('000002',start='2015-01-01',end='2019-12-31')
df.head()

df = df.set_index('date')
df.head()

# **2.简单衍生变量的计算**
df['close-open'] = (df['close'] - df['open'])/df['open']
df['high-low'] = (df['high'] - df['low'])/df['low']
df['pre_close'] = df['close'].shift(1)
df['price_change'] = df['close']-df['pre_close']
df['p_change'] = (df['close']-df['pre_close'])/df['pre_close']*100
df.head()

# **3.移动平均线指标MA值**
df['MA5'] = df['close'].rolling(5).mean()
df['MA10'] = df['close'].rolling(10).mean()
df.head(15)  # head(15)表示展示前15行，因为要展示10行以上，才能看到MA10有值

df.dropna(inplace=True)  # 删除空值行，也可以写成df = df.dropna()
df.head()
# 4. TA-Lib安装法
# pip install TA_Lib-0.4.17-cp37-cp37m-win_amd64.whl

# **5.通过TA-Lib库生成相对强弱指标RSI值**
import talib
df['RSI'] = talib.RSI(df['close'], timeperiod=12)

# **6.通过TA-Lib库生成动量指标MOM值**
df['MOM'] = talib.MOM(df['close'], timeperiod=5)

# **7.通过TA-Lib库生成指数移动平均值EMA**
df['EMA12'] = talib.EMA(df['close'], timeperiod=12)
df['EMA26'] = talib.EMA(df['close'], timeperiod=26)

# **8.通过TA-Lib库生成异同移动平均线MACD值**
df['MACD'], df['MACDsignal'], df['MACDhist'] = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
df.dropna(inplace=True)
df.tail()

# # 补充内容：Talib库的一些验证
import pandas as pd
import talib
data = pd.DataFrame()
data['close'] = [10, 12, 11, 13, 12, 14, 13]
data['RSI'] = talib.RSI(data['close'], timeperiod=6)
print(data)
