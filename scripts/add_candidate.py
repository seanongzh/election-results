# Script to add a single candidate into the candidates table of the database
# 1. Table needs "first" and "last" columns for first and last names
# 2. Script will check for duplicates and not insert duplicates
# 
# USAGE: add_candidate.py [First Name] [Last Name]

import psycopg2
import sys

conn = psycopg2.connect("dbname=results user=sean password=sean")
cur = conn.cursor()

cur.execute("select * from candidates where first=%s and last =%s",
            (sys.argv[1], sys.argv[2]))

if (cur.fetchone() == None):
  cur.execute("insert into candidates(first, last, full_name) values(%s, %s, %s)",
              (sys.argv[1], sys.argv[2], sys.argv[1]+" "+sys.argv[2]))
  print("Inserted")
  conn.commit()
else:
  print("Found and not inserted")

cur.close()
conn.close()