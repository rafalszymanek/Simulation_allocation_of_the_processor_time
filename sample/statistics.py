from sample.fcsfalgorythm import *
import statistics

def averageOfArray(array):

    if isinstance(array[0], list):
        result = []
        result = averageForList2D(array)
    else:
        result = 0
        result = averageForList1D(array)
    return result


def averageForList2D(array):
    averageResult = []
    for i in range(0, len(array)):
        averageResult.append(statistics.mean(array[i]))
    return averageResult


def averageForList1D(array):
    return statistics.mean(array)






def medianOfArray(array):

    if isinstance(array[0], list):
        result = []
        result = medianForList2D(array)
    else:
        result = 0
        result = medianForList1D(array)
    return result


def medianForList2D(array):
    medianResult = []
    for i in range(0, len(array)):
        medianResult.append(statistics.median(array[i]))
    return medianResult

def medianForList1D(array):
    return statistics.median(array)
