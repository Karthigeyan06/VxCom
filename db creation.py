import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("database.db")

# Create a cursor object
cursor = conn.cursor()

# Create the vid table with vno and loc columns
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vid (
        vno INTEGER PRIMARY KEY, 
        loc TEXT NOT NULL
    )
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Table 'vid' created successfully.")
