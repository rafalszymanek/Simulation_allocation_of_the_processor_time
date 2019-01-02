from sample.thread import Thread


def fcfs(listOfThreadNotClass = [], *args):
    listOfWaitingTime = []
    listOfProcessingTime = []
    listOfThread = createArrayOfTheads(listOfThreadNotClass)

    listOfWaitingTime, listOfProcessingTime = fscsExecution(listOfThread)
    return listOfWaitingTime, listOfProcessingTime

def createArrayOfTheads(listOfThreadNotClass):
    listOfThread = []
    for x in listOfThreadNotClass:
        listOfThread.append(Thread(x))

    return listOfThread

def fscsExecution(listOfThread = [], *args):
    i = 0
    listOfWaitingTime = []
    listOfProcessingTime = []
    for actualExecThread in listOfThread:
        i += 1
        actualExecThread.executeProcess()
        listOfWaitingTime, listOfProcessingTime = actualExecThread.putResultsToTable(listOfWaitingTime, listOfProcessingTime)
        for j in range(i,len(listOfThread)):
            listOfThread[j].endingPreviousProcess(actualExecThread.allocationOfProcessorTime)

    return listOfWaitingTime, listOfProcessingTime
