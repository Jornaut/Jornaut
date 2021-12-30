import urllib.request
import os
from   bs4         import BeautifulSoup
from   bs4.element import Comment
from   datetime    import datetime

class GetNews:
    def __init__ (self, UrlList):
        for url in UrlList:    
            NewsGot = NewsGetter(url)
            self.NewsOrigin = str(url)[(url.index(".")+1):(url.index(".", url.index(".")+1))]
            try: NewsClean = globals()[self.NewsOrigin+'NewsCleaner'](NewsGot.soup)
            except KeyError: NewsClean = globals()["default"+'NewsCleaner'](NewsGot.soup)
            self.response = [self.NewsOrigin, NewsClean.html, datetime.now(), NewsClean.htmltext, NewsClean.title]

class NewsGetter:
    def __init__ (self, NewsUrl):
        self.webUrl  = urllib.request.urlopen(NewsUrl)
        self.data = str(self.webUrl.read(), 'utf-8')
        self.soup = BeautifulSoup(self.data, "html.parser")

class NewsCleaner:
    def __init__ (self, soup):
        self.soup = soup
        self.DefInp()
        self.GetText()
        #self.GetImg()
        self.ConcHtml()
        self.SaveHtml()
        self.HtmlTxt()
        self.GetTit()
    def DefInp (self):
        self.article = "article"
        self.TxtItag = "tag"
        self.TxtIclassname = "classname"
        self.ImgItag = "tag"
        self.ImgIclassname = "classname"
    def GetText (self):
        self.TxtAll = self.soup.find_all(self.TxtItag, {"class_": self.TxtIclassname})
    def GetImg (self):
        self.ImgUrlAll = []
        for link in self.soup.find(self.article).find_all(self.ImgItag, {"class_": self.ImgIclassname}):
            self.ImgUrlAll.append(link.get('src'))
    def ConcHtml(self):
        self.html = self.TxtAll
        #for url in self.ImgUrlAll:
        #    tag = "<tag img src='"+url+"' width='500' height='600'>"
        #    self.html.insert(int(random.uniform(int(0),int(len(self.html)))), tag)
        self.html = ''.join(str(e) for e in self.html)
        self.html = str(self.html).replace("'", '"')
    def SaveHtml (self):
        self.file = open("News/news.html","w")
        self.file.write(self.html)
        self.file.close()
    def HtmlTxt(self):
        self.file = open("News/news.html","r")
        data = str(self.file.read())
        soup = BeautifulSoup(data, "html.parser")
        visible_texts = filter(self.TagVis, soup.findAll(text=True))  
        self.htmltext = u" ".join(t.strip() for t in visible_texts)
        self.file.close()
        os.remove("News/news.html")
    def GetTit(self):
        self.title = str(self.soup.findAll("title")[0])
        self.title = self.title[(self.title.index(">")+1):(self.title[(self.title.index(">")+1):].index("<"))]
    def TagVis(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

class nytimesNewsCleaner (NewsCleaner):
    def DefInp (self):
        self.article = "article"
        self.TxtItag = "p"
        self.TxtIclassname = "css-axufdj evys1bk0"
        self.ImgItag = "img"
        self.ImgIclassname = "css-r3fift"

class defaultNewsCleaner(NewsCleaner):
    def DefInp (self):
        self.article = "body"
        self.TxtItag = "p"
        self.TxtIclassname = ""
        self.ImgItag = "img"
        self.ImgIclassname = ""