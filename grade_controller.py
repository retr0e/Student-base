from tkinter import *
from tkinter import messagebox
import sqlite3


def handle_add_subject():

    def add_subject():
        db_connect = sqlite3.connect('dziekanat.db')
        db_cursor = db_connect.cursor()
        db_cursor.execute("INSERT INTO przedmioty VALUES (:p_name)", { 'p_name': entry_subject.get()})
        db_connect.commit()
        db_connect.close()
        messagebox.showinfo("Info dodania", "Przedmiot dodany")
        subject_add_window.destroy()

    subject_add_window = Tk()
    subject_add_window.title("Dodawanie przedmiotu")

    subject_label = Label(subject_add_window, text="Nazwa przedmiotu: ")
    subject_label.grid(row=0, column=0)

    entry_subject = Entry(subject_add_window, width=30)
    entry_subject.grid(row=0, column=1)

    submit_subject = Button(subject_add_window, text="Dodaj Przedmiot", fg="green", command=add_subject)
    submit_subject.grid(row=1, columnspan=2)

    submit_subject.mainloop()


def add_grade(student_id, update_callback):
    def on_select(value):
        subject_choice_label['text'] = subject.get()

    db_connect = sqlite3.connect('dziekanat.db')
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT oid, * FROM przedmioty")
    subject_values = db_cursor.fetchall()
    db_connect.commit()
    # print(subject_values)

    subjects = []
    for val in subject_values:
        subjects.append(val[1])

    add_grade_window = Tk()
    add_grade_window.title("Dodanie Oceny")
    add_grade_window.geometry("500x120")

    first_input_label = Label(add_grade_window, text="Przedmiot:")
    first_input_label.grid(row=0, column=0, padx=10)

    subject = StringVar()
    subject_choice_label = Label(add_grade_window, text=subject.get(), width=20)
    subject_choice_label.grid(row=0, column=1, padx=20, pady=10)

    subject_menu = OptionMenu(add_grade_window, subject, *subjects, command=on_select)
    subject_menu.grid(row=0, column=2, padx=20, pady=10)

    second_input_label = Label(add_grade_window, text="Ocena: ")
    second_input_label.grid(row=1, column=0, padx=10)

    grade_entry = Entry(add_grade_window, width=20)
    grade_entry.grid(row=1, column=1)

    def handle_add_grade():
        db_cursor.execute("INSERT INTO oceny VALUES (?, ?, ?)", (
            int(student_id),
            subject.get(),
            int(grade_entry.get())
        ))

        db_connect.commit()
        db_connect.close()
        update_callback()
        add_grade_window.destroy()

    submit_grade_button = Button(add_grade_window, text="Dodaj ocene", command=handle_add_grade, fg="green")
    submit_grade_button.grid(row=2, columnspan=2, pady=10)

    close_window = Button(add_grade_window, text="Zamknij okno", command=add_grade_window.destroy, fg="red")
    close_window.grid(row=2, column=2, pady=10)

    add_grade_window.mainloop()


def edit_grade(student_id, tile_values, update_callback):

    def change_grade():
        db_connect = sqlite3.connect('dziekanat.db')
        db_cursor = db_connect.cursor()
        db_cursor.execute("UPDATE oceny SET id_studenta=?, przedmiot=?, ocena=? WHERE oid=?", (
            student_id,
            edit_subject_entry.get(),
            int(edit_grade_entry.get()),
            int(tile_values[2])
        ))
        db_connect.commit()
        db_connect.close()
        update_callback()
        grade_edition_window.destroy()

    grade_edition_window = Tk()
    grade_edition_window.title("Edycja oceny")

    subject_label = Label(grade_edition_window, text="Nazwa przedmiotu: ")
    subject_label.grid(row=0, column=0)
    edit_subject_entry = Entry(grade_edition_window, width=20)
    edit_subject_entry.insert(0, tile_values[0])
    edit_subject_entry.grid(row=0, column=1)

    grade_label = Label(grade_edition_window, text="Ocena z przedmiotu: ")
    grade_label.grid(row=1, column=0)
    edit_grade_entry = Entry(grade_edition_window, width=5)
    edit_grade_entry.insert(0, tile_values[1])
    edit_grade_entry.grid(row=1, column=1)

    submit_changes_button = Button(grade_edition_window, fg='green', text="Edytuj ocene", command=change_grade)
    submit_changes_button.grid(row=2, column=0)

    close_window = Button(grade_edition_window, fg='red', text="Zamknij okno", command=grade_edition_window.destroy)
    close_window.grid(row=2, column=1)

    def delete_grade_handler():
        res = messagebox.askquestion("Usunięcie oceny", "Czy napewno chcesz usunąć ocene?")
        if res == "yes":
            db_connect = sqlite3.connect('dziekanat.db')
            db_cursor = db_connect.cursor()
            db_cursor.execute("DELETE FROM oceny WHERE id_studenta=:p_id", {
                'p_id': int(student_id),
            })
            db_connect.commit()
            db_connect.close()
            update_callback()
            grade_edition_window.destroy()

    delete_grade_button = Button(grade_edition_window, fg='red', text='Usuń ocene', command=delete_grade_handler)
    delete_grade_button.grid(row=2, column=2)

    grade_edition_window.mainloop()
