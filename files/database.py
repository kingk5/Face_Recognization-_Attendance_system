import sqlite3 as sql
from datetime import date


def create():
    conn = sql.connect('attendance.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE STUDENTS (
            first text,
            last text
            )""")
    conn.commit()
    conn.close()

def add(first,last):
    conn = sql.connect('attendance.db')
    c = conn.cursor()
    c.execute("INSERT INTO STUDENTS VALUES('first','last') (?, ?)", (first, last))
    #c.execute("SELECT * FROM STUDENTS")
    #print(c.fetchall())
    conn.commit()
    conn.close()
    
def attendance(first,last):
    conn = sql.connect('attendance.db')
    c = conn.cursor()
    today = date.today()
    #c.execute("""ALTER TABLE STUDENTS
     #         ADD (?) integer DEFAULT 0""", (today))
    c.execute("""ALTER TABLE STUDENTS
              ADD today2 integer DEFAULT 0""")
    c.execute("""INSERT INTO STUDENT(today) VALUES(1)
                where first=?""", (first,))
    conn.commit()
    conn.close()
    
