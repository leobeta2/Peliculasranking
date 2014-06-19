
import sqlite3

def connect():
    con = sqlite3.connect('movies.db')
    con.row_factory = sqlite3.Row
    return con

def get_movies():
	#consigue y ordena las peliculas
    con = connect()
    c = con.cursor()
    query = "select * from movies order by ranking asc"
    result = c.execute(query)
    movies = result.fetchall()
    return movies

def get_reparto(id_movie):
	#consigue el reparto
	con = connect()
    c = con.cursor()
    query = "select stars from movies where id = ?"
    result = c.execute(query, [id_movie])
    reparto = result.fetchall()
    return reparto

def get_descripcion(id_movie):
    #consigue la descripción de la respectiva película
    con = connect()
    c = con.cursor()
    query = "select description from movies where id = ?"
    result = c.execute(query, [id_movie])
    descripcion = result.fetchall()
    return descripcion








