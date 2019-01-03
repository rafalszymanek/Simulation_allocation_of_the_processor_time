#Generate random values to list and put it to file

import random


with open("../data/random100x100values.txt", "w") as myfile:
    processesInAttempt = 10
    manyOfAttempt = 20
    #range of random
    fromNumber = 1
    toNumber = 100

    for i in range(manyOfAttempt):
        for j in range(processesInAttempt):
            randomNumber = random.randint(fromNumber,toNumber+1)
            myfile.write(str(randomNumber) + ' ')
        myfile.write('\n')
