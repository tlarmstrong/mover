import mConverter
import mDB
import mFind
from flask import Flask, render_template, json, request, redirect, session
from flask.ext.mysql import MySQL
app = Flask(__name__) 
app.secret_key = 'why would I tell you my secret key?'
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'mover'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
className = ''
term = ''
days = ''
time = ''
myString = ''
myString2 = ''

@app.route("/ShowChooseClass")
def ShowChooseClass():
    return render_template('chooseClass.html')

@app.route("/classChooser", methods=['POST'])
def classChooser():
    className = request.form['className']
    days = request.form['days']
    time = request.form['time']

    #print className
    # setup table 'section'
    #term = mDB.setupDB()
    term = '201610'#mDB.setupDB()
    #_title = request.form['inputTitle'] #make this the course name
    # convert the input if user entered anything other than a CRN
    if(not className.isdigit()):
        className = mConverter.convert(className)
    #print className
    # use the CRN to setup the tables for student and prereq and find the students in that section
    if(className.isdigit()):
        myString = mFind.getClassInfo(className, term)
        myString2 = mFind.getStudentInfo(className, term, days, time)
        # if there is more than one section of a class, and we are unable to convert the 
        # input into a CRN, we will not build the tables for student and prereqs until we have specifics
        print myString2
        return json.dumps(str(myString2)) 
    else:
        return json.dumps(className)

@app.route("/")
def main():
    return render_template('indexMover.html')

if __name__ == "__main__":
    app.run(debug = True) 
# app.run(host='0.0.0.0')  
