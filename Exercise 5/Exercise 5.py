import datetime


def getdate():
    return datetime.datetime.now()


def retreive_file():
    """
    Retrieves Client Data
    """
    print("Enter '1' for Harry.")
    print("Enter '2' for Rohan.")
    print("Enter '3' for Hammad.")
    ret = int(input("Whoes file do you want to retrieve : "))
    print("1 For Food.")
    print("2 For Exercise.")
    inp_op = int(input("What Do you want to retrieve : "))
    if ret == 1 and inp_op == 1:
        with open("Harry Food.txt") as f:
            print(f.read())
    elif ret == 1 and inp_op == 2:
        with open("Harry Exercise.txt") as f:
            print(f.read())
    elif ret == 2 and inp_op == 1:
        with open("Rohan Food.txt") as f:
            print(f.read())
    elif ret == 2 and inp_op == 2:
        with open("Rohan Exercise.txt") as f:
            print(f.read())
    elif ret == 3 and inp_op == 1:
        with open("Hammad Food.txt") as f:
            print(f.read())
    elif ret == 3 and inp_op == 2:
        with open("Hammad Exercise.txt") as f:
            print(f.read())


print("Welcome to Health Management System.")
while True:
    print("Enter '1' to append in file")
    print("Enter '2' to retrieve the file")
    inp_1 = int(input("What do you want to do : "))
    if inp_1 == 1:
       print("Enter '1 for Harry.")
       print("Enter '2' for Rohan.")
       print("Enter '3' for Hammad.")
       inp_2 = int(input("Who's data do you want to write in : "))
       print("Enter '1' for Food")
       print("Enter '2' for Exercise")
       inp_3 = int(input("What do you want to edit : "))
       if inp_3 == 1 and inp_2 == 1:
            with open("Harry Food.txt","a") as x:
                p = input("What do you want to write :\n")
                x.write(str([str(getdate())])+p.capitalize()+"\n")
       elif inp_3 == 2 and inp_2 == 1:
            with open("Harry Exercise.txt","a") as x:
                 p = input("What do you want to write :\n")
                 x.write(str([str(getdate())])+p.capitalize()+"\n")
       elif inp_3 == 1 and inp_2 == 2:
            with open("Rohan Food.txt","a") as x:
                p = input("What do you want to write :\n")
                x.write(str([str(getdate())])+p.capitalize()+"\n")
       elif inp_3 == 2 and inp_2 == 2:
            with open("Rohan Exercise.txt","a") as x:
                 p = input("What do you want to write :\n")
                 x.write(str([str(getdate())])+p.capitalize()+"\n")
       elif inp_3 == 3 and inp_2 == 1:
           with open("Hammad Food.txt", "a") as x:
               p = input("What do you want to write :\n")
               x.write(str([str(getdate())]) + p.capitalize() + "\n")
       elif inp_3 == 3 and inp_2 == 2:
           with open("Hammad Exercise.txt", "a") as x:
               p = input("What do you want to write :\n")

               x.write(str([str(getdate())]) +p.capitalize() + "\n")

    elif inp_1 == 2:
        retreive_file()