from sample.fcsfalgorythm import *
import statistics


#AVERAGE MEAN
def averageOfArray(array):
    if isinstance(array[0], list): # Check that
        return averageForList2D(array)
    else:
        return averageForList1D(array)

def averageForList2D(array):
    averageResult = []
    for i in range(0, len(array)):
        averageResult.append(statistics.mean(array[i]))
    return averageResult

def averageForList1D(array):
    return statistics.mean(array)

#MEDIAN
def medianOfArray(array):

    if isinstance(array[0], list):
        return medianForList2D(array)
    else:
        return medianForList1D(array)

def medianForList2D(array):
    medianResult = []
    for i in range(0, len(array)):
        medianResult.append(statistics.median(array[i]))
    return medianResult

def medianForList1D(array):
    return statistics.median(array)

def test(listOfAllWaitingTime):
    listAverageOfEachAttemptOfWaitingTime = averageOfArray(listOfAllWaitingTime)
    listMedianOfEachAttemptOfWaitingTime = medianOfArray(listOfAllWaitingTime)
    return averageOfArray(listAverageOfEachAttemptOfWaitingTime), medianOfArray(listMedianOfEachAttemptOfWaitingTime)
