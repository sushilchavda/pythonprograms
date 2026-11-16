import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 30, 45, 50]

plt.plot(months, sales, marker="o")
plt.title("Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.bar(months, sales, color="green")
plt.title("Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

marks = [35, 45, 50, 55, 60, 62, 65, 70, 72, 75, 80, 85, 90]
plt.hist(marks, bins=5, color="orange")
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.show()

subjects = ["Python", "Java", "DBMS", "Maths"]
hours = [40, 25, 20, 15]
plt.pie(hours, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()
