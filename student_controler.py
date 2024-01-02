from tkinter import *
from tkinter import messagebox
from grade_view import show_grades
from photo_controller import show_photo, edit_photo
import sqlite3


def add_form():

    def add_student():
        db_connect = sqlite3.connect('dziekanat.db')
        db_cursor = db_connect.cursor()
        db_cursor.execute("INSERT INTO studenci VALUES (:p_imie, :p_nazwisko, :p_adres, :p_pesel, :p_album)",
                          {
                              'p_imie': edit_firstname.get(),
                              'p_nazwisko': edit_lastname.get(),
                              'p_adres': edit_adres.get(),
                              'p_pesel': edit_pesel.get(),
                              'p_album': edit_album.get()
                          })
        db_connect.commit()
        db_cursor.execute("SELECT oid FROM studenci WHERE pesel=? AND album=?", (
            edit_pesel.get(),
            edit_album.get()
        ))
        new_student_id = db_cursor.fetchall()
        print(new_student_id[0][0])

        # Add default photo information to data_base
        default_photo_path = "Photos/default_img.png"
        db_cursor.execute("INSERT INTO zdjecia VALUES (?, ?)", (
            int(new_student_id[0][0]),
            default_photo_path
        ))
        db_connect.commit()
        db_connect.close()

        messagebox.showinfo("Info dodania", "Student dodany")
        main_window.destroy()

    main_window = Tk()
    main_window.title("Dodawanie Studenta")

    # Imie
    label_firstname = Label(main_window, text="imię: ")
    label_firstname.grid(row=0, column=0, padx=20)
    edit_firstname = Entry(main_window, width=30)
    edit_firstname.grid(row=0, column=1, padx=20)

    # Nazwisko
    label_lastname = Label(main_window, text="nazwisko: ")
    label_lastname.grid(row=1, column=0, padx=20)
    edit_lastname = Entry(main_window, width=30)
    edit_lastname.grid(row=1, column=1, padx=20)

    # Adres
    label_adres = Label(main_window, text="adres: ")
    label_adres.grid(row=2, column=0, padx=20)
    edit_adres = Entry(main_window, width=30)
    edit_adres.grid(row=2, column=1, padx=20)

    # PESEL
    label_pesel = Label(main_window, text="PESEL: ")
    label_pesel.grid(row=3, column=0, padx=20)
    edit_pesel = Entry(main_window, width=30)
    edit_pesel.grid(row=3, column=1, padx=20)

    # Numer albumu
    label_album = Label(main_window, text="album: ")
    label_album.grid(row=4, column=0, padx=20)
    edit_album = Entry(main_window, width=30)
    edit_album.grid(row=4, column=1, padx=20)

    # Execute Operation

    # Add Operation
    student_save_button = Button(main_window, text="Dodaj nowego studenta", command=add_student)
    student_save_button.grid(row=5, columnspan=2, pady=10, padx=20, ipadx=100)

    main_window.mainloop()


def personal_profile(personal_data, update_callback):

    def save_edited_data():
        db_connect = sqlite3.connect('dziekanat.db')
        db_cursor = db_connect.cursor()
        db_cursor.execute(
            "UPDATE studenci SET imie=:p_imie, nazwisko=:p_nazwisko, adres=:p_adres, "
            "pesel=:p_pesel, album=:p_album WHERE oid=:p_oid",
            {
                'p_imie': firstname_dialog.get(),
                'p_nazwisko': lastname_dialog.get(),
                'p_adres': adres_dialog.get(),
                'p_pesel': pesel_dialog.get(),
                'p_album': album_dialog.get(),
                'p_oid': str(personal_data[0])
            })
        db_connect.commit()
        db_connect.close()
        update_callback()

    personal_window = Tk()
    personal_window.geometry("700x270")
    personal_window.title("Profil Studenta")

    def handle_show_picture_button():
        show_photo(personal_data)

    def handle_edit_picture_button():
        edit_photo(personal_data)

    image_button = Button(personal_window, text="Pokaż zdjęcie", command=handle_show_picture_button)
    image_button.grid(row=0, column=3, pady=20)
    change_image_button = Button(personal_window, text="Edytuj zdjęcie", command=handle_edit_picture_button)
    change_image_button.grid(row=1, column=3)

    header = Label(personal_window, text="Edycja profilu studenta:")
    header.grid(row=0, columnspan=2, pady=10)

    firstname_label = Label(personal_window, text="Imie Studenta: ")
    firstname_label.grid(row=1, column=0, padx=20)
    firstname_dialog = Entry(personal_window, width=30)
    firstname_dialog.grid(row=1, column=1, padx=20)
    firstname_dialog.insert(0, personal_data[1])

    lastname_label = Label(personal_window, text="Nazwisko Studenta: ")
    lastname_label.grid(row=2, column=0, padx=20)
    lastname_dialog = Entry(personal_window, width=30)
    lastname_dialog.grid(row=2, column=1, padx=20)
    lastname_dialog.insert(0, personal_data[2])

    adres_label = Label(personal_window, text="Adres: ")
    adres_label.grid(row=3, column=0, padx=20)
    adres_dialog = Entry(personal_window, width=30)
    adres_dialog.grid(row=3, column=1, padx=20)
    adres_dialog.insert(0, personal_data[3])

    pesel_label = Label(personal_window, text="PESEL: ")
    pesel_label.grid(row=4, column=0, padx=20)
    pesel_dialog = Entry(personal_window, width=30)
    pesel_dialog.grid(row=4, column=1, padx=20)
    pesel_dialog.insert(0, personal_data[4])

    album_label = Label(personal_window, text="Album: ")
    album_label.grid(row=5, column=0, padx=20)
    album_dialog = Entry(personal_window, width=30)
    album_dialog.grid(row=5, column=1, padx=20)
    album_dialog.insert(0, personal_data[5])

    def handle_grades_button():
        show_grades(personal_data[0])

    show_grades_button = Button(personal_window, text="Pokaż Oceny", fg="blue", command=handle_grades_button)
    show_grades_button.grid(row=6, column=0, pady=20)

    edit_button = Button(personal_window, text="Potwierdź Edycje", command=save_edited_data, fg="green")
    edit_button.grid(row=6, column=1, pady=20)

    exit_button = Button(personal_window, text="Zamknij okno", command=personal_window.destroy, fg="red")
    exit_button.grid(row=6, column=3, padx=40)

    personal_window.mainloop()

