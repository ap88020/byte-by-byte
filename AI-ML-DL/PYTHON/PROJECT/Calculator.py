def add(a,b):
    return a + b

def minus(a,b):
    return a - b

def divide(a,b):
    return a / b

def mul(a,b):
    return a * b

def history():
    try:
        with open("history.txt","r") as f:
            lines = f.readlines()

        if not lines:
            print("not history left")
        else: 
            print("----HISTORY----")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
            print("File Not Found")


        
        


while(True):
    a = int(input("Enter the first Number : "))
    b = int(input("Enter the second Number : "))
    exp = str(input("Enter the expression : "))
    hce = str(input("save history->save , clear history->clr , exit loop->exit , print History->his : "))

    if(exp == "+"):
        if(hce == "save"):
            with open("history.txt","a") as f:
                f.write(f"\n{a} {exp} {b} = {add(a,b)}")

    if(exp == "-"):
        if(hce == "save"):
            with open("history.txt","a") as f:
                f.write(f"\n{a} {exp} {b} = {minus(a,b)}")

    if(exp == "*"):
        if(hce == "save"):
            with open("history.txt","a") as f:
                f.write(f"\n{a} {exp} {b} = {mul(a,b)}")

    if(exp == "/"):
        if(hce == "save"):
            with open("history.txt","a") as f:
                f.write(f"\n{a} {exp} {b} = {divide(a,b)}")
    
    if(hce == "his"):
        history()

    if(hce == "exit"):
        break
