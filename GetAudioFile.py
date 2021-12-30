import urllib.request
import requests
import time
import os
import wave
from   bs4                 import BeautifulSoup
from   requests.structures import CaseInsensitiveDict
from   pydub               import AudioSegment
import shutil
import unicodedata

class GetAudioFile:
    def __init__(self, title, text):
        self.title = str(title)
        text = str(text)+"."
        nfkd_form = unicodedata.normalize('NFKD', text)
        text = u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
        y = ""
        c = 0
        while len(y) < len(text):
            try: ponto = text[len(y):].index(".")+1+len(y)
            except Exception: ponto = len(text)
            try: pontoexc = text[len(y):].index("!")+1+len(y)
            except Exception: pontoexc = len(text)
            try: pontoint = text[len(y):].index("?")+1+len(y)
            except Exception: pontoint = len(text)
            try: 
                x = text[len(y):min(ponto, pontoexc, pontoint)]
                print(x)
            except Exception: x = text[len(y):]
            try: 
                    self.Exec(x, c)
                    err =  str(self.response)[11]
                    print(err)
            except Exception: pass
            if err == "4":
                x = x[:int(len(x)/2)]
                self.Exec(x, c)
            y += 2*x
            c += 1
        z = 0
        a = []
        while z+2 <= c:
            self.ConcAud('c:/xampp/htdocs/jornaut/adds/tmp/'+self.title+str(z)+'.wav','c:/xampp/htdocs/jornaut/adds/tmp/'+self.title+str(z+1)+'.wav')
            os.remove('c:/xampp/htdocs/jornaut/adds/tmp/'+self.title+str(z)+'.wav')
            z += 1
        src_folder = 'c:/xampp/htdocs/jornaut/adds/tmp/'
        dst_folder = 'c:/xampp/htdocs/jornaut/adds/'
        file_name  = self.title+str(z)+'.wav'
        shutil.move(src_folder + file_name, dst_folder + self.title+'.wav')


    def ConcAud(self, file1, file2):
        sound1 = AudioSegment.from_wav(file1)
        sound2 = AudioSegment.from_wav(file2)
        combined_sounds = sound1 + sound2
        combined_sounds.export(file2, format="wav")
    def Exec(self, text, c):
        self.response = PyCurl(str(self.title), text).resp
        time.sleep(20)
        DowloadFile(GetFromGithub().link, str(self.title), c)


class PyCurl:
    def __init__(self, title, text):
        self.title = str(title)
        self.text = str(text)
        self.Resemble()
        #self.PipeDream()
    def Resemble(self):
        url = "https://app.resemble.ai/api/v1/projects/9d2b87ed/clips"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer orTCdxTt0zQJP7gybct9rgtt"
        headers["Content-Type"] = "application/json"
        data = '''
        {
            "data": {
            "title": "'''+str(self.title)+'''",
            "body": "'''+str(self.text)+'''",
            "voice": "f6bf47ca",
            "public": "true"
        },
        "callback_uri": "https://enkznbyw1kliwgd.m.pipedream.net"
        }
        '''
        self.resp = requests.post(url, headers=headers, data=data)
        print(self.resp)

class GetFromGithub:
    def __init__(self):
        self.GetSoup()
        self.linkD = []
        self.GetLink()
    def GetSoup(self):
        self.webUrl  = urllib.request.urlopen("https://github.com/Jornaut/Jornaut/issues?q=is%3Aopen+is%3Aissue")
        self.data = str(self.webUrl.read(), 'utf-8')
        self.soup = BeautifulSoup(self.data, "html.parser")
    def GetLink (self):
        for link in self.soup.find_all("div", {"class": "js-navigation-container js-active-navigation-container"}):
            self.linkD.append(link.find("a", {"class":"Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title"}).encode_contents())
        self.link = self.linkD[0]

class DowloadFile:
    def __init__(self, url, title, c):
        self.file = open('c:/xampp/htdocs/jornaut/adds/tmp/'+title+str(c)+'.wav', 'wb+')
        self.file.write(requests.get(url, allow_redirects=True).content)
        self.file.close()