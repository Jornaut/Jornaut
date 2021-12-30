import Tutorial.GetTutorial
import Tutorial.CreateTutorialHtml
import Tutorial.SearchTutorial

class MaestroTutorial:
    def __init__(self):
        for url in Tutorial.SearchTutorial.SearchTutorial().urls:
            try:
                TutorialPayload = Tutorial.GetTutorial.GetTutorial(url).response
                Tutorial.CreateTutorialHtml.CreateTutorialHtml(TutorialPayload[1], TutorialPayload[4])
            except Exception:
                pass