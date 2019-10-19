import os
import random

from pathlib import Path

# Company DB
# Job ID (auto-incrementing), Company, Position, Number of Slots, Student Rank #1, Student Rank #2, Student Rank #3, Student Rank #4, Student Rank #5, etc.

# Student DB
# Student ID (auto-incrementing), Student Name, Job ID #1, Job ID #2, Job ID #3, Job ID #4, Job ID #5

PATH = str(Path(__file__).parent.absolute())

COMPANY_LIST = PATH + "/User_Generator_Info/companies.txt"
POSITION_LIST = PATH + "/User_Generator_Info/positions.txt"
FNAME_LIST = os.path.join(os.getcwd(), "/User_Generator_Info/first_names.txt")
LNAME_LIST = os.path.join(os.getcwd(), "/User_Generator_Info/last_names.txt")

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

    job = {"company" : company, "position" : position, "num_slots" : num_slots}
    
    print(job)

    return job

# for i in range(10):
#     generate_job()

def generate_student():
    return ""

def select_positions_for_student():
    return ""

def generate_num_top_students(min_num):
    return min_num + random.randint(1,6)

def rank_rand_students(num_available):
    return ""

def populate_students():
    for i in range(1000):
        student = generate_student()
        select_positions_for_student()

    return ""

def populate_jobs():
    for i in range(500):
        job = generate_job()
        num_students = generate_num_top_students(job["num_slots"])
        rank_rand_students(num_students)
        print("%d %s %s %s", i, job["company"], job["position"])
    
    return ""

populate_jobs()

# generate 1000 students
# generate 500 job positions