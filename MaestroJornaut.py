import News.MaestroNews
import Tutorial.MaestroTutorial
import Opinion.MaestroOpinion
import Opinion.ConcatenateAudios
from   subprocess import check_output
import os
import subprocess

Tutorial.MaestroTutorial.MaestroTutorial()
News.MaestroNews.MaestroNews()
ConcAud = []
for file in os.listdir("C:/xampp/htdocs/Jornaut/adds"):
    if file.endswith(".wav"):
        meuArquivo = open('c:/xampp/htdocs/jornaut/opinion/'+file[:-4].replace(" ", "-").replace("'", "").replace('"', "").replace("|", "")+"OpEd"+'.php', "r")
        txt = str(meuArquivo.read())
        os.rename('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav', ('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav').replace(" ", "-").replace("'", "").replace('"', "").replace("|", ""))
        ConcAud.append([('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav').replace(" ", "-").replace("'", "").replace('"', "").replace("|", ""), txt[txt.index('src=')+5 :txt.index('src=')+5+ txt[ txt.index('src=')+5 :].index('"')]])
        print(ConcAud)
Opinion.ConcatenateAudios.ConcatenateAudios(ConcAud)

# INSTRUÇÕES DE USO:
#  RODAR ESTE ARQUIVO (./MaestroJornaut.py); RESOLVER EVENTUAIS BUGS, RODAR NO TERMINAL, NO DIRETÓRIO RAIZ ./ 
#  O SEGUINTE COMANDO: node ./Opinion/YoutubeApi.js C:/xampp/htdocs/Jornaut/adds/30-12-2021.mp4 30-12-2021
#  SIGA AS INSTRUÇÕES, E PRONTO!


#check_output(["node", "c:users/veron/marcelo/Opinion/YoutubeApi.js"+'C:/xampp/htdocs/Jornaut/adds/'+str(datetime.date.today().strftime('%d-%m-%Y'))+'.mp4'+" "+str(datetime.date.today().strftime('%d-%m-%Y'))])
#cmd = '''node c:users/veron/marcelo/Opinion/YoutubeApi.js'''+' C:/xampp/htdocs/Jornaut/adds/'+str(datetime.date.today().strftime('%d-%m-%Y'))+'.mp4'+" "+str(datetime.date.today().strftime('%d-%m-%Y'))
#start = subprocess.Popen(cmd, shell=True)