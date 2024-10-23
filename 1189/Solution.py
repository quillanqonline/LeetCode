class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letterB = text.count("b")
        letterA = text.count("a")
        letterL = text.count("l") // 2
        letterO = text.count("o") // 2
        letterN = text.count("n")

        return max(0, min(letterB, letterA, letterL, letterO, letterN))