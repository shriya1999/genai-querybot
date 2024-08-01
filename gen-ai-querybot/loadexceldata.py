import pandas as pd
import sqlite3

# Read the CSV file
csv_file_path = "account.csv"
df = pd.read_csv(csv_file_path)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('banking.db')
cursor = conn.cursor()

# Create table if it doesn't exist
table_name = 'Account'
columns = df.columns.tolist()
print(columns)
columns_definition = ", ".join([f"{column} TEXT" for column in columns])  # Assuming all columns are of TEXT type, adjust as needed
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})"
print(create_table_query)
cursor.execute(create_table_query)

# Insert the data from the DataFrame into the SQLite table
df.to_sql(table_name, conn, if_exists='append', index=False)

# Commit the transaction
conn.commit()

print("The inserted records are:")
data = cursor.execute('''SELECT * FROM Account''')

print(type(data))


# Close the connection
conn.close()
