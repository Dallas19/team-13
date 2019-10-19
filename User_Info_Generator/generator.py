import os
import random

# Company DB
# Job ID (auto-incrementing), Company, Position, Number of Slots, Student Rank #1, Student Rank #2, Student Rank #3, Student Rank #4, Student Rank #5, etc.

# Student DB
# Student ID (auto-incrementing), Student Name, Job ID #1, Job ID #2, Job ID #3, Job ID #4, Job ID #5

COMPANY_LIST = os.path.join(os.getcwd, "/User_Generator_Info/companies.txt")
POSITION_LIST = os.path.join(os.getcwd, "/User_Generator_Info/positions.txt")
FNAME_LIST = os.path.join(os.getcwd, "/User_Generator_Info/first_names.txt")
LNAME_LIST = os.path.join(os.getcwd, "/User_Generator_Info/last_names.txt")

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

    return job

for i in range(10):
    print(generate_job)

def generate_student():
    return ""

def select_positions_for_student():
    return ""

def generate_num_top_students():
    return ""

def rank_rand_students():
    return ""

# generate 1000 students
# generate 500 job positions