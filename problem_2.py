"""
Project 2: Show Me the Data Structures

problem 2. File Recursion
For this problem, the goal is to write code for finding all files under a directory
(and all directories beneath it) that end with ".c"

It recursively goes down to traverse the file hierarchy and find files ending with
".c".

Time: O(nk), where n is the number of files, including directories, under the input
path, and k is the max length of paths including the number of '/'s (delimiters).

Space: O(n) for possible intermediate lists and output length

"""

import os

def find_files(suffix="", path="."):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    fl = []
    if not os.path.isdir(path):
        if os.path.isfile(path):
            if path.endswith(suffix):
                return fl.append(path)
        return fl
    
    for fn in os.listdir(path):
        p2 = os.path.join(path, fn)
        if os.path.isfile(p2):
            if p2.endswith(suffix):
                fl.append(p2)
        elif os.path.isdir(p2):
            fl.extend(find_files(suffix, p2))
    
    return fl

def test_func(fla, flb):
    print(fla, end="  ")
    if fla == flb:
        print("Pass")
    else:
        print("Fail")

test_func(find_files(".c","./testdir"),
         ['./testdir\\subdir1\\a.c','./testdir\\subdir3\\subsubdir1\\b.c','./testdir\\subdir5\\a.c',
          './testdir\\t1.c'])
test_func(find_files(".h","./testdir"),
         ['./testdir\\subdir1\\a.h','./testdir\\subdir3\\subsubdir1\\b.h','./testdir\\subdir5\\a.h',
          './testdir\\t1.h'])
test_func(find_files(".c"),
         ['.\\testdir\\subdir1\\a.c','.\\testdir\\subdir3\\subsubdir1\\b.c',
          '.\\testdir\\subdir5\\a.c',
          '.\\testdir\\t1.c'])
test_func(find_files("","./testdir"),
          ['./testdir\\subdir1\\a.c','./testdir\\subdir1\\a.h','./testdir\\subdir2\\.gitkeep',
           './testdir\\subdir3\\subsubdir1\\b.c','./testdir\\subdir3\\subsubdir1\\b.h',
           './testdir\\subdir4\\.gitkeep',
           './testdir\\subdir5\\a.c','./testdir\\subdir5\\a.h',
           './testdir\\t1.c','./testdir\\t1.h'])
test_func(find_files(".c",""),
          [])
