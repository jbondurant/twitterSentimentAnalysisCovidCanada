import tweepy
import json

def read_json(credentials_path):
    with open(credentials_path, 'r') as fh:
        credentials = json.load(fh)
        return credentials

def get_api_tweets(client):
    #TODO make actual method
    #hopefully I'm not far from the return format from tweepy search


    #search_results = client.search_all_tweets(q="apples", count=100)
    #return search_results

    #TODO fix return here since it should be Union[dict, requests.Response, Response] according to docs
    return {"john": "here's some opinion"}

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


def main():
    # TODO make this valid for multiple OS
    # TODO change to credentials instead of fake_credentials
    credentials_path = '../data/fake_credentials.json'
    credentials_dict = read_json(credentials_path)
    api = get_twitter_client(credentials_dict)
    api_tweets = get_api_tweets()



if __name__ == '__main__':
    main()