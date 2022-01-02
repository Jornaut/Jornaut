from nltk import tokenize

class CreateHtml:
    def __init__(self, FilipeDeschamps):
        self.response = ""
        for item in tokenize.sent_tokenize(FilipeDeschamps):
            self.response += "<p>"+str(item)+"</p>"
        self.theme = tokenize.sent_tokenize(FilipeDeschamps)[0]