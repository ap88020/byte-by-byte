import pandas as pd

# Creating a sample employee dataset similar to the one in the screenshot
data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Amit Sharma", "Riya Gupta", "Rajesh Verma", "Priya Singh", "Sunil Kumar",
             "Alok Mehta", "Kavita Yadav", "Pankaj Mishra", "Deepika Reddy", "Ramesh Patil"],
    "Age": [27, 32, 45, 29, 26, 52, 31, 24, 34, 29],
    "Salary (INR)": [650000, None, 1200000, 700000, 500000, 2100000, None, 400000, 380000, 440000],
    "Experience (Years)": [4, 8, float("inf"), 6, 3, 28, float("inf"), 10, 30, 6],
    "City": ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai",
             "Hyderabad", "Pune", "Jaipur", "Bangalore", "Kolkata"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "Operations", "IT", "Marketing", "Management", "IT"],
    "Performance Rating": [4.5, 3.8, 4.9, 4.2, None, 5.0, 4.0, 3.5, 5.0, 4.2]
}

df = pd.DataFrame(data)

# file_path = '/mnt/data/employee_data_sheet.csv'
# df.to_csv(file_path, index=False)

# file_path
