"""Module providing a function that initializes a database."""
import sqlite3

# inits database
def initdb():
    """Function that initializes a database."""
    connection = sqlite3.connect('database.db')

    # Open and execute sql script to drop and create the schema
    with open('schema.sql', encoding="utf-8") as f:
        connection.executescript(f.read())

    # Get the cursor
    cur = connection.cursor()

    # Insert 1st group
    cur.execute("INSERT INTO groups (name, member1, member2, member3, member4, member5)"+
                 "VALUES (?, ?, ?, ?, ?, ?)",
                ('Group 1',	'2022MT03577 - Puneet Singh', '2022MT03599 - Murtaz Mastim',
                 '2022MT03564 - Shivraj Dagadi',
                '2022MT03537 - Paras Jain', '2022MT03593 - Sherine Evangeline Arunodhaya R')
                )

    # Insert 2nd group
    cur.execute("INSERT INTO groups (name, member1, member2, member3, member4, member5)"+
                "VALUES (?, ?, ?, ?, ?, ?)",
                ('Group 2', '2022MT03527 - Anirudh Uppal', '2022MT03589 - KARMAKAR ANKITA ASHOK',
                 '2022mt03573 - DAYALAN P', '2022mt03545 - DILIP K.G.', None)
                )

    # Commit the changes
    connection.commit()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    initdb()
