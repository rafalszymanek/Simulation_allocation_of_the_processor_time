#Generate random values to list and put it to file

import random


with open("../data/random100x100values.txt", "w") as myfile:
    for i in range(100):
        for j in range(100):
            randomNumber = random.randint(1,101)
            myfile.write(str(randomNumber) + ' ')
        myfile.write('\n')
