from utils.db_schema import TODO_SCHEMA
import sqlite3

DB_NAME = 'todo.db'


# create new connection
def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        return conn, conn.cursor()
    except Exception as e:
        print("Error Form database Connection: ", e)
        return None


# initialize database 
def initialize_database():
    conn, c = create_connection() 
    c.execute(TODO_SCHEMA)
    conn.commit()
    conn.close()