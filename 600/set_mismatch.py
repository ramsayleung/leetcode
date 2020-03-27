'''
source: https://leetcode.com/problems/set-mismatch/
author: Ramsay Leung
date: 2020-03-08
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Note:

    The given array size will in the range [2, 10000].
    The given array's numbers won't have any order.
'''

# time comlexity: O(N): N is the length of nums
# space complexity: O(N): N is the length of nums
from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        originSeqence = [x for x in range(1, len(nums) + 1)]
        originCounter = Counter(originSeqence)
        mismatchCounter = Counter(nums)
        originCounter.subtract(mismatchCounter)
        result = []
        mostCommon = originCounter.most_common()
        result.append(mostCommon[-1][0])
        result.append(mostCommon[0][0])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([2, 2]))
