import sqlite3


def execute_SQL_command(database, command):
    with sqlite3.connect(database) as conn:
        crsr = conn.cursor()
        crsr.execute(command)
        conn.commit()
    return crsr