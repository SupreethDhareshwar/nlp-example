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
#Parse the html markup and retreive different documents
soup = helpers.parseCorpus()

#To keep track of all words in the corpus
totalWordCount = 0

#To keep track of unigram, bigram and trigram frequencies for tokens before stemming
unigramFrequencies = Counter([])
bigramFrequencies = Counter([])
trigramFrequencies = Counter([])

#To keep track of unigram, bigram and trigram frequencies for tokens after stemming
unigramStemFrequencies = Counter([])
bigramStemFrequencies = Counter([])
trigramStemFrequencies = Counter([])

#Iterate through each document
for doc_tag in soup.find_all('doc'):
    #Tokenize and lowercase the text
    tokens = word_tokenize(doc_tag.text)
    tokens= [token.lower() for token in tokens if not re.match(r'^[_\W]+$', token)]
    totalWordCount += len(tokens)

    #Calculate the unigrams, bigrams and trigrams for the tokens
    unigrams = ngrams(tokens, 1)
    bigrams = ngrams(tokens, 2)    
    trigrams = ngrams(tokens, 3)

    #Updating frequencies of words
    unigramFrequencies += Counter(unigrams)
    bigramFrequencies += Counter(bigrams)
    trigramFrequencies += Counter(trigrams)

    #Stem all the tokens
    stemmed_words = helpers.stem_words(tokens)

    #Calculate the unigrams, bigrams and trigrams for the tokens after stemming
    unigramsStem = ngrams(stemmed_words, 1)
    bigramsStem = ngrams(stemmed_words, 2)    
    trigramsStem = ngrams(stemmed_words, 3)

    #Updating frequencies of stemmed words
    unigramStemFrequencies += Counter(unigramsStem)
    bigramStemFrequencies += Counter(bigramsStem)
    trigramStemFrequencies += Counter(trigramsStem)

#Before Stemming processing
print("Results before stemming")

helpers.processResults(n=1,ngramFrequencies=unigramFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=2,ngramFrequencies=bigramFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=3,ngramFrequencies=trigramFrequencies,totalWordCount=totalWordCount)

#After Stemming processing
print("Results after stemming")

helpers.processResults(n=1,ngramFrequencies=unigramStemFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=2,ngramFrequencies=bigramStemFrequencies,totalWordCount=totalWordCount)
helpers.processResults(n=3,ngramFrequencies=trigramStemFrequencies,totalWordCount=totalWordCount)


