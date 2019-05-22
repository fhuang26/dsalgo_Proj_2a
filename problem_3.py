"""
Project 2: Show Me the Data Structures

problem 3. Huffman Code

The Huffman algorithm works by assigning codes that correspond to the relative
frequency of each character for each character. The Huffman code can be of any
length and does not require a prefix; therefore, this binary code can be visualized
on a binary tree with each encoded character being stored on leafs.

huffman_encoding(data) calculates frequencies of chars in input data, builds
Huffman tree, and creates encoded data. It returns: (encoded_data, tree).

During Huffman tree construction, we need to find two nodes with smallest frequencies
and build a parent node for them. PriorityQueue is used since there may be duplicate
frequencies and we want smallest two. In Python, usual dictionary {} and set are
unordered. OrderedDict in collections remembers the order in which its contents are
added, keeping unique keys, and it is not appropriate either to construct Huffman tree.

Each put() in PriorityQueue takes O(K) time, and get() from top takes O(K) to
restore heap properties, where K is the number of different chars in input data.
Construction of Huffman tree takes O(K logK) time.

create_code() in encoding takes O(K) time and O(K) space since it traverses
Huffman tree once and creates a hashmap of size K, where K is the number of
different chars in input data (also number of leaves in the tree).

Overall, huffman_encoding(data) takes O(N + (K logK)) time, where N is size of input
data and K is the number of different chars in input data.
Space: O(K), where K is the number of different chars in input data.

huffman_decoding(encoded_data, tree) traverses Huffman tree to create a hashmap
which maps Huffman code to char. Then it scans input encoded data and matches
Huffman code to produce output string. It outputs the original data.

create_code() in decoding takes O(K) time and O(K) space since it traverses
Huffman tree once and creates a hashmap of size K, where K is the number of
different chars in input data (also number of leaves in the tree).

In decoding, maxLen - minLen <= tree depth = O(K), where K is the number of
different chars in input data (also number of leaves in the tree).

huffman_decoding(encoded_data, tree) takes time O(N*K), where N is size of the
encoded data and K is the number of different chars in the original data (also
the number of leaves in Huffman tree).

huffman_decoding(encoded_data, tree) takes space O(K), where K is the number of
different chars in the original data (also the number of leaves in Huffman tree).

"""
import sys
import queue as Q

class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.code = None
        self.left = None
        self.right = None

def create_code(n, code, code_h, kind):
    # n: node  code: Huffman code from parent
    # code_h: code hashmap
    # kind: 0: code_h[ch]=code  1:code_h[code]=ch
    if n == None:
        return
    n.code = code
    if n.left == None and n.right == None:
        if kind == 0: # huffman_encoding
            code_h[n.ch] = code
        else:         # hufman_decoding
            code_h[code] = n.ch
        return
    create_code(n.left,  code + "0", code_h, kind)
    create_code(n.right, code + "1", code_h, kind)

def huffman_encoding(data):
    """
    This calculates frequencies of chars in input data, builds Huffman tree, and
    creates encoded data.
    Returns: (encoded_data, tree)
    """
    if data == None:
        return (None, None)
    if data == "":
        return ("", None)
    h = {}
    for ch in data:
        if ch in h:
            h[ch] = h[ch] + 1
        else:
            h[ch] = 1
    
    p = Q.PriorityQueue()
    node_h = {}
    node_idx = 0
    for ch in h:
        freq = h[ch]
        c = Node(ch, freq) # current node
        node_h[node_idx] = c
        p.put((freq, node_idx))
        node_idx += 1
    
    while (not p.empty()) and (p.qsize() >= 2):
        t1 = p.get()
        t2 = p.get()
        freq = t1[0] + t2[0]
        c = Node(None, freq)
        c.left = node_h[t1[1]]
        c.right = node_h[t2[1]]
        node_h[node_idx] = c
        p.put((freq, node_idx))
        node_idx += 1
    t3 = p.get()
    tree = node_h[t3[1]]
    
    code_h = {} # key: char  value: Huffman code
    create_code(tree, "", code_h, 0)
    
    result = ""
    for ch in data:
        code = code_h[ch]
        result = result + code
    return (result, tree)

def huffman_decoding(encoded_data, tree):
    """
    This traverses Huffman tree to create a hashmap which maps Huffman code to char.
    Then it scans input encoded data and matches Huffman code to produce output string.
    Returns: original data
    """
    if tree == None:
        return encoded_data
    code_ch = {} # key: Huffman code  value: char
    create_code(tree, "", code_ch, 1)
    maxLen = 0
    minLen = 100000000
    for code in code_ch:
        codeLen = len(code)
        if maxLen < codeLen:
            maxLen = codeLen
        if minLen > codeLen:
            minLen = codeLen
    k = 0
    n = len(encoded_data)
    result = ""
    s = encoded_data
    while k < n:
        for j in range(maxLen,minLen-1,-1):
            code = s[k:k+j]
            if code in code_ch:
                ch = code_ch[code]
                #print(f"k={k}  code={code}  ch={ch}")
                result = result + ch
                k = k + j
                break
    return result

def test_func(a_great_sentence):
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    if len(encoded_data) == 0:
        print ("The size of the encoded data is: 0\n")
    else:
        print ("The size of the encoded data is:  {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)
    
    if len(decoded_data) == 0:
        print ("The size of the decoded data is: 0\n")
    else:
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    # Test case 1
    print("Test case 1:\n")
    a_great_sentence = "The bird is the word"
    test_func(a_great_sentence)

    # Test case 2
    print("-------------------------------------------------------\n\nTest case 2:\n")
    a_great_sentence = "A Huffman code is a type of optimal prefix code that is used for compressing data"
    test_func(a_great_sentence)

    # Test case 3
    print("-------------------------------------------------------\n\nTest case 3:\n")
    a_great_sentence = "The Huffman encoding and decoding schema is also lossless , meaning that when compressing the data to make it smaller , there is no loss of information"
    test_func(a_great_sentence)

    # Test case 4
    print("-------------------------------------------------------\n\nTest case 4:\n")
    a_great_sentence = ""
    test_func(a_great_sentence)
"""
Output:

Test case 1:

The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is:  36

The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word

---------------------------------------------------------------

Test case 2:

The size of the data is: 130

The content of the data is: A Huffman code is a type of optimal prefix code that is used for compressing data

The size of the encoded data is:  68

The content of the encoded data is: 0100100001001111101101100110110101010010000011011101111110110000011110000010100010010101001111111000010110110001011111111001011111010101001010100111111110011000110011101011000110111011111101100001001010111101010010001111000001110111000110011110000110101111100001101110111101011111111001100100010000111010001110100011110101010011010

The size of the decoded data is: 130

The content of the encoded data is: A Huffman code is a type of optimal prefix code that is used for compressing data

--------------------------------------------------------------

Test case 3:

The size of the data is: 200

The content of the data is: The Huffman encoding and decoding schema is also lossless , meaning that when compressing the data to make it smaller , there is no loss of information

The size of the encoded data is:  108

The content of the encoded data is: 01110101011111011110111011011110001010010100011100111001111101110001011101010110100011000110011110011100101101111011011010101110101011010001100011001110000101110111110100111001111100000011110010010000101011100101010000000001011010000001110111001110011110110011100100011000110011101001011110010100111011110110111110111001110101110100011011111001101110100000010001100011001110100101111101111101101001010010011110100101011100111001011111111011111000010011100000111001001000101101011011110111001110100101111101011011101111100000011111001010111001010100000001111010010101111000110001010101001101001110010100100010101100

The size of the decoded data is: 200

The content of the encoded data is: The Huffman encoding and decoding schema is also lossless , meaning that when compressing the data to make it smaller , there is no loss of information

"""