import matplotlib.pyplot as plt
import numpy as np
import io
import pandas as pd

# 1. Draw a line from position (1,3) and (2,10) then to (6,12) and finally to position (18,20). Mark each point with a beautiful green color and set line colour to red and line style dotted.
x1, y1 = [1, 2, 6, 18], [3, 10, 12, 20]
plt.figure()
plt.plot(x1, y1, color='red', linestyle='dotted', marker='o', markerfacecolor='green', markeredgecolor='green')
plt.title("1. Custom Styled Line Plot")
plt.show()

# 2. Draw a plot for the following data Temperature in degree Sales
temp = [12, 14, 16, 18, 20, 22, 24]
sales = [100, 200, 250, 400, 300, 450, 500]
plt.figure()
plt.plot(temp, sales, marker='o')
plt.xlabel("Temperature (°C)")
plt.ylabel("Sales")
plt.title("2. Temperature vs Sales")
plt.show()

# 3. Write a python program to draw a line using given axis values taken from a text file, with suitable labels in x and y axis and a title.
file_content = "1 2\n2 4\n3 6\n4 8\n5 10"
data = np.loadtxt(io.StringIO(file_content))
plt.figure()
plt.plot(data[:, 0], data[:, 1], marker='s', color='blue')
plt.xlabel("X Axis Values")
plt.ylabel("Y Axis Values")
plt.title("3. Line Plot from Text File Data")
plt.show()

# 4. Write a python program to plot two or more lines on same plot with suitable legends for each line.
x4 = [1, 2, 3, 4]
y4_1 = [1, 4, 9, 16]
y4_2 = [1, 2, 3, 4]
plt.figure()
plt.plot(x4, y4_1, label='Squares')
plt.plot(x4, y4_2, label='Linear')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("4. Multiple Lines with Legends")
plt.legend()
plt.show()

# 5. Write a python program to create multiple plots.
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6], color='orange')
plt.title("Subplot 1")
plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [6, 5, 4], color='purple')
plt.title("Subplot 2")
plt.tight_layout()
plt.show()

# 6. Consider the following data. Programming language Popularity...
langs = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# i. Write a python program to display a bar chart of the popularity of programming languages.
plt.figure()
plt.bar(langs, pop)
plt.title("6.i. Bar Chart of Popularity")
plt.show()

# ii. Write a python program to display a horizontal bar chart of the popularity of programming languages. (Make it red color).
plt.figure()
plt.barh(langs, pop, color='red')
plt.title("6.ii. Horizontal Bar Chart (Red)")
plt.show()

# iii. Write a python program to display a bar chart of the popularity of programming languages. Use different colors for each bar.
plt.figure()
plt.bar(langs, pop, color=['blue', 'green', 'orange', 'purple', 'brown', 'pink'])
plt.title("6.iii. Multi-colored Bar Chart")
plt.show()

# 7. Write a python program to create bar plots of scores by group and gender. Use multiple x values on the same chart for men and women.
groups = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
x7 = np.arange(len(groups))
width = 0.35
plt.figure()
plt.bar(x7 - width/2, men_means, width, label='Men')
plt.bar(x7 + width/2, women_means, width, label='Women')
plt.xticks(x7, groups)
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("7. Scores by Group and Gender")
plt.legend()
plt.show()

# 8. Write a python program to create a pie chart on the popularity of programming languages.
plt.figure()
plt.pie(pop, labels=langs, autopct='%1.1f%%', startangle=140)
plt.title("8. Pie Chart of Programming Languages")
plt.show()

# 9. Write a python program to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file.
csv_content = "Country,Gold\nUSA,46\nGreat Britain,27\nChina,26\nRussia,19\nGermany,17"
df = pd.read_csv(io.StringIO(csv_content))
plt.figure()
plt.pie(df['Gold'], labels=df['Country'], autopct='%1.1f%%', startangle=90)
plt.title("9. 2016 Olympics Gold Medals")
plt.show()

# 10. Write a python Program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students.
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [75, 79, 90, 80, 88, 75, 65, 95, 78, 40]
plt.figure()
plt.scatter(math_marks, science_marks, color='teal')
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.title("10. Math vs Science Marks Scatter Plot")
plt.show()