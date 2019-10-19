import csv

#class ranking():
#     def __init__(self, ):
def firstMatchingAlgo(studentFilename, comFilename):
    with open(studentFilename) as csvfile:
        readCSV1 = csv.reader(csvfile, delimiter=',')
        studentInfo = []
        companyRanking = []
        for row in readCSV1:
            studentInfo = 



    with open(comFilename) as csvfile:
        readCSV2 = csv.reader(csvfile, delimiter=',')


















if __name__ == '__main__':