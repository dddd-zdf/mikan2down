import feedparser
import ssl
#import requests
import xmlrpc.client
import re
from lxml import etree
import datetime
import time
import json
import pync

ssl._create_default_https_context = ssl._create_unverified_context

def today():
     now = datetime.datetime.now().strftime("%Y-%m")
     t = datetime.datetime.now().timetuple()
     today = now +"-"+ str(t.tm_mday)
     return today

with open("config.json",'r') as load_f:
    sublist = json.load(load_f)
interval = sublist['interval']
#initialize check list and timer for repetitive download check
check = {}
timer = {}
for item in sublist['title']:
     check[item['title']]=0
     timer[item['title']]=0

def download(torrent):
     #port 16800 is for Motrix, the default port for aria2 is 6800
     s = xmlrpc.client.ServerProxy('http://localhost:16800/rpc')
     s.aria2.addUri([torrent])


while True:
     for rss in sublist['list']:
          if check[rss['title']] == 1:
               if timer[rss['title']] >= 86400/interval:
                    timer[rss['title']] = 0
                    check[rss['title']] = 0
                    else:
                         timer[rss['title']] += 1
          feed = feedparser.parse(rss['rss'])
          for item in feed['entries']:
               date = re.split(r'T',item['published'])[0]
               keybool = re.findall(rss['key'], item['id'])
               if date == today() and keybool != [] and check[rss['title']] == 0:
                    torrent = feed['entries'][0]['links'][2]['href']
                    download(torrent)
                    print('downloading '+ rss['title'])
                    pync.notify('downloading '+ rss['title'])
                    check[rss['title']] = 1



     time.sleep(interval)

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