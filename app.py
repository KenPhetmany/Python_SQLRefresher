from database import read_query, create_db_connection

q1 = """
select * from teacher;
"""

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "school")

results = read_query(connection, q1)

for result in results:
    print(result)
