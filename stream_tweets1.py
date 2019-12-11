import json
import tldextract
import re
import urllib.request as urllib2
import requests
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv
import sys
from requests.packages.urllib3.exceptions import ProtocolError

consumer_key = '9dCS7SyHnh6L6CH8DyqbIwFxr'
consumer_secret = 'uZREEXYvSYenLn4pKxRwkU4b968cImJlDwncc6jRjbKAFowjr6'
access_token = "1176626239748001792-8jJNIp9ZluvsEO4eRE7QYvCUtVz3up"
access_token_secret = "Uk4hMItngB1tD7ojvUk3wBL8vGgcK6Q1XOGP8ldvcVinZ"

query_string = ['google com', 'youtube com', 'amazon com', 'facebook com', 'yahoo com', 'reddit com', 'wikipedia org',
'ebay com', 'bing com', 'netflix com', 'office com'
]
query_string_com = ['google.com', 'youtube.com', 'amazon.com', 'facebook.com', 'yahoo.com', 'reddit.com', 'wikipedia.org', 'ebay.com', 'bing.com', 'netflix.com', 'office.com']
# Create a streamer object
class StdOutListener(StreamListener):

    # Define a function that is initialized when the miner is called
    def __init__(self, api = None):
        # That sets the api
        self.api = api
        # Create a file with 'data_' and the current time
        self.filename = '/data/ravis/smmProject/twitter/tweets1'+'.csv'
        # Create a new file with that filename
        csvFile = open(self.filename, 'w')

        # Create a csv writer
        csvWriter = csv.writer(csvFile)

        # Write a single row with the headers of the columns
        csvWriter.writerow(['created_at',
                            'url',
                            'text',
                            'user.screen_name'
                            ])

    # When a tweet appears
    def on_status(self, status):

        # Open the csv file created previously
        csvFile = open(self.filename, 'a')

        # Create a csv writer
        csvWriter = csv.writer(csvFile)

        # If the tweet is not a retweet
        if not 'RT @' in status.text:
            urls = re.findall('((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)',status.text)
            #print(urls)
            # Try to 
            for i in range(len(urls)):
                try:
                    #print(i)
                    url_str = requests.get(urls[i]).url
                    url_string = tldextract.extract(url_str)
                    #url_string = tldextract.extract(status.entities['urls'][i]['expanded_url']) 
                    #print(urls[i])
                    url_s = url_string.domain+'.'+ url_string.suffix
                    #print(url_s)
                    if url_s == 'twitter.com':
                                                                                              
                        #print(url_str)
                        #print('=============')
                        print(status.id)
                        #print('-------------')
                    elif url_s in query_string_com:
                    # Write the tweet's information to the csv file
                        #print(url_str)
                        #print('HI-------')
                        csvWriter.writerow([status.created_at,
                                    status.entities['urls'][i]['expanded_url'],
                                    status.text,
                                    status.user.screen_name])
                # If some error occurs
                except Exception as e:
                    # Print the error
                    print(e)
                    # and continue
                    pass

        # Close the csv file
        csvFile.close()

        # Return nothing
        return

    # When an error occurs
                                                                                               
    def on_error(self, status_code):
        # Print the error code
        print('Encountered error with status code:', status_code)

        # If the error code is 401, which is the error for bad credentials
        if status_code == 401:
            # End the stream
            return False

    # When a deleted tweet appears
    def on_delete(self, status_id, user_id):

        # Print message
        print("Delete notice")

        # Return nothing
        return

    # When reach the rate limit
    def on_limit(self, track):

        # Print rate limiting error
        print("Rate limited, continuing")

        # Continue mining tweets
        return True

    # When timed out
    def on_timeout(self):

        # Print timeout message
        print(sys.stderr, 'Timeout...')

        # Wait 10 seconds
        time.sleep(10)

        # Return nothing
        return

# Create a mining function
def start_mining(queries):
    '''
    Inputs list of strings. Returns tweets containing those strings.
    '''

    # Create a listener
    l = StdOutListener()

    # Create authorization info
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create a stream object with listener and authorization
    stream = Stream(auth,l, tweet_mode='extended')

    # Run the stream object using the user defined queries
    while(True):
        try:
            stream.filter(track=queries, languages = ['en'], stall_warnings=True)
        except (ProtocolError, AttributeError):
            continue

start_mining(query_string)
