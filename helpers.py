"""
@author: Supreeth Dhareshwar
ID : 2019HT12489
"""
import os
from collections import defaultdict
import math
import string
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer 
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk import word_tokenize

#Path to wiki corpus file
resources_path = os.path.join(os.getcwd(), 'wiki_00')

#Parse the corpus by using beautiful soup which can separate each document and ignore <a> tags
def parseCorpus():
    fp = open(file = resources_path, mode= "r", encoding="utf8")
    soup = BeautifulSoup(fp,features="html.parser")
    return soup

#Use Porter Stemmer to stem all words
def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

#Process the output of corpus Analysis
def processResults(n,ngramFrequencies,totalWordCount):
    freqDist = FreqDist(ngramFrequencies)  
    #Get n-grams sorted from highest to lowest frequencies
    freqDistMostCommon = freqDist.most_common()

    #Count of 90% of corpus words
    corpus90count = 0.9 * totalWordCount

    gramIndexCount = 0
    totalGramFrequencyCount = 0
    # values = []
    for k,v in freqDistMostCommon:
        if totalGramFrequencyCount < corpus90count:
            totalGramFrequencyCount += v
            gramIndexCount +=1
        else:
            break    
        # values.append(v)

    #Get total n-gram length
    print('Total unique {}-grams : {}'.format(n,len(ngramFrequencies)))  

    print('{}-grams required to cover 90% of the complete corpus : {}'.format(n,gramIndexCount)) 
  
    # fig = plt.figure() 
    # plt.xscale("log")
    # plt.yscale("log")
    # ax = fig.add_axes([0,0,2,1]) 
    # ax.plot(values) 
    # # naming the x axis 
    # ax.set_xlabel('Rank') 
    # # naming the y axis 
    # ax.set_ylabel('Word Count') 
    # # giving a title to  graph 
    # display = "Frequency Distribution of {n}-grams" 
    # ax.set_title("Frequency Word Distribution") 
    # plt.show()

    fig = plt.figure(figsize = (10,6))
    fig.subplots_adjust(bottom=0.45) # to avoid x-ticks cut-off
   
    plotCount = 50
    display = "Plot of the {plotCount} most common {n}-grams"
    
    #Use NLTK Freq Dist to Plot 50 most common n-grams
    freqDist.plot(plotCount,title=display.format(plotCount = plotCount,n=n), cumulative=False)
    return

def compute_idf(corpus):
    # N - Total Number of Docs
    num_docs = len(corpus)
    idf = defaultdict(lambda: 0)
    
    #Calculate idf by getting count of how many docs the word is present 
    for doc in corpus:
        for word in doc.keys():
            idf[word] += 1

    #Calculate the idf of each word
    for word, value in idf.items():
        idf[word] = math.log(num_docs / value)
    return idf

#Compute weights of each word in document only by term frequency
def compute_weights(idf, doc):
    for word, value in doc.items():
        doc[word] =  (1 + math.log(value))

#Normalize the weights of each doc
def normalize(doc):
    denominator = math.sqrt(sum([e ** 2 for e in doc.values()]))
    for word, value in doc.items():
        doc[word] = value / denominator

#build inverted index of corpus
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

#Remove any puctuations in text
def remove_punctuations(text):
    out = text.translate(str.maketrans('', '', string.punctuation))
    return out

#preprocess the text by setting text to lowercase and remove punctuations
def preprocess_text(text):
    processed_text = remove_punctuations(text.lower())
    words = word_tokenize(processed_text)
    return words