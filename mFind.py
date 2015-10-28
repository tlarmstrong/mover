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
        #print(section)
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

    trynew = raw_input('\nNew time (or done): ')
    while( trynew != 'done' ):

        conflicts = 0

        query = ("SELECT a.*, b.* FROM enrollment a, student b WHERE a.crn = %(crn)s AND a.termCode = %(term)s AND a.id = b.id ORDER BY b.hours desc")
        c.execute(query, { 'crn': course, 'term': term })
        for student in c.fetchall():
            # print(student)
            # student = (u'214275', u'11081', u'201610', 3, u'214275', u'Paul', u'Neal', u'SR', u'paulneal@acu.edu', u'SITC', 97, u'B')
            print('\n')
            print('--------------------------------------------------------')
            print (student[0]+'\t'+student[5]+' '+student[6]+'\t'+student[8]+'\t'+student[9])
            print('--------------------------------------------------------')

            print ('Hours: '+str(student[10]))
            if(student[10] >= 90):
                #se += 1
                print('Year: Senior')
            elif(student[10] < 90 and student[10] >= 60):
                #j += 1
                print('Year: Junior')
            elif(student[10] < 60 and student[10] >= 30):
                #so += 1
                print('Year: Sophomore')
            else:
                #f += 1
                print('Year: Freshman')

            # only checking student schedule, also need to check prof and room
            query = ("SELECT a.*, b.* FROM section a, enrollment b WHERE a.crn = b.crn AND b.termCode = a.termCode AND b.id = %(id)s AND b.termCode = %(term)s")
            c.execute(query, { 'id': student[0], 'term': student[2] })
            for time in c.fetchall():
                #print(time)
                # time = (u'10170', u'201610', u'68002', u'', u'T', u'', u'R', u'', u'800', u'920', u'OSC', u'241', u'30', u'27', u'136011', u'10170', u'201610', 3)
                # detail = (u'11081', u'201610', u'9979', u'M', u'', u'W', u'', u'F', u'1400', u'1450', u'MBB', u'314', u'30', u'6', u'9979', u'Reeves, Brent')
                if (time[0] != course and (trynew == time[8] or (trynew > time[8] and trynew < time[9])) and (time[3] == detail[3] or time[4] == detail[4]) ): 
                    query = ("SELECT a.*, b.* FROM section a, enrollment b WHERE a.crn = b.crn AND b.termCode = a.termCode AND a.beginTime = %(begin)s AND (a.d1 = %(d1)s OR a.d2 = %(d2)s) AND b.id = %(id)s AND a.termCode = %(term)s")
                    c.execute(query, { 'id': student[0], 'term': student[2], 'begin': time[8], 'd1': time[3], 'd2': time[4] })
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
                            print('\tWhere: '+time[10]+' '+time[11])

                    conflicts += 1

        print('\n======================================================')
        print('\nClass Breakdown')
        print('Enrolled: \t'+str(detail[13]))
        print('Seniors: \t'+str(se)+' / '+str(detail[13]))
        print('Juniors: \t'+str(j)+' / '+str(detail[13]))
        print('Sophomores: \t'+str(so)+' / '+str(detail[13]))
        print('Freshmen: \t'+str(f)+' / '+str(detail[13]))

        print('\nConflicts: '+str(conflicts))

        trynew = raw_input('\nNew time (or done): ')

    print('\n')

    c.close()
    conn.close()