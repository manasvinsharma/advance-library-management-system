import mysql.connector
from mysql.connector import Error
def connect():
    """Set up a connection with the database."""
    conn_obj = mysql.connector.connect(host='localhost',database='mydb',user='root',password='kks')
    cur_obj = conn_obj.cursor()
    cur_obj.execute('''CREATE TABLE IF NOT EXISTS book
                       ( 
                        title text,
                        author text,
                        year integer,
                        isbn integer,
                        shelf integer,
                        raw integer)''')
    conn_obj.commit()
    conn_obj.close()
def insert(title, author, year, isbn,shelf,raw):
    """Insert entry into database."""

    conn_obj = mysql.connector.connect(host='localhost',database='mydb',user='root',password='kks')
    cur_obj = conn_obj.cursor()
    sql="INSERT INTO book (title, author, year, isbn,shelf,raw) VALUES(%s, %s, %s, %s, %s, %s)"
    cur_obj.execute(sql,(title, author, year, isbn,shelf,raw))
    conn_obj.commit()
    conn_obj.close()

def view():
    """View all database entries."""
    conn_obj = mysql.connector.connect(host='localhost',database='mydb',user='root',password='kks')
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * FROM book")
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows

def update(d,title, author, year, isbn,shelf,raw):
    """Update a database entry."""
    conn_obj = mysql.connector.connect(host='localhost',database='mydb',user='root',password='kks')
    cur_obj = conn_obj.cursor()
    cur_obj.execute("UPDATE book where isbn=%s"
                    "SET title = %s, "
                    "author = %s, "
                    "year = %s, "
                    "shelf=%s,"
                    "raw=%s", 
                    (isbn,title, author, year,shelf,raw))
    conn_obj.commit()
    conn_obj.close()

def delete(d):
    """Delete a database entry."""
    conn_obj = mysql.connector.connect(host='localhost',database='mydb',user='root',password='kks')
    cur_obj = conn_obj.cursor()
    cur_obj.execute("DELETE FROM book WHERE isbn = %s",(d,))
    conn_obj.commit()
    conn_obj.close()

def search(title = "", author = "", year = "", isbn = ""):
    """Search for a database entry."""
    conn_obj = mysql.connector.connect(host='localhost',database='mydb',user='root',password='kks')
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * "
                    "FROM book "
                    "WHERE title = %s OR author = %s OR year = %s OR isbn = %s", 
                    (title, author, year, isbn))
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows
    
connect()
