import pandas as pd

def split_tweets_randomly(num_sample_1, path_tweets_csv):
    df_tweets = pd.read_csv(path_tweets_csv)
    #df_tweets.drop('Unnamed: 0', axis=1, inplace=True)


    df_sample_1 = df_tweets.sample(num_sample_1)
    df_rest = df_tweets.drop(df_sample_1.index)

    print(df_sample_1)
    print('aaa')
    print(df_rest)

    return (df_sample_1, df_rest)




def main():
    path_input = '../data/mergedTweets/2021-11-26T00:00:00Z-to-2021-11-29T00:00:00Z.csv'
    num_sample_1 = 200
    path_sample_1 = '../data/tweetSamples/sample1OfSize' + str(num_sample_1) + '.csv'
    path_rest = '../data/tweetSamples/remainderOfSample1OfSize' + str(num_sample_1) + '.csv'

    df_sample_1, df_rest = split_tweets_randomly(num_sample_1, path_input)

    df_sample_1.to_csv(path_sample_1, index = False)
    df_rest.to_csv(path_rest, index = False)







if __name__ == '__main__':
    main()