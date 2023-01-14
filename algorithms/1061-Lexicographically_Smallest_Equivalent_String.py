# Objective: Given a base string, replace every letter with lexicographically
# smallest applicable character based on the key provided in the first two strings.

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # UnionFind

        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            while x != parent[x]:
                x = parent[x]
            return x
        
        def union(a, b):
            ra = find(a)
            rb = find(b)
            parent[ra] = parent[rb] = min(ra, rb)

        # Call union function
        for c1,c2 in zip(s1, s2):
            union(c1,c2)

        # Build up final string
        result = []
        for c in baseStr:
            result.append( parent[find(c)] )
        return ''.join(result)
