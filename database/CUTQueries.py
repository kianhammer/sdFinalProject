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
  floridaScore = cur.fetchone()
  print('Final score against Florida:')
  if floridaScore == None:
    print('The opponent Florida does not exist in the database')
  else:
    print(floridaScore[2])

  
  sql_CornellHucksCompleted = """SELECT * FROM cutstats WHERE Opponent = 'Cornell';"""

  cur.execute(sql_CornellHucksCompleted)
  cornellHucks = cur.fetchall()
  print('Total hucks completed against Cornell:')
  if cornellHucks == None:
    print('The opponent Cornell does not exist in the database')
  else:
    totalHucksCompleted = 0
    for point in cornellHucks:
      totalHucksCompleted = totalHucksCompleted + point[6]
    print(totalHucksCompleted)

  
  gameOpponent = input("Enter opponent:")
  gamePlayer = input("Enter CUT player:")
  sql_pointsPlayedInGame = """SELECT * FROM cutstats WHERE Opponent = %s;"""

  cur.execute(sql_pointsPlayedInGame, [gameOpponent])
  gameAgainstOpponent = cur.fetchall()
  print('Total points ' + gamePlayer + ' played against ' + gameOpponent + ':')
  if gameAgainstOpponent == None:
    print(gamePlayer + ' played zero points against ' + gameOpponent)
  else:
    totalPoints = 0
    print(str(gameAgainstOpponent[18]))
    for point in gameAgainstOpponent:
      if str(gameAgainstOpponent[18]).find(gamePlayer) > -1:
        totalPoints += 1
    print(gamePlayer + ' played ' + str(totalPoints) + ' points against ' + gameOpponent)
    
  
    
  

test_connection()
answer_query()
