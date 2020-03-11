"""
source: https://leetcode.com/problems/design-search-autocomplete-system/
author: Ramsay Leung
date: 2020-03-10
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

    1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
    2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
    3. If less than 3 hot sentences exist, then just return as many as you can.
    4. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.
 

Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
 

Note:

    1. The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
    2. The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
    3. Please use double-quote instead of single-quote when you write test cases even for a character input.
    4. Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
from typing import Dict, List


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # How many times this character appeared in the addition process
        self.value = None

    def add(self, word: str, value: object) -> None:
        """
        Adding a word in the trie structure
        """
        node = self
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.value = value

    def findAllByPrefix(self, prefix: str) -> Dict:
        """
        Check and return related suffix, value, it not found, return empty dict
        """
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        node = self
        result = {}
        for i, char in enumerate(prefix):
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return result
        if node.value:
            result[prefix] = node.value
        return self.findSuffix(node, prefix, result)

    def findSuffix(self, node, prefix: str, result: Dict):
        for child in node.children:
            self.findSuffix(child, prefix + child.char, result)
        if node.value:
            result[prefix] = node.value
        return result


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = TrieNode('*')
        for word, time in zip(sentences, times):
            self.trie.add(word, time)
        self.data = ""

    def input(self, c: str) -> List[str]:
        allSequenceTimes = {}
        if c == '#':
            allSequenceTimes = self.trie.findAllByPrefix(self.data)
            value = 1
            if self.data in allSequenceTimes:
                value += allSequenceTimes[self.data]
            self.trie.add(self.data, value)
            self.data = ""
            return []
        else:
            self.data += c
            allSequenceTimes = self.trie.findAllByPrefix(self.data)
        allSequenceTimes = [(k, v) for k, v in allSequenceTimes.items()]
        result = [
            i[0]
            for i in sorted(allSequenceTimes, key=lambda x: (-x[1], x[0]))
        ]
        return result[:3]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)