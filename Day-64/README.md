**LeetCode : 786. K-th Smallest Prime Fraction**

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]
 

Constraints:

2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2
 

****

**GeeksForGeeks : Combination Sum II**

Given an array of integers arr, the length of the array n, and an integer k, find all the unique combinations in arr where the sum of the combination is equal to k. Each number can only be used once in a combination.
Return the combinations in the lexicographically sorted order, where each combination is in non-decreasing order.

Example 1:

Input: 
n = 5, k = 7
arr[] = { 1, 2, 3, 3, 5 }
Output:
{ { 1, 3, 3 }, { 2, 5 } }
Explanation:
1 + 3 + 3 = 7
2 + 5 = 7
Example 2:

Input:
n = 6, k = 30
arr[] = { 5, 10, 15, 20, 25, 30 }
Output:
{ { 5, 10, 15 }, { 5, 25 }, { 10, 20 }, { 30 } }
Explanation:
5 + 10 + 15 = 30
5 + 25 = 30
10 + 20 = 30
Your Task:
You don't need to read input or print anything. Your task is to complete the function CombinationSum2() which takes arr[],n, and k as input parameters and returns all the unique combinations.
 

Constraints:
1 <= n <= 100
1 <= arr[i] <= 50
1 <= k <= 30

let p = number of elements, at maximum, can sum up to the given value k.

Expected Time Complexity: O(2min(n,p))
Expected Auxiliary Space: O(n)

