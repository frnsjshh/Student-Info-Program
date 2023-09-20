# Prompt the user to enter a radius

Name = (input("Full name: "))
ID = input("Student number: ")
course = input("Course: ")
section = input("Section: ")
Quarter1 = eval(input("First Quarter Grade: "))
Quarter2 = eval(input("Second Quarter Grade: "))
Quarter3 = eval(input("3rd Quarter Grade: "))
Quarter4 = eval(input("4th Quarter Grade: "))
Ave = Quarter1 + Quarter2 + Quarter3 + Quarter4
Average = Ave / 4

print("Name of the student:", Name)
print("Student ID Number:", ID)
print("Course and Section:", course + "_" + section)
print("Quarter Grades: ")
print("1st Quarter Grade:", Quarter1)
print("2nd Quarter Grade:", Quarter2)
print("3rd Quarter Grade:", Quarter3)
print("4th Quarter Grade:", Quarter4)
print("Student's Average:", Average)
