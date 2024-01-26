from tkinter import *
from pandas import *
def calculate():
    Python_marks1 = int(marks_entry1.get())
    Android_marks2 = int(marks_entry2.get())
    DW_marks3 = int(marks_entry3.get())
    Project_marks4 = int(marks_entry4.get())
    

    total_marks = Python_marks1 + Android_marks2 + DW_marks3 +  Project_marks4

    percentage = (total_marks / 400) * 100

    if percentage >= 70:
        grade = "A"
    elif percentage >= 50:
        grade = "B"
    elif percentage >= 35:
        grade = "C"
    else:
        grade = "F"

    if Python_marks1 < 28 or Android_marks2 < 28 or DW_marks3 < 28 or Project_marks4 < 28 :
        result = "Fail"
    else:
        result = "Pass"
    
    total_marks_label.config(text="Total Marks:        " + str(total_marks))
    percentage_label.config(text="Percentage:        {:.2f}%".format(percentage))
    grade_label.config(text="Grade:        " + grade)
    result_label.config(text="Result:        " + result)

window = Tk()
window.title("DAGIYA NITESH>>>>MARKSHEET")
name_label = Label(window, text="NAME").grid(row=0, column=0)
name_entry = Entry(window).grid(row=0, column=1)


rollno_label =Label(window, text="ROLL No.").grid(row=1, column=0)
rollno_entry =Entry(window).grid(row=1, column=1)
 
seatno_label=Label(window, text='        SEAT NO.').grid(row=0, column=3)
seatno_entry=Entry(window).grid(row=0, column=4)

sr_label=Label(window,text='SR.No.').grid(row=3, column=0)
sr_label2=Label(window,text='1').grid(row=4, column=0)
sr_label3=Label(window,text='2').grid(row=5, column=0)
sr_label4=Label(window,text='3').grid(row=6, column=0)
sr_label5=Label(window,text='4').grid(row=7, column=0)

sub_label=Label(window,text='SUBJECTS').grid(row=3, column=1)
sub_label=Label(window,text='Python').grid(row=4, column=1)
sub_label=Label(window,text='Android').grid(row=5, column=1)
sub_label=Label(window,text='DW').grid(row=6, column=1)
sub_label=Label(window,text='Project').grid(row=7, column=1)

ENTER_MARKS_label=Label(window,text='ENTER MARKS').grid(row=3, column=2)
marks_entry1 = Entry(window)
marks_entry1.grid(row=4, column=2)


marks_entry2 = Entry(window)
marks_entry2.grid(row=5, column=2)


marks_entry3 = Entry(window)
marks_entry3.grid(row=6, column=2)


marks_entry4 = Entry(window)
marks_entry4.grid(row=7, column=2)
button=Button(window,text='SUBMIT',fg='red',bg='pink',command=calculate).grid(row=8, column=2)


total_marks_label = Label(window, text="")
total_marks_label.grid(row=4, column=3)

percentage_label = Label(window, text="")
percentage_label.grid(row=5, column=3)

grade_label = Label(window, text="")
grade_label.grid(row=6, column=3)

result_label = Label(window, text="")
result_label.grid(row=7, column=3)

window.mainloop()