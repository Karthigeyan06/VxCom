import sqlite3

# Function to insert data into vid table
def insert_data(vno, loc):
    # Connect to the database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Insert data into the vid table
    cursor.execute("INSERT INTO vid (vno, loc) VALUES (?, ?)", (vno, loc))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print(f"Data inserted: vno={vno}, loc='{loc}'")

# Example usage
insert_data(101, "sig1")
insert_data(102, "sig2")
insert_data(103, "sig1")
