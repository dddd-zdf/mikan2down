import feedparser
import ssl
import requests
import xmlrpc.client
import re
from lxml import etree
import time




info = requests.get('https://mikanani.me/Home/Bangumi/2335')
selector = etree.HTML(info.text)
date = selector.xpath("//*[@id='sk-container']/div[2]/table[8]/tbody/tr[1]/td[3]/text()")[0]

title = selector.xpath("//*[@id='sk-container']/div[2]/table[8]/tbody/tr[1]/td[1]/a[1]/text()")[0]
lang = re.split(r'\[',title)[3][0]

print(time.strftime("%Y/%m/%d"))
#2020/12/28 04:14

#magnet = selector.xpath('//*[@id="sk-container"]/div[2]/table[8]/tbody/tr[1]/td[1]/a[2]/@data-clipboard-text')

ssl._create_default_https_context = ssl._create_unverified_context
rss_mikan = feedparser.parse('https://mikanani.me/RSS/Bangumi?bangumiId=2335&subgroupid=92')


#print(rss_mikan['entries'][1]['link'])

'''
for entry in rss_mikan['entries']:
     print(entry['title'])
     print(entry['link'])
     print(entry['published'])
'''