class Solution:
    def dfs(self, i, j, text1, text2, cache):
        print(f"Entering dfs(i={i}, j={j})")

        if i >= len(text1) or j >= len(text2):
            print(f"  Base case at ({i}, {j}) → return 0")
            return 0

        if (i, j) in cache:
            print(f"  Cache hit at ({i}, {j}) → {cache[(i, j)]}")
            return cache[(i, j)]

        print(f"  Comparing '{text1[i]}' vs '{text2[j]}'")

        if text1[i] == text2[j]:
            print(f"  Match at ({i}, {j}) → move diagonally")
            res = 1 + self.dfs(i + 1, j + 1, text1, text2, cache)
        else:
            print(f"  No match at ({i}, {j}) → branching")
            res = max(
                self.dfs( i + 1, j, text1, text2, cache),
                self.dfs( i, j + 1, text1, text2, cache)
            )

        cache[(i, j)] = res
        print(f"  Returning from ({i}, {j}) → {res}")
        return res

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dfs(0, 0, text1, text2, {})