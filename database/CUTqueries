import psycopg2

def test_connection():

  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="chend2",
    user="chend2",
    password="plad242books")
  
  if conn is not None:
    print("Connection Worked!")
  else:
    print("Problem With Connection")
    
  return None

def answer_query():
  
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="chend2",
    user="chend2",
    password="plad242books")


  cur = conn.cursor()

  #search for Northfield
  sql_FloridaPoints = """SELECT * FROM cutstats WHERE Opponent = 'Florida' ORDER BY Point DESC;"""

  cur.execute(sql_FloridaPoints)
  floridaGame = cur.fetchone()
  if floridaGame == None:
    print('The opponent Florida does not exist in the database')
  else:
    print(floridaGame[3])
    
  

test_connection()
answer_query()
