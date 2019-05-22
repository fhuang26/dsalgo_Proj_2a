Seven required items are fixed as follows.

### (1) problem_1.py LRU Cache
issue: our_cache.get(), a blank value, was not covered in test cases.

In problem_1.py, this is added.

### (2) problem_2.py File Recursion
issue: More test cases are expected (previously 1 test case).

In problem_2.py, 5 test cases are made, including some paths as blank or empty string,
as suggested by the reviewer.

### (3) problem_4.py Active Directory
issue: user or group as None or blank are not covered in test cases.

In problem_4.py, these are added.

### (4) README Problem 2. File Recursion
issue: Time: O(n) does not seem to be correct, where n is the number of files,
       including directories.

The following is modified in README.

* Time: O(nk), where n is the number of files including directories under the input
path, and k is the max length of paths including the number of '/'s (delimiters).

### (5) README Problem 3. Huffman Coding
issue: 1. You have a recursion element in create_code() function. How does
that affect your complexities (time and space)?

The following are added to README.

* create_code() in encoding takes O(K) time and O(K) space since it traverses
Huffman tree once and creates a hashmap of size K, where K is the number of
different chars in input data (also number of leaves in the tree).

* create_code() in decoding takes O(K) time and O(K) space since it traverses
Huffman tree once and creates a hashmap of size K, where K is the number of
different chars in original input data (also number of leaves in the tree).


### (6) README Problem 3. Huffman Coding
issue: 2. In decoding,
          while k < n:
              for j in range(maxLen,minLen-1,-1):
What do you think would be the complexity based on the above?

The following are modified in README.

* In decoding, maxLen - minLen <= tree depth = O(K), where K is the number of
different chars in original input data (also number of leaves in the tree).

* huffman_decoding(encoded_data, tree) takes time O(N*K), where N is size of the
encoded data and K is the number of different chars in the original input data
(also the number of leaves in Huffman tree).


### (7) README Problem 4. Active Directory
issue: previous time and space analysis does not seem to be correct.

The following are modified in README.

is_user_in_group(user, group) checks whether a user is in the group.
   
In this group structure, from input group g1, there can be multiple paths to
go to another group g3. For example g1 -> g2 -> g3 and g1 -> g4 -> g3. So
this can be a dense group graph like a complete graph.
   
* We do BFS (breath-first search) with a visited set to visit each group once.
   
* Time: O(N*(M + N)), where M is the number of users and N is the number of groups.
                For worst case, most users may be in all groups, g3.get_groups()
                returns a list of neighbor groups of group g3, the graph of groups is
                dense, and it traverses each group once.
   
* Space: O(M + N), where M is the number of users and N is the number of groups.
                For worst case, most users may be in all groups, g3.get_groups()
                returns a list of neighbor groups of group g3, the graph of groups is
                dense, and it traverses each group once. As BFS goes on in the while
                loop, one copy of ul (user list, max length M) and gpList (group list,
                max length N) exist in memory. The length of gp_queue is O(N).
                The size of visited set is O(N). These lead to space O(M + N).


### (8) README Problem 5. Blockchain
issue: Space analysis was missing for Problem 5 in version 1.

The following is added to README.
* Space: O(n), where n is the size of input data, including timestamp,
   data, and the number of blocks.

