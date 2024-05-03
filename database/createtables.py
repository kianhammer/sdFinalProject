import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS cutstats
        """,
        """
        CREATE TABLE cutstats (
            Date timestamp,
            Opponent text,
            Final Score text,
            Point real,
            Pulled text,
            Scored text,
            Hucks - Completed real,
            Hucks - Incomplete - Forced real,
            Hucks - Incomplete - Unforced real,
            Hucks - Incomplete - Other real,
            Endzone - Scored real,
            Endzone - Not Scored - Forced real,
            Endzone - Not Scored - Unforced real,
            Endzone - Not Scored - Unknown real,
            Blocks - Forced,Blocks - Unforced real,
            Turnovers - Forced real,
            Turnovers - Unforced real,
            Players text,
        )
        """)

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    for command in commands:
        cur.execute(command)

    conn.commit()

if __name__ == '__main__':
    create_tables()