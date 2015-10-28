# https://pymotw.com/2/csv/
import csv
import sys
import mysql.connector

def convert(input):

    result = "None"

    # using a set to find the sections (unique elements only)
    findSection = set([])
    #f = open('info/CS374_2016_registrations.csv','rU')

    # DictReader translates rows to dictionaries
    # Keys for the dictionary are inferred from the first row in the input
    #reader = csv.DictReader(f)

    # Connect to the database.
    #import pymysql
    #conn = pymysql.connect(
    conn = mysql.connector.connect(
        db='example', #prereq
        user='root',
        passwd='', #sett!ngupServerFrs0ftEngCl@s5
        host='localhost')
    c = conn.cursor()
    c.execute("START TRANSACTION")

    c.execute("SELECT * FROM `section` " )
    for section in c.fetchall():
        if (input.find('.') != -1):
            input = input.replace(" ", "")
            input = input.replace(".0", ".")
            #`id`, `subjCode`, `courseNum`, `section`, `title`, `termCode`
            if (input.upper() == section[1]+section[2]+'.'+section[3]):
                result = section[0]
        # subject code + a course number
        elif (input[0].isalpha() and input[len(input)-1].isdigit()):
            input = input.replace(" ", "")
            input = input.upper()
            if(input.upper() == section[1]+section[2]):
                findSection.add(section[1]+section[2]+'.'+section[3])
                result = section[0]
        # subject code only
        elif(input[0].isalpha() and len(input) < 5):
            input = input.upper()
            if (input == section[1]):
                findSection.add(section[1]+section[2]+'.'+section[3])
                result = section[0]
        # course title
        else:
            if (input.lower() == section[4].lower()):
                findSection.add(section[1]+section[2]+'.'+section[3])
                #result = row['Subject Code']+row['Course Number']+'.'+row['Section Number']
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