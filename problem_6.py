"""
Project 2: Show Me the Data Structures

problem 6. Union and Intersection

This takes in two linked lists and return a linked list that is composed of either
the union or intersection, respectively.

5 test cases are made, including one or two empty linked lists.

Since self.tail is added to class LinkedList and each append() in LinkedList takes
O(1) time, it take O(n) time to create two input linked lists, where n is the
input size.

It takes O(n) time convert two input linked lists to set in Python.
Union and intersection of two sets in Python take O(n) time, roughly going through
two sets once and using hash table.
It takes O(n) time to output the results of union and intersection.

All together, it takes O(n) time.

Space: O(n) for set, where n is the input size.

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        c = self.head # current node
        if c == None:
            return "<empty>"
        out_string = ""
        while c:
            if c == self.head:
                out_string += str(c.value)
            else:
                out_string += " -> " + str(c.value)
            c = c.next
        return out_string

    def append(self, value):
        c = Node(value) # current node
        if self.head is None:
            self.head = c
            self.tail = self.head
            return
        self.tail.next = c
        self.tail = c

    def to_set(self):
        h = set()
        c = self.head # current node
        while c:
            h.add(c.value)
            c = c.next
        return h
    
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    h1 = llist_1.to_set()
    h2 = llist_2.to_set()
    h3 = h1 | h2
    l3 = LinkedList()
    for e in h3:
        l3.append(e)
    return l3

def intersection(llist_1, llist_2):
    # Your Solution Here
    h1 = llist_1.to_set()
    h2 = llist_2.to_set()
    h3 = h1 & h2
    l3 = LinkedList()
    for e in h3:
        l3.append(e)
    return l3

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,9,7,35,6,65,6,8,3,4,27]
element_2 = [7,32,6,1,8,11,7,2,26]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test case 4 (one empty linked list)

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [7,32,6,1,8]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))

# Test case 5 (two empty linked list)

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = []
element_2 = []
for i in element_1:
    linked_list_5.append(i)
for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

"""
Output:

32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21
4 -> 21 -> 6
65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23
<empty>
32 -> 65 -> 1 -> 3 -> 35 -> 4 -> 6 -> 7 -> 8 -> 9 -> 2 -> 11 -> 26 -> 27
8 -> 6 -> 7
32 -> 1 -> 6 -> 7 -> 8
<empty>
<empty>
<empty>

"""