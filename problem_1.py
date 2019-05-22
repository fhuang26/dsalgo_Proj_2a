"""
Project 2: Show Me the Data Structures

problem 1. LRU Cache

The lookup operation (i.e., get()) and put()/set() is supposed to be fast
for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is
known as a cache hit. If, however, the entry is not found, it is known as
a cache miss. set(key, value) will move current node to the latest (tail).

A hashmap (key: data, value: Node) and doubly-linked list are used to do
LRU cache. Each get() and set() takes O(1) time.

get() and set() may move a node in the middle of a list to the latest, tail.
Doubly-linked list is used to support this so that we can move a node in the
list to the tail in O(1) time.

Node needs to keep the input key since when the least-used node is removed
from head of the list, we need to remove the corresponding key in hash table
as well.

To save memory allocation and release time, we remove the least-used node
(head), use the removed node as the new node. New (key, value) is assigned
to this node, and this node is moved to the tail of the list (latest).

Time: get(): O(1)   set(): O(1)

Space: O(K), where K is the capacity of this LRU cache.

"""

class Node:
    def __init__(self, key, value):
        self.value = value
        self.prev = None
        self.next = None
        self.key = key # for removal in hashmap

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cap = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.h = {} # key: data, value: Node

    def get(self, key=None):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key == None:
            return -1
        if key in self.h:
            c = self.h[key] # current node
            if self.size > 1 and self.tail != c:
                if self.head == c:
                    self.head = c.next
                    self.head.prev = None
                else:
                    c.prev.next = c.next
                    c.next.prev = c.prev
                self.tail.next = c
                c.prev = self.tail
                self.tail = c
                c.next = None
            return c.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.h:
            c = self.h[key] # current node
            c.value = value
            if self.size > 1 and self.tail != c:
                if self.head == c:
                    self.head = c.next
                    self.head.prev = None
                else:
                    c.prev.next = c.next
                    c.next.prev = c.prev
                self.tail.next = c
                c.prev = self.tail
                self.tail = c
                c.next = None
        else:
            if self.size < self.cap:
                self.size += 1
                c = Node(key, value)
                self.h[key] = c
                if self.head == None:
                    self.head = c
                    self.tail = c
                else:
                    self.tail.next = c
                    c.prev = self.tail
                    self.tail = c
            else: # cache is full
                # To save memory allocation and release time, we remove the least-used node (head), use
                # the removed node as the new node. New (key, value) is assigned to this node, and this node
                # is moved to the tail of the doubly-linked list (latest).
                self.h.pop(self.head.key)
                c = self.head
                c.value = value
                c.key = key
                self.h[key] = c
                if self.size > 1:
                    self.head = c.next
                    self.head.prev = None
                    self.tail.next = c
                    c.prev = self.tail
                    self.tail = c
                    c.next = None

our_cache = LRU_Cache(5)

def test_func(d, e): # data retrieved
    print(d, end="  ")
    if d == e:  # e: expected result
        print("Pass")
    else:
        print("Fail")
    
our_cache.set(1, 3)
our_cache.set(1, 1)
our_cache.set(2, 2)

test_func(our_cache.get(1), 1)       # 1
test_func(our_cache.get(2), 2)       # 2
test_func(our_cache.get(3), -1)      # -1
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)
test_func(our_cache.get(1), -1)      # -1
test_func(our_cache.get(2), 2)       # 2
test_func(our_cache.get(3), 3)       # 3
test_func(our_cache.get(4), 4)       # 4
test_func(our_cache.get(5), 5)       # 5
test_func(our_cache.get(6), 6)       # 6
our_cache.set(2, 7)
our_cache.set(8, 8)
test_func(our_cache.get(3), -1)      # -1
test_func(our_cache.get(2), 7)       # 7
test_func(our_cache.get(6), 6)       # 6
test_func(our_cache.get(8), 8)       # 8
test_func(our_cache.get(5), 5)       # 5
test_func(our_cache.get(), -1)       # -1
our_cache.set(1, 9)
test_func(our_cache.get(4), -1)      # -1
test_func(our_cache.get(2), 7)       # 7
test_func(our_cache.get(6), 6)       # 6
test_func(our_cache.get(8), 8)       # 8
test_func(our_cache.get(1), 9)       # 9
test_func(our_cache.get(5), 5)       # 5

"""
Output:
1  Pass
2  Pass
-1  Pass
-1  Pass
2  Pass
3  Pass
4  Pass
5  Pass
6  Pass
-1  Pass
7  Pass
6  Pass
8  Pass
5  Pass
-1  Pass
-1  Pass
7  Pass
6  Pass
8  Pass
9  Pass
5  Pass

"""
