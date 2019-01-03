from sample.fcsfalgorythm import *
from sample.open_data import *
from sample.statistics import *

path = "data/test_values.txt"


if __name__ == "__main__":
    #OUR MAIN LISTS
    global listOfAllWaitingTime
    global listOfAllProcessingTime

    #Matrix is a 2D list
    matrix = openFileAndPutIntoMatrix(path)

    #Do FCFS for every row in matrix
    for i in range(0, len(matrix)):
        listOfProcess = matrix[i]
        fcfs(listOfProcess)

    listAverageOfEachAttemptOfWaitingTime = averageOfArray(listOfAllWaitingTime)
    averageOfAllAttemptOfWaitingTime = averageOfArray(listAverageOfEachAttemptOfWaitingTime)

    listMedianOfEachAttemptOfWaitingTime = medianOfArray(listOfAllWaitingTime)
    medianOfAllAttemptOfWaitingTime = medianOfArray(listMedianOfEachAttemptOfWaitingTime)

    print("FCFS")
    print("Waiting time: ")
    print("Median = "+ str(medianOfAllAttemptOfWaitingTime) + " [ms]")
    print("Mean = " + str(averageOfAllAttemptOfWaitingTime) + " [ms]")

    listAverageOfEachAttemptOfProcessingTime = averageOfArray(listOfAllProcessingTime)
    averageOfAllAttemptOfProcessigTime = averageOfArray(listAverageOfEachAttemptOfProcessingTime)

    listMedianOfEachAttemptOfProcssingTime = medianOfArray(listOfAllProcessingTime)
    medianOfAllAttemptOfProcessingTime = medianOfArray(listMedianOfEachAttemptOfProcssingTime)
    print("\nProcessing time: ")
    print("Median = "+ str(medianOfAllAttemptOfProcessingTime) + " [ms]")
    print("Mean = " + str(averageOfAllAttemptOfProcessigTime) + " [ms]")
