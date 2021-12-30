#import os, sys
#sys.path.insert(0, os.path.abspath(".."))
from GetAudioFile import GetAudioFile

class CreateNewsHtml:
    def __init__(self, html, title, text):
        self.html = html
        self.title = title
        GetAudioFile(title, text)
        self.SaveHtml()
    def SaveHtml(self):
        self.file = open("c:/xampp/htdocs/jornaut/news/"+str(self.title).replace(" ", "-").replace("'", "").replace('"', "")+".php","w", encoding='utf-8')
        self.file.write("<?php include '../header.php'?>"+str(self.title)+"<?php include '../middleA.php'?>"+"<embed height='50' width='100' src='c:/xampp/htdocs/jornaut/adds/"+str(self.title).replace(" ", "-").replace("'", "").replace('"', "")+".wav'>"+"<? include '../middleB.php'?>"+self.html+"<? include '../footer.php'?>")
        self.file.close()