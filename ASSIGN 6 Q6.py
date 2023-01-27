a = input("Enter a student name if u want : ")
try :
      b = int(input("Enter a student ID : "))
except :
      b = 0
try :
      c = int(input("Enter a student class if u want : "))
except :
      c = 0


def student_data(student_id = 22105011 ,student_name = "",student_class = -1):
     if student_id == 0 :
         print("Student ID : ",22105011)
     else:
         print("Student ID : ",student_id)
     if student_name != "":
         print("Student Name : ",student_name)
     if student_class == 0:
         print()
     else:
         print("Student Class : ", student_class)


student_data(b,a,c)