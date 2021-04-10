import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def baidu(keyword, page):  # 定义函数，方便之后批量调用
    num = (page - 1) * 10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + keyword + '&pn=' + str(num)
    res = requests.get(url, headers=headers).text  # 通过requests库爬虫

    # 正则提取信息 - 网址和标题
    p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)"'
    href = re.findall(p_href, res)
    p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
    title = re.findall(p_title, res, re.S)
    # 正则提取信息 - 日期和来源
    p_date = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
    date = re.findall(p_date, res)
    p_source = '<span class="c-color-gray c-font-normal c-gap-right">(.*?)</span>'
    source = re.findall(p_source, res)

    # 数据清洗
    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        print(str(i + 1) + '.' + title[i] + ' ' + source[i] + ' ' + date[i])  # 这个是纯字符串拼接
        print(href[i])

    # 通过2.2.1节字典生成二维DataFrame表格   
    result = pd.DataFrame({'关键词': keyword, '标题': title, '网址': href, '来源': source, '日期': date})
    return result


# 通过pandas库将数据进行整合并导出为Excel
import pandas as pd

df = pd.DataFrame()

keywords = ['华能信托', '人工智能', '科技', '体育', 'Python', '娱乐', '文化', '阿里巴巴', '腾讯', '京东']
for keyword in keywords:
    for i in range(10):  # 循环10遍，获取10页的信息
        result = baidu(keyword, i + 1)
        df = df.append(result)  # 通过append()函数添加每条信息到df中
        print(keyword + '第' + str(i + 1) + '页爬取成功')

df.to_excel('新闻_new.xlsx')  # 在代码所在文件夹生成EXCEL文件
