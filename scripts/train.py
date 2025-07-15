import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle


df = pd.read_csv('dataset/cleaned_movies.csv')


df['tags'] = df['tags'] + ' ' + df['genre'] + ' ' + df['actor'] + ' ' + df['language']


cv = CountVectorizer(stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()


similarity = cosine_similarity(vectors)


pickle.dump(df, open('pkl/movies.pkl', 'wb'))
pickle.dump(similarity, open('pkl/similarity.pkl', 'wb'))