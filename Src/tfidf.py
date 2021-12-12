import json
import math
import pandas as pd
import re
import os
import math


from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer


ps = PorterStemmer()
lemma_function = WordNetLemmatizer()

file_path = "../Data/annotatedTweets/combo_annotated_complete_table_comp_598-sample2OfSize1000.csv"
is_combo = False
is_stem = False
is_lemma = False #this might required using python in your command line to download the appropriate files

# extract all the text from the csv and store in a list.
def extract_text ():
    dict = {}
    df = pd.read_csv(file_path);

    for idx, row in df.iterrows():
        if is_combo:
            dict[row["text"]] = row["combo"]
        else:
            dict[row["text"]] = row["topic"]

    return dict

# extract all the text from the csv and store in a list.
def under_threshold_words(min_freq):
    dict = {}
    lst = extract_text()
    lst = remove_punct(lst)
    # go through each element and check if each vacabs have been stored in the dictionary.

    for text, topic in lst.items():
        for i in text.split():
            try:
                dict[i] += 1
            except:
                dict[i] = 1
    infrequent_words = set()
    for word, freq in dict.items():
        if freq < 5:
            infrequent_words.add(word)

    return infrequent_words




#go through the list and remove all the stop words and punctuations
def remove_punct(dict):
    stop_word = []


    # find the stopword.txt path
    dir = os.path.dirname(__file__)
    stopword_path = os.path.join(dir, '..', 'data', 'stopwords.txt')

    with open(stopword_path, 'r') as f:
        lines = f.readlines()
        for i in lines:
            i = i.strip('\n')
            stop_word.append(i)

    new_dict = {}

    for text,topic in dict.items():
        # remove the urls
        text = re.sub(r'http\S+', '', text)
        # remove the punctuations
        text = re.sub(r'[\(\)\[\]\,\-\.\?\!\:\;\#\&\’\%\@\”\"\'\‘\“\| ]+', " ", text)

        new_dict[text] = topic

    # remove stopwords
    res = {}
    for text, topic in new_dict.items():
        lst = []
        for i in text.split():
            if i.lower() not in stop_word:
                if is_stem:
                    lst.append(ps.stem(i.lower()))
                elif is_lemma:
                    lst.append(lemma_function.lemmatize(i.lower()))
                else:
                    lst.append(i.lower())
                s = ' '.join(lst)

        res[s]= topic


    # return a dictionary with filtered text as a key and corresponding topic as a value
    return res



def num_words_each_topic():
    num_words_in_topic = {}
    lst = extract_text()
    lst = remove_punct(lst)
    all_topics = set()
    for text, topic in lst.items():
        all_topics.add(topic)
    for topic in all_topics:
        num_words_in_topic[topic] = 0

    for t in all_topics:
        for text, topic in lst.items():
            # check the topic
            if topic == t:
                num_words_in_topic[t] += len(text.split())
            else:
                pass
    return num_words_in_topic


def tf (t):
    dict = {}
    lst = extract_text()
    lst = remove_punct(lst)
    # go through each element and check if each vacabs have been stored in the dictionary.

    for text, topic in lst.items():
        # check the topic
        if topic == t:
            for i in text.split():
                try:
                    dict[i] += 1
                except:
                    dict[i] = 1
        else:
            pass

    num_words_in_topic = num_words_each_topic()[t]

    for word in dict:
        dict[word] = float(dict[word] / num_words_in_topic)

    return dict



def idf ():
    dict = {}
    res = {}

    lst = extract_text()
    lst = remove_punct(lst)

    #go through the filtered dictionary and check how many words appear in the data
    for text, topic in lst.items():
        tweet_words_prev_seen = set()
        for j in text.split():
            if j not in tweet_words_prev_seen:
                try:
                    dict[j] += 1
                except:
                    dict[j] = 1
                tweet_words_prev_seen.add(j)

    # go through the dictionary again and calculate idf
    for word, count in dict.items():
        res[word] = math.log(1000/count, 10)



    return res

# eliminating the data that shows up less than a certain threshold.
def threshold (dict, threshold):
    words_under_thresh = under_threshold_words(threshold)
    new_dict = {}
    for text, topic in dict.items():
        if text not in words_under_thresh:
            new_dict[text] = topic
        else:
            pass

    return new_dict




def tf_idf (topic, thres):


    tf_dict = tf(topic)
    tf_dict = threshold(tf_dict,thres)
    idf_dict = idf()
    #idf_dict = threshold(idf_dict, thres)

    tf_idf = {}

    for (k, v), (k2, v2) in zip(tf_dict.items(), idf_dict.items()):
        tf_idf[k] = v*v2

    tf_idf = dict(sorted(tf_idf.items(), key=lambda item: -item[1]))
    tf_idf_list = [(k, v) for k, v in tf_idf.items()]



    return tf_idf_list

topics = [1,2,3,4,5,6]
min_threshold = 5
is_unique = True
#is_combo is at the top of this file

if is_combo:
    topics = ['1Positive', '1Neutral', '1Negative',
              '2Positive', '2Neutral', '2Negative',
              '3Positive', '3Neutral', '3Negative',
              '4Positive', '4Neutral', '4Negative',
              '5Positive', '5Neutral', '5Negative',
              '6Positive', '6Neutral', '6Negative',]

all_tfidfs = {}
for topic in topics:
    all_tfidfs[topic] = tf_idf(topic, min_threshold)

if is_unique:
    word_max_scores = {}
    word_max_topic = {}
    for topic, tfidf in all_tfidfs.items():
        for word, score in tfidf:
            current_max = word_max_scores.get(word, 0.0)
            if score > current_max:
                word_max_scores[word] = score
                word_max_topic[word] = topic


    all_tfidfs_unique = {}
    for topic in topics:
        all_tfidfs_unique[topic] = []

    for topic, tfidf in all_tfidfs.items():
        for word, score in tfidf:
            if word_max_topic[word] == topic:
                all_tfidfs_unique[topic].append((word, score))

    all_tfidfs = all_tfidfs_unique
    a=1

for topic, tfidf in all_tfidfs.items():
    print('topic:\t' + str(topic))
    # print(idf())
    #print(tf(topic))
    tfidf_top_25 = tfidf[:25]
    print(tfidf_top_25)
    print('--------------------')




