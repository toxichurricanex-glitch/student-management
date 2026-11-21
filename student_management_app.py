import tkinter
from tkinter import PhotoImage
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("620x420")
window.title("Student Management System")

class Student:
    def __init__(self, name, age, grade, section, lrn):
        self.name = name
        self.age = age
        self.grade = grade
        self.section = section
        self.lrn = lrn

students = []
student_labels = []

icon = PhotoImage(file = "student.png")
window.iconphoto(True, icon)
#-----------------------------------------------------------------------------------------------------------------------Functions
def home():
    student_list_screen.pack_forget()
    add_student_screen.pack_forget()
    home_screen.pack()

def add_student():
    student_list_screen.pack_forget()
    home_screen.pack_forget()
    add_student_screen.pack()

def student_list():
    home_screen.pack_forget()
    add_student_screen.pack_forget()
    student_list_screen.pack()

    for student in student_labels:
        student.destroy()

    student_labels.clear()

    row = 1

    for student in students:
        student_info = tkinter.Label(student_list_screen, text = f"\n\nName: {student.name}\n"
                                                                 f"Age: {student.age}\n"
                                                                 f"Grade Level {student.grade}\n"
                                                                 f"Section: {student.section}\n"
                                                                 f"LRN: {student.lrn}", font = ("Arial", 12, "bold"))
        student_info.grid(row = row, column = 0, columnspan = 2, sticky = "w")
        student_labels.append(student_info)

        row += 1


#-----------------------------------------------------------------------------------------------------------------------Navigation Frame
navigation_frame = tkinter.Frame(window)
navigation_frame.pack(side = "left", fill = 'y', padx = 50, pady = 85)

home_button = tkinter.Button(navigation_frame, text = "[ Home ]", command = home)
home_button.grid(row = 0, column = 0, sticky = "we")

add_student_button = tkinter.Button(navigation_frame, text = "[ Add Student ]", command = add_student)
add_student_button.grid(row = 1, column = 0, sticky = "we")

student_list_button = tkinter.Button(navigation_frame, text = "[ Enrollees ]", command = student_list)
student_list_button.grid(row = 2, column = 0, sticky = "we")


#-----------------------------------------------------------------------------------------------------------------------Content Frame
content_frame = tkinter.Frame(window)
content_frame.pack(side = "left", fill = 'y')

#-- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    home screen
home_screen = tkinter.Frame(content_frame)
home_screen.pack(pady = 40)

home_header = tkinter.Label(home_screen, text = "Student Management", font = ("Times new Roman", 28, "bold"))
home_header.grid(row = 0, column = 0, columnspan = 2, sticky = 'w')

home_label = tkinter.Label(home_screen, text = '\n\n\n- This application is mainly built for Buenaventura Alandy National Highschool\n'
                                               '- Keep tracks of your students thoroughly and accurately\n')
home_feats = tkinter.Label(home_screen, text = "Features:", font = ("Arial", 12, "bold"))
home_features = tkinter.Label(home_screen, text = "• Enroll new students\n"
                                                  "• Keep track of their work records\n"
                                                  "• View student's lists", font = ("Arial", 10))

student_counter = tkinter.Label(home_screen, text = f"Student enrollees counter: {len(students)}", font = ("Times new Roman", 15, "bold"))


home_label.grid(row = 1, column = 0, sticky = "w")
home_feats.grid(row = 2, column = 0, sticky = "w")
home_features.grid(row = 3, column = 0, sticky = "w")
student_counter.grid(row = 4, column = 0, sticky = "w")

#-- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    add student screen
add_student_screen = tkinter.Frame(content_frame)

def enroll():
    name = student_name_entry.get().strip().title()
    age = student_age_entry.get().strip()
    grade_level = student_grade_level_entry.get().strip()
    section = student_section_entry.get().strip().capitalize()
    lrn = student_LRN_entry.get().strip()

    if name == "" and age == "" and grade_level == "" and section == "" and lrn == "":
        messagebox.showerror(
            "Enrolling Failed",
            "Please fill in the blanks."
        )
    elif name == "" or age == "" or grade_level == "" or section == "" or lrn == "":
        messagebox.showerror(
            "Enrolling Failed",
            "Please complete filling the blanks."
        )

    else:
        try:
            age = int(age)

        except ValueError:
            student_age_entry.delete(0, "end")
            messagebox.showerror(
                "Enrolling Failed",
                "Please make sure age are in numbers."
            )
            return
#--------------- -------------------------------------------------------
        try:
            grade_level = int(grade_level)

        except ValueError:
            student_grade_level_entry.delete(0, "end")
            messagebox.showerror(
                "Enrolling Failed",
                "Please make sure grade level are digits."
            )
            return
#----------------------------------------------------------------------
        try:
            lrn = int(lrn)

        except ValueError:
            student_LRN_entry.delete(0, "end")
            messagebox.showerror(
                "Enrolling Failed",
                "Please make sure LRN are digits."
            )
            return

        if age < 0:
            student_age_entry.delete(0, "end")

            messagebox.showerror(
                "Enrolling Failed",
                "Age cannot be negative."
            )
            return
        if grade_level <= 6:
            student_grade_level_entry.delete(0, "end")

            messagebox.showerror(
                "Enrolling Failed",
                "We cant have elementary students in this school."
            )
            return

        students.append(Student(name, age, grade_level, section, lrn))
        messagebox.showinfo(
            "Enrolling Success",
            f"{name} is enrolled."
        )
        student_name_entry.delete(0, "end")
        student_section_entry.delete(0, "end")
        student_LRN_entry.delete(0, "end")
        student_age_entry.delete(0, "end")
        student_grade_level_entry.delete(0, "end")

        student_counter.config(text = f"Student enrollees counter: {len(students)}", font = ("Times new Roman", 15, "bold"))






add_student_header = tkinter.Label(add_student_screen, text = "Enroll a new Student!", font = ("Georgia", 24, "bold"))
add_student_header.grid(row = 0, column = 0, columnspan = 2, sticky = 'w')

student_name = tkinter.Label(add_student_screen, text = "Name:")
student_age = tkinter.Label(add_student_screen, text = "Age:")
student_grade_level = tkinter.Label(add_student_screen, text = "Grade:")
student_section = tkinter.Label(add_student_screen, text = "Section:")
student_LRN = tkinter.Label(add_student_screen, text = "LRN:")

student_name_entry = tkinter.Entry(add_student_screen)
student_age_entry = tkinter.Entry(add_student_screen)
student_grade_level_entry = tkinter.Entry(add_student_screen)
student_section_entry = tkinter.Entry(add_student_screen)
student_LRN_entry = tkinter.Entry(add_student_screen)

student_name.grid(row = 1, column = 0)
student_age.grid(row = 2, column = 0)
student_grade_level.grid(row = 3, column = 0)
student_section.grid(row = 4, column = 0)
student_LRN.grid(row = 5, column = 0)

student_name_entry.grid(row = 1, column = 1, sticky = "w")
student_age_entry.grid(row = 2, column = 1, sticky = "w")
student_grade_level_entry.grid(row = 3, column = 1, sticky = "w")
student_section_entry.grid(row = 4, column = 1, sticky = "w")
student_LRN_entry.grid(row = 5, column = 1, sticky = "w")

enroll_button = tkinter.Button(add_student_screen, text = "[ Enroll ]", command = enroll)
enroll_button.grid(row = 6, column = 0, columnspan =2, sticky = "ew", pady = 10)

#-- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    students list screen
student_list_screen = tkinter.Frame(content_frame)

student_list_header = tkinter.Label(student_list_screen, text = "Students Enrollees", font = ("Georgia", 26, "bold"))
student_list_header.grid(row = 0, column = 0, columnspan = 2, sticky = "w")




window.mainloop()


