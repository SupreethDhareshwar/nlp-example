"""
@author: Supreeth D
ID : 2019HT12489
"""
import os
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk.probability import FreqDist
import helpers

#Analyses Document Corpus
print("Analyzing Corpus")
soup = helpers.parseCorpus()
totalWordCount = 0
unigramFrequencies = Counter([])
bigramFrequencies = Counter([])
trigramFrequencies = Counter([])
unigramStemFrequencies = Counter([])
bigramStemFrequencies = Counter([])
trigramStemFrequencies = Counter([])
for doc_tag in soup.find_all('doc'):
    token = word_tokenize(doc_tag.text)
    totalWordCount += len(token)
    unigrams = ngrams(token, 1)
    bigrams = ngrams(token, 2)    
    trigrams = ngrams(token, 3)
    unigramFrequencies += Counter(unigrams)
    bigramFrequencies += Counter(bigrams)
    trigramFrequencies += Counter(trigrams)

    #Stem all the tokens
    stemmed_words = helpers.stem_words(token)

    unigramsStem = ngrams(stemmed_words, 1)
    bigramsStem = ngrams(stemmed_words, 2)    
    trigramsStem = ngrams(stemmed_words, 3)
    unigramStemFrequencies += Counter(unigramsStem)
    bigramStemFrequencies += Counter(bigramsStem)
    trigramStemFrequencies += Counter(trigramsStem)

corpus90count = 0.9 * totalWordCount
#Before Stemming
print("Total unique unigrams : ",len(unigramFrequencies))
freqDistUni = FreqDist(unigramFrequencies)  
freqDistUniMostCommon = freqDistUni.most_common()
freqDistUni.plot(50,title="Plot of the 50 most common 1-grams")   

print("Total unique bigrams : ",len(bigramFrequencies))
freqDistBi = FreqDist(bigramFrequencies)  
freqDistBiMostCommon = freqDistBi.most_common()

freqDistBi.plot(50,title="Plot of the 50 most common 2-grams")   

print("Total unique trigrams : ",len(trigramFrequencies))
freqDistTri = FreqDist(trigramFrequencies)  
freqDistTriMostCommon = freqDistTri.most_common()

freqDistTri.plot(50,title="Plot of the 50 most common 3-grams")   

#After Stemming
print("Total unique unigrams after stemming : ",len(unigramStemFrequencies))
freqDistUniStem = FreqDist(unigramStemFrequencies)  
freqDistUniStemMostCommon = freqDistUniStem.most_common()

freqDistUniStem.plot(50,title="Plot of the 50 most common 1-grams after stemming")   

print("Total unique bigrams after stemming : ",len(bigramStemFrequencies))
freqDistBiStem = FreqDist(bigramStemFrequencies)  
freqDistBiStemMostCommon = freqDistBiStem.most_common()

freqDistBiStem.plot(50,title="Plot of the 50 most common 2-grams after stemming")   

print("Total unique trigrams after stemming : ",len(trigramStemFrequencies)) 
freqDistTriStem = FreqDist(trigramStemFrequencies)  
freqDistTriStemMostCommon = freqDistTriStem.most_common()

freqDistTriStem.plot(50,title="Plot of the 50 most common 3-grams after stemming")   
