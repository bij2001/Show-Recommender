#EXTRACT TITLES
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#The dataset we are using here is from IMDB dataset of 5000 movies.
#Step1: Read the CSV File.
df = pd.read_csv("netflix_titles.csv")

#print(df.head()) #Printing head of data for veryfying.

#Step2: Select Features:
new_df=df['title']

##Dump Picke File
pickle.dump(new_df,open('movies.pkl','wb'))

