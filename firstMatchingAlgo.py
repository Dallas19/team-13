import csv

#class ranking():
#     def __init__(self, ):
"""with open("example_company.csv") as csvfile1:
    readCSV1= csv.reader(csvfile1, delimiter=',')
    counter = 0
    titleEliminator = csv.reader(csvfile1)
    jobCounter = []
    for row in readCSV1:
        comID = row[0]
        jobCounter.append(comID)
    numOfJob = len(jobCounter) """

def firstMatchingAlgo():
    with open("example_student.csv") as csvfile2:
        readCSV2 = csv.reader(csvfile2, delimiter=',')
        rankDict = {}
        finalArr = []
        next(readCSV2)
        for row in readCSV2: #store -1 for no entry of the rank
            stuID = row[0]
            #jID = row[2]
            colCounter = 2
            stringConcat = ""

            while colCounter < len(row):
                """if not(row[colCounter]):
                    continue
                else:"""
                jID = row[colCounter]
                stringConcat = str(jID) + '_'  + str(colCounter-1) + '_' + str(stuID)
                finalArr.append(stringConcat)
                colCounter += 1
        for i in range(len(finalArr)):
            tempContainer = finalArr[i].split('_')
            rankDict[(tempContainer[0], tempContainer[1])] = tempContainer[2]
        #sorted(rankDict.items(), key=lambda x: x[0])
        #sorted(rankDict.items(), key=lambda s: s[0][1])
        for k,v in sorted(rankDict.items(), key=lambda  x: x[0][0]):
            print (k, v)


if __name__ == "__main__":
    firstMatchingAlgo()