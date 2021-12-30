import os
from   bs4            import BeautifulSoup
from   bs4.element    import Comment
from   datetime       import datetime
from   urllib.request import urlopen, Request

class GetTutorial:
    def __init__ (self, url):
            NewsGot = TutorialGetter(url)
            self.NewsOrigin = 'digitalocean'
            NewsClean = TutorialCleaner(NewsGot.soup)
            self.response = [self.NewsOrigin, NewsClean.html, datetime.now(), NewsClean.htmltext, NewsClean.title]

class TutorialGetter:
    def __init__ (self, TutorialUrl):
        self.webUrl = urlopen(Request(url = TutorialUrl, headers = {'User-Agent': 'Mozilla / 5.0 (Windows NT 6.1) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 41.0.2228.0 Safari / 537.3'})).read()
        self.data = str(self.webUrl, 'utf-8')
        self.soup = BeautifulSoup(self.data, "html.parser")

class TutorialCleaner:
    def __init__ (self, soup):
        self.soup = soup
        self.GetHtml()
        self.SaveHtml()
        self.HtmlTxt()
        self.GetTit()
    def GetHtml (self):
        self.html = '<head><link rel="stylesheet" media="all" href="https://www.digitalocean.com/assets/community/application-f83055fcd56386b341605dbcf13938f4f12fdf60ab68e00f47eb9c1d0d51c74c.css"/></head><body>'
        self.html = self.html+''.join(str(e) for e in self.soup.find_all("div", {"class": "container tutorial-header"}))
        self.html = self.html+(''.join(str(e) for e in self.soup.find_all("div", {"class": "content-body tutorial-content"})))
        self.html = self.html+'</body>'
        self.html = str(self.html).replace("'", '"')
    def SaveHtml (self):
        self.file = open("Tutorials/tutorial.html","w", encoding="utf-8")
        self.file.write(self.html)
        self.file.close()
    def HtmlTxt(self):
        self.file = open("Tutorials/tutorial.html","r", encoding="utf-8")
        data = str(self.file.read())
        soup = BeautifulSoup(data, "html.parser")
        visible_texts = filter(self.TagVis, soup.findAll(text=True))  
        self.htmltext = u" ".join(t.strip() for t in visible_texts)
        self.file.close()
        os.remove("Tutorials/tutorial.html")
    def GetTit(self):
        self.title = str(self.soup.findAll("title")[0])
        self.title = self.title[(self.title.index(">")+1):(self.title[(self.title.index(">")+1):].index("<")+1)]
    def TagVis(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True