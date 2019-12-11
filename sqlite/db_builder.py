import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


command = " "          # test SQL stmt in sqlite3 shell, save as string
command += '''CREATE TABLE tpotusa
            (name TEXT, id INTEGER PRIMARY KEY);
            INSERT INTO tpotusa VALUES (“baisatr”, 2);
            INSERT INTO tpotusa VALUES (‘guitarbass’, 1);
            '''

c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
