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
            FinalScore text,
            Point real,
            Pulled text,
            Scored text,
            Hucks-Completed real,
            Hucks-Incomplete-Forced real,
            Hucks-Incomplete-Unforced real,
            Hucks-Incomplete-Other real,
            Endzone-Scored real,
            Endzone-NotScored-Forced real,
            Endzone-NotScored-Unforced real,
            Endzone-NotScored-Unknown real,
            Blocks-Forced,Blocks-Unforced real,
            Turnovers-Forced real,
            Turnovers-Unforced real,
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