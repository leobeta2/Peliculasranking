# -*- coding: utf-8 -*-

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

def get_imagen(id_movie):
	#busco mi imagen
    con = connect()
    c = con.cursor()
    query = "select poster from movies where id = ?"
    result = c.execute(query, [id_movie]) #la cargo
    imagen = result.fetchall()
    return imagen

def get_descripcion(id_movie):
    #consigue la descripción de la respectiva película seleccionada
    con = connect()
    c = con.cursor()
    query = "select description from movies where id = ?"
    result = c.execute(query, [id_movie])
    descripcion = result.fetchall()
    return descripcion

def up(id_movie):
    # sube la posicion de la peli e el ranking
    exito = False
    con = connect()
    c = con.cursor()
    q1 = "select ranking from movies where id = ?"
    result1 = c.execute(q1, [id_movie])
    r_actual = result1.fetchall()
    r_actual = int(r_actual[0][0])
    r_sup = r_actual - 1
    if r_sup == 0:
        return False 
    q2 = "update movies set ranking = 9999 where ranking = ?"
    q3 = "update movies set ranking =" + str(r_sup) + " where id = ?"
    q4 = "update movies set ranking = ? where ranking = 9999"
    try:
        c.execute(q2, [r_sup])
        c.execute(q3, [id_movie])
        c.execute(q4, [r_actual])
        con.commit()
        exito = True

    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito


def down(id_movie):
    exito = False
    con = connect()
    c = con.cursor()
    query0 = "select count(id) from movies"
    result0 = c.execute(query0)
    n = result0.fetchall()
    q1 = "select ranking from movies where id = ?"
    result1 = c.execute(query1, [id_movie])
    r_actual = result1.fetchall()
    if int(r_actual[0][0]) == int(n[0][0]):
        return False  
    r_actual = int(r_actual[0][0])
    r_inf = r_actual + 1
    q2 = "update movies set ranking = 9999 where ranking = ?"
    q3 = "update movies set ranking =" + str(r_inf) + " where id = ?"
    q4 = "update movies set ranking = ? where ranking = 9999"
    try:
        c.execute(q2, [r_inf])
        c.execute(q3, [id_movie])
        c.execute(q4, [r_actual])
        con.commit()
        exito = True

    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito







