# CustomerSimulation.py

import datetime as dt
import random as rd

def createFiles():
    initialFileName = "cust_arrival_"
    extension = ".log"
    for f in range(1, 11):
        # file names follows cust_arrival_*.log
        writeIntoFile(initialFileName + str(f) + extension)
    ## END
## END


def writeIntoFile(fileName):
    with open(fileName, "w", encoding="utf-8") as f:
        f.write("CUSTID,TIMESTAMP\n")
        for i in range(20):
            line = str(rd.randint(1,200)) + str(",") + str(dt.date.today()) + ("\n")
            f.write(line)
        ## END
    ## END
## END


if __name__ == '__main__':
    createFiles()
## END

