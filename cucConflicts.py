import csv
import sys
#import cucDuration

result = []

input = sys.argv[1]

pList = input.split(',')
dList = []
dList = dList + ['']*5 
#print(dList)
#print(pList)

for i in pList[2]:
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

#print(dList)

duration = 0

if len(pList[2]) == 1:
	f = open('info/ourClass-1.csv')

	reader = csv.DictReader(f)
	header = reader.next()

	for row in reader:
		if int(row['Credit Hours']) == 3:
			duration = 250
		elif int(row['Credit Hours']) == 1:
			duration = 50
	f.close()

elif len(pList[2]) == 2:
	duration = 120
elif len(pList[2]) == 3:
	duration = 50


end = int(pList[3]) + duration

result.append('New time: '+pList[2]+' '+pList[3]+' - '+str(end))

f = open('info/ourClass-1.csv')

reader = csv.DictReader(f)
header = reader.next()

for row in reader:
	# get an student or instructor's schedule 
	# perhaps we could try for different sections?
	#437247,201610,TR,1200
	if ( pList[0] == str(row['Banner ID']) and pList[1] == str(row['Term Code']) ):
		if ( (int(row['Begin Time 1']) == int(pList[3]) or int(row['End Time1']) == int(pList[3])) and ( (str(row['Monday Ind1']) == dList[0] and dList[0] != '') or (str(row['Tuesday Ind1']) == dList[1] and dList[1] != '') or (str(row['Wednesday Ind1']) == dList[2] and dList[2] != '') or (str(row['Thursday Ind1']) == dList[3] and dList[3] != '') or (str(row['Friday Ind1']) == dList[4] and dList[4] != '')) ):
			result.append( 'Conflict: '+str(row['CRN'])+' '+str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])+' '+str(row['Begin Time 1'])+' - '+str(row['End Time1']) )

		elif ( (((int(pList[3]) > int(row['Begin Time 1']) and int(pList[3]) < int(row['End Time1']))) or (end > int(row['Begin Time 1']) and end < int(row['End Time1']))) and ( (str(row['Monday Ind1']) == dList[0] and dList[0] != '') or (str(row['Tuesday Ind1']) == dList[1] and dList[1] != '') or (str(row['Wednesday Ind1']) == dList[2] and dList[2] != '') or (str(row['Thursday Ind1']) == dList[3] and dList[3] != '') or (str(row['Friday Ind1']) == dList[4] and dList[4] != '')) ):
			result.append( 'Conflict: '+str(row['CRN'])+' '+str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])+' '+str(row['Begin Time 1'])+' - '+str(row['End Time1']) )

	elif ( pList[0] == str(row['Instructor ID']) and pList[1] == str(row['Term Code']) ):
		if ( (int(row['Begin Time 1']) == int(pList[3]) or int(row['End Time1']) == int(pList[3])) and ( (str(row['Monday Ind1']) == dList[0] and dList[0] != '') or (str(row['Tuesday Ind1']) == dList[1] and dList[1] != '') or (str(row['Wednesday Ind1']) == dList[2] and dList[2] != '') or (str(row['Thursday Ind1']) == dList[3] and dList[3] != '') or (str(row['Friday Ind1']) == dList[4] and dList[4] != '')) ):
			result.append( 'Conflict: '+str(row['CRN'])+' '+str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])+' '+str(row['Begin Time 1'])+' - '+str(row['End Time1']) )
			break

		elif ( (((int(pList[3]) > int(row['Begin Time 1']) and int(pList[3]) < int(row['End Time1']))) or (end > int(row['Begin Time 1']) and end < int(row['End Time1']))) and ( (str(row['Monday Ind1']) == dList[0] and dList[0] != '') or (str(row['Tuesday Ind1']) == dList[1] and dList[1] != '') or (str(row['Wednesday Ind1']) == dList[2] and dList[2] != '') or (str(row['Thursday Ind1']) == dList[3] and dList[3] != '') or (str(row['Friday Ind1']) == dList[4] and dList[4] != '')) ):
			result.append( 'Conflict: '+str(row['CRN'])+' '+str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])+' '+str(row['Begin Time 1'])+' - '+str(row['End Time1']) )
			break

f.close()
if len(result) < 2:
	result[0] = 'Conflict: None'
sys.stdout.write(str(result))
