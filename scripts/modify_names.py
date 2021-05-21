# Script to create a single field of full names in the candidates table of the database
# 1. Table needs "first_name", "middle_initial", "last_name", "suffix" columns
# 2. Table will check for unique ids, assumed to be sequential (but not necessarily consecutive)
#
# USAGE: modify_names.py

import psycopg2

conn = psycopg2.connect("dbname=results user=sean password=sean")
cur = conn.cursor()
cur.execute("SELECT max(id) FROM candidates")
num_rows = cur.fetchone()[0]

for id in range(num_rows):
  cur.execute("SELECT first_name, middle_initial, last_name, suffix FROM candidates \
               WHERE id=%s", (id,))
  if cur.rowcount > 0:
    full_name_in_tuple = cur.fetchone()
    full_name_concat = ""
    for name in full_name_in_tuple:
      if name != None:
        full_name_concat = full_name_concat + name + " "
    full_name_concat = full_name_concat.strip()
    cur.execute("UPDATE candidates SET name=%s WHERE id=%s",
                (full_name_concat, id))
    cur.execute("SELECT name FROM candidates where id=%s", (id,))
    print(cur.fetchone())
    conn.commit()

cur.close()
conn.close()