import string
import re
import nltk
import spellchecker.spellchecker 

from nltk import word_tokenize, sent_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer


def removePunctuation(text):
    punctuationfree = "".join([i for i in text if i not in string.punctuation])
    punctuationfree = punctuationfree.lower()
    return punctuationfree

def spellingChecker(words):
    correct = []
    checker = spellchecker.spellchecker.SpellChecker()
    for word in words:
        correct.append(checker.correction(word))
    return correct
        
def removeStopWords(words):
    enStopWords = stopwords.words('english')
    requiredWords = []
    for word in words:
        if word not in enStopWords:
            requiredWords.append(word)
    return requiredWords

def stemming(words):
    porter = PorterStemmer()
    result=[]
    for word in words:
        result.append(porter.stem(word))
    return result

    
def lemmatization(words):
    lemmatized = []
    wordnet = WordNetLemmatizer()
    for word in words:
        if(str(type(word)) != "<class 'NoneType'>"):
            lemmatized.append(wordnet.lemmatize(word))
    return lemmatized

def tokenize(text):
    sentences = sent_tokenize(text)
    sentenceWords = []
    for sentence in sentences:
        wordsInSentence = word_tokenize(removePunctuation(sentence))
        sentenceWords.append(stemming(lemmatization(removeStopWords(spellingChecker(wordsInSentence)))))
    return sentenceWords

def preprocess(text):
    return tokenize(text)