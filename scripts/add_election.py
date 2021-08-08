# Interactive script to add a set of election results into the database
# Will prompt for name of position, year of election, and candidates info
# 
# USAGE: add_election.py
# (then follow the prompts)

import psycopg2
from distutils.util import strtobool

def int_or_empty(string):
  """Function to convert numeric string to int (or None if string is empty)"""
  if string:
    return int(string)
  else:
    return None

def bool_or_empty(string):
  """Function to convert boolean string to bool (or None if string is empty)"""
  if string:
    return bool(strtobool(string))
  else:
    return None

conn = psycopg2.connect("dbname=results user=sean password=sean")
cur = conn.cursor()

# Finding the elected position
while True:
  position = input("Position? ")
  cur.execute("SELECT id FROM elected_positions WHERE name=%s",(position,))
  position_result = cur.fetchone()
  if position_result is not None:
    break
  else:
    print(">> Not found in database. Try again.")
position_id = str(position_result[0])

# Creating the election in year X for the elected position found earlier
while True:
  # Basic data validation on year X
  while True:
    year = int(input("Year? "))
    if (year > 1899 and year < 2100):
      break
    else:
      print(">> Input between 1900 and 2099 only. Try again.")

  # Checking if the election is to fill an unexpired term
  # Then inserting the new election into the db
  unexp_length = int_or_empty(input("Unexpired term? (no. of years) "))
  cur.execute("INSERT INTO elections(year, position_id, unexpired_term_length) \
              VALUES(%s, %s, %s) RETURNING id", (year, position_id, unexp_length))
  election_result = cur.fetchone()
  if election_result is not None:
    break
  else:
    print(">> Error inserting election into database. Try again.")
election_id = str(election_result[0])

# Finding all the candidates
num_candidates = int(input("How many candidates? "))
for x in range(num_candidates):
  print("** Candidate", x+1, "**")
  while True:
    candidate = input("Candidate? ")
    cur.execute("SELECT id FROM candidates WHERE full_name=%s",(candidate,))
    candidate_result = cur.fetchall()
    if candidate_result != []:
      to_keep = 0
      if (len(candidate_result) > 1):
        print(candidate_result)
        to_keep = int(input("Multiple candidates found. Select one: ")) - 1
      break
    else:
      print(">> Not found in database. Try again.")
  candidate_id = str(candidate_result[to_keep][0])

  # Finding the party affiliation of the candidate
  while True:
    party = input("Party? ")
    if not party:
      party_id = None
      break
    else:
      cur.execute ("SELECT id FROM parties WHERE name=%s",(party,))
      party_result = cur.fetchone()
      if party_result is not None:
        party_id = str(party_result[0])
        break
      else:
        print(">> Not found in database. Try again.")

  # Getting input on no. of votes and winner/incumbency statuses
  # Empty input is treated as None (or null value in the db)
  votes = int_or_empty(input("No. of votes? "))
  municipal_winner = bool_or_empty(input("Municipal winner? (t/f) "))
  overall_winner = bool_or_empty(input("Overall winner? (t/f) "))
  incumbent = bool_or_empty(input("Incumbent? (t/f) "))

  cur.execute("INSERT INTO results(election_id, candidate_id, party_id, votes, municipal_winner, \
              overall_winner, incumbent) VALUES(%s,%s,%s,%s,%s,%s,%s)",
              (election_id, candidate_id, party_id, votes, municipal_winner, overall_winner, incumbent))
  print(">> Successfully inserted.\n")

conn.commit()
cur.close()
conn.close()