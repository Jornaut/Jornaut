import datetime
from FilipeDeschamps.GetEmails import GetEmails
from FilipeDeschamps.CreateHtml import CreateHtml
from FilipeDeschamps.AddFilipeDeschampsImages import AddFilipeDeschampsImages
from FilipeDeschamps.CreateFilipeDeschampsHtml import CreateFilipeDeschampsHtml
import os

class MaestroFilipeDeschamps:
    def __init__(self):
        time = datetime.date.today().strftime('%d-%m-%Y')
        self.list = GetEmails().response
        os.mkdir("c:/xampp/htdocs/Jornaut/FilipeDeschamps/"+str(time))
        if datetime.date.today().weekday() < 5:
        for FilipeDeschamps in self.list:
            if not self.list[self.list.index(FilipeDeschamps)] in [self.list[0], self.list[-1]]:
                FilipeDeschamps = str(FilipeDeschamps).replace('''\r''', "").replace('''\n''', "")
                self.text = FilipeDeschamps
                self.html = CreateHtml(FilipeDeschamps)
                self.theme = self.html.theme
                self.html = AddFilipeDeschampsImages(self.text, self.html.response)
                CreateFilipeDeschampsHtml(self.html.response, self.theme, self.text, time)
                # self.ConcAud.append(['c:/xampp/htdocs/jornaut/adds/'+str(theme).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", "")+"OpEd"+'.wav', self.html.img])