import random
import datetime

subjects = [
    "Sarukh khan",
    "Hritik Roshan",
    "A Mumbai Cat",
    "A Group Of Monkey",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi",
    "Nirmala Sitaraman"
]

actions = [
    "launches",
    "cancles",
    "dance with aswarya",
    "declare war on",
    "orders",
    "celebrates",
    "cooks"
]

places = [
    "at Rad-Fort",
    "at Kapashera Border",
    "in delhi metro",
    "a plate of somasa",
    "at ganga ghat",
    "during Ipl Match",
    "at India Gate"
]

emojis = ["😂","🔥","🐒","🚀","💥","🎉"]

count = 0

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    emoji = random.choice(emojis)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    headLine = f"{count} : [{now}] Breaking news : {subject} {action} {place} {emoji}"
    print("\n"+headLine)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()


    if user_input == "no":
        break


    save_heading = input("\nDo you want save this headLine(y/n)").strip().lower()

    if(save_heading == "y"):
        with open("jokes.txt","a",encoding="utf-8") as f:
            f.write(headLine+"\n")
    
    count += 1


print("\nThanks for using this fake headline news generator, Have a fun day")