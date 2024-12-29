# News Recommender 💬

A personalized news recommendation system built with Flask that fetches and recommends news articles based on user interests using NLP techniques.

## 🌟 Features

- Real-time news fetching using NewsAPI
- Content-based article recommendations using TF-IDF and cosine similarity
- Simple and responsive web interface
- Search functionality for specific topics/interests

## 🛠️ Prerequisites

Before running the project, ensure you have:

- Python 3.7+
- NewsAPI Key (Get one from https://newsapi.org)

## 📦 Installation

1. Clone the Repository:

```bash
git clone https://github.com/Amusse7/NewsReco

cd NewsReco
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your NewsAPI key:

   - Open `bash config.py`
   - Replace `bash YOUR_NEWS_API_KEY` with your actual NewsAPI key

## Project Structure 🚧

```bash
news/
├── app.py                  # Main Flask application
├── config.py              # Configuration file for API keys
├── requirements.txt       # Python dependencies
├── services/             # Service scripts
│   ├── news_fetcher.py   # News fetching service
│   ├── recommender.py    # Recommendation engine
├── static/               # Static files
│   └── styles.css        # CSS styles
├── templates/            # HTML templates
│   └── home.html        # Main page template
```

## 🚀 Usage

1. Start the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to:

```bash
http://localhost:5000
```

## Results ⌛

<img src="Screenshot.png" alt="Demo" width="600"/>
