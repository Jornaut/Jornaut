from pytrends.request import TrendReq

class SearchOpinion:
    def __init__(self):
        self.themes = []
        for link in TrendReq().today_searches(pn = 'US'):
            self.themes.append(str(link)[str(link).index("q")+2:str(link).index("&")].replace("+", " ").replace("-", " "))
