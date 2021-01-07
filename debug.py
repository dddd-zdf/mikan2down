import xmlrpc.client

def download(torrent):
     #port 16800 is for Motrix, the default port for aria2 is 6800
     s = xmlrpc.client.ServerProxy('http://localhost:16800/rpc')
     s.aria2.addUri([torrent])
exit()

print('1')
torrent = 'https://mikanani.me/Download/20201228/da6e6b6155787f317ca943a066be671c7244e8eb.torrent'
download(torrent)