import praw
import time
import csv
reddit = praw.Reddit(client_id = 'YpISJB1UYhCrpA', client_secret = 'f73WwF-69Q5MHQoN1HVxqbcAHtY', user_agent = 'rs3011')
with open('posts1.csv', 'a') as p1, open('posts2.csv', 'a') as p2:
    cw1 = csv.writer(p1)
    cw1.writerow(['created_at','url', 'id', 'author_name'])
    for submission in reddit.subreddit('all').stream.submissions(skip_existing=True):   
        if (submission.permalink != submission.url) and ('nytimes.com' in submission.url or  'cnn.com' in submission.url or  'theguardian.com' in submission.url or  'shutterstock.com' in submission.url or  'indiatimes.com' in submission.url or  'washingtonpost.com' in submission.url or  'forbes.com' in submission.url or  'foxnews.com' in submission.url or  'weather.com' in submission.url):
        try:
                if submission.author:
                    cw1.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created_utc)),submission.url, submission.id, submission.author.name])
                else:
                    cw1.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created_utc)),submission.url, submission.id,])
            except exception as e:
                print(e)
                continue
        print('total Lines for Url:'+ url + ' ' +str(count) )
