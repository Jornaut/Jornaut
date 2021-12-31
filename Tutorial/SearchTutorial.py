from   bs4            import BeautifulSoup
from   urllib.request import urlopen, Request
from   datetime       import date

class SearchTutorial:
    def __init__(self):
        self.urls = []
        self.GetUrls()
    def GetUrls(self):
        self.webUrl = urlopen(Request(url = "https://www.digitalocean.com/community/tutorials?subtype=-tech_talk", headers = {'User-Agent': 'Mozilla / 5.0 (Windows NT 6.1) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 41.0.2228.0 Safari / 537.3'})).read()
        self.data = str(self.webUrl, 'utf-8')
        self.soup = BeautifulSoup(self.data, "html.parser")
        self.html = self.soup.find_all("li", {"class": "tutorial tutorial"})
        # for url in self.html:
        #     if str(url.find("span", {"class":"publish-date timeago"}))[42:52] == str(date.today()):
        #         self.urls.append("https://www.digitalocean.com"+url.find("a").get('href'))