from GetAudioFile import GetAudioFile

class CreateOpinionHtml:
    def __init__(self, html, title, text):
        self.html = html
        self.title = title
        GetAudioFile(str(title).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""), text)
        
        self.SaveHtml()
    def SaveHtml(self):
        self.file = open("c:/xampp/htdocs/jornaut/opinion/"+str(self.title).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", "")+"OpEd"+".php","w", encoding='utf-8')
        self.response = "<?php include '../header.php'?>"+str(self.title)+" OpEd"+"<?php include '../middle.php'?>"+str(self.html)+"<? include '../footer.php'?>"
        self.file.write(self.response)
        self.file.close()