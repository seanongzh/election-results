# Interactive script to add a set of election results into the database
# Will prompt for name of position, year of election, and candidates info
# 
# USAGE: add_election.py
# (then follow the prompts)

import psycopg2

conn = psycopg2.connect("dbname=results user=sean password=sean")
cur = conn.cursor()

position = " "
position_id = None
while (position_id == None):
  position = input("Position? ")
  cur.execute("SELECT id FROM elected_positions WHERE name=%s",(position,))
  position_id = cur.fetchone()
  if position_id == None:
    print("Not found in database. Try again.")
position_id = str(position_id[0])

election_id = None
while (election_id == None):
  year = input("Year? ")
  cur.execute("INSERT INTO elections(year, position_id) VALUES(%s, %s) RETURNING id", (year, position_id))
  election_id = cur.fetchone()
  if election_id == None:
    print("Error inserting election into database. Try again.")
election_id = str(election_id[0])

num_candidates = int(input("How many candidates? "))
for x in range(num_candidates):
  print("Candidate", x+1)
  candidate = " "
  candidate_id = None
  while (candidate_id == None):
    candidate = input("Candidate? ")
    cur.execute("SELECT id FROM candidates WHERE full_name=%s",(candidate,))
    candidate_id = cur.fetchall()
    if candidate_id == None:
      print("Not found in database. Try again.")
  to_keep = 0
  if (len(candidate_id) > 1):
    print(candidate_id)
    to_keep = int(input("Multiple candidates found. Select one: ")) - 1
  candidate_id = str(candidate_id[to_keep][0])

  party_is_present = False
  if (input("Party is present? (Y/N) ") == "Y"):
    party_is_present = True
  if party_is_present:
    party = " "
    party_id = None
    while (party_id == None):
      party = input("Party? ")
      cur.execute ("SELECT id FROM parties WHERE name=%s",(party,))
      party_id = cur.fetchone()
      if party_id == None:
        print("Not found in database. Try again.")
    party_id = str(party_id[0])

  votes = input("No. of votes? ")
  municipal_winner = input("Municipal winner? (true/false) ")
  overall_winner = input("Overall winner? (true/false) ")
  incumbent = input("Incumbent? (true/false) ")

  if party_is_present:
    cur.execute("INSERT INTO results(election_id, candidate_id, party_id, votes, municipal_winner, \
                overall_winner, incumbent) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                (election_id, candidate_id, party_id, votes, municipal_winner, overall_winner, incumbent))
  else:
    cur.execute("INSERT INTO results(election_id, candidate_id, votes, municipal_winner, \
                overall_winner, incumbent) VALUES(%s,%s,%s,%s,%s,%s)",
                (election_id, candidate_id, votes, municipal_winner, overall_winner, incumbent))
  print("Successfully inserted.\n")

conn.commit()
cur.close()
conn.close()