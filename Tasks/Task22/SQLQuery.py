import sqlite3
PATH = 'Tasks/Task22/StudentData.db'

db = sqlite3.connect(PATH)
cursor = db.cursor()

create_table = '''CREATE TABLE IF NOT EXISTS Student(
    STU_NUM CHAR(6) PRIMARY KEY,
    STU_SNAME VARCHAR(15),
    STU_FNAME VARCHAR(15),
    STU_INITIAL CHAR(1),
    STU_STARTDATE DATE,
    COURSE_CODE CHAR(3),
    PROJ_NUM INT(2)
    );'''

insert_values = '''INSERT INTO Student VALUES'''
users = [
    (01, 'Snow', 'Jon', 'E', 2014-04-05, 201, 6),
    (02, 'Stark', 'Arya', 'C', 2017-07-12, 305, 11),
    (03, 'Lannister', 'Jamie', 'C', 2012-09-05, 101, 2),
    (04, 'Lannister', 'Cercei', 'J', 2012-09-05, 101, 2),
    (05, 'Greyjoy', 'Theon', 'I', 2015-12-09, 402, 14),
    (06, 'Tyrell', 'Margaery', 'Y', 2017-07-12, 402, 14),
    (07, 'Baratheon', 'Tommen', 'R', 2019-06-13, 201, 5)]


def main():
    cursor.execute(create_table)
    cursor.execute(insert_values)
    # cursor.execute(insert_values)

    db.commit()
    db.close()


if __name__ == "__main__":
    main()
