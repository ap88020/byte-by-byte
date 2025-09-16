import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1200,1000,1199,1500]

plt.plot(months,sales , color="blue",marker="o", linewidth=2,linestyle="--",label="2025 sales data")
plt.xlabel("Months")
plt.xlabel("Sales")
plt.title("sales per month")
plt.show()