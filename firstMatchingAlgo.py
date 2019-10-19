import csv


def firstMatchingAlgo():
    with open("example_student.csv") as csvfile2:
        readCSV2 = csv.reader(csvfile2, delimiter=',')
        rankDict = {}
        finalArr = []
        next(readCSV2)
        for row in readCSV2:
            stuID = row[0]
            #jID = row[2]
            colCounter = 2
            stringConcat = ""

            while colCounter < len(row):

                jID = row[colCounter]
                stringConcat = str(jID) + '_'  + str(colCounter-1) + '_' + str(stuID)
                finalArr.append(stringConcat)
                colCounter += 1
        for i in range(len(finalArr)):
            tempContainer = finalArr[i].split('_')
            rankDict[(tempContainer[0], tempContainer[1])] = tempContainer[2]
        rankDict.update(sorted(rankDict.items(), key=lambda x: x[0][0]))
        rankDict.update(sorted(rankDict.items(), key=lambda s: s[0][1]))
        # format of rankDict Dictionary
         # (JOBID, Priority) -> StudentID
        for k,v in sorted(rankDict.items()):
            print (k, v)
    finalDict = {}
    jobIDtracker = 0
    for i in range(len(rankDict.keys()):
        


if __name__ == "__main__":
    firstMatchingAlgo()