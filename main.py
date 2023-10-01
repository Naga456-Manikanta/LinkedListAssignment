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

#defining class for a node in a linkedlist. Since this is doubly linked list each node will have a value, a previous node and next node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
#defining class for creating a doubly linked list since this is a doubly linked list it will have a head and tail properties, which are bacially nodes
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #to insert an element in doubly linked list we first check if it is the first node
    #if it is first node i.e. no other node exists then that node becomes both head and tail
    #else we link the node by setting the prev and next elements of the nodes properly.
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    #code to parse throught the linked list and print it
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    #function to count number of elements greater than certain value in the given linked list.
    def count_greater_than(self, value):
        count = 0
        current = self.head
        while current:
            if current.data > value:
                count += 1
            current = current.next
        return count
    #We would use a sort of bubble sort alogrithm for sorting the items in the linked list
    #this basically swaps the items in the list until the items are at right place according the the required order.
    def bubble_sort(self, ascending=True):
        if not self.head:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if (current.data > current.next.data and ascending) or (current.data < current.next.data and not ascending):
                    # Swap the data of the current node and its next node
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
    #while deleting index we have to check if this item is at the head.in that case we just have to replace the head. otherwise we have to remove it from link
    def delete_at_index(self, index):
        if index < 0:
            return
        current = self.head
        count = 0
        while current:
            if count == index:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
            count += 1

    #code to insert a node when the linked list is already sorted. We have to loop through the sorted list and check for the right position to insert.
    def insert_with_sorting(self, data, ascending=True):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current:
                if (data <= current.data and ascending) or (data >= current.data and not ascending):
                    new_node.next = current
                    new_node.prev = current.prev
                    if current.prev:
                        current.prev.next = new_node
                    else:
                        self.head = new_node
                    current.prev = new_node
                    return
                if not current.next:
                    current.next = new_node
                    new_node.prev = current
                    self.tail = new_node
                    return
                current = current.next

# #testing the linked list
# dll = DoublyLinkedList()
# dll.insert(5)
# dll.insert(2)
# dll.insert(8)
# dll.insert(1)
# dll.insert(6)
# dll.display()
# dll.bubble_sort(ascending=True)
# dll.display()
# dll.bubble_sort(ascending=False)
# dll.display()
# dll.delete_at_index(2)
# dll.display()
# dll.insert_with_sorting(7,ascending=False)
# dll.display()

#testing random number insertion
# mainLL = DoublyLinkedList()
# for number in listOfRandomNumbers:
#   mainLL.insert(number)
# mainLL.display()
# mainLL.bubble_sort(ascending=False)
# mainLL.display()

def linkedListCompleteTest(n,m):
  listOfRandomNumbers=generateRandomNumbers(n,m)
  #print(listOfRandomNumbers)
  ll = DoublyLinkedList()
  for number in listOfRandomNumbers:
    ll.insert(number)
  #ll.display()
  greaterthan50 = ll.count_greater_than(50)
  #print(greaterthan50)
  ll.bubble_sort(ascending=False)
  #ll.display()
  if greaterthan50 > 5:
    ll.delete_at_index(4)
    #ll.display()
  else:
    ll.delete_at_index(1)
    #ll.display()
  ll.insert_with_sorting(10,ascending=False)
  #ll.display()

linkedListCompleteTest(10,100)

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
execution_times = []

# Measuring the time for different values of n
for n in n_values:
    execution_time = measure_time(linkedListCompleteTest, n)
    execution_times.append(execution_time)

# Plot the measured times against the values of n
plt.plot(n_values, execution_times, marker='o')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. n (m = 10n)')
plt.grid(True)
plt.show()

import csv
time_dict = dict(zip(n_values, execution_times))
print(time_dict)
csv_filename = "execution_times_linked_list.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['n', 'execution_time'])  # Write header row
    for n, time_val in time_dict.items():
        writer.writerow([n, time_val])