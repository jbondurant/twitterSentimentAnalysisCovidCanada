from get_tweets import read_json, write_tweets

#change to make method to merge 2, then make method to merge list



def main():

    all_tweets_paths = []
    all_tweets_dicts = []
    tweets_merged_path = '../Data/mergedTweets/2021-11-26T00:00:00Z-to-2021-11-29T00:00:00Z.json'

    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-26T00:00:00Z-to-2021-11-26T02:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-26T02:00:00Z-to-2021-11-26T04:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-26T04:00:00Z-to-2021-11-26T10:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-26T10:00:00Z-to-2021-11-26T12:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-26T12:00:00Z-to-2021-11-26T18:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-26T18:00:00Z-to-2021-11-27T00:00:00Z.json')

    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-27T00:00:00Z-to-2021-11-27T06:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-27T06:00:00Z-to-2021-11-27T08:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-27T08:00:00Z-to-2021-11-27T10:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-27T10:00:00Z-to-2021-11-27T12:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-27T12:00:00Z-to-2021-11-27T14:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-27T14:00:00Z-to-2021-11-27T16:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-27T16:00:00Z-to-2021-11-28T00:00:00Z.json')

    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T00:00:00Z-to-2021-11-28T06:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T06:00:00Z-to-2021-11-28T08:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T08:00:00Z-to-2021-11-28T12:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T12:00:00Z-to-2021-11-28T14:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T14:00:00Z-to-2021-11-28T16:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T16:00:00Z-to-2021-11-28T18:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T18:00:00Z-to-2021-11-28T22:00:00Z.json')
    all_tweets_paths.append('../Data/sample70every8min/tweets/2021-11-28T22:00:00Z-to-2021-11-29T00:00:00Z.json')


    for tweets_path in all_tweets_paths:
        all_tweets_dicts.append(read_json(tweets_path))



    merged_tweets_dict = {}
    for tweet_dict in all_tweets_dicts:
        merged_tweets_dict.update(tweet_dict)



    write_tweets(merged_tweets_dict, tweets_merged_path)





if __name__ == '__main__':
    main()