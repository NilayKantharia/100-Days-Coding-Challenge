class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [0]*n
        q = deque(range(n))


        for i in deck:
            j = q.popleft()
            res[j] = i
            if q:
                q.append(q.popleft())
        return res
            
