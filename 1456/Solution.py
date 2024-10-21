class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowelCount = 0
        for startingIndex in range(len(s) - k + 1):
            substring = s[startingIndex:startingIndex + k]
            substringVowelCount = self.countVowelsInString(substring)
            if substringVowelCount > maxVowelCount:
                maxVowelCount = substringVowelCount

        return maxVowelCount
    

    def countVowelsInString(self, string: str) -> int:
        stringLength = len(string)
        stringWithoutVowels = string.translate({ ord(i): None for i in 'aeiou'})

        return stringLength - len(stringWithoutVowels)
    