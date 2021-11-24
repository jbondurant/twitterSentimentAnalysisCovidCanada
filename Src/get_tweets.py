import tweepy
import json

def read_json(credentials_path):
    with open(credentials_path, 'r') as fh:
        credentials = json.load(fh)
        return credentials

def write_tweets(tweet_results, tweets_path):
    tweets_file = open(tweets_path, "w")
    for tweet in tweet_results:
        tweets_file.write(tweet + "\n")
    tweets_file.close()


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

#mycourses mentions getting canadian tweets by timezone, but I don't think that's possible
#we can't search for tweets by location without an academic account, which is for masters students and above
#however we can possibly filter tweets by location after the search
#in which case we want to get way more than 1000 tweets
#this link might help https://stackoverflow.com/questions/36490085/how-to-get-twitter-users-location-with-tweepy
def get_api_tweets(client, query_string):
    if len(query_string) > 512:
        raise ValueError('Query length too long')

    # dates can be changed, but must remain a span of 3 days
    start_time = '2021-11-19T00:00:00Z'
    end_time = '2021-11-22T00:00:00Z'

    #old attempt without pagination or cursor,
    #also am not sure which tutorial or stackexchange page made me do count=100
    #search_results = client.search_recent_tweets(q=query_string,  count=100, start_time = start_time, end_time = end_time)
    #starting with items = 150 to be gentle to api as I test the waters
    num_tweets_collected = 150
    search_results = tweepy.cursor(client.search_recent_tweets, q=query_string, start_time = start_time, end_time = end_time).items(num_tweets_collected)
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
    query_word_list = get_query_word_list()
    query_string = build_query_string(query_word_list)
    tweets = get_api_tweets(client, query_string)

    #TODO make this valid for multiple OS
    tweets_path = '../data/tweets.txt' #might get changed to json later
    write_tweets(tweets, tweets_path)


    #in report, we'll probably have to mention that we manually remove tweets about say Johnson and Johnson, or Pfizer
    #that weren't about the vaccine
    #this means we collect enough tweets (1500 should be more than enough) so we can have 1000 relevant tweets
    #also, if we can filter by location, then we might need to collect like 50000 tweets



if __name__ == '__main__':
    main()