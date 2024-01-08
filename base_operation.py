import tkinter as tk
from PIL import Image, ImageTk
import sqlite3


def add_form():
    db_connect = sqlite3.connect('dziekanat.db')
    db_cursor = db_connect.cursor()
    # Un-comment below to create table studenci
    # sqlquery = "DROP TABLE oceny"
    # db_cursor.execute(sqlquery)
    # db_connect.commit()
    # sqlquery = "CREATE TABLE oceny (id_studenta integer, przedmiot text, ocena integer)"
    # sqlquery = "CREATE TABLE zdjecia (id_studenta integer, zdjecie_studenta text)"
    nazwa = input("Podaj nazwe przedmiotu")
    sqlquery = "DELETE FROM przedmioty WHERE nazwa=:naz"
    db_cursor.execute(sqlquery, {
        'naz': nazwa,
    })
    db_connect.commit()
    # choices = ['Matematyka', 'Język Polski', 'Język Angielski', 'Biologia', 'Informatyka', 'Chemia', 'Historia']
    # for choice in choices:
    #     db_cursor.execute("INSERT INTO przedmioty VALUES (:p_nazwa)", {
    #                         'p_nazwa': choice
    #                       })
    #     db_connect.commit()
    db_connect.close()


add_form()
