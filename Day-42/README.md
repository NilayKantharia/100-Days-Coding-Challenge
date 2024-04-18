****LeetCode : 463. Island Perimeter****

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:![island](https://github.com/NilayKantharia/100-Days-Coding-Challenge/assets/125391394/f3155160-4849-48e0-8884-0793031daae0)

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.

************

************

**GeeksForGeeks : Two Repeated Elements**

You are given an integer n and an integer array arr of size n+2. All elements of the array are in the range from 1 to n. Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
Note: Return the numbers in their order of appearing twice. So, if X and Y are the repeating numbers, and X's second appearance comes before second appearance of Y, then the order should be (X, Y).

Example 1:

Input:
n = 4
arr[] = {1,2,1,3,4,3}
Output: 
1 3
Explanation: 
In the given array, 1 and 3 are repeated two times and as 1's second appearance occurs before 2's second appearance, so the output should be 1 3.
Example 2:

Input:
n = 2
arr[] = {1,2,2,1}
Output: 
2 1
Explanation: 
In the given array, 1 and 2 are repeated two times and second occurence of 2 comes before 1. So the output is 2 1.
Your Task:
The task is to complete the function repeatedElements() which takes an integer array arr[] and an integer n as inputs (the size of the array is n + 2 and elements are in the range [1, n]) and finds the two repeated elements in the array and return them in an array.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1). 

Constraints:
2 ≤ n ≤ 105
1 ≤ arr[i] ≤ n
