count = 0

def wap():
    with open("practice.txt","r") as f:
        data = f.read()

        num = data.split(",")

        for val in num:
            if(int(val) % 2 == 0) :
                print(val)

wap()
# print(count)
# def check_for_line():
#     word = "easy"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return line_no
#             line_no += 1
    
#     return -1


# print(check_for_line())

# with open("practice.txt","r") as f:
#     data = f.read()

# data = data.replace("python","java")

# print(data)

# with open("practice.txt","w") as f:
#     f.write(data)

# with open("practice.txt","w") as f:
# with open("practice.txt","w") as f:
#     f.write("learning python\nit is easy to learn")
#     f.write("experiance is good or enjoyable")

# import os

# os.remove("demo.txt")

# print(os.getcwd())  # shows where Python is looking for file.txt



# import os

# # os.remove("file.txt")

# os.remove("file.txt")


# with open("file.txt","w+") as f:
#     data = f.

# with open("file.txt","r+") as f:
#     data = f.read()
#     print(data)

# f = open("file.txt","r+")

# f.write("abcd\n")
# data = f.read()
# print(data)

# f = open("file.txt","a")


# f.write("\nlooking good this one")

# data = f.read(19)


# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# print(data)
# print(type(data))
# f.close()
# print("hllo world")