import praw
reddit = praw.Reddit(client_id='[clientID]',
                     client_secret='[ClientSecret]',
                     password='[password]',
                     user_agent='Wikipedia Post',
                     username='[username]')


import requests
r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
url = r.url
import bs4
html = bs4.BeautifulSoup(r.text)
wikititle = html.title.text

title = wikititle
title = title.replace(" - Wikipedia", "")
reddit.subreddit('Wikipedia').submit(title, url=url)