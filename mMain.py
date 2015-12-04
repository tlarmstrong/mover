import mConverter
import mDB
import mFind

def main ():
    
    print("\nGet current class details.")
    course = raw_input("Course Number / Class Name / CRN: ")
    print("\n")
    #course = 'cs374'

    # setup table 'section'
    term = mDB.setupDB()

    #print(not course.isdigit())
    # convert the input if user entered anything other than a CRN
    if(not course.isdigit()):
        course = mConverter.convert(course)

    # use the CRN to setup the tables for student and prereq and find the students in that section
    if(course.isdigit()):
        mFind.getStudentInfo(course, term)

    # if there is more than one section of a class, and we are unable to convert the 
    # input into a CRN, we will not build the tables for student and prereqs until we have specifics
    else: 
        print(course)

main ()