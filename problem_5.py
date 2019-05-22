"""
Project 2: Show Me the Data Structures

problem 5. Blockchain

   A Blockchain is a sequential chain of records, similar to a linked list. 
   Each block contains a sha256 hash of the previous block, a timestamp,
   and transaction data.
   
   In class LinkedList (blockchain), self.tail is used to ensure append()
   takes O(1) time.
   
   self.num_blocks is used to ensure size() takes O(1) time.
   
   verify() can verify in a blockchain each block's previous_hash equals
   sha256 hash of data in the previous block. verify() takes O(n) time,
   where n is the number of blocks in the blockchain.
   
   Space: O(n), where n is the size of input data, including timestamp,
   data, and the number of blocks.
   
   For each block, datetime.utcnow() is used to get Greenwich Mean Time,
   or equivalently UTC.

"""
import hashlib
from datetime import datetime

def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(data)
        self.next = None
    
    def __repr__(self):
        return str(self.data) + "  " + str(self.timestamp)

# blockchain
class LinkedList:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.tail = None
        self.prev_hash = None
        self.num_blocks = 0

    def __str__(self):
        out_string = f"{self.name}: "
        c = self.head # current node
        if c == None:
            out_string += "<empty>"
            return out_string
        while c:
            if c == self.head:
                out_string += ("   " + str(c))
            else:
                out_string += ("\n     -> " + str(c))
            c = c.next
        return out_string

    def append(self, timestamp, data):
        # to append a block to this blockchain
        c = Block(timestamp, data, self.prev_hash) # current block
        self.prev_hash = c.hash
        if self.head is None:
            self.head = c
            self.tail = self.head
            self.num_blocks = 1
            return
        self.tail.next = c
        self.tail = c
        self.num_blocks += 1
    
    def verify(self):
        c = self.head # current block
        if c is None:
            return True
        while c != None:
            hash = calc_hash(c.data)
            if hash != c.hash:
                return False
            if c != self.head:
                if c.previous_hash != prev_hash:
                    return False
            c = c.next
            prev_hash = hash
        
        return True
    
    def size(self):
        return self.num_blocks

# Test

bc1 = LinkedList("bc1")  # blockchain 1
bc2 = LinkedList("bc2")  # blockchain 2
bc3 = LinkedList("bc3")  # blockchain 3

t1 = datetime.utcnow()
bc1.append(t1, "foo1")
print(bc1)

t2 = datetime.utcnow()
bc2.append(t2, "bar1")
print(bc2)

t3 = datetime.utcnow()
bc1.append(t3, "foo2")
print(bc1)

t4 = datetime.utcnow()
bc1.append(t4, "foo3")
print(bc1)

t5 = datetime.utcnow()
bc1.append(t5, "foo4")
print(bc1)

t6 = datetime.utcnow()
bc1.append(t6, "foo5")
print(bc1)

t7 = datetime.utcnow()
bc2.append(t7, "bar2")
print(bc2)

t8 = datetime.utcnow()
bc1.append(t8, "foo6")
print(bc1)

print(bc3)

def test_func(a, b):
    if a == b:
        print(f"{a}  Pass")
    else:
        print("Fail")

print("\nto check size of blockchain:")
test_func(bc1.size(), 6)
test_func(bc2.size(), 2)
test_func(bc3.size(), 0)

print("\nto verify in a blockchain each block's previous_hash equals sha256 hash of data in the previous block:")
test_func(bc1.verify(), True)
test_func(bc2.verify(), True)
test_func(bc3.verify(), True)

"""
Output:

bc1:    foo1  2019-05-21 21:10:02.593125
bc2:    bar1  2019-05-21 21:10:02.593653
bc1:    foo1  2019-05-21 21:10:02.593125
     -> foo2  2019-05-21 21:10:02.594290
bc1:    foo1  2019-05-21 21:10:02.593125
     -> foo2  2019-05-21 21:10:02.594290
     -> foo3  2019-05-21 21:10:02.594677
bc1:    foo1  2019-05-21 21:10:02.593125
     -> foo2  2019-05-21 21:10:02.594290
     -> foo3  2019-05-21 21:10:02.594677
     -> foo4  2019-05-21 21:10:02.594934
bc1:    foo1  2019-05-21 21:10:02.593125
     -> foo2  2019-05-21 21:10:02.594290
     -> foo3  2019-05-21 21:10:02.594677
     -> foo4  2019-05-21 21:10:02.594934
     -> foo5  2019-05-21 21:10:02.595153
bc2:    bar1  2019-05-21 21:10:02.593653
     -> bar2  2019-05-21 21:10:02.595445
bc1:    foo1  2019-05-21 21:10:02.593125
     -> foo2  2019-05-21 21:10:02.594290
     -> foo3  2019-05-21 21:10:02.594677
     -> foo4  2019-05-21 21:10:02.594934
     -> foo5  2019-05-21 21:10:02.595153
     -> foo6  2019-05-21 21:10:02.595668
bc3: <empty>

to check size of blockchain:
6  Pass
2  Pass
0  Pass

to verify in a blockchain each block's previous_hash equals sha256 hash of data in the previous block:
True  Pass
True  Pass
True  Pass

"""