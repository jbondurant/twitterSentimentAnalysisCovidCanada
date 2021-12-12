'''

5) check the tfidf for not only categories, but for categories&sentiment combos (it's not mentioned in the instructions if i recall correctly but might lead to interesting observations to make writing the report easier
6) reprint these tfidfs into files ( i just opened a file, gave it a descriptive name and pasted the output of the tfidf function)
7) calculate the percentage of each sentiment within a topic (like make a dict that looks like {topic 1: {positive: 0.201, neutral: 0.507, negative: 0.292}, topic2: {...

'''


import pandas as pd



df = pd.read_csv("../Data/annotatedTweets/annotated_complete_table_comp_598-sample2OfSize1000.csv")


def num_tweets_category ():
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    total = 0

    for index, row in df.iterrows():
        if row['topic'] == 1:
            num1 += 1
        elif row['topic'] == 2:
            num2 +=1
        elif row['topic'] == 3:
            num3 +=1
        elif row['topic'] == 4:
            num4 +=1
        elif row['topic'] == 5:
            num5 +=1
        elif row['topic'] == 6:
            num6 +=1

    total = num1 + num2 + num3 + num4 + num5 + num6

    dict = {1: num1, 2: num2, 3:num3, 4:num4, 5:num5, 6:num6, "total": total}

    return dict


def num_tweets_sentiments ():
    pos = 0
    neg = 0
    neu = 0

    for index, row in df.iterrows():
        if row['sentiment'] == 'Positive':
            pos +=1
        elif row['sentiment'] == 'Negative':
            neg +=1
        elif row['sentiment'] == 'Neutral':
            neu +=1

    total = pos + neg + neu
    dict = {'Positive': pos, 'Negative':neg, 'Neutral': neu, 'Total': total}

    return dict

def num_tweets_topic_sentiment_combo():
    topic = [1,2,3,4,5,6]
    sentiment = ['Positive', 'Negative', 'Neutral']
    dict = {}
    total = 0


    for i in topic:
        for j in sentiment:
            key = str(i) + " and " + j
            val = 0
            for index, row in df.iterrows():
                if row ['topic'] == i and row['sentiment'] == j:
                    val +=1
                    dict[key] = val


    for key,value in dict.items():
        total += value

    dict['total'] = total

    return dict





print(num_tweets_category())
print(num_tweets_sentiments())
print(num_tweets_topic_sentiment_combo())