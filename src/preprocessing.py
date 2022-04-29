# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite da Silva - drigols <drigols.creative@gmail.com>
# License: MIT
"""
The :mod:`preprocessing.py` apply preprocessing for text documents.
"""

import pandas as pd
import scipy.sparse
import platform
import datetime
import py7zr
import nltk
import os

from collections import Counter
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


class Preprocessing:

  def extract_7z_data(self, path):
    start_time = datetime.now()
    if platform.system() == 'Windows':
      try:
        # For Windows users.
        with py7zr.SevenZipFile(path, mode='r') as archive:
          archive.extractall(path="C:\Windows\Temp")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("File extracted!")
    elif platform.system() == 'Linux':
      try:
        # For Linux users.
        with py7zr.SevenZipFile(path, mode='r') as archive:
          archive.extractall(path="/tmp")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("File extracted!")
    else:
      print("This method only works with Windows and Linux Operating Systems.")
    end_time = datetime.now()
    print('Method runtime: {}'.format(end_time - start_time))


  def get_training_data(self):
    start_time = datetime.now()
    if platform.system() == 'Windows':
      try:
        # For Windows users.
        df_training = pd.read_csv("C:\Windows\Temp\Train_rev1.csv")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Training data ready!")
        end_time = datetime.now()
        print('Method runtime: {}'.format(end_time - start_time))
        return df_training
    elif platform.system() == 'Linux':
      try:
        # For Linux users.
        df_training = pd.read_csv("/tmp/Train_rev1.csv")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Training data ready!")
        end_time = datetime.now()
        print('Method runtime: {}'.format(end_time - start_time))
        return df_training


  def get_testing_data(self):
    start_time = datetime.now()
    if platform.system() == 'Windows':
      try:
        # For Windows users.
        df_testing = pd.read_csv("C:\Windows\Temp\Test_rev1.csv")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Testing data ready!")
        end_time = datetime.now()
        print('Method runtime: {}'.format(end_time - start_time))
        return df_testing
    elif platform.system() == 'Linux':
      try:
        # For Linux users.
        df_testing = pd.read_csv("/tmp/Test_rev1.7z")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Testing data ready!")
        end_time = datetime.now()
        print('Method runtime: {}'.format(end_time - start_time))
        return df_testing


  def missing_by_numbers(self, df):
    missing = df.isnull().sum()
    return missing


  def missing_by_percent(self, df):
    try:
      percentMissing = (df.isnull().sum() / len(df.index)) * 100
    except ZeroDivisionError:
      print("Sorry! You are dividing by zero.")
    else:
      return percentMissing


  def apply_lower_casing(self, df):
    df = df.str.lower()
    return df


  def remove_punctuations(self, df):
    df = df.str.replace('[^\w\s]',' ', regex=True)
    return df


  def remove_numbers(self, df):
    df = df.str.replace('[0-9]+', '', regex=True)
    return df


  def apply_stemming(self, df):
    start_time = datetime.now()
    stemmer = PorterStemmer() # Instance.
    return " ".join([stemmer.stem(word) for word in str(df).split() ])


  def apply_lemmatization(self, df):
    try:
      lemmatizer = WordNetLemmatizer()
      wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV} # Apply dict mapping.
      pos_tagged_text = nltk.pos_tag(df.split())
      return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])
      print("Lemmatization concluded!")
    except (LookupError, OSError):
      nltk.download('wordnet')
      nltk.download('omw-1.4')
      nltk.download('averaged_perceptron_tagger')
    finally:
      lemmatizer = WordNetLemmatizer()
      wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV} # Apply dict mapping.
      pos_tagged_text = nltk.pos_tag(df.split())
      return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])


  def check_most_common_words(self, df):
    start_time = datetime.now()
    cnt_df = Counter() # Instance
    for text in df.values:
      for word in text.split():
        cnt_df[word] += 1
    df_most_common = pd.DataFrame(
      cnt_df.most_common(),
      columns = ["Word", "Frequency"]
    )
    end_time = datetime.now()
    print('Method runtime: {}'.format(end_time - start_time))
    return df_most_common.sort_values(by=["Frequency"], ascending=False)


  def apply_tfidf_vectorizer(self, df, max_df=1, min_df=1):
    start_time = datetime.now()
    vectorizer = TfidfVectorizer(
      stop_words="english",
      max_df = max_df,
      min_df = min_df,
    )
    df_vectorized = vectorizer.fit_transform(df)
    end_time = datetime.now()
    print("DataFrame Vectorized!")
    print('Method runtime: {}'.format(end_time - start_time))
    return df_vectorized


  def save_feature(self, feature_name, feature):
    scipy.sparse.save_npz(f"../resources/processed_features/{feature_name}", feature)
    print("Feature saved!")


  def save_to_csv(self, df, df_name):
    df.to_csv(
      path_or_buf=f"../resources/load/{df_name}.csv",
      header=True,
      encoding='utf-8',
      index=False,
    )
    print("DataFrame saved!")
