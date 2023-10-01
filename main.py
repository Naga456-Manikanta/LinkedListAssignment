#Function to generate n random number in inclusive range 1 to m
import random
def generateRandomNumbers(n,m):
  numbers = []
  for i in range(n):
    numbers.append(random.randint(1,m))
  return numbers
# #test the generated list of Random Numbers
listOfRandomNumbers = generateRandomNumbers(10,100)
# print(listOfRandomNumbers)

#Here the theoratical complexity of generating the list is O(n).

class DynamicArray:
    def __init__(self):
        self.array = []

    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < len(self.array):
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def insert(self, value):
        self.array.append(value)

    def count_greater_than(self, value):
        count = 0
        for item in self.array:
            if item is not None and item > value:
                count += 1
        return count

    def bubble_sort(self, ascending=True):
        if ascending:
            self.array = [item for item in self.array if item is not None]
            self.array.sort()
        else:
            self.array = [item for item in self.array if item is not None]
            self.array.sort(reverse=True)

    def delete_at_index(self, index):
        if 0 <= index < len(self.array):
            del self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def insert_with_sorting(self, data, ascending=True):
        if ascending:
            index = 0
            while index < len(self.array) and (self.array[index] is not None and self.array[index] < data):
                index += 1
        else:
            index = 0
            while index < len(self.array) and (self.array[index] is not None and self.array[index] > data):
                index += 1
        self.array.insert(index, data)

    def display(self):
        print(self.array)

# Example usage:
# dynamic_array = DynamicArray()

# dynamic_array.insert(5)
# dynamic_array.insert(2)
# dynamic_array.insert(8)
# dynamic_array.insert(1)
# dynamic_array.insert(6)

# dynamic_array.display()  # Output: [5, 2, 8, 1, 6]

# print(dynamic_array.count_greater_than(3))  # Output: 3

# dynamic_array.bubble_sort(ascending=False)
# dynamic_array.display()  # Output: [8, 6, 5, 2, 1]

# dynamic_array.delete_at_index(2)
# dynamic_array.display()  # Output: [8, 6, 2, 1]

# dynamic_array.insert(4)
# dynamic_array.display()  # Output: [8, 6, 2, 1, 4]
#testing random number insertion
# mainarray = DynamicArray()
# for number in listOfRandomNumbers:
#   mainarray.insert(number)
# mainarray.display()
# mainarray.bubble_sort(ascending=False)
# mainarray.display()

def arrayCompleteTest(n,m):
  listOfRandomNumbers=generateRandomNumbers(n,m)
  #print(listOfRandomNumbers)
  arr = DynamicArray()
  for number in listOfRandomNumbers:
    arr.insert(number)
  #arr.display()
  greaterthan50 = arr.count_greater_than(50)
  #print(greaterthan50)
  arr.bubble_sort(ascending=False)
  #arr.display()
  if greaterthan50 > 5:
    arr.delete_at_index(4)
    #arr.display()
  else:
    arr.delete_at_index(1)
    #arr.display()
  arr.insert_with_sorting(10,ascending=False)
  #arr.display()

arrayCompleteTest(10,100)

#to empirically measure the time and space complexity of the the given test code we would define a follwing block
import time
import matplotlib.pyplot as plt

# Define a function to measure time and store the execution times
def measure_time(func, n):
    m = 10 * n  # Set m as 10 times n
    start_time = time.time()
    func(n, m)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Create a list to store values of n
n_values = [10,50,100,500,1000,5000,10000]
execution_times_dynamic_array = []

# Measuring the time for different values of n
for n in n_values:
    execution_time = measure_time(arrayCompleteTest, n)
    execution_times_dynamic_array.append(execution_time)

# Plot the measured times against the values of n
plt.plot(n_values, execution_times_dynamic_array, marker='o')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. n (m = 10n)')
plt.grid(True)
plt.show()



import csv
time_dict = dict(zip(n_values, execution_times_dynamic_array))
print(time_dict)
csv_filename = "execution_times_dynamic_array.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['n', 'execution_time'])  # Write header row
    for n, time_val in time_dict.items():
        writer.writerow([n, time_val])