import os
import sys
import pickle
import math
from collections import Counter
import  helpers
from bs4 import BeautifulSoup

''' Index data '''
resources_path = os.path.join(os.getcwd(), 'wiki_02')
data_path = os.path.join(os.getcwd(), 'data')

print('Indexing....')

with open(file = resources_path, mode= "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp,features="html.parser")


if not os.path.exists(data_path):
    os.mkdir(data_path)

corpus = []
docs = []

for doc_tag in soup.find_all('doc'):
    words = helpers.preprocess_text(doc_tag.text)
    bag_of_words = Counter(words)
    corpus.append(bag_of_words)
    docs.append(doc_tag["title"])

idf = helpers.compute_idf(corpus)
for doc in corpus:
    helpers.compute_weights(idf, doc)
    helpers.normalize(doc)

inverted_index = helpers.build_inverted_index(idf, corpus)

docs_file = os.path.join(data_path, 'docs.pickle')
inverted_index_file = os.path.join(data_path, 'inverted_index.pickle')
dictionary_file = os.path.join(data_path, 'dictionary.txt')

# Serialize data
with open(docs_file, 'wb',encoding='utf-8') as f:
    pickle.dump(docs, f)

with open(inverted_index_file, 'wb',encoding='utf-8') as f:
    pickle.dump(inverted_index, f)

with open(dictionary_file, 'w',encoding='utf-8') as f:
    for word in idf.keys():
        f.write(word + '\n')

print('Index done.')
