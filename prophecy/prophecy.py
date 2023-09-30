from cs50 import SQL
import csv

# open database
db = SQL("sqlite:///roster.db")

# open csv file and load into dict reader
FILE = open("students.csv")
reader = csv.DictReader(FILE)

# list to store if a particular house has been added to db
househead = []
insertstring = "INSERT INTO {} (?, ?) VALUES (?, ?);"
for student in reader:
    if (student['house'] not in househead):
        househead.append(student['house'])
        db.execute(insertstring.format('houses'), 'house', 'head', student['house'], student['head'])
    db.execute(insertstring.format('students1'), 'id', 'studentname', student['id'], student['student_name'])
    db.execute(insertstring.format('housea'), 'id', 'house', student['id'], student['house'])


FILE.close()

