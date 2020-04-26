"""
@author: Supreeth D
ID : 2019HT12489
"""
import os
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import helpers

#Analyses Document Corpus
print("Analyzing Corpus")
soup = helpers.parseCorpus()

token = word_tokenize(cleaned_text)
totalWordCount = len(token)
unigrams = ngrams(token, 1)
bigrams = ngrams(token, 2)    
trigrams = ngrams(token, 3)

#Stem all the tokens
stemmed_words = helpers.stem_words(token)

unigramsStem = ngrams(stemmed_words, 1)
bigramsStem = ngrams(stemmed_words, 2)    
trigramsStem = ngrams(stemmed_words, 3)
   
#Before Stemming

print("Results before stemming")

helpers.processResults(n=1,ngramFrequencies=Counter(unigrams),totalWordCount=totalWordCount)

helpers.processResults(n=2,ngramFrequencies=Counter(bigrams),totalWordCount=totalWordCount)

helpers.processResults(n=3,ngramFrequencies=Counter(trigrams),totalWordCount=totalWordCount)

#After Stemming

print("Results after stemming")

helpers.processResults(n=1,ngramFrequencies=Counter(unigramsStem),totalWordCount=totalWordCount)

helpers.processResults(n=2,ngramFrequencies=Counter(bigramsStem),totalWordCount=totalWordCount)

helpers.processResults(n=3,ngramFrequencies=trigramStemFrequencies,totalWordCount=totalWordCount)
