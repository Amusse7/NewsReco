from flask import Flask, request, render_template
from services.news_fetcher import fetch_news
from services.recommender import recommend_articles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_query = request.form.get("query")
        news_df = fetch_news()
        recommendations = recommend_articles(user_query, news_df)
        return render_template("home.html", query=user_query, articles=recommendations.to_dict(orient="records"))
    return render_template("home.html", query="", articles=[])

if __name__ == "__main__":
    app.run(debug=True)
