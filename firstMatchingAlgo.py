import csv
import pandas as pd
# import numpy as np

def firstMatchingAlgo():
    with open("students.csv") as csvfile2:
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
    df = pd.DataFrame(data=rankDict.items(), columns=["col1", "col2"])
    #df1 = pd.DataFrame(columns=['col1', 'col2'])
    df1 = pd.DataFrame(df["col1"].tolist(), index= df.index)
    df1 = df1.assign(col3 = df["col2"])
    df1 = df1.sort_values(by=[0])
    df1 = df1.sort_values(by=[1])
    print(df1)
    for index, row in df1.iterrows():
        finalDict[row[0]] = []
    for index, row in df1.iterrows():
        if row[0] in finalDict:
            #print(row['col3'])
            finalDict[row[0]].append(row['col3'])
    for k in finalDict.values():
        if(len(k) > 36):
            k = k[:37]
    for k, v in finalDict.items():
        print(k, v)

    return finalDict
if __name__ == "__main__":
    firstMatchingAlgo()