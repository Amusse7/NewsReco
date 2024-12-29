from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_articles(user_input, articles_df):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(articles_df['description'].fillna(''))
    
    user_query_tfidf = tfidf.transform([user_input])
    cosine_sim = cosine_similarity(user_query_tfidf, tfidf_matrix).flatten()
    
    articles_df['similarity'] = cosine_sim
    return articles_df.sort_values(by='similarity', ascending=False).head(5)
