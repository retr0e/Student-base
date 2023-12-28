from tkinter import *
from tkinter import ttk
from grade_controller import add_grade
import sqlite3


def show_grades(identification):

    grades_window = Tk()
    grades_window.title('Lista ocen')
    grades_window.geometry('230x150')

    columns = ('k_przedmiot', 'k_ocena')

    grades_net = ttk.Treeview(grades_window, columns=columns, show='headings', height=5)
    # grades_net.column('k_oid', minwidth=10, width=50)
    grades_net.column('k_przedmiot', minwidth=170, width=170)
    grades_net.column('k_ocena', minwidth=10, width=50)

    # grades_net.heading('k_oid', text='Id')
    grades_net.heading('k_przedmiot', text='Przedmioty')
    grades_net.heading('k_ocena', text='Ocena')

    def update_grades():
        for item in grades_net.get_children():
            grades_net.delete(item)

        db_connect = sqlite3.connect('dziekanat.db')
        db_cursor = db_connect.cursor()
        db_cursor.execute('SELECT przedmiot, ocena FROM oceny WHERE id_studenta=:p_id_stud', {
            "p_id_stud": identification
        })
        student_grades = db_cursor.fetchall()

        for grades in student_grades:
            grades_net.insert('', END, values=grades)

        db_connect.commit()
        db_connect.close()

    update_grades()

    def tile_select():
        for selected_item in grades_net.selection():
            chosen_tile = grades_net.item(selected_item)
            values_from_tile = chosen_tile['values']
            print(values_from_tile)

    grades_net.bind('<<TreeviewSelect>>', tile_select)

    grades_net.grid(row=0, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(grades_window, orient=VERTICAL, command=grades_net.yview)
    grades_net.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    def handle_add_grade_button():
        add_grade(identification, update_grades)

    add_grade_button = Button(grades_window, text="Dodaj Ocenę", fg="orange", command=handle_add_grade_button)
    add_grade_button.grid(row=1, columnspan=2)

    grades_window.mainloop()
