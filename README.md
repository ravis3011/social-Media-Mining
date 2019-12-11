# social-Media-Mining
A Comparative Study of Information Spread in Twitter and Reddit

This project is divided into 3 parts:
1) Extracting data via Through tweepy
2) Extracting Data through Reddit
3) Comparing the Urls from step 1 and 2

For more details refer: https://github.com/ravis3011/social-Media-Mining/blob/master/Social_Media_Mining_Project_Fall_2019.pdf

# To execute the data extraction for set 1 twitter
python3 stream-twitter1.py

# To execute the data extraction for set 2 twitter date range 1
python3 stream-twitter2.py

# To execute the data extraction for set 2 twitter date range 2 (Simply run the file again)
python3 stream-twitter2.py

# To execute the data extraction using domain Listing for Reddit for set 1 and Set 2 date range(1)
python3 reddit-posts.py

# To execute the data extraction using all submission for Reddit for set 1 and Set 2 date range(2)
python3 reddit-posts_all.py 

# To compare URls with filtering (required reddit files and twitter files to compare)
python3 compare.py

