class Thread:
    waitingTime = 0
    processingTime = 0
    allocationOfProcessorTime = 0
    didFinished = False

    def __init__(self, allocationOfProcessorTime):
        self.allocationOfProcessorTime = allocationOfProcessorTime

    def endingPreviousProcess(self, durationOfEndingProcess):
        self.waitingTime += durationOfEndingProcess
        self.processingTime += durationOfEndingProcess

    def executeProcess(self):
        self.waitingTime += self.allocationOfProcessorTime
        self.processingTime += self.allocationOfProcessorTime
        didFinished = True

    def putResultsToTable(self, resultArray = [], *args):
        resultArray.append('50')
