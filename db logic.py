import sqlite3

# Function to fetch data from vid table and apply conditions based on loc
def get_data():
    # Connect to the database
    r1=[]
    r2=[]
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Fetch all data from vid table
    cursor.execute("SELECT vno, loc FROM vid")
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Process the data
    for vno, loc in rows:
        if loc == "sig1":
            r1.append(vno)
        elif loc == "sig2":
            r2.append(vno)
        
        else:
            print(f"Vehicle {vno} is in {loc}. Action: No specific action.")

    v1=len(r1)
    v2=len(r2)
    if v1<v2:
        print(f"Signal 2 has more vehicles than Signal 1")
        print("Signal 2 : Green, Signal 1 : Red")
    elif v1>v2:
        print(f"Signal 1 has more vehicles than Signal 2")
        print("Signal 1 : Green, Signal 2 : Red")
    else:
        print(f"Signal 1 and Signal 2 have equal number of vehicles")

# Call the function to get data
get_data()
