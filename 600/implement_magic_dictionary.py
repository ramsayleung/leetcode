'''
source: https://leetcode.com/problems/implement-magic-dictionary/
author: Ramsay Leung
date: 2020-02-22

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

Note:

    1. You may assume that all the inputs are consist of lowercase letters a-z.
    2. For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
    3. Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
'''
from typing import List


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.data = dict

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for element in self.data:
            if self.isOneCharDifferent(word, element):
                return True
        return False

    def isOneCharDifferent(self, word: str, source: str) -> bool:
        if len(word) != len(source):
            return False
        differenceCounter = 0
        for index, element in enumerate(source):
            if element != word[index]:
                differenceCounter += 1
                if differenceCounter > 1:
                    return False
        return differenceCounter == 1


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)