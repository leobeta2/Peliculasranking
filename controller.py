import sqlite3

def connect():
    con = sqlite3.connect('movies.db')
    con.row_factory = sqlite3.Row
    return con

def get_movies():
    con = connect()
    c = con.cursor()
    query = "select * from movies order by ranking asc"
    result = c.execute(query)
    movies = result.fetchall()
    return movies