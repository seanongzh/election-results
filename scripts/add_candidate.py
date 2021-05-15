# Script to add a single candidate into the candidates table of the database
# 1. Table needs "first_name" and "last_name" columns
# 2. Script will check for duplicates and not insert duplicates
# 
# USAGE: add_candidate.py [First Name] [Last Name]

import psycopg2
import sys

conn = psycopg2.connect("dbname=results user=sean password=sean")
cur = conn.cursor()

cur.execute("select * from candidates where first_name=%s and last_name =%s",
            (sys.argv[1], sys.argv[2]))

if (cur.fetchone() == None):
  cur.execute("insert into candidates(first_name, last_name) values(%s, %s)",
              (sys.argv[1], sys.argv[2]))
  print("Inserted")
  conn.commit()
else:
  print("Found and not inserted")

cur.close()
conn.close()