import csv
import sys

result = ''

input = sys.argv[1]

pList = []
c = input.find(',')
pList.append(input[:c])
pList.append(input[c+1:])

f = open('info/ourClass-1.csv')

reader = csv.DictReader(f)
header = reader.next()

for row in reader:
	# find who is teaching a section 
	# perhaps we could try for different sections?
	if ( pList[0] == str(row['Subject Code'])+str(row['Course Number']) and pList[1] == str(row['Term Code']) ):
		if ( result != str(row['Instructor Name'])):
			result = result + str(row['Instructor Name'])

	elif( pList[0] == str(row['CRN']) and pList[1] == str(row['Term Code']) ):
		if ( result != str(row['Instructor Name'])):
			result = result + str(row['Instructor Name'])

f.close()
sys.stdout.write(str(result))
