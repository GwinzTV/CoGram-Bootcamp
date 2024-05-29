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
    ('01', 'Snow', 'Jon', 'E', '2014-04-05', '201', 6),
    ('02', 'Stark', 'Arya', 'C', '2017-07-12', '305', 11),
    ('03', 'Lannister', 'Jamie', 'C', '2012-09-05', '101', 2),
    ('04', 'Lannister', 'Cercei', 'J', '2012-09-05', '101', 2),
    ('05', 'Greyjoy', 'Theon', 'I', '2015-12-09', '402', 14),
    ('06', 'Tyrell', 'Margaery', 'Y', '2017-07-12', '305', 14),
    ('07', 'Baratheon', 'Tommen', 'R', '2019-06-13', '201', 5);
'''

select_condition = '''SELECT * FROM Student WHERE COURSE_CODE='305';'''

delete = '''DELETE FROM Student
WHERE STU_FNAME='Jamie'
AND STU_SNAME='Lannister'
AND STU_STARTDATE='2012-09-05'
AND COURSE_CODE='101';'''

update = '''UPDATE Student SET COURSE_CODE = '304' WHERE STU_NUM='07';'''

update2 = '''UPDATE Student SET PROJ_NUM=14
WHERE STU_STARTDATE < '2016-01-01'
AND COURSE_CODE >= '201';'''

drop = '''DROP TABLE Student'''


def main():
    cursor.execute(create_table)
    # cursor.execute(delete)
    # cursor.execute(insert_values)
    # result = list(cursor.execute(select_condition))
    # for x in result:
    #     print(x)
    # cursor.execute(drop)

    db.commit()
    db.close()


if __name__ == "__main__":
    main()
