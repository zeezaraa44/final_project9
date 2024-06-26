import re
from textblob import TextBlob


class SentimentAnalysis:

    def __init__(self, text):
        self.text = text

    def execute(self):
        analysis = TextBlob(self.text)

        if analysis.sentiment.polarity > 0:
            data = {'text': self.text, 'sentiment': 'positive'}
        elif analysis.sentiment.polarity == 0:
            data = {'text': self.text, 'sentiment': 'neutral'}
        else:
            data = {'text': self.text, 'sentiment': 'negative'}

        return data


if __name__ == "__main__":
    SentimentAnalysis("hard to learn NLTK").execute()
