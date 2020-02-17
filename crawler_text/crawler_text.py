# 导入模块
import requests
from lxml import etree
import pandas as pd
from pandas import DataFrame

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0)Gecko/20100101 Firefox/68.0'
cookies = {'cookie': '复制浏览器上的cookies'}

for i in range(0, 500, 50):
    print('第' + str(i) + '条开始：\n')
    r = requests.get('https://www.douban.com/group/search?start=' + str(i) + '&cat=1013&sort=time&q=新型冠状病毒',
                     headers={'User-Agent': user_agent}, cookies=cookies)
    html = r.text
    html = etree.HTML(html)
    name_results = html.xpath("//td[@class='td-subject']/a/text()")
    href_results = html.xpath("//td[@class='td-subject']/a//@href")
    text_results = []
    for href_result in href_results:
        r = requests.get(href_result, headers={'User-Agent': user_agent}, cookies=cookies)
        html2 = r.text
        html2 = etree.HTML(html2)

        text_result = html2.xpath("//div[@class='topic-richtext']//text()")

        text_result = str(text_result).lstrip("[\'\\n                    ', '")

        text_result = str(text_result).strip("\', \'\\n                  \']")

        text_results.append(text_result)
        print('正在保存' + href_result + '的内容...')

    pd.set_option('display.max_columns', None)
    data = {'标题': name_results, '链接': href_results, '内容': text_results}
    df = DataFrame(data)

    df.to_csv('data/data.csv', encoding='utf_8_sig', index=False, mode='a')
print('爬取完成......................................................................................')
