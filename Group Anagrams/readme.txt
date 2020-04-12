Problem: Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

Two words are anagrams if the count of characters are equal in them. First initialize a
dictionary, and for each word initialize a list with 26 0's (one for each letter in the
alphabet). Then for each letter, increment one in it's corresponding index(a=0, b=1, etc).
Use unicode values for that. Then  convert this list into a tuple and check whether it 
exists in the keys of the dictionary we declared. If it exists, add the word to the values
of that key, if not, create a new key value pair with the tuple as the key and the word as
the value. Finally add all the values into a single list and return
