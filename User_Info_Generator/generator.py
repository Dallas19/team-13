import os
import random
import csv

from pathlib import Path

# Company DB
# Job ID (auto-incrementing), Company, Position, Number of Slots, Student Rank #1, Student Rank #2, Student Rank #3, Student Rank #4, Student Rank #5, etc.

# Student DB
# Student ID (auto-incrementing), Student Name, Job ID #1, Job ID #2, Job ID #3, Job ID #4, Job ID #5

PATH = str(Path(__file__).parent.absolute())

COMPANY_LIST = PATH + "/User_Generator_Info/companies.txt"
POSITION_LIST = PATH + "/User_Generator_Info/positions.txt"
FNAME_LIST = PATH + "/User_Generator_Info/first_names.txt"
LNAME_LIST = PATH + "/User_Generator_Info/last_names.txt"

def generate_job():
    # generate random number from 0 to 99
    cIndex = random.randint(0, 99)

    cList = open(COMPANY_LIST)
    companies = cList.readlines()

    company = companies[cIndex]

    cList.close()

    # generate random number from 0 to 24
    pIndex = random.randint(0, 24)

    pList = open(POSITION_LIST)
    positions = pList.readlines()

    position = positions[pIndex]

    pList.close()

    # generate number of slots (random int from 1 to 5)
    num_slots = random.randint(1, 5)

    job = {"company" : company.replace("\n", ""), "position" : position.replace("\n", ""), "num_slots" : num_slots}

    return job

# for i in range(10):
#     generate_job()

def generate_student():
    # generate random number from 0 to 39
    fIndex = random.randint(0, 39)

    fList = open(FNAME_LIST)
    fnames = fList.readlines()

    fname = fnames[fIndex].replace("\n", "")

    fList.close()

    # generate random number from 0 to 39
    lIndex = random.randint(0, 39)

    lList = open(LNAME_LIST)
    lnames = lList.readlines()

    lname = lnames[lIndex].replace("\n", "")

    fList.close()

    # generate number of positions wanted (random int from 1 to 5)
    # num_wanted = random.randint(1, 5)
    num_wanted = 5

    student = {"name" : f"{fname} {lname}", "num_wanted" : num_wanted}

    return student

def select_positions_for_student(num_wanted):
    job_arr = []
    for i in range(7):
        if i <= num_wanted:
            job_id = random.randint(0,499)
            if job_id in job_arr:
                i-=1
                continue
            else:
                job_arr.append(job_id)
                continue
        else:
            job_arr.append("")
    return job_arr

def generate_num_top_students(min_num):
    return min_num + random.randint(1,8)

def rank_rand_students(num_available):
    student_arr = []
    for i in range(18):
        if i <= num_available:
            student_id = random.randint(0,999)
            if student_id in student_arr:
                i-=1
                continue
            else:
                student_arr.append(student_id)
                continue
        else:
            student_arr.append("")
    return student_arr

def populate_students():
    with open("students.csv", "w") as students_csv:
        filewriter = csv.writer(students_csv, delimiter = ",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        filewriter.writerow(["Student ID", "Student Name", "Job ID #1", "Job ID #2", "Job ID #3", "Job ID #4", "Job ID #5"])

        for i in range(2500):
            student = generate_student()
            position = select_positions_for_student(student["num_wanted"])
            filewriter.writerow([i, student["name"], position[0], position[1], position[2], position[3], position[4]])

    return

def populate_jobs():
    with open("jobs.csv", "w") as jobs_csv:
        filewriter = csv.writer(jobs_csv, delimiter = ",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerow(["Job ID", "Company", "Position", "Number of Slots", "Student ID Rank #1", "Student ID Rank #2", "Student ID Rank #3", "Student ID Rank #4", "Student ID Rank #5", "Student ID Rank #6", "Student ID Rank #7", "Student ID Rank #8", "Student ID Rank #9", "Student ID Rank #10", "Student ID Rank #11", "Student ID Rank #12", "Student ID Rank #13", "Student ID Rank #14", "Student ID Rank #15"])

        for i in range(60):
            job = generate_job()
            num_students = generate_num_top_students(job["num_slots"])
            ranked_students = rank_rand_students(num_students)
            filewriter.writerow([i, job["company"], job["position"], job["num_slots"], ranked_students[0], ranked_students[1], ranked_students[2], ranked_students[3], ranked_students[4], ranked_students[5], ranked_students[6], ranked_students[7], ranked_students[8], ranked_students[9], ranked_students[10], ranked_students[11], ranked_students[12], ranked_students[13], ranked_students[14]])

    return

populate_jobs()
populate_students()