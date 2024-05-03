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
            HucksCompleted real,
            HucksIncompleteForced real,
            HucksIncompleteUnforced real,
            HucksIncompleteOther real,
            EndzoneScored real,
            EndzoneNotScoredForced real,
            EndzoneNotScoredUnforced real,
            EndzoneNotScoredUnknown real,
            BlocksForced real,
            BlocksUnforced real,
            TurnoversForced real,
            TurnoversUnforced real,
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