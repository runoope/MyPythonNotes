# 导入相关包
import time

from efficient_apriori import apriori
from lxml import etree
from selenium import webdriver

name_lists = []
for i in range(0, 31, 15):

    url = 'https://search.douban.com/movie/subject_search?search_text=宁浩&cat=1002&start=' + str(i)
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(1)
    html = browser.find_element_by_xpath("//*").get_attribute('outerHTML')
    html = etree.HTML(html)
    names_sets = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div["
                            "@class='detail']/div[@class='meta abstract_2']/text()")
    for name_set in names_sets:
        name_set = name_set.split('/')
        a_name_set = []
        for name in name_set:
            a_name_set.append(name.strip(' '))
        if '宁浩' == a_name_set[0]:
            name_lists.append(a_name_set)

for name_list in name_lists:
    print(name_list)
item_sets, rules = apriori(name_lists, min_support=0.5, min_confidence=0.8)
print(item_sets)
print(rules)
