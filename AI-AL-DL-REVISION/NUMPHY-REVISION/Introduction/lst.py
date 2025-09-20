temperature = [22,33,44,55,66]

total = 0

# for i in range(0,len(temperature)):
#     total += i


# average = total/len(temperature)
# print(average)

for temp in temperature:
    total += temp

average = total/len(temperature)
print(average)