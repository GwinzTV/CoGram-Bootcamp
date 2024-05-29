import sqlite3

PATH = 'Tasks/Task23/Student_db.db'


def create_table(cursor):
    query = '''CREATE TABLE IF NOT EXISTS python_programming (
    id CHAR(6) PRIMARY KEY,
    name VARCHAR(16),
    grade INT(3)
    );'''
    try:
        cursor.execute(query)
    except Exception as e:
        raise e


def insert_data(cursor):
    query = '''INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)'''
    student_data = [('55', 'Carl Davis', 61),
                    ('66', 'Dennis Fredrickson', 88),
                    ('77', 'Jane Richards', 78),
                    ('12', 'Peyton Sawyer', 45),
                    ('2', 'Lucas Brooke', 99)]
    try:
        cursor.executemany(query, student_data)
    except Exception as e:
        raise e


def select_records(cursor):
    query = '''SELECT * FROM python_programming
               WHERE grade < 80 AND grade > 60'''
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(f'{row[1]} : {row[2]}')
    except Exception as e:
        raise e


def update_grade(cursor, name, grade):
    query = '''UPDATE python_programming SET grade = ? WHERE name = ?'''
    try:
        cursor.execute(query, (grade, name))
    except Exception as e:
        raise e


def main():
    db = sqlite3.connect(PATH)
    cursor = db.cursor()

    try:
        create_table(cursor)
        insert_data(cursor)
        db.commit()
        print("Initial Data:")
        select_records(cursor)

        update_grade(cursor, 'Carl Davis', 65)
        db.commit()
        print("\nAfter Updating Carl Davis's Grade:")
        select_records(cursor)

    except Exception as e:
        db.rollback()
        print(f'Error: {e}')
    finally:
        db.close()


if __name__ == "__main__":
    main()
