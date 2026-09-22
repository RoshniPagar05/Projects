#create student dictionray
#teacher:
#1 add student
#2view all student
#3check result
#4exit
student = {}
while  True:
    print("-----STUDENT MANGER APP -----")
    print("1.add student")
    print("2.view all studnet")
    print("3.check result")
    print("4.delete record")
    print("5.update record")
    print("6.exit")

    choice = input("enter your choice")
    if choice == "1":
        name = input("enter name :")
        marks = input("enter marks :")
        student[name] = marks
        print(f"{name} added sucessfully")

    elif choice == "2":
        if not student:
            print("no student found")
        else:
            for name,marks in student.items():
                print(name,"->",marks)

    elif choice == "3":
        name = input("enter student name :")
        if name in student:
            marks = student[name]
            if marks >= "40":
                print("pass")
            else:
                print("fail")
        else:
            print("student not found")

    elif choice == "4":
        name = input("enter name you want to delete :")
        if name in student:
            del student[name]
            print(f"{name} sucessfully deleted ")
        else:
            print(f"{name} not found")
    elif choice =="5":
        name = input("enter the name you want to update : ")
        if name in student:
            new_marks = int(input(f"enter new marks  :"))
            student[name] = new_marks
            print(f"{name} sucessfully added ")
        else:
            print(f"{name} not found")

    
    elif choice =="6":
        print("exit")
        break
    else:
        print("Inalid choice ")


            

