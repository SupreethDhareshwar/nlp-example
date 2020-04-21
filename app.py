"""
@author: Supreeth D
ID : 2019HT12489
"""
import os
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.stem import PorterStemmer 
from collections import Counter

ps = PorterStemmer() 

filename = "wiki_02"

with open(file = os.getcwd() + "\\"+filename, mode= "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp,features="html.parser")

#Analyses Document Corpus
def corpusAnalysis():
    print("Analysing Corpus")
    unigramFrequencies = Counter([])
    bigramFrequencies = Counter([])
    trigramFrequencies = Counter([])
    unigramStemFrequencies = Counter([])
    bigramStemFrequencies = Counter([])
    trigramStemFrequencies = Counter([])
    for doc_tag in soup.find_all('doc'):
        token = word_tokenize(doc_tag.text)
        unigrams = ngrams(token, 1)
        bigrams = ngrams(token, 2)    
        trigrams = ngrams(token, 3)
        unigramFrequencies += Counter(unigrams)
        bigramFrequencies += Counter(bigrams)
        trigramFrequencies += Counter(trigrams)

        #Stem all the tokens
        stemToken = []
        for w in token: 
            stemToken.append( ps.stem(w)) 

        unigramsStem = ngrams(stemToken, 1)
        bigramsStem = ngrams(stemToken, 2)    
        trigramsStem = ngrams(stemToken, 3)
        unigramStemFrequencies += Counter(unigramsStem)
        bigramStemFrequencies += Counter(bigramsStem)
        trigramStemFrequencies += Counter(trigramsStem)    
    return

#Start of Code
def main():
    print("Starting IR Code!")
    corpusAnalysis()
    print("Ending IR Code!")


if __name__ == "__main__":
    main() 