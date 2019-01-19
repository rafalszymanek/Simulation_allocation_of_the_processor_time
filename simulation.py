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
    saveIntToFile(averageValue)
    # Interface
    print("\n---------------------\n\tFCFS\n---------------------")
    print("Waiting time: ")
    print("Median = "+ str(medianValue) + " [s]")
    print("Mean = " + str(averageValue) + " [s]")

    # Processing Time Statistic Stuff
    averageValue, medianValue = arytythmeticStuff(listOfAllProcessingTime)

    saveIntToFile(averageValue)
    print("\nProcessing time: ")
    print("Median = "+ str(medianValue) + " [s]")
    print("Mean = " + str(averageValue) + " [s]")

    clearAllLists()

    # Do SJF
    listOfAllWaitingTime, listOfAllProcessingTime = sjf(matrix)

    # Waiting Time Statistic Stuff
    averageValue, medianValue = arytythmeticStuff(listOfAllWaitingTime)
    saveIntToFile(averageValue)
    # Interface
    print("\n---------------------\n\tSJF\n---------------------")
    print("Waiting time: ")
    print("Median = "+ str(medianValue) + " [s]")
    print("Mean = " + str(averageValue) + " [s]")

    # Processing Time Statistic Stuff
    averageValue, medianValue = arytythmeticStuff(listOfAllProcessingTime)
    saveIntToFile(averageValue)
    # Interface
    print("\nProcessing time: ")
    print("Median = "+ str(medianValue) + " [s]")
    print("Mean = " + str(averageValue) + " [s]")

    clearAllLists()
