def openFileAndPutIntoMatrix():
    fileWithData = open("data/test_values.txt", "r")
    w, h = 100, 100;
    matrix = [[0 for x in range(w)] for y in range(h)]

    data = True
    i = 0
    for line in fileWithData:
        ourList = (list(map(int, line.split())))
        for j in range(0,100):
            matrix[i][j] = ourList[j]
        i+=1

    return matrix
