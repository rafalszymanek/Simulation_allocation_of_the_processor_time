from sample.fcsfalgorythm import *
from sample.open_data import *
from sample.statistics import *



if __name__ == "__main__":
    global listOfWaitingTime
    global listOfProcessingTime

    matrix = openFileAndPutIntoMatrix()

    for i in range(0, len(matrix)):
        listOfThread = matrix[i]
        fcfs(listOfThread)

    listAverageOfEachAttemptOfWaitingTime = averageOfArray(listOfWaitingTime)
    averageOfAllAttemptOfWaitingTime = averageOfArray(listAverageOfEachAttemptOfWaitingTime)

    listMedianOfEachAttemptOfWaitingTime = medianOfArray(listOfWaitingTime)
    medianOfAllAttemptOfWaitingTime = medianOfArray(listMedianOfEachAttemptOfWaitingTime)

    print("Median = "+ str(medianOfAllAttemptOfWaitingTime) + " [ms]")
    print("Mean = " + str(averageOfAllAttemptOfWaitingTime) + " [ms]")
