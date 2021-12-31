class CreateTutorialHtml:
    def __init__(self, html, title):
        self.html = html
        self.title = title
        self.SaveHtml()
    def SaveHtml(self):
        self.file = open("c:/xampp/htdocs/jornaut/tutorial/"+str(self.title).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", "")+".php","w", encoding='utf-8')
        self.file.write("<?php include '../header.php'?>"+str(self.title)+"<?php include '../middle.php'?>"+self.html+"<? include '../footer.php'?>")
        self.file.close()