import csv
import sys

#def findDuration(input):

input = sys.argv[1]

result = []

f = open('info/ourClass-1.csv')

reader = csv.DictReader(f)
header = reader.next()
n = 1
for row in reader:
	duration = 50
	if str(row['CRN']) == input and int(row['Credit Hours']) == 3:
		duration = 150
		if row['Monday Ind1'] != '' and row['Wednesday Ind1'] != '' and row['Friday Ind1'] != '':
			n = 3
			days = str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])
			result.append('Days: '+days+', Duration: '+str(duration/n)+' x '+str(n))
		elif row['Monday Ind1'] != '' and row['Wednesday Ind1'] != '' and row['Friday Ind1'] == '':
			n = 2
			days = str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])
			result.append('Days: '+days+', Duration: '+str((duration/n)+5)+' x '+str(n))
		elif row['Tuesday Ind1'] != '' and row['Thursday Ind1'] != '':
			n = 2
			days = str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])
			result.append('Days: '+days+', Duration: '+str((duration/n)+5)+' x '+str(n))
		elif (row['Monday Ind1'] != '' or row['Wednesday Ind1'] != '') and row['Friday Ind1'] == '':
			n = 3
			days = str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])
			result.append('Days: '+days+', Duration: '+str(duration/n)+' x '+str(n))
		elif (row['Monday Ind1'] != '' or row['Wednesday Ind1'] != '' or row['Friday Ind1'] != '') or (row['Tuesday Ind1'] != '' or row['Thursday Ind1'] != ''):
			n = 2
			days = str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])
			result.append('Days: '+days+', Duration: '+str((duration/n)+5)+' x '+str(n))
		break
	elif str(row['CRN']) == input and int(row['Credit Hours']) == 1:
		n = 1
		days = str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])
		result.append('Days: '+days+', Duration: '+str(duration)+' x '+str(n))
		break
f.close()

sys.stdout.write(str(result))