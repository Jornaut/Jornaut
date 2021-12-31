import yake
import json
import requests
from ApiKeys import GetApiKeys

class AddImages:
    def __init__(self, text, html):
        self.html = html
        self.GetPar()
        self.response = ConectHtmlUrl(html, GetImages(text, self.ParIdx).ImgUrls, self.ParIdx).html
    def GetPar(self):
        self.ParTag = '</p>'
        self.ParIdx = self.find_all(str(self.html), self.ParTag)
    def find_all(self, a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += len(sub)

class GetImages:
    def __init__(self, text, ParIdx):
        self.ParIdx = ParIdx
        self.DefInp(text)
        self.GetKey()
        self.GetKey()
        self.GetImgUrl()
    def DefInp(self, text):
        self.language = "en"
        self.max_ngram_size = 1
        self.deduplication_threshold = 0.9
        self.numOfKeywords = int(len(list(self.ParIdx))/3+2)
        self.text = text
        self.response = []
        self.ImgUrls = []
    def GetKey(self):
        self.custom_kw_extractor = yake.KeywordExtractor(lan=self.language, n=self.max_ngram_size, dedupLim=self.deduplication_threshold, top=self.numOfKeywords, features=None)
        self.keywords = self.custom_kw_extractor.extract_keywords(self.text)
    def GetImgUrl(self):
        for keyword in self.keywords:
            self.ImgUrls.append(json.loads(requests.request("GET", "https://bing-image-search1.p.rapidapi.com/images/search", headers={'x-rapidapi-host': "bing-image-search1.p.rapidapi.com",'x-rapidapi-key': GetApiKeys.Bing}, params={"q":keyword[0]}).text)["value"][0]["contentUrl"])
        
class ConectHtmlUrl:
    def __init__(self, html, ImgUrls, ParIdx):
        self.DefInp(html, ImgUrls)
        self.ParIdx = ParIdx
        # self.GetPar()
        self.PutImg()
    def DefInp(self, html, ImgUrls):
        self.html = html
        self.ImgUrls = ImgUrls
    def PutImg(self):
        payload = 0
        counter = 0
        for Par in self.ParIdx:
            if counter%3==0 :
                self.html = self.html[:(Par+len(self.ParTag)+payload)]+'<img src="'+self.ImgUrls[int(counter/3)]+'">'+self.html[(Par+len(self.ParTag)+payload):]
                payload += len('<img src="'+self.ImgUrls[int(counter/3)]+'">')
            counter += 1