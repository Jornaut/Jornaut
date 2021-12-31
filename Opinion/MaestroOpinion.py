import Opinion.SearchOpinion
import Opinion.GetOpinionTopics
import Opinion.GetOpinionFormed
import Opinion.CreateOpinionHtml
import Opinion.AddOpinionImages
import Opinion.ConcatenateAudios
import os
from   subprocess import check_output
import datetime

class MaestroOpinion:
    def __init__(self):
        self.ConcAud = []
        for theme in Opinion.SearchOpinion.SearchOpinion().themes:
            # try:
                if len(self.ConcAud)>0:
                    if not os.path.isfile(self.ConcAud[-1][0]): 
                        del self.ConcAud[-1]
                self.topics = Opinion.GetOpinionTopics.GetOpinionTopics(theme).response
                GotOpinionFormed = Opinion.GetOpinionFormed.GetOpinionFormed(theme, self.topics)
                self.text = GotOpinionFormed.text
                self.html = GotOpinionFormed.response
                self.html = Opinion.AddOpinionImages.AddOpinionImages(self.text, self.html)
                print(Opinion.CreateOpinionHtml.CreateOpinionHtml(self.html.response, theme, self.text).response)
                self.ConcAud.append(['c:/xampp/htdocs/jornaut/adds/'+str(theme).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", "")+"OpEd"+'.wav', self.html.img])
            # except Exception:
            #     pass