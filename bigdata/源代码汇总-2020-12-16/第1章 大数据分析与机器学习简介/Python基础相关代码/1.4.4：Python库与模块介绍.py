# =============================================================================
# 1.4.4 Python库与模块介绍 by 华能信托-王宇韬
# =============================================================================

# 显示时间的一种方式
import time
print(time.strftime("%Y/%m/%d"))

# 显示时间的另一种方式
from datetime import datetime
print(datetime.now())

# 上面的也可以这么写，不一定要from import这么写
import datetime
print(datetime.datetime.now())

# 尝试获取百度首页的网页源代码，你可以把这个网址换成别的试试看
import requests
url = 'https://www.baidu.com/'
res = requests.get(url).text
print(res)

# 获取Python官网源代码
import requests
url = 'https://www.python.org'
res = requests.get(url).text
# print(res) # 该内容较多，感兴趣的读者可以将注释取消看看运行结果，小技巧：ctrl+/可以添加和取消注释


