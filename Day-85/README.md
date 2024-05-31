**LeetCode : 260. Single Number III**

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.

****

**GeeksForGeeks : Swap two nibbles in a byte**

Given a number n, Your task is to swap the two nibbles and find the resulting number. 

A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte. For example, the decimal number 150 is represented as 10010110 in an 8-bit byte. This byte can be divided into two nibbles: 1001 and 0110.

Example 1:

Input: n = 100
Output: 70
Explanation: 100 in binary is 01100100, two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.
Example 2:

Input: n = 129
Output: 24
Explanation: 129 in binary is 10000001, two nibbles are (1000) and (0001). If we swap the two nibbles, we get 00011000 which is 24 in decimal.
Your Task:
You don't need to read input or print anything. Your task is to complete the function swapNibbles() which takes an integer n as input parameter and returns an integer after swapping nibbles in the binary representation of n.

Expected Time Complexity: O(1)
Expected Space Complexity: O(1)

Constraints:
0 ≤ n ≤ 255
