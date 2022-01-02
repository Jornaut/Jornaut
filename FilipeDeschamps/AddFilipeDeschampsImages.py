import yake
import json
import requests
from ApiKeys import GetApiKeys

class AddFilipeDeschampsImages:
    def __init__(self, text, html):
        ImgUrls = GetImages(text).ImgUrls
        self.response = html[:html.index("</p>")+6]+'<img src="'+str(ImgUrls[0])+'">'+html[html.index("</p>")+6:]+'<img src="'+str(ImgUrls[1])+'">'
        self.img = str(ImgUrls[0])

class GetImages:
    def __init__(self, text):
        self.DefInp(text)
        self.GetKey()
        self.GetKey()
        self.GetImgUrl()
    def DefInp(self, text):
        self.language = "en"
        self.max_ngram_size = 1
        self.deduplication_threshold = 0.9
        self.numOfKeywords = 2
        self.text = text
        self.response = []
        self.ImgUrls = []
    def GetKey(self):
        self.custom_kw_extractor = yake.KeywordExtractor(lan=self.language, n=self.max_ngram_size, dedupLim=self.deduplication_threshold, top=self.numOfKeywords, features=None)
        self.keywords = self.custom_kw_extractor.extract_keywords(self.text)
    def GetImgUrl(self):
        for keyword in self.keywords:
            self.ImgUrls.append(json.loads(requests.request("GET", "https://bing-image-search1.p.rapidapi.com/images/search", headers={'x-rapidapi-host': "bing-image-search1.p.rapidapi.com",'x-rapidapi-key': GetApiKeys.Bing}, params={"q":keyword[0]}).text)["value"][0]["contentUrl"])