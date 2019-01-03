from sample.process import Process


def createArrayOfProcesses(listOfProcessNotClass):
    listOfProcess = []

    for x in listOfProcessNotClass:
        listOfProcess.append(Process(x))

    return listOfProcess

def algorythmExecution(listOfProcess, listOfAllWaitingTime, listOfAllProcessingTime, actualAttempt):
    i = 0   # index of next Process

    for actualExecProcess in listOfProcess:   # ececute process though FCFS queue
        actualExecProcess.executeProcess()
        listOfAllWaitingTime[actualAttempt][i], listOfAllProcessingTime[actualAttempt][i] = actualExecProcess.putResultsToTable(listOfAllWaitingTime, listOfAllProcessingTime)

        # Do for other process then actual
        i += 1
        # Add allocationOfProcessorTime to waitingTime and processingTime to other Processs in queue
        for j in range(i,len(listOfProcess)):
            listOfProcess[j].endingPreviousProcess(actualExecProcess.allocationOfProcessorTime)

    return listOfAllWaitingTime, listOfAllProcessingTime
