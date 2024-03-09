**LeetCode**
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.

************
**GeeksForGeeks**
Given a binary string s. Perform r iterations on string s, where in each iteration 0 becomes 01 and 1 becomes 10. Find the nth character (considering 0 based indexing) of the string after performing these r iterations (see examples for better understanding).

Example 1:

Input:
s = "1100"
r = 2
n = 3
Output:
1
Explanation: 
After 1st iteration s becomes "10100101".
After 2nd iteration s becomes "1001100101100110".
Now, we can clearly see that the character at 3rd index is 1, and so the output.
Example 2:

Input:
s = "1010"
r = 1
n = 2
Output:
0
Explanation : 
After 1st iteration s becomes "10011001".
Now, we can clearly see that the character at 2nd index is 0, and so the output.
Your task:
You don't need to read input or print anything. Your task is to complete the function nthCharacter() which takes the string s and integers r and n as input parameters and returns the n-th character of the string after performing r operations on s.
 
Expected Time Complexity: O(r*|s|)
Expected Auxilary Space: O(|s|)
 
Constraints:
1 ≤ |s| ≤ 103
1 ≤ r ≤ 20
0 ≤ n < |s|
