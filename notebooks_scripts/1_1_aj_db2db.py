import sqlite3

# Connect to the source database
source_path = '../data/source.db'
source_conn = sqlite3.connect(source_path)
source_cursor = source_conn.cursor()

# Connect to the destination database
destination_path = '../data/destination.db'
dest_conn = sqlite3.connect(destination_path)
dest_cursor = dest_conn.cursor()

# Execute a SELECT statement to retrieve the data from the source table
source_cursor.execute('SELECT * FROM properties')
rows = source_cursor.fetchall()

# Execute an INSERT statement for each row in the result set
for row in rows:
    dest_cursor.execute('INSERT INTO properties VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

# Commit the changes to the destination database
dest_conn.commit()

# Close the connections to the databases
source_cursor.close()
source_conn.close()
dest_cursor.close()
dest_conn.close()