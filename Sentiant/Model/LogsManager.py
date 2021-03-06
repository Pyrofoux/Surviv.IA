from datetime import datetime
from os import path
#from Sentiant.Model.LogsManager import LogsManager


class LogsManager :
    def __init__(self):
        pass

    @staticmethod
    def timeString():
        return datetime.now().strftime("%H:%M:%S.%f")[:-3]

    scriptPath = path.abspath(__file__)
    scriptDir = path.split(scriptPath)[0]
    scriptDirDir = path.dirname(scriptDir) #Sentiant

    finalPathGen=path.join(scriptDirDir,'Logs\\generals.log')
    finalPathUse=path.join(scriptDirDir,'Logs\\users.log')

    #BASE = "Sentiant\\Logs\\" #mais ça marche peut-être pas sur Linux
    #EXT = ".log"

    @staticmethod
    def StdOut(type, msg, isUser=False, end="\n"):
        pre = "["+type+"] ("+LogsManager.timeString()+")> "
        out = pre + str(msg).replace("\n", "\n" + " " * len(pre)) + end # .replace(a,b) remplace toutes les occurrences de a par b
        print(out)

        with open(LogsManager.finalPathGen, "a") as generals:
            # logs are opened in "a"ppend mode in order not to erase the previous lines each time it is opened (if it used "w" mode)
            generals.write(out)
        if isUser:
            with open(LogsManager.finalPathUse, "a") as users:
                users.write(out)

    @staticmethod
    def Error(details, userFailure=False):
        LogsManager.StdOut("Error", details, userFailure)

    @staticmethod
    def Warning(details):
        """Not for user usage"""
        LogsManager.StdOut("Warning", details)

    @staticmethod
    def Info(info, isUser=False):
        LogsManager.StdOut("Info", info, isUser)

    @staticmethod
    def Debug(msg, isUser=True):
        """Recommended for user usage"""
        LogsManager.StdOut("Debug", msg, isUser)

    @staticmethod
    def NotADirectionError(antId, antTeam, direction, action):
        """Writes in generals and users log files
           when a non-valid direction is given to an Ant.
        """
        details = ("Une erreur a eu lieu car la direction '{direction}' " \
                + "donnee a la fourmi '{antId}' 'de l'equipe '{antTeam}' " \
                + "pour l'action '{action}' n'est pas une direction valide.") \
                .format(antId=antId, antTeam=antTeam, direction=direction, action=action)
        LogsManager.Error(details, True)

    @staticmethod
    def NotAPheromoneError(antId, antTeam, pheromone):
        """Writes in generals and users log files
           when a non-valid pheromone is given to an Ant.
        """
        details = ("Une erreur a eu lieu car la pheromone '{pheromone}' " \
                + "qu'a essaye de poser la fourmi '{antId}' de l'équipe " \
                + "'{antTeam}' n'est pas une valeur de pheromone valide.") \
                .format(antId=antId, antTeam=antTeam, pheromone=pheromone)
        LogsManager.Error(details, True)

    @staticmethod
    def PrivateVariableError(antId, antTeam, varName, tryValue):
        """Writes in generals and users text files
           when a non-valid pheromone is given to an Ant
        """
        details = ("Une erreur a eu lieu car la variable '{varName}' " \
                + "qu'a essaye de modifier la fourmi '{antId}' de l'equipe " \
                + "'{antTeam}' pour la nouvelle valeur de '{tryValue}' " \
                + "est une variable privee inaccessible.") \
                .format(antId=antId, antTeam=antTeam, varName=varName, tryValue=tryValue)
        LogsManager.Error(details, True)
