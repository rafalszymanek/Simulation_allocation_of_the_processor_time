from sample.thread import Thread

listOfWaitingTime = []
listOfProcessingTime = []

def fcfs(listOfThreadNotClass = [], *args):
    global listOfWaitingTime
    global listOfProcessingTime

    listOfThread = createArrayOfTheads(listOfThreadNotClass)

    fscsExecution(listOfThread)


def createArrayOfTheads(listOfThreadNotClass):
    listOfThread = []
    for x in listOfThreadNotClass:
        listOfThread.append(Thread(x))

    return listOfThread

def fscsExecution(listOfThread = [], *args):
    i = 0
    global listOfWaitingTime
    global listOfProcessingTime

    for actualExecThread in listOfThread:
        i += 1
        actualExecThread.executeProcess()
        listOfWaitingTime, listOfProcessingTime = actualExecThread.putResultsToTable(listOfWaitingTime, listOfProcessingTime)
        for j in range(i,len(listOfThread)):
            listOfThread[j].endingPreviousProcess(actualExecThread.allocationOfProcessorTime)
