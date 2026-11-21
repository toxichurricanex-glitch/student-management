import tkinter
from tkinter import PhotoImage

window = tkinter.Tk()
window.geometry("620x420")
window.title("Student Management System")

icon = PhotoImage(file = "student.png")
window.iconphoto(True, icon)
#-----------------------------------------------------------------------------------------------------------------------Functions
def home():
    add_student_screen.pack_forget()
    home_screen.pack()

def add_student():
    home_screen.pack_forget()
    add_student_screen.pack()

#-----------------------------------------------------------------------------------------------------------------------Navigation Frame
navigation_frame = tkinter.Frame(window)
navigation_frame.pack(side = "left", fill = 'y', padx = 50, pady = 85)

home_button = tkinter.Button(navigation_frame, text = "[ Home ]", command = home)
home_button.grid(row = 0, column = 0, sticky = "we")

add_student_button = tkinter.Button(navigation_frame, text = "[ Add Student ]", command = add_student)
add_student_button.grid(row = 1, column = 0, sticky = "we")


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

home_label.grid(row = 1, column = 0, sticky = "w")
home_feats.grid(row = 2, column = 0, sticky = "w")
home_features.grid(row = 3, column = 0, sticky = "w")

#-- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    -- -- -- -    add student screen
add_student_screen = tkinter.Frame(content_frame)

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



window.mainloop()


# PROCEED TO FINISH ENROLLING THE STUDENT