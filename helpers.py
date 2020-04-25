import os
from collections import defaultdict
import math
import string
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer 

ps = PorterStemmer() 

resources_path = os.path.join(os.getcwd(), 'wiki_02')

def parseCorpus():
    fp = open(file = resources_path, mode= "r", encoding="utf8")
    soup = BeautifulSoup(fp,features="html.parser")
    return soup

def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words
    
     
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
        doc[word] = idf[word] * (1 + math.log(value))


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
    words = processed_text.split()
    return words