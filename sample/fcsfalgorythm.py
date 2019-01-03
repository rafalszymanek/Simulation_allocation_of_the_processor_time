from simulation import path
from sample.process import Process
from sample.open_data import checkWidthAndHeightOfFile
from sample.doalgorythm import *

width, height = checkWidthAndHeightOfFile(path)
#Create 2D List with zeros
listOfAllWaitingTime = [[0 for x in range(width)] for y in range(height)]
listOfAllProcessingTime = [[0 for x in range(width)] for y in range(height)]

listOfProcess = []
actualAttempt = 0 # Number of row to insert data

def fcfs(matrix):

    for i in range(0, len(matrix)):
        fcfsProcess(matrix[i])
    return listOfAllWaitingTime, listOfAllProcessingTime

def fcfsProcess(listOfProcessNotClass = [], *args):
    global listOfAllWaitingTime
    global listOfAllProcessingTime
    global listOfProcess
    global actualAttempt

    #put classes of process to ListOfProcess
    listOfProcess = createArrayOfProcesses(listOfProcessNotClass)
    listOfAllWaitingTime, listOfAllProcessingTime = algorythmExecution(listOfProcess, listOfAllWaitingTime, listOfAllProcessingTime, actualAttempt)
    actualAttempt+=1

def clearAllLists():
    global listOfAllWaitingTime
    global listOfAllProcessingTime
    global listOfProcess


    for row in listOfAllWaitingTime:
        for item in range(0,len(listOfAllWaitingTime[0])):
            row[item]=0

    for row in listOfAllProcessingTime:
        for item in range(0,len(listOfAllProcessingTime[0])):
            row[item]=0

    listOfProcess.clear()
