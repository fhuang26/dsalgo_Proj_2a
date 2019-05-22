### Problem 1. LRU Cache
The lookup operation (i.e., get()) and put()/set() is supposed to be fast
for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is
known as a cache hit. If, however, the entry is not found, it is known as
a cache miss. set(key, value) will move current node to the latest (tail).

A hashmap (key: data, value: Node) and doubly-linked list are used to do
LRU cache. Each get() and set() takes O(1) time.

* get() and set() may move a node in the middle of a list to the latest, tail.
Doubly-linked list is used to support this so that we can move a node in the
list to the tail in O(1) time.

* Node needs to keep the input key since when the least-used node is removed
from head of the list, we need to remove the corresponding key in hash table
as well.

* To save memory allocation and release time, we remove the least-used node
(head), use the removed node as the new node. New (key, value) is assigned
to this node, and this node is moved to the tail of the list (latest).

* Time: get(): O(1)   set(): O(1)

* Space: O(K), where K is the capacity of this LRU cache.

### Problem 2. File Recursion

For this problem, the goal is to write code for finding all files under a directory
(and all directories beneath it) that end with ".c"

It recursively goes down to traverse the file hierarchy and find files ending with
".c".

* Time: O(nk), where n is the number of files including directories under the input
path, and k is the max length of paths including the number of '/'s (delimiters).

* Space: O(n) for possible intermediate lists and output length

### Problem 3. Huffman Coding
The Huffman algorithm works by assigning codes that correspond to the relative
frequency of each character for each character. The Huffman code can be of any
length and does not require a prefix; therefore, this binary code can be visualized
on a binary tree with each encoded character being stored on leafs.
* huffman_encoding(data) calculates frequencies of chars in input data, builds
Huffman tree, and creates encoded data. It returns: (encoded_data, tree).

* During Huffman tree construction, we need to find two nodes with smallest frequencies
and build a parent node for them. PriorityQueue is used since there may be duplicate
frequencies and we want smallest two. In Python, usual dictionary {} and set are
unordered. OrderedDict in collections remembers the order in which its contents are
added, keeping unique keys, and it is not appropriate either to construct Huffman tree.

* Each put() in PriorityQueue takes O(K) time, and get() from top takes O(K) to
restore heap properties, where K is the number of different chars in input data.
Construction of Huffman tree takes O(K logK) time.

* create_code() in encoding takes O(K) time and O(K) space since it traverses
Huffman tree once and creates a hashmap of size K, where K is the number of
different chars in input data (also number of leaves in the tree).

* Overall, huffman_encoding(data) takes O(N + (K logK)) time, where N is size of input
data and K is the number of different chars in input data.
* huffman_encoding(data) takes space O(K), where K is the number of different chars in
input data.

* huffman_decoding(encoded_data, tree) traverses Huffman tree to create a hashmap
which maps Huffman code to char. Then it scans input encoded data and matches
Huffman code to produce output string. It outputs the original data.

* create_code() in decoding takes O(K) time and O(K) space since it traverses
Huffman tree once and creates a hashmap of size K, where K is the number of
different chars in original input data (also number of leaves in the tree).

* In decoding, maxLen - minLen <= tree depth = O(K), where K is the number of
different chars in original input data (also number of leaves in the tree).

* huffman_decoding(encoded_data, tree) takes time O(N*K), where N is size of the
encoded data and K is the number of different chars in the original input data
(also the number of leaves in Huffman tree).

* huffman_decoding(encoded_data, tree) takes space O(K), where K is the number
of different chars in the original data (also the number of leaves in Huffman tree).

### Problem 4. Active Directory

is_user_in_group(user, group) checks whether a user is in the group.
   
In this group structure, from input group g1, there can be multiple paths to
go to another group g3. For example g1 -> g2 -> g3 and g1 -> g4 -> g3. So
this can be a dense group graph like a complete graph.
   
* We do BFS (breath-first search) with a visited set to visit each group once.
   
* Time: O(N*(M + N)), where M is the number of users and N is the number of groups.
                For worst case, most users may be in all groups, g2.get_groups()
                returns a list of neighbor groups of group g2, the graph of groups is
                dense, and it traverses each group once.
   
* Space: O(M + N), where M is the number of users and N is the number of groups.
                For worst case, most users may be in all groups, g2.get_groups()
                returns a list of neighbor groups of group g2, the graph of groups is
                dense, and it traverses each group once. As BFS goes on in the while
                loop, one copy of ul (user list, max length M) and gpList (group list,
                max length N) exist in memory. The length of gp_queue is O(N).
                The size of visited set is O(N). These lead to space O(M + N).

### Problem 5. Blockchain

   A Blockchain is a sequential chain of records, similar to a linked list. 
   Each block contains a sha256 hash of the previous block, a timestamp,
   and transaction data.
   
   * In class LinkedList (blockchain), self.tail is used to ensure append()
   takes O(1) time.
   
   * self.num_blocks is used to ensure size() takes O(1) time.
   
   * verify() can verify in a blockchain each block's previous_hash equals
   sha256 hash of data in the previous block. verify() takes O(n) time,
   where n is the number of blocks in the blockchain.
   
   * Space: O(n), where n is the size of input data, including timestamp,
   data, and the number of blocks.
   
   * For each block, datetime.utcnow() is used to get Greenwich Mean Time,
   or equivalently UTC.
   
### Problem 6. Union and Intersection

This takes in two linked lists and return a linked list that is composed of either
the union or intersection, respectively.

5 test cases are made, including one or two empty linked lists.

* Since self.tail is added to class LinkedList and each append() in LinkedList takes
O(1) time, it take O(n) time to create two input linked lists, where n is the
input size.

* It takes O(n) time convert two input linked lists to set in Python.
* Union and intersection of two sets in Python take O(n) time, roughly going through
two sets once and using hash table.
* It takes O(n) time to output the results of union and intersection.

* All together, it takes O(n) time.

* Space: O(n) for set, where n is the input size.
