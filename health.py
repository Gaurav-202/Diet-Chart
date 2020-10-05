#yeh code health management code hai ek software
d = {"1": "Harry", "2": "Rohan"} #dict to assign the values
def client():
    a = input(
        "Enter a number 1 or 2 to access the data of Harry and Rohan:\n")  # it will take the input
    b = input("Enter what you want to access exercise or diet?, press x for exercise and y for diet:\n")
    if a == "1" and b == "x":
        print("Okay so you want the exercise plan of:", d[a])
        with open("harry-ex.txt", "r") as f:
            print(f.read())
    elif a == "1" and b == "y":
        print("Diet is:\n")
        with open("harryd.txt", "r") as f:
            print(f.read())
    elif a == "2" and b == "x":
        print("exercise of", d[a])
        with open("rohane.txt", "r") as f:
            print(f.read())
    elif a == "2" and b == "y":
        print("Diet is:\n")
        with open("rohand.txt", "r") as f:
            print(f.read(), end="")
def loc():
    n = int(input("press 1 for retrieving Harry and 2 for Rohan:\n"))
    if n==1:
        o = int(input("press 1 for exercise and 2 for diet:\n"))
        if o == 1:
            print("type what you did?")
            t= input()
        else:
            print("type what did you ate?")
            k= input()
    else:
        o = int(input("press 1 for exercise and 2 for diet:\n"))
        if o == 1:
            print("type what you did?")
            t = input()
        else:
            print("type what you ate?")
            k = input()
try:
    print("Health management system: \n")
    print("Press 1 to lock the exercise and 2 for retrieving the data: \n")
    m = int(input())
    if m == 1:
        loc()
        g = input("Do you want to access again? y/n ")
        if g == "y":
            loc()
        else:
            exit()
    if m == 2:
        client()
        g = input("Do you want to access again? y/n ")
        if g == "y":
            client()
        else:
            exit()
except Exception as e:
    print("Invalid input")







