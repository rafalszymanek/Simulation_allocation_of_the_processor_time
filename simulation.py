from sample.fcsfalgorythm import *
from sample.sjfalgorythm import *
from sample.open_data import *
from sample.statistics import *
from sample.globals import path

if __name__ == "__main__":
    #Matrix is a 2D list
    matrix = openFileAndPutIntoMatrix(path)

    # Do FCFS
    listOfAllWaitingTime, listOfAllProcessingTime = fcfs(matrix)

    # Waiting Time Statistic Stuff
    averageValue, medianValue = arytythmeticStuff(listOfAllWaitingTime)

    # Interface
    print("\n---------------------\n\tFCFS\n---------------------")
    print("Waiting time: ")
    print("Median = "+ str(medianValue) + " [ms]")
    print("Mean = " + str(averageValue) + " [ms]")

    # Processing Time Statistic Stuff
    averageValue, medianValue = arytythmeticStuff(listOfAllProcessingTime)

    print("\nProcessing time: ")
    print("Median = "+ str(medianValue) + " [ms]")
    print("Mean = " + str(averageValue) + " [ms]")

    clearAllLists()

    # Do SJF
    listOfAllWaitingTime, listOfAllProcessingTime = sjf(matrix)

    # Waiting Time Statistic Stuff
    averageValue, medianValue = arytythmeticStuff(listOfAllWaitingTime)

    # Interface
    print("\n---------------------\n\tSJF\n---------------------")
    print("Waiting time: ")
    print("Median = "+ str(medianValue) + " [ms]")
    print("Mean = " + str(averageValue) + " [ms]")

    # Processing Time Statistic Stuff
    averageValue, medianValue = arytythmeticStuff(listOfAllProcessingTime)

    # Interface
    print("\nProcessing time: ")
    print("Median = "+ str(medianValue) + " [ms]")
    print("Mean = " + str(averageValue) + " [ms]")

    clearAllLists()
