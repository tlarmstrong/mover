import csv
import sys
import mConnect

def convert(input):

    result = "None"

    # using a set to find the sections (unique elements only)
    findSection = set([])

    # Connect to the database.
    conn = mConnect.connection()
    c = conn.cursor()
    c.execute("START TRANSACTION")

    c.execute("SELECT * FROM `class` " )
    for section in c.fetchall():
        if (input.find('.') != -1):
            input = input.replace(" ", "")
            input = input.replace(".0", ".")
            #section = '11081','201610','CS','374','1','Software Engineering',3)
            if (input.upper() == section[2]+section[3]+'.'+section[4]):
                result = section[0]
        # subject code + a course number
        elif (input[0].isalpha() and input[len(input)-1].isdigit()):
            input = input.replace(" ", "")
            input = input.upper()
            if(input.upper() == section[2]+section[3]):
                findSection.add(section[2]+section[3]+'.'+section[4])
                result = section[0]
        # subject code only
        elif(input[0].isalpha() and len(input) < 5):
            input = input.upper()
            if (input == section[1]):
                findSection.add(section[2]+section[3]+'.'+section[4])
                result = section[0]
        # course title
        else:
            if (input.lower() == section[5].lower()):
                findSection.add(section[2]+section[3]+'.'+section[4])
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
