# A Python program to demonstrate common binary heap operations

# Import the heap functions from python library
from heapq import heappush, heappop, heapify


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#			 heap invarient
# heapify - transform list into heap, in place, in linear time

# A class for Min Heap
class MinHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)
        print(self.heap)

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

        # Method to remove minium element from min heap

    def extractMin(self):
        return heappop(self.heap)

    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        # print(self.heap)
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]

    # Driver pgoratm to test above function


heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)
heapObj.insertKey(43)

print(heapObj.extractMin())
print(heapObj.getMin())
heapObj.decreaseKey(2, 1)
print(heapObj.getMin())

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

#Fixme MaxHeap는 값을 넣을 때 -를 붙여 값을 넣고 뺄 때 -1을 곱한 값을 출력시킨다.
