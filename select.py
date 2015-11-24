import sqlite3
conn = sqlite3.connect('test.db')
print "opened database successfully"

cursor = conn.execute("SELECT * from COMPANY where AGE= 25")

for row in cursor:
	print "ID = ", row[0]
	print "NAME = ", row[1]
	print "ADDRESS = ", row[2]
	print "SALARY = ", row[3], "\n"

conn.close()