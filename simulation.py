from sample.fcsfalgorythm import *
from sample.open_data import *



if __name__ == "__main__":
    global listOfWaitingTime
    global listOfProcessingTime

    matrix = openFileAndPutIntoMatrix()


    for i in range(0, len(matrix)):
        listOfThread = matrix[i]
        fcfs(listOfThread)


    print (listOfProcessingTime[1])
