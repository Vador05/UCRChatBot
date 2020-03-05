#  >>> import nltk
#  >>> nltk.download('stopwords')


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
import csv

words=[]
classes = []
documents = []
ignore_words = ['?', '!', ',', '.']
csv_file = open('questions.csv')
csv_data = csv.reader(csv_file)
matrix = list(csv_data)
for i in range(1,len(matrix)-1):
    # tokenize each word
    w = nltk.word_tokenize(matrix[i][1])
    words.extend(w)
    # add documents in the corpus
    documents.append((w, matrix[i][0]))

    # add to our classes list
    if matrix[i][0] not in classes:
        classes.append(matrix[i][0])

# lemmaztize and lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
stopWords = set(stopwords.words('english'))
wordsFiltered = []
for w in words:
    # From 323 unique words we filter stopwords -> 267 unique words
    # From 267 unique words we filter less than 4 letter words -> 229 unique words
    if (w not in stopWords) and (len(w)>3):
        wordsFiltered.append(w)
# sort classes
classes = sorted(list(set(classes)))
# documents = combination between patterns and intents
print("#############################################################")
print("                  Preprocessing Result:")
print("#############################################################")


print(len(documents), "documents\n")
# classes = intents
print(len(classes), "classes", classes,"\n")
# words = all words, vocabulary
print(len(wordsFiltered), "unique lemmatized words", wordsFiltered, "\n")
