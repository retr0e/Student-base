from tkinter import *
from tkinter import messagebox
import sqlite3


def add_student():
    db_connect = sqlite3.connect('dziekanat.db')
    db_cursor = db_connect.cursor()
    # Un-comment below to create table studenci
    # sqlquery = "CREATE TABLE studenci (imie text, nazwisko text, adres text, pesel text, album integer)"
    # db_cursor.execute(sqlquery)
    # db_connect.commit()
    db_cursor.execute("INSERT INTO studenci VALUES (:p_imie, :p_nazwisko, :p_adres, :p_pesel, :p_album)",
                      {
                            'p_imie': edit_firstname.get(),
                            'p_nazwisko': edit_lastname.get(),
                            'p_adres': edit_adres.get(),
                            'p_pesel': edit_pesel.get(),
                            'p_album': edit_album.get()
                        })
    db_connect.commit()
    db_connect.close()


def show_students():
    db_connect = sqlite3.connect('dziekanat.db')
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT oid, * FROM studenci")
    query_result = db_cursor.fetchall()
    show_line = ""
    for line in query_result:
        show_line += "id: " + str(line[0])
        show_line += ", imię: " + line[1]
        show_line += ", nazwisko: " + line[2]
        show_line += ", adres: " + line[3]
        show_line += ", pesel: " + line[4]
        show_line += ", album: " + str(line[5]) + "\n"
    print(show_line)
    result_label['text'] = show_line
    db_connect.commit()
    db_connect.close()
    return


def delete_student(deletion_id):
    db_connect = sqlite3.connect('dziekanat.db')
    db_cursor = db_connect.cursor()
    db_cursor.execute("DELETE FROM studenci WHERE oid= " + str(deletion_id))
    db_connect.commit()
    db_connect.close()

def delete_handler():
    handler = student_delete.get()
    if not (handler.isdigit()):
        messagebox.showinfo("Informacja", "Nie podano identyfikatora studenta do usuniecia")
        return
    student_delete_id = int(handler)

    result = messagebox.askquestion("Zapytanie", "Czy na pewno chcesz usunąć studenta o oid " +
                                    str(student_delete_id) + "?")
    if result == "yes":
        delete_student(student_delete_id)
    return


main_window = Tk()
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

# Show Operation
student_show_button = Button(main_window, text="Wyświetl studentów", command=show_students)
student_show_button.grid(row=6, column=0, pady=5, columnspan=2, padx=20, ipadx=100)

result_label = Label(main_window, text="")
result_label.grid(row=7, column=0, columnspan=2)

# Delete Operation
student_delete = Entry(main_window, width=20)
student_delete.grid(row=8, column=0, padx=3)
student_delete_button = Button(main_window, text="Usuń studenta", command=delete_handler)
student_delete_button.grid(row=8, column=1, padx=3)


main_window.mainloop()
