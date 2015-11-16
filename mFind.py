from collections import defaultdict
import mysql.connector    

def getStudentInfo(course, term):

    conn = mysql.connector.connect(
        db='mover', 
        user='root',
        passwd='', 
        host='localhost')
    c = conn.cursor()
    #c.execute("START TRANSACTION")

    sList = []

    # section: crn, termCode, profID, d1, d2, d3, d4, d5, beginTime, endTime, building, room, capacity, enrolled
    # student: id, firstName, lastName, classification, email, dept, hours, grade
    # enrollment: id, crn, termCode, hours
    # class: crn, termCode, subjectCode, courseNum, section, title
    # instructor: id, prof
    # instSection: id, crn, termCode, eval

    query = ("SELECT a.crn, b.* FROM section a, class b WHERE a.crn = %(id)s AND a.termCode = %(term)s AND a.crn = b.crn AND a.termCode = b.termCode")
    c.execute(query, { 'id': course, 'term': term })
    for section in c:
        # output example: CS374: Software Engineering
        print ('\n'+section[3]+section[4]+': '+section[6])
        # print(section)
        # section = (u'11081', u'11081', u'201610', u'CS', u'374', u'1', u'Software Engineering')

    c.execute("SELECT a.*, b.* FROM section a, instructor b WHERE a.crn = %s AND a.termCode = %s AND a.profID = b.id", (section[0], section[2]))
    for detail in c:
        #print(detail)
        # detail = (u'11081', u'201610', u'9979', u'M', u'', u'W', u'', u'F', u'1400', u'1450', u'MBB', u'314', u'30', u'6', u'9979', u'Reeves, Brent')
        print ('Instructor: '+detail[15])
        print ('When: '+detail[3]+' '+detail[4]+' '+detail[5]+' '+detail[6]+' '+detail[7]+' '+detail[8]+' - '+detail[9])
        print ('Where: '+detail[10]+' Room '+detail[11])
        print ('Enrolled: '+str(detail[13]))


    se = 0
    j = 0
    so = 0
    f = 0

    query = ("SELECT a.*, b.* FROM enrollment b, student a WHERE a.id = b.id AND b.crn = %(crn)s AND b.termCode = %(term)s")
    c.execute(query, { 'crn': course, 'term': term })
    for classList in c.fetchall():
        #print(classList)
        # classList = (u'111564', u'Lola', u'Pucci', u'JR', u'lolapucci@acu.edu', u'SITC', 0, u'A', u'111564', u'11081', u'201610', 3)
        query = ("SELECT b.id, sum(b.hours), a.id FROM enrollment b, student a WHERE b.id = a.id AND b.id = %(id)s")
        c.execute(query, { 'id': classList[0] })
        for hours in c.fetchall():
            #print(hours)
            h = int(hours[1])
            query = ("UPDATE student SET hours = %(hours)s WHERE id = %(id)s")
            c.execute(query, { 'hours': h, 'id': classList[0] }) 
            query = ("SELECT hours FROM student WHERE id = %(id)s")
            c.execute(query, { 'id': classList[0] })
            for shours in c:
                if(shours[0] >= 90):
                    se += 1
                elif(shours[0] < 90 and shours[0] >= 60):
                    j += 1
                elif(shours[0] < 60 and shours[0] >= 30):
                    so += 1
                else:
                    f += 1

    print('\n--------------------------------------------------------')
    change = raw_input('\nChange time (time), day and time (both), or done: ')
    change = change.lower()

    while( change != 'done' ):

        trynew = ''
        changeDay = detail[3]+detail[4]+detail[5]+detail[6]+detail[7]
        duration = 0
        if change == 'time':
            trynew = raw_input('\nNew time: ')
            while (not trynew.isdigit()):
                trynew = raw_input('\nPlease enter a number: ')
            duration = int(detail[9]) - int(detail[8])
        elif change == 'both':
            trynew = raw_input('\nNew time: ')
            while (not trynew.isdigit()):
                trynew = raw_input('\nPlease enter a number: ')
            changeDay = raw_input('\nNew days (MWF, TR, MW, M, W, F): ')
            while (not changeDay.isalpha()):
                changeDay = raw_input('\nPlease enter your days: ')
            changeDay = changeDay.upper()

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

        # print(dList)

        end = 0
        duration = int(duration)
        trynew = int(trynew)
        if duration == 80:
            end = trynew + 120
        elif duration == 150:
            end = trynew + 250
        else:
            end = trynew + duration

        #print(end)

        print('\nAttempting to move '+section[3]+section[4]+': '+section[6])
        print('From '+detail[3]+' '+detail[4]+' '+detail[5]+' '+detail[6]+' '+detail[7]+' '+detail[8]+' - '+detail[9])

        print('To   '+dList[0]+' '+dList[1]+' '+dList[2]+' '+dList[3]+' '+dList[4]+' '+str(trynew)+' - '+str(end))

        conflicts = 0
        iStatus = 'Available'

        seConflict = 0
        jConflict = 0
        soConflict = 0
        fConflict = 0

        # check instructor schedule
        query = ("SELECT * FROM section WHERE termCode = %(term)s AND profID = %(detail)s")
        c.execute(query, { 'term': term, 'detail': detail[2] })
        for itime in c.fetchall():
            #print(itime)
            # itime = (u'11084', u'201610', u'9979', u'M', u'', u'W', u'', u'F', u'1300', u'1350', u'MBB', u'216', u'35', u'31')
            if (itime[0] != course and (trynew == int(itime[8]) or (trynew > int(itime[8]) and trynew < int(itime[9])) or (end > int(itime[8]) and end < int(itime[9]))) and ((itime[3] != '' and itime[3] == dList[0]) or (itime[4] != '' and itime[4] == dList[1]) or (itime[5] != '' and itime[5] == dList[2]) or (itime[6] != '' and itime[6] == dList[3]) or (itime[7] != '' and itime[7] == dList[4]))): 
                query = ("SELECT * FROM class WHERE crn = %(crn)s AND termCode = %(term)s")
                c.execute(query, { 'crn': itime[0], 'term': term})
                for other in c.fetchall():
                    print ('\n****************** INSTRUCTOR CONFLICT ********************')
                    print ('\nInstructor: '+detail[15])
                    print ('Class: '+other[2]+other[3]+': '+other[5])
                    print ('When: '+itime[3]+' '+itime[4]+' '+itime[5]+' '+itime[6]+' '+itime[7]+' '+itime[8]+' - '+itime[9])
                    print ('Where: '+itime[10]+' Room '+itime[11])

                iStatus = 'UNAVAILABLE'
                conflicts += 1

        query = ("SELECT a.*, b.* FROM enrollment a, student b WHERE a.crn = %(crn)s AND a.termCode = %(term)s AND a.id = b.id ORDER BY b.hours desc")
        c.execute(query, { 'crn': course, 'term': term })
        for student in c.fetchall():
            # print(student)
            # student = (u'214275', u'11081', u'201610', 3, u'214275', u'Paul', u'Neal', u'SR', u'paulneal@acu.edu', u'SITC', 97, u'B')
            print('\n')
            print('--------------------------------------------------------')
            print (student[0]+'\t'+student[5]+' '+student[6]+'\t'+student[8]+'\t'+student[9])
            print('--------------------------------------------------------')

            print ( 'Major: '+str(student[12]))
            print ('Hours: '+str(student[10]))
            if(student[10] >= 90):
                #se += 1
                print('Year:  Senior')
            elif(student[10] < 90 and student[10] >= 60):
                #j += 1
                print('Year:  Junior')
            elif(student[10] < 60 and student[10] >= 30):
                #so += 1
                print('Year:  Sophomore')
            else:
                #f += 1
                print('Year:  Freshman')

            trynew = int(trynew)
            end = int(end)

            # check student schedules
            query = ("SELECT a.*, b.* FROM section a, enrollment b WHERE a.crn = b.crn AND b.termCode = a.termCode AND b.id = %(id)s AND b.termCode = %(term)s")
            c.execute(query, { 'id': student[0], 'term': student[2] })
            for time in c.fetchall():
                oStart = int(time[8])
                oEnd = int(time[9])
                if (time[0] != course and (trynew == oStart or (trynew > oStart and trynew < oEnd) or (end > oStart and end < oEnd)) and ((time[3] != '' and time[3] == dList[0]) or (time[4] != '' and time[4] == dList[1]) or (time[5] != '' and time[5] == dList[2]) or (time[6] != '' and time[6] == dList[3]) or (time[7] != '' and time[7] == dList[4]))):

                    query = ("SELECT a.*, b.* FROM section a, enrollment b WHERE a.crn = b.crn AND b.termCode = a.termCode AND a.beginTime = %(begin)s AND (a.d1 = %(d1)s OR a.d2 = %(d2)s OR a.d3 = %(d3)s OR a.d4 = %(d4)s OR a.d5 = %(d5)s) AND b.id = %(id)s AND a.termCode = %(term)s")
                    c.execute(query, { 'id': student[0], 'term': student[2], 'begin': time[8], 'd1': time[3], 'd2': time[4], 'd3': time[5], 'd4': time[6], 'd5': time[7] })
                    for i in c.fetchall():
                        #print(i)

                        query = ("SELECT * FROM class WHERE crn = %(crn)s AND termCode = %(term)s")
                        c.execute(query, { 'crn': i[0], 'term': i[1] })
                        for k in c.fetchall():
                            #print(k)
                            print('\n\t******************** CONFLICT *********************')
                            print('\n\tClass: '+k[2]+k[3]+' '+k[5])
                            #print('\tInstructor: '+time[9])
                            print('\tWhen: '+time[3]+' '+time[4]+' '+time[5]+' '+time[6]+' '+time[7]+' '+time[8]+' - '+time[9])
                            print('\tWhere: '+time[10]+' Room '+time[11])

                    if(student[10] >= 90):
                        seConflict += 1
                    elif(student[10] < 90 and student[10] >= 60):
                        jConflict += 1
                    elif(student[10] < 60 and student[10] >= 30):
                        soConflict += 1
                    else:
                        fConflict += 1

                    conflicts += 1

        total = int(detail[13]) + 1

        print('\n\n=========================================================')
        print('Total Conflicts: '+str(conflicts)+' / '+str(total))+' \t\t(instructor included)'
        print('=========================================================')

        print('\nInstructor Status: '+iStatus)

        print('\nStudent Status: ')
        print('\nSeniors \t'+str(seConflict)+' / '+str(se)+' have a conflict')
        print('Juniors \t'+str(jConflict)+' / '+str(j))
        print('Sophomores \t'+str(soConflict)+' / '+str(so))
        print('Freshmen \t'+str(fConflict)+' / '+str(f))

        print('\n--------------------------------------------------------')
        change = raw_input('\nChange time (time), day and time (both), or done: ')
        

    print('\n')

    c.close()
    conn.close()