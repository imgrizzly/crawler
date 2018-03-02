# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect("film.db")

with open('../item1.json', "r") as f:
    movies = json.load(f)
for movie in movies:

    filmname = movie["filmname"][0]
    director = movie["director"][0]
    try:
        performer = movie["performer"][0]
    except IndexError:
        performer = u'暂无'
    imdb = movie["imdb"][0]
    release_time = movie["release_time"][0]
    language = movie["language"]
    synopsis = movie["synopsis"]
    sql = 'INSERT INTO movie(filmname, director, performer, imdb, release_time, language,synopsis)\
    VALUES("%s", "%s", "%s", "%s", "%s", "%s")' % (filmname, director, performer, imdb, release_time, language, synopsis)
    conn.execute(sql)
    conn.commit()
