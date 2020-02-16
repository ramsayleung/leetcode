'''
source: https://leetcode.com/problems/valid-palindrome-ii/
author: Ramsay leung
date: 2020-02-16

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
   The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''


class Solution(object):
    def validPalindrome(self, s:str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        index = self.isPalindrome(s)
        chars = list(s)
        size = len(chars)
        if (index != -1):
            k = size - index
            firstS = chars[index:k - 1]
            if self.isPalindrome(firstS) == -1:
                return True
            lastS = chars[index + 1:k]
            return self.isPalindrome(lastS) == -1
        else:
            return True

    def isPalindrome(self, chars:list)->int:
        """
        :type chars:list<str>
        :rtype: int
        """
        size = len(chars)
        for i in range(int(size / 2) + 1):
            if chars[i] != chars[size - i - 1]:
                return i
        return -1