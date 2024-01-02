from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def show_photo(student):
    db_connect = sqlite3.connect('dziekanat.db')
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT zdjecie_studenta FROM zdjecia WHERE id_studenta=?", (
        student[0],
    ))

    image_path = db_cursor.fetchone()[0]

    db_cursor.close()
    db_connect.close()

    show_image(image_path)


def show_image(image_path):
    root = Toplevel()
    root.title("Wyświetlanie Zdjęcia")

    image = Image.open(image_path)

    tk_image = ImageTk.PhotoImage(image)

    label = Label(root, image=tk_image)
    label.pack()

    root.mainloop()


def edit_photo(student):
    print('xd')


