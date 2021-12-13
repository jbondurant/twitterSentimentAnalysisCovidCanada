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


def percentage_of_sentiment_within_topic():
    dict_num = num_tweets_category()
    dict_each_sentiment = num_tweets_topic_sentiment_combo()
    lst = []
    values1 = {}
    values2 = {}
    values3 = {}
    values4 = {}
    values5 = {}
    values6 = {}
    res = {}

    for i in dict_num.values():
        lst.append(i)

    for key,value in dict_each_sentiment.items():

        if '1 and Positive' == key:
            values1['Positive'] = (int(value)/int(lst[0]))
            res['topic 1'] = values1

        elif '1 and Negative' == key:
            values1['Negative'] = (int(value) / int(lst[0]))
            res['topic 1'] = values1

        elif '1 and Neutral' == key:
            values1['Neutral'] = (int(value) / int(lst[0]))
            res['topic 1'] = values1

        elif '2 and Positive' == key:
            values2['Positive'] = (int(value)/int(lst[1]))
            res['topic 2'] = values2

        elif '2 and Negative' == key:
            values2['Negative'] = (int(value) / int(lst[1]))
            res['topic 2'] = values2

        elif '2 and Neutral' == key:
            values3['Neutral'] = (int(value) / int(lst[1]))
            res['topic 2'] = values2

        elif '3 and Positive' ==  key:
            values3['Positive']=(int(value)/int(lst[2]))
            res['topic 3'] = values3

        elif '3 and Negative' == key:
            values3['Negative'] = (int(value) / int(lst[2]))
            res['topic 3'] = values3

        elif '3 and Neutral' == key:
            values3['Neutral'] = (int(value) / int(lst[2]))
            res['topic 3'] = values3

        elif '4 and Positive' == key:
            values4['Positive']=(int(value)/int(lst[3]))
            res['topic 4'] = values4

        elif '4 and Negative' == key:
            values4['Negative'] = (int(value) / int(lst[3]))
            res['topic 4'] = values4

        elif '4 and Neutral' == key:
            values4['Neutral'] = (int(value) / int(lst[3]))
            res['topic 4'] = values4

        elif '5 and Positive' == key:
            values5['Positive']=(int(value)/int(lst[4]))
            res['topic 5'] = values5

        elif '5 and Negative' == key:
            values5['Negative'] = (int(value) / int(lst[4]))
            res['topic 5'] = values5

        elif '5 and Neutral' == key:
            values5['Neutral'] = (int(value) / int(lst[4]))
            res['topic 5'] = values5

        elif '6 and Positive' == key:
            values6['Positive']=(int(value)/int(lst[5]))
            res['topic 6'] = values6

        elif '6 and Negative' == key:
            values6['Negative'] = (int(value) / int(lst[5]))
            res['topic 6'] = values6

        elif '6 and Neutral' == key:
            values6['Neutral'] = (int(value) / int(lst[5]))
            res['topic 6'] = values6




    return res





print(num_tweets_category())
print(num_tweets_sentiments())
print(num_tweets_topic_sentiment_combo())
print(percentage_of_sentiment_within_topic())
