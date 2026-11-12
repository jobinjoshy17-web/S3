
import numpy as np

# 1. Fahrenheit to Centigrade
f = np.array([32, 50, 68, 86, 104])
c = (f - 32) * 5 / 9
print("Centigrade:", c)


# 2. Average, Variance and Standard Deviation
a = np.random.rand(1000)
print("Average:", np.mean(a))
print("Variance:", np.var(a))
print("Standard Deviation:", np.std(a))


# 3. Degrees to Radians
degrees = np.array([0, 30, 45, 60, 90, 180])
radians = np.radians(degrees)
print("Radians:", radians)


# 4. Difference Between Neighbouring Elements
a = np.array([10, 20, 35, 50, 70])
diff = np.diff(a)
print("Difference:", diff)


# 5. Sort Complex Array
a = np.array([3+2j, 1+4j, 2+1j, 1+2j])
sorted_array = np.sort_complex(a)
print("Sorted Array:", sorted_array)


# 6. Print Random Numbers Greater Than 4
a = np.random.randint(1, 10, 10)
print("Array:", a)
print("Values greater than 4:", a[a > 4])


# 7. Search a Particular Number
a = np.array([10, 20, 30, 40, 50])
n = int(input("Enter number to search: "))

if n in a:
    print("Number found")
else:
    print("Number not found")


# 8. Save Array to Text File and Load It
a = np.array([10, 20, 30, 40, 50])
np.savetxt("array.txt", a)
b = np.loadtxt("array.txt")
print("Loaded Array:", b)


# 9. Even Integers from 30 to 60
a = np.arange(30, 61, 2)
print("Even Numbers:", a)


# 10. Sum of All Elements, Rows and Columns
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Total Sum:", np.sum(a))
print("Column Sum:", np.sum(a, axis=0))
print("Row Sum:", np.sum(a, axis=1))
