import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv('movies_dataset.csv')

cv = CountVectorizer()
vectors = cv.fit_transform(df['tags']).toarray()

similarity = cosine_similarity(vectors)

pickle.dump(df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("Training completed and files saved.")