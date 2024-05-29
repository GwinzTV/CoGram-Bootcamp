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

insert_values = '''INSERT INTO Student (STU_NUM, STU_SNAME, STU_FNAME,
STU_INITIAL, STU_STARTDATE, COURSE_CODE, PROJ_NUM)
VALUES
    ('11', 'Snow', 'Jon', 'E', '2014-04-05', '201', 6),
    ('12', 'Stark', 'Arya', 'C', '2017-07-12', '305', 11),
    ('13', 'Lannister', 'Jamie', 'C', '2012-09-05', '101', 2),
    ('14', 'Lannister', 'Cercei', 'J', '2012-09-05', '101', 2),
    ('15', 'Greyjoy', 'Theon', 'I', '2015-12-09', '402', 14),
    ('16', 'Tyrell', 'Margaery', 'Y', '2017-07-12', '402', 14),
    ('17', 'Baratheon', 'Tommen', 'R', '2019-06-13', '201', 5);
'''


def main():
    cursor.execute(create_table)
    cursor.execute(insert_values)
    # cursor.execute(insert_values)

    db.commit()
    db.close()


if __name__ == "__main__":
    main()
