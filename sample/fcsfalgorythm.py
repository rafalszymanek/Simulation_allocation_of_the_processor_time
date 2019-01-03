from simulation import path
from sample.process import Process
from sample.open_data import checkWidthAndHeightOfFile

width, height = checkWidthAndHeightOfFile(path)
#Create 2D List with zeros
listOfAllWaitingTime = [[0 for x in range(width)] for y in range(height)]
listOfAllProcessingTime = [[0 for x in range(width)] for y in range(height)]

listOfProcess = []
actualAttempt = 0

def fcfs(listOfProcessNotClass = [], *args):
    global listOfAllWaitingTime
    global listOfAllProcessingTime
    global listOfProcess

    #put classes of process to ListOfProcess
    createArrayOfProcesses(listOfProcessNotClass)
    fscsExecution()


def createArrayOfProcesses(listOfProcessNotClass):
    global listOfProcess
    listOfProcess = []

    for x in listOfProcessNotClass:
        listOfProcess.append(Process(x))


def fscsExecution():
    global listOfAllWaitingTime
    global listOfAllProcessingTime
    global listOfProcess
    global actualAttempt
    i = 0   # index of next Process

    for actualExecProcess in listOfProcess:   # ececute process though FCFS queue
        actualExecProcess.executeProcess()
        listOfAllWaitingTime[actualAttempt][i], listOfAllProcessingTime[actualAttempt][i] = actualExecProcess.putResultsToTable(listOfAllWaitingTime, listOfAllProcessingTime)

        # Do for other process then actual
        i += 1
        # Add allocationOfProcessorTime to waitingTime and processingTime to other Processs in queue
        for j in range(i,len(listOfProcess)):
            listOfProcess[j].endingPreviousProcess(actualExecProcess.allocationOfProcessorTime)

    actualAttempt += 1
