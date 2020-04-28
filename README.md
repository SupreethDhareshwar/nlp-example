# Installation and Usage Guidelines

## Pre-requisuites

* This project uses python 3.8 running on windows 10
* Run `py -m pip install <package_name>` for installing packages like nltk, BeautifulSoup and matplotlib
Example : `py -m pip install nltk` and `py -m pip install beautifulsoup4` `py -m pip install matplotlib`
* For nltk, if you get punkt error, run on python shell the following :
    `import nltk
    nltk.download('punkt')`
* Open https://drive.google.com/drive/folders/1ZsnuEm7_N6aUwhjFpv-TZXFt4DiYex4t
* Download the file AF/wiki_63
* Copy the file into current project directory and rename it as wiki_00

## Running the project 

### Corpus Analysis (Part 1)
* cd to the project directory
* Run `py .\analyzeCorpus.py`
* This will take 5-10 mins to process. Each Figure is plotted one at a time
* Close the figure to continue seeing plots of other n-gram figures

### Vector Space Model (Part 2)
1) Creating Index
* cd to the project directory
* Run `py .\createIndex.py`
* This will analyze the input wiki corpus file and generate inverted index in a separate data folder

2) Running Query on Inverted Index
* cd to the project directory
* This query.py will query and read only the output files from the Index Creation Code and not the corpus
* Run `py .\query.py "<query_text>"` to query the inverted index and get the top 10 results. Example: `py .\query.py "7th infantry"` 

**Note** : I have kept general helper functions in a separate helpers.py . This contains common functions used by the above 3 files.




