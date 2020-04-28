import pickle
import os
import sys
import math
import helpers
from collections import Counter

#Set the output files generate from createIndex Code
docs_file = os.path.join(os.getcwd(), 'data', 'docs.pickle')
inverted_index_file = os.path.join(os.getcwd(), 'data', 'inverted_index.pickle')

# Deserialize data and read the output file
with open(docs_file, 'rb') as f:
    docs = pickle.load(f)
with open(inverted_index_file, 'rb') as f:
    inverted_index = pickle.load(f)

#Set dictionary of unique words
dictionary = set(inverted_index.keys())

# Get query from command line
query = sys.argv[1]

# Preprocess query, lookup word in dictionary and set the frequency of words
query = helpers.preprocess_text(query)
query = [word for word in query if word in dictionary]
query = Counter(query)

# Compute weights for words in query
for word, value in query.items():
    query[word] = inverted_index[word]['idf'] * (1 + math.log(value))

#Normalize the weights
helpers.normalize(query)

#Calculate the score of query wrt to each document
scores = [[i, 0] for i in range(len(docs))]
for word, value in query.items():
    for doc in inverted_index[word]['postings_list']:
        index, weight = doc
        scores[index][1] += value * weight

#Sort the scores in reverse order with highest score first
scores.sort(key=lambda doc: doc[1], reverse=True)

#Print only top 10 scores
print('----- Results ------ ')
for index, score in enumerate(scores):
    if score[1] == 0:
        break
    print('{}. {} - {}'.format(index + 1, docs[score[0]], score[1]))
    if index == 9:
        break
