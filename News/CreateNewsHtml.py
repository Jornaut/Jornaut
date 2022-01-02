#import os, sys
#sys.path.insert(0, os.path.abspath(".."))
from GetAudioFile import GetAudioFile

class CreateNewsHtml:
    def __init__(self, html, title, text):
        self.html = html
        self.title = title
        GetAudioFile(str(title).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""), text)
        self.SaveHtml()
    def SaveHtml(self):
        self.file = open("c:/xampp/htdocs/jornaut/news/"+str(self.title).replace(" ", "-").replace("'", "").replace('"', "").replace(":", "")+".php","w", encoding='utf-8')
        self.file.write("<?php include '../header.php'?>"+str(self.title)+" OpEd"+"<?php include '../middle.php'?>"+str(self.html)+"<? include '../footer.php'?>")
        self.response = "<?php include '../header.php'?>"+str(self.title)+" OpEd"+"<?php include '../middle.php'?>"+str(self.html)+"<? include '../footer.php'?>"
        self.file.close()