from database import execute_list_query, execute_query, read_query, create_db_connection
import pandas as pd

q1 = """
SELECT * 
FROM teacher;
"""

q2 = """
SELECT course.course_id, course.course_name, course.language, client.client_name, client.address
FROM course 
JOIN client 
ON course.client = client.client_id
WHERE course.in_school = FALSE;
"""

q3 = """
UPDATE client 
SET address = '23 Fingiertweg, 14534 Berlin' 
WHERE client_id = 101;
"""

q4 = """
DELETE FROM course
WHERE course_id = 20;
"""

sql = '''
    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''

val = [
    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'),
    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
]

from_db = []

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "school")

execute_list_query(connection, sql, val)

'''
for result in results:
    result = list(result)
    from_db.append(result)
columns = ["course_id", "course_name", "language", "client_name", "address"]
df = pd.DataFrame(from_db, columns=columns)

print(df)
'''
