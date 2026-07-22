import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()

matrix = vectorizer.fit_transform(movies["genre"])

similarity = cosine_similarity(matrix)


def recommend(movie):

    movie = movie.lower()

    if movie not in movies["title"].str.lower().values:
        return None

    index = movies[movies["title"].str.lower() == movie].index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i in scores[1:6]:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations