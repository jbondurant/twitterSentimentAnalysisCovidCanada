
from get_tweets import read_json
import pandas as pd

def main():
    tweets_path = '../data/sample60every8min/tweets/2021-11-24T00:00:00Z-to-2021-11-25T00:00:00Z.json'

    tweets_json = read_json(tweets_path)

    tweets_clean = []
    for tweet_id, tweet_content in tweets_json.items():
        tweets_content_clean = {}
        tweets_content_clean['id'] = tweet_content['id']
        tweets_content_clean['user_location'] = tweet_content['user_location']
        tweets_content_clean['text'] = tweet_content['text']
        tweets_content_clean['created_at'] = tweet_content['created_at']
        tweets_content_clean['username'] = tweet_content['username']
        tweets_content_clean['lang'] = tweet_content['lang']

        tweets_content_clean['retweet_count'] = tweet_content['public_metrics']['retweet_count']
        tweets_content_clean['reply_count'] = tweet_content['public_metrics']['reply_count']
        tweets_content_clean['like_count'] = tweet_content['public_metrics']['like_count']
        tweets_content_clean['quote_count'] = tweet_content['public_metrics']['quote_count']

        tweets_clean.append(tweets_content_clean)

    df = pd.DataFrame(tweets_clean)
    df.to_csv('../data/sample60every8min/csvTweets/2021-11-24T00:00:00Z-to-2021-11-25T00:00:00Z.csv')
    print(df)


if __name__ == '__main__':
    main()