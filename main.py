from tkinter import *
from students_view import show_students
from student_controler import add_form

main_window = Tk()
main_window.geometry("630x150")
main_window.title('Student Database')

logo_label = Label(main_window, text="Spis Studentów")
logo_label.grid(columnspan=3, row=0, pady=20)

show_students_button = Button(main_window, text="Pokaż Studentów uczelni", command=show_students)
show_students_button.grid(column=0, row=1, pady=10, padx=30)

add_student_button = Button(main_window, text="Dodaj studenta", command=add_form)
add_student_button.grid(column=1, row=1, pady=10, padx=30)

add_subject = Button(main_window, text="Dodaj przedmiot")
add_subject.grid(column=2, row=1, pady=10, padx=30)

main_window.mainloop()