from tkinter import *
from students_view import show_students
from student_controler import add_form
from grade_controller import handle_add_subject

main_window = Tk()
main_window.geometry("550x200")
main_window.title('Student Database')

logo_label = Label(main_window, text="Spis Studentów")
logo_label.grid(columnspan=3, row=0, pady=20)
# logo_label.pack()

show_students_button = Button(main_window, text="Pokaż Studentów uczelni", command=show_students, width=20)
show_students_button.grid(column=0, row=1, pady=10, padx=30)
# show_students_button.pack()
add_student_button = Button(main_window, text="Dodaj studenta", command=add_form, width=20)
add_student_button.grid(column=1, row=1, pady=10, padx=30)
# add_student_button.pack()
add_subject_button = Button(main_window, text="Dodaj przedmiot", command=handle_add_subject, width=20)
add_subject_button.grid(column=1, row=2, pady=10, padx=30)
# add_subject_button.pack()

main_window.mainloop()
