"""
爬取豆瓣上指定关键字的图片并下载
"""
# 导入模块
import requests
import json


# 下载图片
def download_picture(name, url):
    try:
        req = requests.get(url, timeout=10)
        filename = 'pictures/' + name + '.jpg'
        with open(filename, 'wb') as picture:
            picture.write(req.content)
    except requests.exceptions.ConnectionError:
        print(name + '的图片无法下载！')


# 获取图片总数并返回总数值
def get_picture_count(keys, browser_agent):
    re = requests.get('https://www.douban.com/j/search_photo?q=' + keys + '&limit=20&start=0',
                      headers={'User-Agent': browser_agent})
    json_data = json.loads(re.text)
    return json_data['total']


# 获取下载地址并开始下载图片

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0)Gecko/20100101 Firefox/68.0'
names = input('请输入您想获取照片的人姓名：')

count = get_picture_count(names, user_agent)

for i in range(0, count, 20):
    r = requests.get('https://www.douban.com/j/search_photo?q=' + names + '&limit=20&start=' + str(i),
                     headers={'User-Agent': user_agent})
    response = json.loads(r.text)

    for image in response['images']:
        print('下载的这张照片id为:' + image['id'])
        print('下载的这张照片地址为:' + image['src'])
        download_picture(image['id'], image['src'])

print('照片全部下载完成！')
