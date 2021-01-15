# mikan2down

This is an RSS scanner (for now it is exclusively for Mikan project) to check the feed regularly and retrive the targeted file url to aria2-like downloader through RPC (xml in this case).

Self-trigger can be implemented by Calendar.app. 

Usage
-----

This script can scan the rss feed list from config.json at a given interval. When the rss feed gets updated it can find an item matched with the keyword and push it to rpc port (6800 for aria2 and 16800 for motrix). More details can be found in the comments in config.json.

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
