# http://radon.readthedocs.org/en/latest/intro.html
# --------------------------------------------------
# Cyclomatic complexity
# --------------------------------------------------
#   F 20:0 convert - C (13)

# --------------------------------------------------
# Halstead complexity
# --------------------------------------------------
#   h1: 7
#   h2: 58
#   N1: 30
#   N2: 60
#   h: 65
#   N: 90
#   length: 359.41
#   volume: 542.01
#   difficulty: 3.62
#   effort: 1962.46

import csv
import sys
import cConnect

def convert(input):

    # if we can not find a match, we return "None" (default)
    result = "None"

    # using a set to find the sections (unique elements only)
    findSection = set([])

    # Connect to the database.
    conn = cConnect.connection()
    c = conn.cursor()
    c.execute("START TRANSACTION")

    c.execute("SELECT * FROM `class` " )
    for section in c.fetchall():
        # if section number, this means we need to format it to work with banner's formatting
        if (input.find('.') != -1):
            input = input.replace(" ", "")
            input = input.replace(".0", ".")
            # then we can match this up with a subject code and course number
            if (input.upper() == section[2]+section[3]+'.'+section[4]):
                # if match, we want to return the CRN
                result = section[0]

        # subject code + course number (no section number)
        elif (input[0].isalpha() and input[len(input)-1].isdigit()):
            input = input.replace(" ", "")
            input = input.upper()
            if(input.upper() == section[2]+section[3]):
                findSection.add(section[2]+section[3]+'.'+section[4])
                # if match, we want to return the CRN
                result = section[0]

        # subject code only
        elif(input[0].isalpha() and len(input) < 5):
            input = input.upper()
            if (input == section[1]):
                findSection.add(section[2]+section[3]+'.'+section[4])
                # if match, we want to return the CRN
                result = section[0]

        # course title
        else:
            if (input.lower() == section[5].lower()):
                findSection.add(section[2]+section[3]+'.'+section[4])
                # if match, we want to return the CRN
                result = section[0]

    # if the course has at least 2 sections, ask the user to tell us which one he/she wants
    if (len(findSection) > 1):
        temp = input+' has '+str(len(findSection))+' sections, please choose one: '+findSection.pop()
        while (len(findSection)) != 0:
            temp += ', '+findSection.pop()  
        result = temp

    c.close()
    conn.close()
    return str(result)
