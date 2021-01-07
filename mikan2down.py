import feedparser
import ssl
import requests
import xmlrpc.client
import re
from lxml import etree
import datetime

now = datetime.datetime.now().strftime("%Y-%m")
time = datetime.datetime.now().timetuple()
today = now +"-"+ str(time.tm_mday)

def download(torrent):
     #port 16800 is for Motrix, the default port for aria2 is 6800
     s = xmlrpclib.ServerProxy('http://localhost:16800/rpc')
     s.aria2.addUri([torrent])

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
ssl._create_default_https_context = ssl._create_unverified_context
rss_mikan = feedparser.parse('https://mikanani.me/RSS/Bangumi?bangumiId=2335&subgroupid=92')

print(re.split(r'\[',item['id'])[3][0])

for item in rss_mikan['entries']:
     date = item['published'][0:9]
     lang = re.split(r'\[',item['id'])[3][0]
     if date = today and lang = '简':
          torrent = print(rss_mikan['entries'][0]['links'][2]['href'])
          download(torrent)



title = rss_mikan['entries'][0]['links']


#print(rss_mikan['entries'][1]['link'])

'''
for entry in rss_mikan['entries']:
     print(entry['title'])
     print(entry['link'])
     print(entry['published'])
'''