import re
import xmlrpc.client
import json


import json

with open("config.json",'r') as load_f:
    sublist = json.load(load_f)

print(sublist[1]['title'])



'''
f = open('config.json')
config = json.loads(f)

print(config)
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