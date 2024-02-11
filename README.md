# Software Testing
# Name: Mr.Peeranat Pathomkul Student ID: 6610110214
## Description
-This project about testing code from hackerrank 

## Setup
Read and follow this section first time

#### first assignment test funny string
-In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. . Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.

##### Input Format
The first line contains an integer q, the number of queries.
The next q lines each contain a string, s.

```console
tree
.
├── software_testing
│   ├── funny_string
    │   └── funny_string.py
    └── tester_funny
        └── tester_funny.py

```
###### Run Test with Code
``` Copy the code
python -m unittest -v software_testing\tester_funny\tester_funny.py
```

#### second assignment test Alternating Characters
-You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

##### Input Format
The first line contains an integer q, the number of queries.
The next q lines each contain a string s to analyze.

```console
tree
.
├── software_testing1
│   ├── alter_test
    │   └── alter_test.py
    └── alternating
        └── alternating.py

```
###### Run Test with Code
``` Copy the code
python -m unittest -v software_testing1\alter_test\alter_test.py
```

#### Third assignment Caesar Cipher
-Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

##### Input Format
The first line contains the integer,n , the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.

```console
tree
.
├── software_testing2
│   ├── caesar_Cipher
    │   └── caesar_Cipher.py
    └── caesar_test
        └── caesar_test.py

```
###### Run Test with Code
``` Copy the code
python -m unittest -v software_testing2\caesar_test\caesar_test.py
```

#### fourth assignment Two Characters
-Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.

##### Input Format
The first line contains a single integer that denotes the length of s.
The second line contains string s.

```console
tree
.
├── software_testing3
│   ├── tChar_test
    │   └── tChar_test.py
    └── two_Char
        └── two_Char.py

```
###### Run Test with Code
``` Copy the code
python -m unittest -v software_testing3\tChar_test\tChar_test.py
```

#### fifth assignment Grid Challenge
-Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

##### Input Format
The first line contains t, the number of testcases.

Each of the next t sets of lines are described as follows:
- The first line contains n, the number of rows and columns in the grid.
- The next n lines contains a string of length n


```console
tree
.
├── software_testing4
│   ├── grid_char
    │   └── grid_char.py
    └── gridcha_test
        └── gridcha_test.py

```
###### Run Test with Code
``` Copy the code
python -m unittest -v software_testing4\gridcha_test\gridcha_test.py
```
