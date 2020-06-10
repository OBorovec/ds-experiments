def load_train_data():
    raise NotImplementedError


def load_test_data():
    raise NotImplementedError


import re
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet, stopwords

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
LEMMATIZER = WordNetLemmatizer()
ENGLISH_STOP_WORDS = set(stopwords.words("english"))

def clean_text_en(text):
    soup = BeautifulSoup(text)
    text = soup.get_text()
    text = text.replace('\n', ' ')
    text = REPLACE_NO_SPACE.sub("", text.lower())
    text = REPLACE_WITH_SPACE.sub(" ", text)
    words = nltk.word_tokenize(text)
    words = [LEMMATIZER.lemmatize(word, wordnet.VERB) for word in words]
    words = [word for word in words if not word in ENGLISH_STOP_WORDS]
    return ' '.join(words)