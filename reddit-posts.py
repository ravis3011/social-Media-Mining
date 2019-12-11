import praw
import time
import csv
#count = 0
reddit = praw.Reddit(client_id = 'YpISJB1UYhCrpA', client_secret = 'f73WwF-69Q5MHQoN1HVxqbcAHtY', user_agent = 'rs3011')
query_string_com = ['google.com', 'youtube.com', 'amazon.com', 'facebook.com', 'yahoo.com', 'reddit.com', 'wikipedia.org', 'ebay.com', 'bing.com', 'netflix.com', 'office.com']

query_string2_com = ['nytimes.com', 'cnn.com', 'theguardian.com', 'shutterstock.com', 'indiatimes.com', 'washingtonpost.com', 'forbes.com', 'foxnews.com', 'weather.com']

with open('posts1.csv', 'a') as p1, open('posts2.csv', 'a') as p2:
    cw1 = csv.writer(p1)
    cw1.writerow(['created_at','url', 'id', 'author_name'])
    for url in query_string_com:
        count = 0
        x= reddit.domain(url).new(limit=10000)
        for i in x:
            count = count+1
            try:
                if i.author:
                    cw1.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.created_utc)),i.url, i.id, i.author.name])
                else:
                    cw1.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.created_utc)),i.url, i.id,])
            except exception as e:
                print(e)
                continue
        print('total Lines for Url:'+ url + ' ' +str(count) )

    cw2 = csv.writer(p2)
    cw2.writerow(['created_at','url', 'id', 'author_name'])
    for url in query_string2_com:
        count = 0
        x= reddit.domain(url).new(limit=10000)
        for i in x:
            count = count+1
            try:
                if i.author:
                    cw2.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.created_utc)),i.url, i.id, i.author.name])
                else:
                    cw2.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.created_utc)),i.url, i.id,])
            except exception as e:
                print(e)
                continue
        print('total Lines for Url :'+ url + ' '+ str(count) )
