import feedparser
import ssl
#import requests
import xmlrpc.client
import re
from lxml import etree
import datetime

now = datetime.datetime.now().strftime("%Y-%m")
time = datetime.datetime.now().timetuple()
today = now +"-"+ str(time.tm_mday)

def download(torrent):
     #port 16800 is for Motrix, the default port for aria2 is 6800
     s = xmlrpc.client.ServerProxy('http://localhost:16800/rpc')
     s.aria2.addUri([torrent])

ssl._create_default_https_context = ssl._create_unverified_context
rss_mikan = feedparser.parse('https://mikanani.me/RSS/Bangumi?bangumiId=2335&subgroupid=92')


for item in rss_mikan['entries']:
     date = re.split(r'T',item['published'])[0]
     lang = re.split(r'\[',item['id'])[3][0]
     if date == today and lang == '简':
          torrent = rss_mikan['entries'][0]['links'][2]['href']
          download(torrent)



#discarded requests method
'''
info = requests.get('https://mikanani.me/Home/Bangumi/2335')
selector = etree.HTML(info.text)

content = selector.xpath("//*[@id='sk-container']/div[2]/table[8]/tbody/")


print(content)

#retrieve the first two items

date = selector.xpath("//*[@id='sk-container']/div[2]/table[8]/tbody/tr[1]/td[3]/text()")[0][0:10]

title = selector.xpath("//*[@id='sk-container']/div[2]/table[8]/tbody/tr[1]/td[1]/a[1]/text()")[0]
lang = re.split(r'\[',title)[3][0]


if date = time.strftime("%Y/%m/%d") and lang = '简':
     magnet = selector.xpath('//*[@id="sk-container"]/div[2]/table[8]/tbody/tr[1]/td[1]/a[2]/@data-clipboard-text')
     download(magnet)

#2020/12/28 04:14
'''