import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import os

class ResearchAgent:
    def __init__(self):
        self.sources = [
            "https://www.shrm.org",
            "https://www.gartner.com",
            "https://www.mercer.com"
        ]
        self.newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
    
    def get_trends(self):
        trends = []
        for source in self.sources:
            try:
                response = requests.get(source + "/hr-trends")
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all('article', class_='trend-item')
                trends.extend([art.h2.text for art in articles[:5]])
            except Exception as e:
                print(f"Error scraping {source}: {str(e)}")
        
        news = self.newsapi.get_everything(
            q='HR trends 2025',
            language='en',
            sort_by='relevancy',
            page_size=10
        )
        trends.extend([article['title'] for article in news['articles']])
        
        return list(set(trends))[:10]

    def get_keyword_volume(self, keyword):
        url = f"https://www.googleapis.com/customsearch/v1?q={keyword}&key={os.getenv('GOOGLE_API_KEY')}&cx={os.getenv('GOOGLE_CSE_ID')}"
        response = requests.get(url).json()
        return response.get('searchInformation', {}).get('totalResults', 0)
