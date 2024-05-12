class Solution:
    def recurse(self, step, taken, d):
        if taken + step >= d and abs(taken + step - d) % 2 == 0:
            return step
        return self.recurse(step + 1, taken + step, d)
        
    def minSteps(self, d):
        d = abs(d)
        return self.recurse(1, 0, d)
