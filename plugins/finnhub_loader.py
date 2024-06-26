import finnhub


def scrape_news():
    finnhub_client = finnhub.Client(api_key="cptpi21r01qnga5iktmgcptpi21r01qnga5iktn0")

    news = finnhub_client.general_news('general', min_id=0)

    return news
