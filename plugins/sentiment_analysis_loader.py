import mongodb_loader
import pandas as pd
from sentiment_analysis import SentimentAnalysis
import postgres_loader


def run_analysis():
    db = mongodb_loader.get("news", "finnhub_news")

    news = [x for x in db.finnhub_news.find()]

    output = []

    for news_summary in news:
        output.append(SentimentAnalysis(text=news_summary["summary"]).execute())

        print(f"Summary {news_summary['summary']} successfully analyzed")

    sentiment_output = pd.DataFrame(output)
    postgres_loader.load(sentiment_output, "sentiment_news_analysis")

    print("Successfully loaded to postgres")
