import os
import sys
import pickle
import math
from collections import Counter
import helpers

data_path = os.path.join(os.getcwd(), 'data')

print('Building Index')

#Parse Html markup and get all the documents
soup = helpers.parseCorpus()

#Create data folder for the output files
if not os.path.exists(data_path):
    os.mkdir(data_path)

corpus = []
docs = []

#Update word frequencies per document and get titles of all docs
for doc_tag in soup.find_all('doc'):
    words = helpers.preprocess_text(doc_tag.text)
    bag_of_words = Counter(words)
    corpus.append(bag_of_words)
    docs.append(doc_tag["title"])

#Calculate IDF of all words in corpus
idf = helpers.compute_idf(corpus)

#Caclulate weights and normalize the weights of all words in document
for doc in corpus:
    helpers.compute_weights(idf, doc)
    helpers.normalize(doc)

#Build the inverted index of document with idf and posting list
inverted_index = helpers.build_inverted_index(idf, corpus)

#Set the output files path
docs_file = os.path.join(data_path, 'docs.pickle')
inverted_index_file = os.path.join(data_path, 'inverted_index.pickle')
dictionary_file = os.path.join(data_path, 'dictionary.txt')

# Serialize data and write doc titles array
with open(docs_file, 'wb') as f:
    pickle.dump(docs, f)

# Serialize data and write inverted index
with open(inverted_index_file, 'wb') as f:
    pickle.dump(inverted_index, f)

#Generate the dictionary for the corpus
with open(dictionary_file, 'w',encoding='utf-8') as f:
    for word in idf.keys():
        f.write(word + '\n')

print('Index creation completed. Output files are at data/')
