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
import re

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
    tokens = word_tokenize(doc_tag.text)
    tokens= [token.lower() for token in tokens if not re.match(r'^[_\W]+$', token)]
    totalWordCount += len(tokens)

    unigrams = ngrams(tokens, 1)
    bigrams = ngrams(tokens, 2)    
    trigrams = ngrams(tokens, 3)

    unigramFrequencies += Counter(unigrams)
    bigramFrequencies += Counter(bigrams)
    trigramFrequencies += Counter(trigrams)

    #Stem all the tokens
    stemmed_words = helpers.stem_words(tokens)

    unigramsStem = ngrams(stemmed_words, 1)
    bigramsStem = ngrams(stemmed_words, 2)    
    trigramsStem = ngrams(stemmed_words, 3)

    unigramStemFrequencies += Counter(unigramsStem)
    bigramStemFrequencies += Counter(bigramsStem)
    trigramStemFrequencies += Counter(trigramsStem)

#Before Stemming
print("Results before stemming")

helpers.processResults(n=1,ngramFrequencies=unigramFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=2,ngramFrequencies=bigramFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=3,ngramFrequencies=trigramFrequencies,totalWordCount=totalWordCount)

#After Stemming
print("Results after stemming")

helpers.processResults(n=1,ngramFrequencies=unigramStemFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=2,ngramFrequencies=bigramStemFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=3,ngramFrequencies=trigramStemFrequencies,totalWordCount=totalWordCount)


