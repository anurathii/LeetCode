class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        
        nemo = {}

        def solve(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1.0
            elif b <= 0:
                return 0.0

            if (a, b) in nemo:
                return nemo[(a,b)]
            
            nemo[(a,b)] = 0.25 * (solve(a - 100, b) + solve(a - 75, b - 25) + solve(a - 50, b - 50) + solve(a - 25, b - 75))

            return nemo[(a, b)]

        return solve(n, n)