import tweepy as tw
import json
from filter_canadian_tweets import is_tweet_canadian
from produce_sampling_strat import get_span_minutes, span_to_splits
import time



def read_json(credentials_path):
    with open(credentials_path, 'r') as fh:
        credentials = json.load(fh)
        return credentials


def write_tweets(clean_tweets, tweets_path):
    with open(tweets_path, 'w') as fh:
        json.dump(clean_tweets, fh, indent=4)

def write_locations(clean_tweets, locations_path):
    user_locations = []
    for clean_tweet_id, clean_tweet_data in clean_tweets.items():
        location_string = clean_tweet_data['user_location']
        if location_string == None:
            location_string = ""
        user_locations.append(location_string)
    locations_file = open(locations_path, "w")
    for location in user_locations:
        locations_file.write(location + "\n")
    locations_file.close()


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
    #query_string += ') lang:en -is:retweet -is:reply -is:nullcast'
    query_string += ') lang:en -is:retweet -is:reply'
    return query_string


#mycourses mentions getting canadian tweets by timezone, but I don't think that's possible
#we can't search for tweets by location without an academic account, which is for masters students and above
#however we can possibly filter tweets by location after the search
#in which case we want to get way more than 1000 tweets
#this link might help https://stackoverflow.com/questions/36490085/how-to-get-twitter-users-location-with-tweepy
def get_api_tweets(client, query_string, start_time, end_time, num_tweets_collected):
    if len(query_string) > 512:
        raise ValueError('Query length too long')
    # dates can be changed, but must remain a span of 3 days

    #starting with items = 110 to be gentle to api as I test the waters

    search_results_list = None
    if num_tweets_collected > 100:
        search_results = tw.Paginator(client.search_recent_tweets, query = query_string, expansions = ["author_id", "geo.place_id"],
                                                 tweet_fields=[
                                                      "author_id", "created_at", "context_annotations",
                                                      "entities", "geo", "id", "lang", "public_metrics",
                                                      "possibly_sensitive", "referenced_tweets", "source", "text"
                                                  ],
                                                  user_fields=["username"],
                                                  place_fields=[
                                                      "full_name", "country", "country_code", "geo", "name"
                                                  ],start_time = start_time, end_time = end_time, max_results=100).flatten(num_tweets_collected)
        search_results_list = list(search_results)
    else:
        #keep this count line for future purposes
        abc = client.get_recent_tweets_count(query=query_string, granularity = "day")
        abc2 = 1
        search_results = client.search_recent_tweets(query=query_string, expansions=["author_id", "geo.place_id"],
                                                      tweet_fields=[
                                                          "author_id", "created_at", "context_annotations",
                                                          "entities", "geo", "id", "lang", "public_metrics",
                                                          "possibly_sensitive", "referenced_tweets", "source", "text"
                                                      ],
                                                      user_fields=["username"],
                                                      place_fields=[
                                                          "full_name", "country", "country_code", "geo", "name"
                                                      ], start_time=start_time, end_time=end_time, max_results=num_tweets_collected)
        search_results_list = search_results.data
    return search_results_list


def get_twitter_client(credentials_dict):
    bearer_token = credentials_dict['bearer_token']
    consumer_key = credentials_dict['api_key']
    consumer_secret = credentials_dict['api_key_secret']
    client = tw.Client(bearer_token = bearer_token, consumer_key = consumer_key, consumer_secret = consumer_secret,  wait_on_rate_limit = True)
    return client


def get_query_word_list():
    covid_words = ['covid', 'coronavirus']#perhaps add pandemic
    vaccine_words = ['vaccine', 'vaccination', 'vax']
    brand_words = ['pfizer', 'moderna', 'janssen', '"johnson and johnson"', '"johnson & johnson"']
    query_word_list = covid_words + vaccine_words + brand_words
    return query_word_list
    # for the report we can explain that we are skipping astrazeneca since it's not really relevant in canada anymore
    # we can also explain that we searched twitter manually and found
    # that many people used the word vax, so we included it
    #also, anti-vax is used a fair amount on twitter, but the api has - as a
    #seperator, so those will be caught by the vax query

def get_username(tweet_user, client):
    userMinimal = client.get_user(id=tweet_user)
    user = userMinimal.data.username
    return user

def get_user_location(username, client):
    response = client.get_user(username = username, expansions="pinned_tweet_id",user_fields=["location"])
    location = response.data.location
    return location


def clean_api_tweets(api_tweets, client):
    clean_tweets = {}
    for api_tweet in api_tweets:

        tweet_user = api_tweet.author_id
        tweet_username = get_username(tweet_user, client)
        tweet_user_location = get_user_location(tweet_username, client)
        if not is_tweet_canadian(tweet_user_location):
            continue

        tweet_id = api_tweet.id
        tweet_text = api_tweet.text
        tweet_lang = api_tweet.lang
        tweet_created_at = api_tweet.created_at
        tweet_public_metrics = api_tweet.public_metrics
        #tweet_entities = api_tweet.entities

        clean_tweets[tweet_id] = {}
        clean_tweets[tweet_id]['text'] = tweet_text
        clean_tweets[tweet_id]['username'] = tweet_username
        clean_tweets[tweet_id]['lang'] = tweet_lang
        clean_tweets[tweet_id]['created_at'] = str(tweet_created_at)
        clean_tweets[tweet_id]['user_location'] = tweet_user_location
        clean_tweets[tweet_id]['id'] = tweet_id
        clean_tweets[tweet_id]['public_metrics'] = tweet_public_metrics
        #clean_tweets[tweet_id]['entities'] = tweet_entities
    return clean_tweets


def main():
    query_word_list = get_query_word_list()
    query_string = build_query_string(query_word_list)
    # TODO make this valid for multiple OS
    credentials_path = '../data/credentials.json'
    credentials_dict = read_json(credentials_path)
    print(query_string)
    client = get_twitter_client(credentials_dict)



    #current sampling approach problems
    #approach has the disadantage perhaps of making tweets in off hours too (relatively) important, but you can't
    #sample perfectly anyways
    #this sample will possibly only collect tweets after 30 seconds of each minute, but that sample should be
    #representative of the tweets between 0s and 30s of each minute

    # honestly it would be amazing if I weighted my sample with the data from
    # the method client.get_recent_tweets_count(query=query_string, granularity = "hour") since
    #it would be imo a better sampling methodology which we can then write about in the report
    #edit: that being said, the amount of canadian tweets will vary wildly, so you need to do like sample 10
    #then if 1 of the tweets is canadian add it to tweets for timeframe, until you reach the weigthed
    # quota of canadian tweets for that hour?
    #edit 2: granulariity is wrong, since the posting time of the whole world likely doesn't reflect the posting times of canadians


    #start_time = '2021-11-24T00:00:00Z'
    #end_time = '2021-11-27T00:00:00Z'

    #test4 started at 5:55pm

    #test5 started at 9:02pm
    #26 batches at 10:33pm
    #done by 11:09

    #attemp1 started at 11:35 nov 26
    #7,260 Tweets pulled after batch 2
    #ended at 10:29
    #17,972 Tweets pulled
    #564 possibly canadian tweets

    start_time = '2021-11-24T00:00:00Z'
    end_time = '2021-11-25T00:00:00Z'
    sample_every_n_minutes = 8
    num_tweets_collected_per_batch = 60

    #TODO make this valid for multiple OS
    tweets_path = '../data/sample' + str(num_tweets_collected_per_batch) + 'every' + str(sample_every_n_minutes) + 'min/tweets/' + start_time + '-to-' + end_time  + '.json'
    location_path = '../data/sample' + str(num_tweets_collected_per_batch) + 'every' + str(sample_every_n_minutes) + 'min/locations/' + start_time + '-to-' + end_time  + '.txt'

    span_minutes = get_span_minutes(start_time, end_time)

    num_sample_batches = int((span_minutes / sample_every_n_minutes) + 1)
    print('num sample batches:\t' + str(num_sample_batches))
    start_time_shift = 240  # this puts the start time 4 minutes before the end time
    start_end_time_splits = span_to_splits(start_time, end_time, num_sample_batches, start_time_shift)

    all_tweets = {}


    sleep_time_constant = 3 * num_tweets_collected_per_batch + 20
    print('sleep time constant:\t' + str(sleep_time_constant))

    estimated_run_time_min = sleep_time_constant * num_sample_batches / 60
    print('estimated run time min:\t' + str(estimated_run_time_min))
    num_batches_processed = 0
    for start_time, end_time in start_end_time_splits:
        api_tweets = get_api_tweets(client, query_string, start_time, end_time, num_tweets_collected_per_batch)
        tweets = clean_api_tweets(api_tweets, client)
        all_tweets.update(tweets)
        num_batches_processed += 1
        print('num batches processed:\t' + str(num_batches_processed))
        time.sleep(sleep_time_constant)


    write_tweets(all_tweets, tweets_path)
    write_locations(all_tweets, location_path)

    #in report, we'll probably have to mention that we manually remove tweets about say Johnson and Johnson, or Pfizer
    #that weren't about the vaccine




if __name__ == '__main__':
    main()