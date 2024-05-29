**LeetCode : 1404. Number of Steps to Reduce a Number in Binary Representation to One**

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  
Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  
Example 3:

Input: s = "1"
Output: 0
 

Constraints:

1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'


****


**GeeksForGeeks : Geek and its Game of Coins**

Given three numbers n, x, and y, Geek and his friend are playing a coin game. In the beginning, there are n coins. In each move, a player can pick x, y, or 1 coin. Geek always starts the game. The player who picks the last coin wins the game. The task is to determine whether Geek will win the game or not if both players play optimally.

Example 1:

Input: 
n = 5
x = 3
y = 4
Output: 
1
Explanation:
There are 5 coins, every player can pick 1 or 3 or 4 coins on his/her turn. Geek can win by picking 3 coins in first chance. Now 2 coins will be left so his friend will pick one coin and now Geek can win by picking the last coin.
Example 2:
Input:
n = 2
x = 3
y = 4
Output:
0
Explanation: 
Geek picks 1 coin and then his friend picks 1 coin.
Your Task: 
You don't need to read input or print anything. Complete the function findWinner() which takes n, x, and y as input parameters and returns 1 if Geek can win otherwise 0.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
 
Constraints:
1 ≤ n, x, y ≤ 105
