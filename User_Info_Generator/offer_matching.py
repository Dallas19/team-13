company_opening_map = {}
def get_data():
    import csv
    with open('jobs.csv') as cfile:
        compfile = csv.reader(cfile, delimiter=',')
        company_map = {}
        for row in compfile:
            if row[0] is '':
                break
            job_id = row[0]
            company = row[1]
            position = row[2]
            opening_num = row[3]
            students = []
            i = 4
            while i < len(row):
                if row[i] is '':
                    break
                students.append(row[i])
                i += 1
            company_map[job_id] = students
            company_opening_map[job_id] = opening_num

    with open('students.csv') as cfile:
        compfile = csv.reader(cfile, delimiter=',')
        student_map = {}
        for row in compfile:
            if row[0] is '':
                break
            student_id = row[0]
            student_name = row[1]
            companies = []
            i = 2
            while i < len(row):
                if row[i] is '':
                    break
                companies.append(row[i])
                i += 1
            student_map[student_id] = companies
        print(company_map)
        print(student_map)
    match_offer(company_map, student_map)
    return None

def match_offer(comp_list, stu_list):
    company_student_matching = {}
    for key in comp_list:
        students = comp_list[key]
        students_matched = []
        for student in students:
            student_likes = stu_list.get(student)
            if student_likes is not None:
                if key in student_likes:
                    students_matched.append(student)
            company_student_matching[key] = students_matched
    print(company_student_matching)
    re_matching(company_student_matching,comp_list)
    return company_student_matching

def re_matching(company_student_matching, comp_list):
    print(company_opening_map)
    for key in company_student_matching:
        if len(company_student_matching[key]) == 0:
            try:
                openings = int(company_opening_map[key]) - 1
            except ValueError:
                continue
            while openings >= 0:
                company_student_matching[key].append(comp_list[key][openings])
                openings -= 1
    print(company_student_matching)
    return(company_student_matching)

get_data()

