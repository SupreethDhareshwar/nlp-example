import os
from collections import defaultdict
import math
import string
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer 
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk import word_tokenize

resources_path = os.path.join(os.getcwd(), 'wiki_00')

def parseCorpus():
    fp = open(file = resources_path, mode= "r", encoding="utf8")
    soup = BeautifulSoup(fp,features="html.parser")
    return soup

def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

def processResults(n,ngramFrequencies,totalWordCount):
    freqDist = FreqDist(ngramFrequencies)  
    freqDistMostCommon = freqDist.most_common()

    corpus90count = 0.9 * totalWordCount
    gramIndexCount = 0
    totalGramFrequencyCount = 0
    values = []
    for k,v in freqDistMostCommon:
        if totalGramFrequencyCount < corpus90count:
            totalGramFrequencyCount += v
            gramIndexCount +=1
        values.append(v)

    print('Total unique {}-grams : {}'.format(n,len(ngramFrequencies)))  

    print('{}-grams required to cover 90% of the complete corpus : {}'.format(n,gramIndexCount)) 
    # plt.xscale("log")
    # plt.yscale("log")
    
    # fig = plt.figure() 
   
    # ax = fig.add_axes([0,0,2,1]) 
    # ax.plot(values) 
    # # naming the x axis 
    # ax.set_xlabel('Rank') 
    # # naming the y axis 
    # ax.set_ylabel('Word Count') 
    # # giving a title to  graph 
    # display = "Frequency Distribution of {n}-grams" 
    # ax.set_title("Word Distribution") 

    # plt.show()

    
    fig = plt.figure(figsize = (10,6))
    fig.subplots_adjust(bottom=0.45) # to avoid x-ticks cut-off
    # plt.xscale("log")
    # plt.yscale("log")
    plotCount = 50
    display = "Plot of the {plotCount} most common {n}-grams"
    freqDist.plot(plotCount,title=display.format(plotCount = plotCount,n=n), cumulative=False)
    return

# def oldcode():
#     plt.figure(figsize = (10,6))
#     plt.gcf().subplots_adjust(bottom=0.45) # to avoid x-ticks cut-off

#     plotCount = 50
#     display = "Plot of the {plotCount} most common {n}-grams"
#     freqDist.plot(plotCount,title=display.format(plotCount = plotCount,n=n), cumulative=False)  
#     plt.show()
#     return

def compute_idf(corpus):
    num_docs = len(corpus)
    idf = defaultdict(lambda: 0)
    for doc in corpus:
        for word in doc.keys():
            idf[word] += 1

    for word, value in idf.items():
        idf[word] = math.log(num_docs / value)
    return idf


def compute_weights(idf, doc):
    for word, value in doc.items():
        # doc[word] = idf[word] * (1 + math.log(value))
        doc[word] =  (1 + math.log(value))



def normalize(doc):
    denominator = math.sqrt(sum([e ** 2 for e in doc.values()]))
    for word, value in doc.items():
        doc[word] = value / denominator


def build_inverted_index(idf, corpus):
    inverted_index = {}
    for word, value in idf.items():
        inverted_index[word] = {}
        inverted_index[word]['idf'] = value
        inverted_index[word]['postings_list'] = []

    for index, doc in enumerate(corpus):
        for word, value in doc.items():
            inverted_index[word]['postings_list'].append([index, value])

    return inverted_index

def remove_punctuations(text):
    out = text.translate(str.maketrans('', '', string.punctuation))
    return out

def preprocess_text(text):
    processed_text = remove_punctuations(text.lower())
    words = word_tokenize(processed_text)
    return words