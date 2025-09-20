temperature = [22.4,22.6,44.6,11.8,66.8,99.6]

add = 0

for temp in temperature:
    add += temp


average = add / len(temperature)

print(average)