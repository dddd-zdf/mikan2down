# mikan2down

This is an RSS scanner (for now it is exclusively for Mikan project) to check the feed regularly and retrive the targeted file url to aria2-like downloader through RPC (xml in this case).

Self-trigger can be implemented by Calendar.app. 

Usage
-----

This script can scan the rss feed list from config.json at a given interval. When the rss feed gets updated it can find an item matched with the keyword and push it to downloader (aria2-like) through RPC. **Be sure to edit config.json.**. You can look into config.json and be able to understand it easily.

config.json
-----------

"interval": interval between each scan in seconds.
"port": RPC port (16800 for motrix, 6800 for aria2 default)
"list":[
        {
        "title": the name you want for the bangumi,
        "rss": the rss url for the bangumi,
        "key": the keyword to match for the file (most cases it should be the keyword for the language you want)
        }
]


rss example
-----------

This is the an example retreived from a mikan-project rss feed. Support for more sites may come in the future.

Future
------

to-do:  
  - [ ] Usage in README    
  - [x] ~~fix bug repetitive download~~    
  - [x] ~~JSON file input~~  
  - [x] ~~multiple match~~  
  - [x] ~~notification (MacOS)~~
  - [ ] notification (Windows)



Reference
---------
  [aria2 RPC interface](http://aria2.github.io/manual/en/html/aria2c.html#rpc-interface)  
  [Motrix RPC port](https://github.com/agalwood/Motrix/wiki/Browser-Extensions)



This project is under MIT License.
