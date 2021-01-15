import feedparser
import ssl
#import requests
import xmlrpc.client
import re
from lxml import etree
import datetime
import time
import json
import os
import pync


with open("config.json",'r') as load_f:
    sublist = json.load(load_f)

check = {}

for item in sublist['list']:
    check[item['title']]=0
print(check)

'''
for item in sublist['list']:
    if item['title'] == 'jjdjj':
'''



'''
id = '【豌豆字幕组】[进击的巨人 / Shingeki_no_Kyojin][63][简体][1080P][MP4]'

key = input()

title = re.findall(key, id)
print(title != [])




#print(re.findall('\[简体\]',id))
key = '繁体'
lang = re.findall(key, id)
print(lang)
print(lang == []) 
#if date == today and lang != None:



def download(torrent):
     #port 16800 is for Motrix, the default port for aria2 is 6800
     s = xmlrpc.client.ServerProxy('http://localhost:16800/rpc')
     s.aria2.addUri([torrent])
exit()

print('1')
torrent = 'https://mikanani.me/Download/20201228/da6e6b6155787f317ca943a066be671c7244e8eb.torrent'
download(torrent)
'''