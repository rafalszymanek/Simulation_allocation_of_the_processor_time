from sample.thread import Thread

w, h = 100, 100;
listOfWaitingTime = [[0 for x in range(w)] for y in range(h)]
listOfProcessingTime = [[0 for x in range(w)] for y in range(h)]
listOfThread = []
actualAttempt = 0

def fcfs(listOfThreadNotClass = [], *args):
    global listOfWaitingTime
    global listOfProcessingTime
    global listOfThread
    createArrayOfTheads(listOfThreadNotClass)
    fscsExecution()


def createArrayOfTheads(listOfThreadNotClass):
    global listOfThread
    listOfThread = []
    for x in listOfThreadNotClass:
        listOfThread.append(Thread(x))


def fscsExecution():
    i = 0   # next thread
    global listOfWaitingTime
    global listOfProcessingTime
    global listOfThread
    global actualAttempt

    for actualExecThread in listOfThread:   # ececute process though FCFS queue
        actualExecThread.executeProcess()
        # print (len(listOfThread))
        listOfWaitingTime[actualAttempt][i], listOfProcessingTime[actualAttempt][i] = actualExecThread.putResultsToTable(listOfWaitingTime, listOfProcessingTime)
        i += 1
        for j in range(i,len(listOfThread)):    # add allocationOfProcessorTime to waitingTime and processingTime to other threads in queue
            listOfThread[j].endingPreviousProcess(actualExecThread.allocationOfProcessorTime)
    actualAttempt += 1
