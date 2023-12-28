from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from student_controler import personal_profile
import sqlite3


def show_students():
    root = Tk()
    root.title('Lista Studentów')
    root.geometry('515x120')

    kolumny = ('k_oid', 'k_imie', 'k_nazwisko', 'k_adres', 'k_pesel', 'k_album')

    siatkaDanych = ttk.Treeview(root, columns=kolumny, show='headings', height=5)
    siatkaDanych.column('k_oid', minwidth=10, width=50)
    siatkaDanych.column('k_imie', minwidth=10, width=50)
    siatkaDanych.column('k_nazwisko', minwidth=10, width=100)
    siatkaDanych.column('k_adres', minwidth=10, width=100)
    siatkaDanych.column('k_pesel', minwidth=10, width=100)
    siatkaDanych.column('k_album', minwidth=10, width=100)

    siatkaDanych.heading('k_oid', text='id')
    siatkaDanych.heading('k_imie', text='imie')
    siatkaDanych.heading('k_nazwisko', text='nazwisko')
    siatkaDanych.heading('k_adres', text='adres')
    siatkaDanych.heading('k_pesel', text='pesel')
    siatkaDanych.heading('k_album', text='album')

    def update_treeview():
        # Update Treeview with the latest data from the database
        for item in siatkaDanych.get_children():
            siatkaDanych.delete(item)

        dbPolaczenie = sqlite3.connect('dziekanat.db')
        dbKursor = dbPolaczenie.cursor()
        dbKursor.execute('select oid, * from studenci')
        wynikZapytania = dbKursor.fetchall()
        for wierszDanych in wynikZapytania:
            siatkaDanych.insert('', END, values=wierszDanych)
        dbPolaczenie.commit()
        dbPolaczenie.close()

    update_treeview()

    def wyborWiersza(event):
        for selected_item in siatkaDanych.selection():
            wybranyWiersz = siatkaDanych.item(selected_item)
            wybraneWartości = wybranyWiersz['values']
            personal_profile(wybraneWartości, update_treeview)

    siatkaDanych.bind('<<TreeviewSelect>>', wyborWiersza)

    siatkaDanych.grid(row=0, column=0, sticky='nsew')

    scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=siatkaDanych.yview)
    siatkaDanych.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    root.mainloop()