# https://pymotw.com/2/csv/
import csv
import sys

result = "None"

input = sys.argv[1]
#sys.stdout.write(str(input))
#sys.stdout.write(str(len(input)))

n = str(len(sys.argv))
#print (n)

# If user inputs the Title of the course, and it is more than one word (with spaces), 
# then each word becomes a separate element in the list 
# ex: Software Engineering = ['Software', 'Engineering']
# So, we need to collapse it into one string to compare it to the database/.csv entry:
if (int(n) > 2):
     for i in range (2, int(n)):
         input = input+' '+sys.argv[i]

# using a set to find the sections (unique elements only)
findSection = set([])
f = open('info/ourClass-1.csv')

# DictReader translates rows to dictionaries
# Keys for the dictionary are inferred from the first row in the input
reader = csv.DictReader(f)
for row in reader:
    # CRN
    if (input.isdigit()):
        if (input == row['CRN']):
            result = row['Subject Code']+row['Course Number']+'.'+row['Section Number']+': '+row['Course Title']
            # add students
    else:
        # subject code + a course number + a section number
        if (input.find('.') != -1):
            input = input.replace(" ", "")
            input = input.replace(".0", ".")
            if (input.upper() == row['Subject Code']+row['Course Number']+'.'+row['Section Number']):
                result = row['CRN']
        # subject code + a course number
        elif (input[0].isalpha() and input[len(input)-1].isdigit()):
            input = input.replace(" ", "")
            input = input.upper()
            if(input.upper() == row['Subject Code']+row['Course Number']):
                findSection.add(row['Subject Code']+row['Course Number']+'.'+row['Section Number'])
                result = row['CRN']
        # subject code only
        elif(input.isalpha() and len(input) < 5):
            input = input.upper()
            if (input == row['Subject Code']):
                findSection.add(row['Subject Code']+row['Course Number']+'.'+row['Section Number'])
                result = row['CRN']
        # course title
        else:
            if (input.lower() == row['Course Title'].lower()):
                findSection.add(row['Subject Code']+row['Course Number']+'.'+row['Section Number'])
                #result = row['Subject Code']+row['Course Number']+'.'+row['Section Number']
                result = row['CRN']

# if the course has at least 2 sections, ask the user to tell us which one he/she wants
if (len(findSection) > 1):
    temp = input+' has '+str(len(findSection))+' sections, please choose one: '+findSection.pop()
    while (len(findSection)) != 0:
        temp += ', '+findSection.pop()  
    result = temp

sys.stdout.write(str(result))
f.close()
