import tkinter as tk
from PIL import Image, ImageTk
import sqlite3


# def add_form():
#     db_connect = sqlite3.connect('dziekanat.db')
#     db_cursor = db_connect.cursor()
#     # Un-comment below to create table studenci
#     sqlquery = "DROP TABLE oceny"
#     db_cursor.execute(sqlquery)
#     db_connect.commit()
#     sqlquery = "CREATE TABLE oceny (id_studenta integer, id_przedmiotu integer, ocena integer)"
#     db_cursor.execute(sqlquery)
#     db_connect.commit()
#     # choices = ['Matematyka', 'Język Polski', 'Język Angielski', 'Biologia', 'Informatyka', 'Chemia', 'Historia']
#     # for choice in choices:
#     #     db_cursor.execute("INSERT INTO przedmioty VALUES (:p_nazwa)", {
#     #                         'p_nazwa': choice
#     #                       })
#     #     db_connect.commit()
#     db_connect.close()
#
# add_form()


# Wyswietlanie zdjęcia
# def show_image(image_path):
#     # Utwórz główne okno
#     root = tk.Tk()
#     root.title("Wyświetlanie Zdjęcia")
#
#     # Wczytaj obraz za pomocą modułu Pillow
#     image = Image.open(image_path)
#
#     # Przekształć obraz na format obsługiwany przez Tkinter
#     tk_image = ImageTk.PhotoImage(image)
#
#     # Utwórz etykietę i umieść na niej obraz
#     label = tk.Label(root, image=tk_image)
#     label.pack()
#
#     # Uruchom główną pętlę programu
#     root.mainloop()
#
#
# # Wprowadź ścieżkę do zdjęcia, które chcesz wyświetlić
# image_path = "default_img.png"
#
# # Wywołaj funkcję show_image, przekazując ścieżkę do zdjęcia
# show_image(image_path)
