import json
import urllib.request

class SearchNews:
    def __init__(self):
        self.urls = []
        self.GetUrls()
    def GetUrls(self):
        self.articles = json.loads(str(urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=us&apiKey=46f499c911f24445a31a61dad5d91e21").read(), 'utf-8'))["articles"]
        for article in self.articles:
            self.urls.append(article["url"])