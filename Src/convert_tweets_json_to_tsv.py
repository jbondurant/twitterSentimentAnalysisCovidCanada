from filter_canadian_tweets import is_tweet_canadian, is_user_can
from get_tweets import read_json
import pandas as pd

def main():

    tweets_path = '../data/mergedTweets/2021-11-26T00:00:00Z-to-2021-11-29T00:00:00Z.json'
    csv_tweets_path = '../data/mergedCanTweets/2021-11-26T00:00:00Z-to-2021-11-29T00:00:00Z.csv'

    #tweets_path = '../Data/sample70every8min/tweets/2021-11-27T10:00:00Z-to-2021-11-27T12:00:00Z.json'
    #csv_tweets_path = '../data/mergedTweets/aaaaa.csv'

    tweets_json = read_json(tweets_path)

    num_not_can = 0

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

        #adding canadian check
        tweet_is_canadian = is_tweet_canadian(tweets_content_clean['user_location'])
        user_is_canadian = is_user_can(tweets_content_clean['username'])
        if tweet_is_canadian and user_is_canadian:
            tweets_clean.append(tweets_content_clean)
        else:
            num_not_can += 1

    df = pd.DataFrame(tweets_clean)

    df.to_csv(csv_tweets_path)
    #print(df)
    print(num_not_can)


if __name__ == '__main__':
    main()