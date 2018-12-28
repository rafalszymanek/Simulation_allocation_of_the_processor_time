from sample.thread import Thread



if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    p1 = Thread(50)
    print (p1.waitingTime)
    p1.putResultsToTable(array)

    print (array[len(array)-1])
