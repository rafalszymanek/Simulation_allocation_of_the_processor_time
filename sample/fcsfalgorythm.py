from sample.thread import Thread

listOfWaitingTime = []
listOfProcessingTime = []
listOfThread = []

def fcfs(listOfThreadNotClass = [], *args):
    global listOfWaitingTime
    global listOfProcessingTime
    global listOfThread
    createArrayOfTheads(listOfThreadNotClass)

    fscsExecution()


def createArrayOfTheads(listOfThreadNotClass):
    global listOfThread
    for x in listOfThreadNotClass:
        listOfThread.append(Thread(x))


def fscsExecution():
    i = 0
    global listOfWaitingTime
    global listOfProcessingTime
    global listOfThread

    for actualExecThread in listOfThread:
        i += 1
        actualExecThread.executeProcess()
        listOfWaitingTime, listOfProcessingTime = actualExecThread.putResultsToTable(listOfWaitingTime, listOfProcessingTime)
        for j in range(i,len(listOfThread)):
            listOfThread[j].endingPreviousProcess(actualExecThread.allocationOfProcessorTime)
