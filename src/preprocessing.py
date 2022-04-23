from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

import pandas as pd
import scipy.sparse
import platform
import py7zr
import nltk
import os


class Preprocessing:

  def extract_7z_data(self, path):
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


  def get_training_data(self):
    if platform.system() == 'Windows':
      try:
        # For Windows users.
        df_training = pd.read_csv("C:\Windows\Temp\Train_rev1.csv")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Training data ready!")
        return df_training
    elif platform.system() == 'Linux':
      try:
        # For Linux users.
        df_training = pd.read_csv("/tmp/Train_rev1.csv")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Training data ready!")
        return df_training


  def get_testing_data(self): 
    if platform.system() == 'Windows':
      try:
        # For Windows users.
        df_testing = pd.read_csv("C:\Windows\Temp\Test_rev1.csv")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Testing data ready!")
        return df_testing
    elif platform.system() == 'Linux':
      try:
        # For Linux users.
        df_testing = pd.read_csv("/tmp/Test_rev1.7z")
      except FileNotFoundError:
        print("File or path not!")
      else:
        print("Testing data ready!")
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
    stemmer = PorterStemmer() # Instance.    
    return " ".join([stemmer.stem(word) for word in str(df).split()])
    print("Stemming concluded!")


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
      print("Lemmatization concluded!")


  def apply_countVectorizer(self, df):
    vectorizer = CountVectorizer(
      stop_words="english", # Add stopwords.
      max_df=0.60, # Ignores terms that appear in MORE than 60% of documents.
      min_df=0.05, # Ignores terms that appear in LESS than 5% of documents
    )
    df_vectorized = vectorizer.fit_transform(df)
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
