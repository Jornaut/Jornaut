from GetAudioFile import GetAudioFile
import unicodedata
class CreateFilipeDeschampsHtml:
    def __init__(self, html, title, text, time):
        self.html = html
        self.title = title
        self.time = time
        GetAudioFile(str(title).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""), text)
        self.SaveHtml()
    def SaveHtml(self):
        self.file = open("c:/xampp/htdocs/jornaut/FilipeDeschamps/"+str(self.time)+"/"+unicodedata.normalize('NFKD', str(self.title)).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", "")+"FiDe"+".php","w", encoding='utf-8')
        self.response = "<?php include '../header.php'?>"+str(self.title)+" FiDe"+"<?php include '../middle.php'?>"+str(self.html)+"<? include '../footer.php'?>"
        self.file.write(self.response)
        self.file.close()