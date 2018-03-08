# coding = utf-8
__author__ = 'mm'
import requests
import time

timestamp = 1520400039
while type(timestamp) == int or type(timestamp) == float:
    url = 'http://www.neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='+str(timestamp)
    html = requests.get(url)
    html.encoding = 'utf-8'
    for i in range(20):
        content = html.json()['data']['data'][i]['group']['text']
        with open('E:\\lll.txt', 'a', encoding='gb18030')as f:
            f.write(content+'\n'*2)
            # time.sleep(2)
    timestamp = html.json()['data']['max_time']


