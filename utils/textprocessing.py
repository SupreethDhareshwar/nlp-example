import string

''' Text processing '''


def remove_punctuations(text):
    # non_words = re.compile(r"[^a-z']")
    # processed_text = re.sub(non_words, ' ', text)

    out = text.translate(str.maketrans('', '', string.punctuation))
    return out


def remove_stopwords(text):
    words = [word for word in text.split()]
    return words

def preprocess_text(text):
    processed_text = remove_punctuations(text.lower())
    words = remove_stopwords(processed_text)
    return words
