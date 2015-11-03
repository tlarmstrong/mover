import csv
import sys

result = []

input = sys.argv[1]

pList = []
c = input.find(',')
pList.append(input[:c])
pList.append(input[c+1:])

f = open('info/ourClass-1.csv')

reader = csv.DictReader(f)
header = reader.next()

for row in reader:
	# get an student or instructor's schedule 
	# perhaps we could try for different sections?
	if ( pList[0] == str(row['Banner ID']) and pList[1] == str(row['Term Code']) ):
		if ( row['Begin Time 1'] != '0' and row['End Time1'] != '1' ):
			result.append( str(row['CRN'])+' '+str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])+' '+str(row['Begin Time 1'])+' - '+str(row['End Time1']) )

	elif ( pList[0] == str(row['Instructor ID']) and pList[1] == str(row['Term Code']) ):
		if ( row['Begin Time 1'] != '0' and row['End Time1'] != '1' ):
			result.append( str(row['CRN'])+' '+str(row['Monday Ind1'])+str(row['Tuesday Ind1'])+str(row['Wednesday Ind1'])+str(row['Thursday Ind1'])+str(row['Friday Ind1'])+' '+str(row['Begin Time 1'])+' - '+str(row['End Time1']) )

f.close()
sys.stdout.write(str(result))
