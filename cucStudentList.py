import csv
import sys

result = ''

input = sys.argv[1]

iList = []
c = input.find(',')
iList.append(input[:c])
iList.append(input[c+1:])
#print(iList)

#mock data to test initial cucumber tests for CS374
#sys.stdout.write("Clanton, Norma; Davis, John; Ford, Thomas; Prince, Leroy; Williams, Leticia")

# let's read it in from a file
f = open('info/ourClass-1.csv')

reader = csv.DictReader(f)
header = reader.next()

for row in reader:
	# let's just test for what students are in a section (we have a different cucumber to test conversion)
	# perhaps we could try for different classes?
	if ( iList[0] == str(row['Subject Code'])+str(row['Course Number']) and iList[1] == str(row['Term Code']) ):
		result = result + str(row['Last Name'])+', '+str(row['First Name'])+';'

	elif( iList[0] == str(row['CRN']) and iList[1] == str(row['Term Code']) ):
		result = result + str(row['Last Name'])+', '+str(row['First Name'])+';'

f.close()
sys.stdout.write(str(result))
