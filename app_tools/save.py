import sqlite3
import logging
import json
import time

from sqlite3 import IntegrityError

logger = logging.getLogger('app.save')


def save_to_database(students):
    logger.info('Opening database and instantiating connection.')
    path = 'students_info/students_database.db'
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS students (table_position integer primary key, rating int, name text,'
                       'learn_program text, course integer, academic_group text, cr_amount integer,'
                       'cr_amount_norm integer,'
                       'normalization_factor float, credits_summary integer, percentile float, average_grade float, '
                       'minimal_grade integer, learn_group_position text);')

        for i, student in enumerate(students):
            cursor.execute('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                i, student.rating, student.name, student.learn_program, student.course, student.academic_group,
                student.cr_amount, student.cr_amount_norm, student.normalization_factor, student.credits_summary,
                student.percentile, student.average_grade, student.minimal_grade, student.learn_group_position
            ))

        logger.info("Committing and closing connection to database.")
        connection.commit()
    except IntegrityError:
        print("Database with this data already exists.")
        time.sleep(1)
    finally:
        connection.close()


def save_to_json(students):
    path = 'students_info/students.json'
    with open(path, 'w') as file:
        st_dict = {
            "students": []
        }
        for student in students:
            st_dict["students"].append(
                {
                    "rating": student.rating,
                    "name": student.name,
                    "learn_program": student.learn_program,
                    "course": student.course,
                    "academic_group": student.academic_group,
                    "cr_amount": student.cr_amount,
                    "cr_amount_norm": student.cr_amount_norm,
                    "normalization_factor": student.normalization_factor,
                    "credits_summary": student.credits_summary,
                    "percentile": student.percentile,
                    "average_grade": student.average_grade,
                    "minimal_grade": student.minimal_grade,
                    "learn_group_position": student.learn_group_position
                 }
            )

        json.dump(st_dict, file, indent=4)
        print(f"Saved to json file: {path}.")
        logger.info(f"Saved to json file: {path}.")
