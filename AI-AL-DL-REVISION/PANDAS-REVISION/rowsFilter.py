import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Kirti','Shruti','Murti'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}
df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print('Employee with Salary > 50000')
# print(high_salary)


# filtering ross whose sallary is greater than 50k or less then 70k

filtered = df[(df['Age'] > 30 ) & (df['Salary'] > 50000)]
print("employee with list age > 30 and salary  > 50000")
# print(filtered)

filtered_or = df[(df['Age'] > 30) | (df['Performance Score'] > 90)]
print(filtered_or)