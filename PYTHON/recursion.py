list = ["orange","mango","papaya","ananas"]
size = len(list)

def print_list(size):
    if(size == 0):
        return 0
    
    print_list(size-1)
    print(list[size-1] , end="->")


print_list(size)

# def cal_sum(n):
#     if(n == 0):
#         return 0
#     return cal_sum(n-1) + n

# val = cal_sum(4)
# print(val)

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1 
#     else:
#         return n * fact(n-1)  

# val = fact(10)
# print(val)

# def num(n):
#     if(n == 10) :
#         return
#     print(n,end=" ")
#     num(n+1)

# num(0)
