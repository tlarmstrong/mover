# http://radon.readthedocs.org/en/latest/intro.html

# --------------------------------------------------
# Cyclomatic complexity
# -------------------------------------------------- 
#    F 87:0 getStudentDetails - E
#    F 154:0 getInstructorDetails - C
#    F 178:0 getClassInfo - C
#    F 52:0 getClassificationBreakdown - B
#    F 28:0 getBasics - A
#    F 39:0 getClassDetails - A

# 6 blocks (classes, functions, methods) analyzed.
# Average complexity: C (13.67)

# --------------------------------------------------
# Halstead complexity
# --------------------------------------------------
# getBasics
#   h1: 1
#   h2: 8
#   N1: 4
#   N2: 8
#   h: 9
#   N: 12
#   length: 24.0
#   volume: 38.04
#   difficulty: 0.5
#   effort: 19.20

# getClassDetails
#   h1: 1
#   h2: 36
#   N1: 18
#   N2: 36
#   h: 37
#   N: 54
#   length: 186.12
#   volume: 281.31
#   difficulty: 0.5
#   effort: 140.66

# getClassificationBreakdown
#   h1: 4
#   h2: 17
#   N1: 11
#   N2: 22
#   h: 21
#   N: 33
#   length: 77.49
#   volume: 144.95
#   difficulty: 2.59
#   effort: 375.16

# getStudentDetails
#   h1: 8
#   h2: 140
#   N1: 76
#   N2: 157
#   h: 148
#   N: 233
#   length: 1022.10
#   volume: 1679.80
#   difficulty: 4.49
#   effort: 7535.11

# getInstructorDetails
#   h1: 7
#   h2: 96
#   N1: 47
#   N2: 99
#   h: 103
#   N: 146
#   length: 651.81
#   volume: 976.23
#   difficulty: 3.61
#   effort: 3523.58

# getClassInfo
#   h1: 6
#   h2: 148
#   N1: 81
#   N2: 159
#   h: 154
#   N: 240
#   length: 1082.51
#   volume: 1744.03
#   difficulty: 3.22
#   effort: 5620.96

from collections import defaultdict
import cConnect  

    # Database tables...
    # section: crn, termCode, profID, d1, d2, d3, d4, d5, beginTime, endTime, building, room, capacity, enrolled
    # student: id, firstName, lastName, classification, email, dept, hours, grade
    # enrollment: id, crn, termCode, hours
    # class: crn, termCode, subjectCode, courseNum, section, title
    # instructor: id, prof
    # instSection: id, crn, termCode, eval 

def getBasics(course, term, c):

    # get basic class information based on input (course) and most current term (term)
    # output example: CS374: Software Engineering
    query = ("SELECT a.crn, b.* FROM section a, class b WHERE a.crn = %(id)s AND a.termCode = %(term)s AND a.crn = b.crn AND a.termCode = b.termCode")
    c.execute(query, { 'id': course, 'term': term })
    for section in c:
        print ('\n'+section[3]+section[4]+': '+section[6])

    return section

def getClassDetails(course, term, c):

    # section details: Instructor, Day/Time, Building/Room, number of students enrollled    
    query = ("SELECT a.*, b.* FROM section a, instructor b WHERE a.crn = %(course)s AND a.termCode = %(term)s AND a.profID = b.id")
    c.execute(query, { 'course': course, 'term': term })
    for detail in c:
        print ('Instructor: '+detail[15])
        print ('When: '+detail[3]+' '+detail[4]+' '+detail[5]+' '+detail[6]+' '+detail[7]+' '+detail[8]+' - '+detail[9])
        print ('Where: '+detail[10]+' Room '+detail[11])
        print ('Enrolled: '+str(detail[13]))

    return detail

def getClassificationBreakdown(course, term, c):

    # class breakdown (# of each classification enrolled)
    se = 0      # seniors
    j = 0       # juniors
    so = 0      # sophomores
    f = 0       # freshman

    # get classification for each student in the section
    query = ("SELECT a.*, b.* FROM enrollment b, student a WHERE a.id = b.id AND b.crn = %(crn)s AND b.termCode = %(term)s")
    c.execute(query, { 'crn': course, 'term': term })
    for classList in c.fetchall():
        query = ("SELECT b.id, sum(b.hours), a.id FROM enrollment b, student a WHERE b.id = a.id AND b.id = %(id)s")
        c.execute(query, { 'id': classList[0] })
        for hours in c.fetchall():
            h = int(hours[1])
            # get student classification based on total hours, add to student table
            query = ("UPDATE student SET hours = %(hours)s WHERE id = %(id)s")
            c.execute(query, { 'hours': h, 'id': classList[0] }) 
            query = ("SELECT hours FROM student WHERE id = %(id)s")
            c.execute(query, { 'id': classList[0] })

            # increment class breakdown vars
            for shours in c:
                if(shours[0] >= 90):
                    se += 1
                elif(shours[0] < 90 and shours[0] >= 60):
                    j += 1
                elif(shours[0] < 60 and shours[0] >= 30):
                    so += 1
                else:
                    f += 1

    return [f, so, j, se]

def getStudentDetails(course, term, c, dList, trynew, end):

    conflicts = 0               # total conflicts

    # conflict breakdown per classification
    seConflict = 0              # senior
    jConflict = 0               # junior
    soConflict = 0              # sophomore
    fConflict = 0               # freshman

    # output details for each enrolled student 
    query = ("SELECT a.*, b.* FROM enrollment a, student b WHERE a.crn = %(crn)s AND a.termCode = %(term)s AND a.id = b.id ORDER BY b.hours desc")
    c.execute(query, { 'crn': course, 'term': term })
    for student in c.fetchall():
        print('\n')
        print('--------------------------------------------------------')
        print (student[0]+'\t'+student[5]+' '+student[6]+'\t'+student[8]+'\t'+student[9])
        print('--------------------------------------------------------')

        # output student's major and classification
        print ( 'Major: '+str(student[12]))
        print ('Hours: '+str(student[10]))
        if(student[10] >= 90):
            print('Year:  Senior')
        elif(student[10] < 90 and student[10] >= 60):
            print('Year:  Junior')
        elif(student[10] < 60 and student[10] >= 30):
            print('Year:  Sophomore')
        else:
            print('Year:  Freshman')

        # check student schedules for conflicts with new time
        query = ("SELECT a.*, b.* FROM section a, enrollment b WHERE a.crn = b.crn AND b.termCode = a.termCode AND b.id = %(id)s AND b.termCode = %(term)s")
        c.execute(query, { 'id': student[0], 'term': student[2] })
        for time in c.fetchall():
            if time[8] != '':
                oStart = int(time[8])
                oEnd = int(time[9])
                if (time[0] != course and (trynew == oStart or (trynew > oStart and trynew < oEnd) or (end > oStart and end < oEnd)) and ((time[3] != '' and time[3] == dList[0]) or (time[4] != '' and time[4] == dList[1]) or (time[5] != '' and time[5] == dList[2]) or (time[6] != '' and time[6] == dList[3]) or (time[7] != '' and time[7] == dList[4]))):

                    query = ("SELECT a.*, b.* FROM section a, enrollment b WHERE a.crn = b.crn AND b.termCode = a.termCode AND a.beginTime = %(begin)s AND (a.d1 = %(d1)s OR a.d2 = %(d2)s OR a.d3 = %(d3)s OR a.d4 = %(d4)s OR a.d5 = %(d5)s) AND b.id = %(id)s AND a.termCode = %(term)s")
                    c.execute(query, { 'id': student[0], 'term': student[2], 'begin': time[8], 'd1': time[3], 'd2': time[4], 'd3': time[5], 'd4': time[6], 'd5': time[7] })
                    for i in c.fetchall():

                        query = ("SELECT * FROM class WHERE crn = %(crn)s AND termCode = %(term)s")
                        c.execute(query, { 'crn': i[0], 'term': i[1] })
                        for k in c.fetchall():
                            # output conflicts (name of class, time, and where)
                            print('\n\t******************** CONFLICT *********************')
                            print('\n\tClass: '+k[2]+k[3]+' '+k[5])
                            print('\tWhen: '+time[3]+' '+time[4]+' '+time[5]+' '+time[6]+' '+time[7]+' '+time[8]+' - '+time[9])
                            print('\tWhere: '+time[10]+' Room '+time[11])

                    # add to conflict classification breakdown vars
                    if(student[10] >= 90):
                        seConflict += 1
                    elif(student[10] < 90 and student[10] >= 60):
                        jConflict += 1
                    elif(student[10] < 60 and student[10] >= 30):
                        soConflict += 1
                    else:
                        fConflict += 1

                    conflicts += 1

    return [conflicts, fConflict, soConflict, jConflict, seConflict]

def getInstructorDetails(course, term, c, dList, detail, trynew, end):

    iStatus = ['Available', 0]       # instructor status flag (default = available)

    # check instructor schedule
    query = ("SELECT * FROM section WHERE termCode = %(term)s AND profID = %(detail)s")
    c.execute(query, { 'term': term, 'detail': detail[2] })
    for itime in c.fetchall():
        # check for conflicts
        if (itime[0] != course and (trynew == int(itime[8]) or (trynew > int(itime[8]) and trynew < int(itime[9])) or (end > int(itime[8]) and end < int(itime[9]))) and ((itime[3] != '' and itime[3] == dList[0]) or (itime[4] != '' and itime[4] == dList[1]) or (itime[5] != '' and itime[5] == dList[2]) or (itime[6] != '' and itime[6] == dList[3]) or (itime[7] != '' and itime[7] == dList[4]))): 
            query = ("SELECT * FROM class WHERE crn = %(crn)s AND termCode = %(term)s")
            c.execute(query, { 'crn': itime[0], 'term': term})
            for other in c.fetchall():
                print ('\n****************** INSTRUCTOR CONFLICT ********************')
                print ('\nInstructor: '+detail[15])
                print ('Class: '+other[2]+other[3]+': '+other[5])
                print ('When: '+itime[3]+' '+itime[4]+' '+itime[5]+' '+itime[6]+' '+itime[7]+' '+itime[8]+' - '+itime[9])
                print ('Where: '+itime[10]+' Room '+itime[11])

            iStatus[0] = 'UNAVAILABLE'
            iStatus[1] = 1

    return iStatus

def getClassInfo(course, term):

    # connect to database
    conn = cConnect.connection()
    c = conn.cursor()
    c.execute("START TRANSACTION")

    section = getBasics(course, term, c)
    detail = getClassDetails(course, term, c)
    breakdown = getClassificationBreakdown(course, term, c)

    # prompt user to change...
    # time: days will remain the same
    # both: day and time can be changed
    # done: exit the program

    print('\n--------------------------------------------------------')
    change = raw_input('\nChange time (time), day and time (both), or done: ')
    change = change.lower()

    while( change != 'done' ):

        trynew = ''         # variable for different time
        # variable for days (default is current schedule)
        changeDay = detail[3]+detail[4]+detail[5]+detail[6]+detail[7]
        duration = 0        # change from 3 days to 2, or 2 to 1, or 3 to 1, or vica versa, duration will change
        if change == 'time':
            trynew = raw_input('\nNew time: ')
            while (not trynew.isdigit()):
                trynew = raw_input('\nPlease enter a number: ')
            # default duration from current schedule if only change time, not days
            duration = int(detail[9]) - int(detail[8])       
        elif change == 'both':
            trynew = raw_input('\nNew time: ')
            while (not trynew.isdigit()):
                trynew = raw_input('\nPlease enter a number: ')
            changeDay = raw_input('\nNew days (MWF, TR, MW, M, W, F): ')
            while (not changeDay.isalpha()):
                changeDay = raw_input('\nPlease enter your days: ')
            changeDay = changeDay.upper()

            # duration check
            if len(changeDay) == 3:
                print('Class duration: 50 minutes x 3 days')
                duration = 50
            elif len(changeDay) == 2:
                print('Class duration: 80 minutes x 2 days')
                duration = 80
            elif len(changeDay) == 1:
                duration = 50 * int(section[7])
                print('Class duration: '+str(duration)+' minutes x '+str(len(changeDay))+' day')

        dList = []
        dList = dList + ['']*5 

        # list of days (parallelized to fit DB output = less checking required)
        for i in changeDay:
            if i == 'M':
                dList[0] = i
            elif i == 'T':
                dList[1] = i
            elif i == 'W':
                dList[2] = i
            elif i == 'R':
                dList[3] = i
            elif i == 'F':
                dList[4] = i

        # need new end time to go with new start time so we can find conflicts
        end = 0
        duration = int(duration)
        trynew = int(trynew)
        if duration == 80:
            end = trynew + 120
        elif duration == 150:
            end = trynew + 250
        else:
            end = trynew + duration

        # output what we are trying to do 
        print('\nAttempting to move '+section[3]+section[4]+': '+section[6])
        print('From '+detail[3]+' '+detail[4]+' '+detail[5]+' '+detail[6]+' '+detail[7]+' '+detail[8]+' - '+detail[9])

        print('To   '+dList[0]+' '+dList[1]+' '+dList[2]+' '+dList[3]+' '+dList[4]+' '+str(trynew)+' - '+str(end))

        iStatus = getInstructorDetails(course, term, c, dList, detail, trynew, end)
        conflicts = getStudentDetails(course, term, c, dList, trynew, end)

        total = int(detail[13]) + 1

        # output conflict breakdown
        print('\n\n=========================================================')
        print('Total Conflicts: '+str(conflicts[0]+iStatus[1])+' / '+str(total))+' \t\t(instructor included)'
        print('=========================================================')

        print('\nInstructor Status: '+iStatus[0])

        print('\nStudent Status: ')
        print('\nSeniors \t'+str(conflicts[4])+' / '+str(breakdown[3])+' have a conflict')
        print('Juniors \t'+str(conflicts[3])+' / '+str(breakdown[2]))
        print('Sophomores \t'+str(conflicts[2])+' / '+str(breakdown[1]))
        print('Freshmen \t'+str(conflicts[1])+' / '+str(breakdown[0]))

        print('\n--------------------------------------------------------')
        change = raw_input('\nChange time (time), day and time (both), or done: ')
        

    print('\n')

    c.close()
    conn.close()