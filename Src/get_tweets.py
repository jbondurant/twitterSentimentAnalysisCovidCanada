import tweepy
import json

def read_json(credentials_path):
    with open(credentials_path, 'r') as fh:
        credentials = json.load(fh)
        return credentials

def build_query_string(query_word_list):
    query_list_hashtag = []
    for query_word in query_word_list:
        hashtag_word = '#' + query_word;
        query_list_hashtag.append(query_word)
        if ' ' not in hashtag_word:
            query_list_hashtag.append(hashtag_word)
    query_list_fixed = list(' OR '.join(query_list_hashtag))
    query_string = '('
    for query_word in query_list_fixed:
        query_string += query_word

    #this doc explains following code parameters https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
    query_string += ') lang:en -is:retweet -is:reply -is:nullcast'
    return query_string

def get_api_tweets(client, query_string):
    if len(query_string) > 512:
        raise ValueError('Query length too long')
    search_results = client.search_recent_tweets(q=query_string,  count=100)
    return search_results

#taken from https://stackoverflow.com/questions/22469713/managing-tweepy-api-search
def get_twitter_client(credentials_dict):
    #hopefully I understand the nomenclature here
    #nomenclature equivalencies taken from https://stackoverflow.com/questions/66156958/how-to-acess-tweets-with-bearer-token-using-tweepy-in-python
    bearer_token = credentials_dict['bearer_token']
    consumer_key = credentials_dict['api_key']
    consumer_secret = credentials_dict['api_key_secret']
    #this tutorial makes me think I don't need the consumer key nor secret https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9
    #note it looks like a great tutorial for other parts of this process too!
    client = tweepy.Client(bearer_token = bearer_token, consumer_key = consumer_key, consumer_secret = consumer_secret,  wait_on_rate_limit = True)
    return client

def get_query_word_list():
    covid_words = ['covid', 'coronavirus']
    vaccine_words = ['vaccine', 'vaccination', 'vax']
    brand_words = ['pfizer', 'moderna', 'janssen', '"johnson and johnson"', '"johnson & johnson"']
    query_word_list = covid_words + vaccine_words + brand_words
    # for the report we can explain that we are skipping astrazeneca since it's not really relevant in canada anymore
    # we can also explain that we searched twitter manually and found
    # that many people used the word vax, so we included it
    #also, anti-vax is used a fair amount on twitter, but the api has - as a
    #seperator, so those will be caught by the vax query

def main():
    # TODO make this valid for multiple OS
    credentials_path = '../data/credentials.json'
    credentials_dict = read_json(credentials_path)
    client = get_twitter_client(credentials_dict)
    api_tweets = get_api_tweets(client)

    #in report, we'll probably have to mention that we manually remove tweets about say Johnson and Johnson, or Pfizer
    #that weren't about the vaccine
    #this means we collect enough tweets (1500 should be more than enough) so we can have 1000 relevant tweets
    query_word_list = get_query_word_list()





if __name__ == '__main__':
    main()