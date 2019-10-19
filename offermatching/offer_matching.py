def match_offer():
    import csv
    with open('companies.csv') as cfile:
        compfile = csv.reader(cfile, delimiter=',')
        for row in compfile:
            if row[0] is '':
                break
            company = row[0]
            department = row[1]
            openings = row[2]
            student_ranking = row[3]
            students = student_ranking.split(',')
            #print(company, department, openings, student_ranking)
            #print(students)
            student_list = []
            for indiv in students:
                element = indiv.split('-')
                student_list.append(element)
            map_list = {}
            map_list[company] = student_list
            print(map_list)
            #     student = Student(element[0],element[1])
            # print(student.name)



# with open('students.csv') as sfile:
#     stufile = csv.readver(sfile, delimiter=',')
#     for row, enumerate in stufile:
#         student = row[0]
#         advisor = row[1]
#         ranking = row[2]

print(match_offer())

