import json
import math
import pandas as pd
import re
import os
import math


# extract all the text from the csv and store in a list.
def extract_text ():
    dict = {}
    df = pd.read_csv("../Data/badTopics/fakeTopicToCalcTFIDF.csv");

    for idx, row in df.iterrows():
        dict[row["text"]] = row["topic"]

    return dict



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
                lst.append(i.lower())
                s = ' '.join(lst)

        res[s]= topic


    # return a dictionary with filtered text as a key and corresponding topic as a value
    return res



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


    return dict



def idf ():
    dict = {}
    res = {}

    lst = extract_text()
    lst = remove_punct(lst)

    #go through the filtered dictionary and check how many words appear in the data
    for text, topic in lst.items():
        for j in text.split():
            try:
                dict[j] += 1
            except:
                dict[j] = 1

    # go through the dictionary again and calculate idf
    for word, count in dict.items():
        res[word] = math.log(1000/count)



    return res

# eliminating the data that shows up less than a certain threshold.
def threshold (dict, threshold):
    new_dict = {}
    for text, topic in dict.items():
        if topic > threshold:
            new_dict[text] = topic
        else:
            pass

    return new_dict




def tf_idf ( topic, thres):

    tf_dict = tf(topic)
    tf_dict = threshold(tf_dict,thres)
    idf_dict = idf()
    idf_dict = threshold(idf_dict, thres)

    tf_idf = {}

    for (k, v), (k2, v2) in zip(tf_dict.items(), idf_dict.items()):
        tf_idf[k] = v*v2

    return tf_idf




print(idf())
print(tf('Other'))
print(tf_idf('Other',0))


