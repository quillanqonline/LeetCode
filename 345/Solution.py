class Solution:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    def reverseVowels(self, s: str) -> str:
        stringVowels = []
        
        for character in s:
            if self.vowels.__contains__(character):
                stringVowels.append(character)

        output = ""
        for character in s:
            if self.vowels.__contains__(character):
                output += stringVowels.pop()
            else:
                output += character

        return output