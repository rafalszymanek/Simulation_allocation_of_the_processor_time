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
    i = 0   # next thread
    global listOfWaitingTime
    global listOfProcessingTime
    global listOfThread

    for actualExecThread in listOfThread:   # ececute process though FCFS queue
        i += 1
        actualExecThread.executeProcess()
        listOfWaitingTime, listOfProcessingTime = actualExecThread.putResultsToTable(listOfWaitingTime, listOfProcessingTime)
        for j in range(i,len(listOfThread)):    # add allocationOfProcessorTime to waitingTime and processingTime to other threads in queue
            listOfThread[j].endingPreviousProcess(actualExecThread.allocationOfProcessorTime)
