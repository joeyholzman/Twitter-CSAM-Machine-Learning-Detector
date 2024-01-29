#Imports
import csv
import os
import glob
import json
import re
import string
import pandas as pd
import numpy as np

#SciKit
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB

#NLTK
import nltk
from nltk.tokenize import TweetTokenizer

#Get Number of Folders - FIX
path = "./Tweet Datasets"

def count_folders(path):
  count = 0
  for folder in os.listdir(path):
    if os.path.isfile(os.path.join(path, folder)):
      count += 1
  return count

number_of_folders = count_folders(path)
print(number_of_folders)

#Iterate through #jailbait csv files
path = "./Tweet Datasets/collections - #jailbait/*.csv"
file_names = []
for fname in glob.glob(path):
    file_names.append(fname)

def returnFileNames(index):
    return file_names[index]

currentFile = 0
noise_amp = []

while (currentFile < len(file_names)):
    file_path = returnFileNames(currentFile)

    if os.path.exists(file_path):
        with open(file_path, 'r') as rf:
            csv_reader = csv.reader(rf, delimiter=',')
            for row in csv_reader:
                if len(row) >= 2:
                    noise_amp.append(row[1])
    else:
        print(f"File not found: {file_path}")
    currentFile = currentFile + 1

print(noise_amp)

#TweetTokenizer

#Need to decide how to clean punctuation from text without cleaning #s

def cleanText(text):
    text_nonum = re.sub(r'\d+', '', text)
    text_nopunct = "".join([char.lower() for char in text_nonum if char not in string.punctuation]) 
    text_no_doublespace = re.sub('\s+', ' ', text_nopunct).strip()
    return text_no_doublespace

tokenized_tweets = []

for i in range(0, len(noise_amp)):
    tweet_tokenizer = TweetTokenizer()
    tweet_tokens = tweet_tokenizer.tokenize(noise_amp[i])
    tokenized_tweets.append(tweet_tokens)

#Writes Tweets to Tokenizer. When I classify each tweet manually, ill figure something

with open('./Tweet_Datasets/Tokenized_Tweets/Tokenized_Tweets.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["text"]
    writer.writerow(field)
    for i in range(0, len(tokenized_tweets)):
        writer.writerow(tokenized_tweets[i])

#I will probably want to write the tokenized tweets to a json file instead of a csv
with open('./Tweet_Datasets/Tokenized_Tweets/Tokenized_Tweets.json', 'w') as f:
    for i in range(0, len(tokenized_tweets)):
        json.dump(tokenized_tweets[i], f, indent=6)
