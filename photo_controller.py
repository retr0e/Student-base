from tkinter import *
from tkinter import filedialog
import shutil
import os
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
    initial_path = "Photos/"

    def copy_file_to_project(file_path):
        project_directory = "/Users/retr0/PycharmProjects/Lista_Six/Student-base/Photos"
        destination_path = os.path.join(project_directory, os.path.basename(file_path))
        if os.path.exists(destination_path):
            print("File already exists in the destination directory. Skipping copy.")
        else:
            shutil.copy(file_path, destination_path)
            print(f"File copied to: {destination_path}")

        db_connect = sqlite3.connect('dziekanat.db')
        db_cursor = db_connect.cursor()
        db_cursor.execute("UPDATE zdjecia SET zdjecie_studenta=? WHERE oid=?", (
            initial_path,
            student[0],
        ))
        db_connect.commit()
        db_connect.close()

    root = Tk()

    chosen_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Wybierz plik",
                                             filetypes=(("Pliki jpg", "*.jpg"), ("Wszystkie pliki", "*.*")))
    li = chosen_file.split(sep="/")
    initial_path = initial_path + li[len(li) - 1]

    if chosen_file:

        copy_file_to_project(chosen_file)

    root.destroy()
