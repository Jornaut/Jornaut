import requests
import subprocess
from   moviepy.editor  import *
from   pydub           import AudioSegment
import datetime
import os
from PIL import Image
from subprocess import PIPE
import asyncio
import time
import threading
import signal
import win32api


class ConcatenateAudios:
    def __init__(self, ConcAud):
        self.ConcAud = ConcAud
        self.CreateVideos()
        self.ConcatenateVideo()
    def CreateVideos(self):
            for item in self.ConcAud:
                #try: 
                AudioSegment.from_wav(item[0]).export(item[0][:-3]+'mp3', format="mp3")
                img_data = requests.get(item[1]).content
                with open(("C:/xampp/htdocs/Jornaut/adds/"+item[0][29:-4]+item[1][-4:]).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""), 'wb') as handler:
                    handler.write(img_data)
                self.ConcAud[self.ConcAud.index(item)][1] = "C:/xampp/htdocs/Jornaut/adds/"+item[0][29:-4]+item[1][-4:]
                item[1] = self.ConcAud[self.ConcAud.index(item)][1]
                # self.Makemp4(item)
                #if os.path.isfile('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4'): os.remove('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4')
                cmd = '''ffmpeg -loop 1 -framerate 1 -i "'''+item[1]+'''" -i "'''+item[0]+'''" -map 0:v -map 1:a -r 10 -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M "C:/xampp/htdocs/Jornaut/adds/tmpf/'''+item[0][29:-4]+'.mp4"'
                start = subprocess.Popen(cmd, shell=True)
                # fnsd = bool(False)
                # while fnsd == False:
                #     try:
                #         os.path.isfile('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4')
                #         fnsd = True
                #         print(os.path.getsize('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4'))
                #     except PermissionError:
                #         print("not yet, more 10sec")
                #         time.sleep(10)
                #         fnsd = False
                #     except FileNotFoundError:
                #         print("not yet, more 10sec")
                #         time.sleep(10)
                #         fnsd = False
                time.sleep(180)
                # win32api.TerminateProcess(int(start._handle), -1)
                # if os.path.isfile('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4'):
                #     print("existe")
                #     if os.path.getsize('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4') == 0:
                #         print("n tem nda")
                #         del self.ConcAud[self.ConcAud.index(item)]
                #     else: 
                #         print("nice one!")
                #         cmd = '''ffmpeg -loop 1 -framerate 1 -i "'''+item[1]+'''" -i "'''+item[0]+'''" -map 0:v -map 1:a -r 10 -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M "C:/xampp/htdocs/Jornaut/adds/tmpf/'''+item[0][29:-4]+'.mp4"'
                #         start = subprocess.Popen(cmd, shell=True)
                # else:
                #     del self.ConcAud[self.ConcAud.index(item)]
                # time.sleep(150)
                # esperar = False
                # while esperar == False:
                #     try:
                # if os.path.isfile('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4'): os.remove('C:/xampp/htdocs/Jornaut/adds/tmpf/lixo.mp4')
                #         esperar == True
                #     except PermissionError:
                #         esperar = False


    # def Makemp4(self, item):
    #     if os.path.isfile(item[1]):
    #     #     res = []
    #         def CSPCM(self):
    #             a = '''ffmpeg -report -loop 1 -framerate 1 -i "C:/Users/veron/Downloads/short.mp3" -i "'''+item[0]+'''" -map 0:v -map 1:a -r 10 -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M "C:/xampp/htdocs/Jornaut/adds/tmpf/'''+item[0][29:-4]+'.mp4"'
    #             self.r = subprocess.Popen(a, stdout=subprocess.PIPE, 
    #             shell=True) 
    #         def wrapper(func, self):
    #             func(self)

    #         t = threading.Thread(target=wrapper, args=(CSPCM, (self)))
    #         t.start()
    #         time.sleep(10)
    #         while t.is_alive():
    #             print("scanning")
    #             if os.path.getsize('C:/xampp/htdocs/Jornaut/adds/tmpf/'''+item[0][29:-4]+'.mp4') == 0:
    #                 os.kill(self.r, signal.CTRL_C_EVENT)
    #                 del self.ConcAud[self.ConcAud.index(item)]
    #                 os.remove('C:/xampp/htdocs/Jornaut/adds/tmpf/'''+item[0][29:-4]+'.mp4')
    #         print("exist"+item[1])
    #     else: 
    #         del self.ConcAud[self.ConcAud.index(item)]
    #         print("dont exist")
    #         print("deleted"+self.ConcAud[self.ConcAud.index(item)])
        #except: 
            #   print("deleted"+str(self.ConcAud[self.ConcAud.index(item)]))
            #del self.ConcAud[self.ConcAud.index(item)]

    def ConcatenateVideo(self):
        method = "reduce"
        self.ConcAud = [] #'c:/xampp/htdocs/jornaut/adds/'+str(theme).replace(" ", "-").replace("'", "").replace('"', "").replace("|", "")+"OpEd"+'.wav',
        #self.html.img
        for file in os.listdir("C:/xampp/htdocs/Jornaut/adds/tmpf"):
            if file.endswith("mp4"):
                self.ConcAud.append("C:/xampp/htdocs/Jornaut/adds/tmpf/"+file)
        # create VideoFileClip object for each video file
        clips = [VideoFileClip(c) for c in self.ConcAud]
        if method == "reduce":
            # calculate minimum width & height across all clips
            min_height = min([c.h for c in clips])
            min_width = min([c.w for c in clips])
            # resize the videos to the minimum
            clips = [c.resize(newsize=(min_width, min_height)) for c in clips]
            # concatenate the final video
            final_clip = concatenate_videoclips(clips)
        elif method == "compose":
            # concatenate the final video with the compose method provided by moviepy
            final_clip = concatenate_videoclips(clips, method="compose")
        # write the output video file
        final_clip.write_videofile('C:/xampp/htdocs/Jornaut/adds/'+str(datetime.date.today().strftime('%d-%m-%Y'))+'.mp4')