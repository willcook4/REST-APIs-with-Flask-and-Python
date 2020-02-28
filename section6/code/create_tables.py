
## Now using sqlalchemy to create the tables
print('This file no longer does anything, Now using sqlalchemy to create the tables')
# import sqlite3

# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()

# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)

# print('Creating users table if it does not exist')

# create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
# cursor.execute(create_items_table)
# print('Creating items table if it does not exist')

# # cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
# # print('Creating a test item')

# connection.commit()
# connection.close()