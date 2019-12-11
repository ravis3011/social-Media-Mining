import pandas as pd
import csv

tweets1 = pd.read_csv("tweets1.csv")
tweets2 = pd.read_csv("tweets2.csv")
tweets3 = pd.read_csv("tweets3.csv")
posts1 = pd.read_csv("posts1.csv")
posts2 = pd.read_csv("posts2.csv")
posts3 = pd.read_csv("posts3.csv")


tweets1 = tweets1.sort_values('created_at', ascending=True).drop_duplicates('url').sort_index()
tweets2 = tweets2.sort_values('created_at', ascending=True).drop_duplicates('url').sort_index()
tweets3 = tweets3.sort_values('created_at', ascending=True).drop_duplicates('url').sort_index()
posts1 = posts1.sort_values('created_at', ascending=True).drop_duplicates('url').sort_index()
posts2 = posts2.sort_values('created_at', ascending=True).drop_duplicates('url').sort_index()
posts3 = posts3.sort_values('created_at', ascending=True).drop_duplicates('url').sort_index()

def compareUrls(file1, file2):
        count1 = 0
        count2 = 0
        tweet_urls = []
        reddit_posts = []
        for i in file1.index:
                for j in file2.index:
                        if file1['url'][i] == file2['url'][j]:
                                if file1['created_at'][i] <= file2['created_at'][j]:
                                        tweet_urls.append([file1['created_at'][i],file1['url'][i]])
                                        count1 += 1
                                else:
                                        reddit_posts.append([file2['created_at'][j],file2['url'][j]])
                                        count2 += 1
        print(count1, count2)
        return(tweet_urls, reddit_posts)
        
# calling compareUrls function to get the first appearance of  information(URL)
#set 1 
tweet_urls1, reddit_posts1 = compareUrls(tweets1, posts1)
#set2
tweet_urls2, reddit_posts2 = compareUrls(tweets2, posts2)
#set2 range 2
tweet_urls3, reddit_posts3 = compareUrls(tweets3, posts3)

info_tweet1 = pd.DataFrame(tweet_urls1)
info_tweet2 = pd.DataFrame(tweet_urls2)
info_tweet3 = pd.DataFrame(tweet_urls3)

info_post1 = pd.DataFrame(reddit_posts1)
info_post2 = pd.DataFrame(reddit_posts2)
info_post3 = pd.DataFrame(reddit_posts3)

info_tweet1.to_csv('info_tweet1.csv', encoding='utf-8', index=False)
info_post1.to_csv('info_post1.csv', encoding='utf-8', index=False)

info_tweet2.to_csv('info_tweet2.csv', encoding='utf-8', index=False)
info_post2.to_csv('info_post2.csv', encoding='utf-8', index=False)

info_tweet3.to_csv('info_tweet3.csv', encoding='utf-8', index=False)
info_post3.to_csv('info_post3.csv', encoding='utf-8', index=False)


print(len(tweet_urls1), len(reddit_posts1))
print(len(tweet_urls2), len(reddit_posts2))
print(len(tweet_urls3), len(reddit_posts3))
