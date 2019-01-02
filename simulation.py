from sample.fcsfalgorythm import *



if __name__ == "__main__":
    global listOfWaitingTime
    global listOfProcessingTime
    listOfThread = [11, 56, 2, 9, 99, 12, 34, 22, 85, 53]
    fcfs(listOfThread)

    print (listOfWaitingTime)
    print (listOfProcessingTime)
