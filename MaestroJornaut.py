# import News.MaestroNews
# import Tutorial.MaestroTutorial
# import Opinion.MaestroOpinion
# import Opinion.ConcatenateAudios
import FilipeDeschamps.MaestroFilipeDeschamps
# from   subprocess import check_output
# import os
# import datetime
# import subprocess

# #Tutorial.MaestroTutorial.MaestroTutorial()
# #News.MaestroNews.MaestroNews()
# Opinion.MaestroOpinion.MaestroOpinion()
# ConcAud = []
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds"):
#     if file.endswith(".wav"):
#         if str(datetime.time.strftime('%d-%m-%Y', datetime.time.localtime(os.path.getmtime("C:/xampp/htdocs/Jornaut/adds"+str(file))))) == str(datetime.date.today().strftime('%d-%m-%Y')):
#             meuArquivo = open('c:/xampp/htdocs/jornaut/opinion/'+file[:-4].replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", "")+"OpEd"+'.php', "r")
#             txt = str(meuArquivo.read())
#             os.rename('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav', ('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav').replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""))
#             ConcAud.append([('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav').replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""), txt[txt.index('src=')+5 :txt.index('src=')+5+ txt[ txt.index('src=')+5 :].index('"')]])
#             print(ConcAud)
# Opinion.ConcatenateAudios.ConcatenateAudios(ConcAud)
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds/tmp"):
#     os.remove(file)
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds/tmpf"):
#     os.remove(file)
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds"):
#     if not file.endswith(".wav"):
#         if not file.endswith(".mp4"):
#             os.remove(file)

# # FilipeDeschamps
FilipeDeschamps.MaestroFilipeDeschamps.MaestroFilipeDeschamps()
# ConcAud = []
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds"):
#     if file.endswith(".wav"):
#         if str(datetime.time.strftime('%d-%m-%Y', datetime.time.localtime(os.path.getmtime("C:/xampp/htdocs/Jornaut/adds"+str(file))))) == str(datetime.date.today().strftime('%d-%m-%Y')):
#             meuArquivo = open('c:/xampp/htdocs/jornaut/FilipeDeschamps/'+str(datetime.date.today().strftime('%d-%m-%Y'))+"/"+file[:-4].replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", "")+"FiDe"+'.php', "r")
#             txt = str(meuArquivo.read())
#             os.rename('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav', ('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav').replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""))
#             ConcAud.append([('c:/xampp/htdocs/jornaut/adds/'+file[:-4]+'.wav').replace(" ", "-").replace("'", "").replace('"', "").replace("|", "").replace(":", ""), txt[txt.index('src=')+5 :txt.index('src=')+5+ txt[ txt.index('src=')+5 :].index('"')]])
#             print(ConcAud)
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds/tmp"):
#     os.remove(file)
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds/tmpf"):
#     os.remove(file)
# for file in os.listdir("C:/xampp/htdocs/Jornaut/adds"):
#     if not file.endswith(".wav"):
#         if not file.endswith(".mp4"):
#             os.remove(file)
# # INSTRUÇÕES DE USO:
# #  RODAR ESTE ARQUIVO (./MaestroJornaut.py); RESOLVER EVENTUAIS BUGS, RODAR NO TERMINAL, NO DIRETÓRIO RAIZ ./ 
# #  O SEGUINTE COMANDO: node ./Opinion/YoutubeApi.js C:/xampp/htdocs/Jornaut/adds/30-12-2021.mp4 30-12-2021
# #  SIGA AS INSTRUÇÕES, E PRONTO!


# #check_output(["node", "c:users/veron/marcelo/Opinion/YoutubeApi.js"+'C:/xampp/htdocs/Jornaut/adds/'+str(datetime.date.today().strftime('%d-%m-%Y'))+'.mp4'+" "+str(datetime.date.today().strftime('%d-%m-%Y'))])
# #cmd = '''node c:users/veron/marcelo/Opinion/YoutubeApi.js'''+' C:/xampp/htdocs/Jornaut/adds/'+str(datetime.date.today().strftime('%d-%m-%Y'))+'.mp4'+" "+str(datetime.date.today().strftime('%d-%m-%Y'))
# #start = subprocess.Popen(cmd, shell=True)