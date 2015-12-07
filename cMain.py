# http://radon.readthedocs.org/en/latest/intro.html
# --------------------------------------------------
# Cyclomatic complexity 
# --------------------------------------------------
#   F 20:0 main - A (3)

# --------------------------------------------------
# Halstead complexity
# --------------------------------------------------
#   h1: 1
#   h2: 1
#   N1: 1
#   N2: 1
#   h: 2
#   N: 2
#   length: 0.0
#   volume: 2.0
#   difficulty: 0.5
#   effort: 1.0

import cConverter
import cDB
import cFind

def main ():
    
    print("\nGet current class details.")
    course = raw_input("Course Number / Class Name / CRN: ")
    print("\n")

    # setup database
    term = cDB.setupDB()

    # convert the input if user entered anything other than a CRN
    if(not course.isdigit()):
    	course = cConverter.convert(course)

    # use the CRN to setup the tables for student and prereq and find the students in that section
    if(course.isdigit()):
        cFind.getClassInfo(course, term)

    # if there is more than one section of a class, and we are unable to convert the 
    # input into a CRN, we will not build the tables for student and prereqs until we have specifics
    else: 
        print(course)

main ()
