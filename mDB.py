#!/usr/bin/env python

import csv
import glob
import os
import mysql.connector
from collections import defaultdict

# Turn on debug mode.
import cgitb

def setupDB():
    cgitb.enable()

    conn = mysql.connector.connect(
        db='mover',
        user='root',
        passwd='', 
        host='localhost')
    c = conn.cursor()
    c.execute("START TRANSACTION")

    
    count = 0

    if (count == 0):
        c.execute("DROP TABLE IF EXISTS `student`")
        c.execute("CREATE TABLE `student` (id varchar(10) NOT NULL, firstName varchar(20) NOT NULL, lastName varchar(20) NOT NULL, classification varchar(10), email varchar(100), dept varchar(50), hours int(10), grade varchar(2), PRIMARY KEY(id))") 

        c.execute("DROP TABLE IF EXISTS `enrollment`")
        c.execute("CREATE TABLE `enrollment` (id varchar(10) NOT NULL, crn varchar(10), termCode varchar(10), hours int(3), PRIMARY KEY(id, crn, termCode))")

        c.execute("DROP TABLE IF EXISTS `section`")
        c.execute("CREATE TABLE `section` (crn varchar(10), termCode varchar(10) NOT NULL, profID varchar(5), d1 varchar(3), d2 varchar(3), d3 varchar(3), d4 varchar(3), d5 varchar(3), beginTime varchar(5), endTime varchar(5), building varchar(6), room varchar(5), capacity varchar(3), enrolled varchar(3), PRIMARY KEY(crn, termCode))")

        c.execute("DROP TABLE IF EXISTS `class`")
        c.execute("CREATE TABLE `class` (crn varchar(10), termCode varchar(10) NOT NULL, subjectCode varchar(5), courseNum varchar(5), section varchar(5), title varchar(70), PRIMARY KEY(crn, termCode, subjectCode, courseNum))")

        c.execute("DROP TABLE IF EXISTS `instructor`")
        c.execute("CREATE TABLE `instructor` (id varchar(10), name varchar(30), PRIMARY KEY(id))")

        c.execute("DROP TABLE IF EXISTS `instSection`")
        c.execute("CREATE TABLE `instSection` (id varchar(10), crn varchar(10), termCode varchar(10), eval varchar(3), PRIMARY KEY(id, crn, termCode))")

        count += 1

    # since we now know CRNs are reused, let's read in the file and make the primary key the max('Term Code') and CRN for section
    f = open('info/cs374_anon.csv')
    reader = csv.DictReader(f)
    term = 0
    for t in reader:
        if(t['Term Code'] > term):
            term = t['Term Code']
    print('Term: '+term)
    f.close()
        
    f = open('info/cs374_anon.csv')
    reader = csv.DictReader(f)
    for row in reader:
        if(row['Term Code'] == term):

            # section: crn, termCode, profID, d1, d2, d3, d4, d5, beginTime, endTime, building, room, capacity, enrolled
            c.execute("""INSERT IGNORE INTO `section` 
                                        (`crn`, `termCode`, `profID`, `d1`, `d2`, `d3`, `d4`, `d5`, `beginTime`, `endTime`, `building`, `room`, `capacity`, `enrolled`)

                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",

                                       (str(row['CRN']),
                                         str(row['Term Code']),
                                         str(row['Instructor ID']),
                                         str(row['Monday Ind1']),
                                         str(row['Tuesday Ind1']),
                                         str(row['Wednesday Ind1']),
                                         str(row['Thursday Ind1']),
                                         str(row['Friday Ind1']),
                                         str(row['Begin Time 1']),
                                         str(row['End Time1']),
                                         str(row['Bldg Code1']),
                                         str(row['Room Code1']),
                                         str(row['Section Max Enrollment']),
                                         str(row['Section Enrollment'])
                                        )
                                    )
    print('section added')
    conn.commit()
    f.close()

    # c.execute("SELECT * FROM `section`")
    # for test in c.fetchall():   
    #     print(test[0])

    f = open('info/cs374_anon.csv')
    reader = csv.DictReader(f)
    for row in reader:
        # student: id, firstName, lastName, classification, email, dept, hours, grade
        c.execute("""INSERT IGNORE INTO `student` 
                                (`id`, `firstName`, `lastName`, `classification`, `email`, `dept`, `hours`, `grade`) 
                                VALUES (%s, %s, %s, %s, %s, %s, 0, %s)""", 

                                (str(row['Banner ID']),
                                 str(row['First Name']),
                                 str(row['Last Name']),
                                 str(row['Class Code']),
                                 str(row['ACU Email Address']),
                                 str(row['Department Code']),
                                 str(row['Grade Code'])
                                 )
                            )

    print('student added')
    conn.commit()
    f.close()

    f = open('info/cs374_anon.csv')
    reader = csv.DictReader(f)
    for row in reader:
        # enrollment: id, crn, termCode, hours
        c.execute("""INSERT IGNORE INTO `enrollment` 
                                (`id`, `crn`, `termCode`, `hours`) 
                                VALUES (%s, %s, %s, %s)""", 

                                (str(row['Banner ID']),
                                 str(row['CRN']),
                                 str(row['Term Code']),
                                 str(row['Credit Hours'])
                                 )
                            )

    print('enrollment added')
    conn.commit()
    f.close()

    f = open('info/cs374_anon.csv')
    reader = csv.DictReader(f)
    for row in reader:
        # class: crn, termCode, subjectCode, courseNum, section, title
        c.execute("""INSERT IGNORE INTO `class` 
                                    (`crn`, `termCode`, `subjectCode`, `courseNum`, `section`, `title`) 
                                    VALUES (%s, %s, %s, %s, %s, %s)""",

                                    (str(row['CRN']),
                                     str(row['Term Code']),
                                     str(row['Subject Code']),
                                     str(row['Course Number']),
                                     str(row['Section Number']),
                                     str(row['Course Title'])
                                     )
                                )

    print('class added')
    conn.commit()
    f.close()

    f = open('info/cs374_anon.csv')
    reader = csv.DictReader(f)
    for row in reader:
        # instructor: id, prof
        c.execute("""INSERT IGNORE INTO `instructor` 
                                (`id`, `name`) 
                                VALUES (%s, %s)""", 

                                (str(row['Instructor ID']),
                                 str(row['Instructor Name'])
                                 )
                            )

    print('instructor added')
    conn.commit()
    f.close()

    f = open('info/cs374_anon.csv')
    reader = csv.DictReader(f)
    for row in reader:
        # instSection: id, crn, termCode, eval
        c.execute("""INSERT IGNORE INTO `instSection` 
                                (`id`, `crn`, `termCode`, `eval`) 
                                VALUES (%s, %s, %s, '')""", 

                                (str(row['Banner ID']),
                                 str(row['CRN']),
                                 str(row['Term Code'])
                                 )
                            )

    print('instSection added\n')
    conn.commit()
    f.close()

    # c.execute("SELECT * FROM `student`")
    # for test in c.fetchall():   
    #     print(test)

    # c.execute("SELECT * FROM `studentclass`")
    # for test in c.fetchall():   
    #     print(test)

    # c.execute("SELECT * FROM `class`")
    # for test in c.fetchall():   
    #     print(test)

    c.close()
    conn.close()
    return term

