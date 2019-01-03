class Process:
    waitingTime = 0
    processingTime = 0
    allocationOfProcessorTime = 0
    didFinished = False

    def __init__(self, allocationOfProcessorTime):
        self.allocationOfProcessorTime = allocationOfProcessorTime

    def executeProcess(self):
        self.processingTime += self.allocationOfProcessorTime
        self.didFinished = True

    def endingPreviousProcess(self, durationOfEndingProcess):
        self.waitingTime += durationOfEndingProcess
        self.processingTime += durationOfEndingProcess

    def putResultsToTable(self, listOfAllWaitingTime = [], listOfAllProcessingTime = [], *args):
        listOfAllWaitingTime = self.waitingTime
        listOfAllProcessingTime = self.processingTime
        return listOfAllWaitingTime, listOfAllProcessingTime
