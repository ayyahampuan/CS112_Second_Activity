
Student_name = str(input("Student Name:"))
id = input("ID#:")
Course_Section = input("Course/Section:")
First_Quarter_Grade = int(input("First Quarter Grade:"))
Second_Quarter_Grade = int(input("Second Quarter Grade:"))
Third_Quarter_Grade = int(input("Third Quarter Grade:"))
Fourth_Quarter_Grade = int(input("Fourth Quarter Grade:"))
Total_Grades = float(First_Quarter_Grade + Second_Quarter_Grade + Third_Quarter_Grade + Fourth_Quarter_Grade) / 4
#Average_Grade = Total_Grades / 4

print("Student Name: ", Student_name)
print("Student's ID #: ", id)
print("Course and Sec:", Course_Section)
print("First Quarter Grade:", First_Quarter_Grade)
print("Second Quarter Grade:", Second_Quarter_Grade)
print("Third Quarter Grade:", Third_Quarter_Grade)
print("Fourth Quarter Grade:", Fourth_Quarter_Grade)
print("Student's Average Grade:", Total_Grades)