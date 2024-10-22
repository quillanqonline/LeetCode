class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        remainingList = nums
        output = []
        while remainingList:
            if len(remainingList) >= 2:
                frequency = remainingList[0]
                value = remainingList[1]
                remainingList = remainingList[2:]
                
                for i in range(frequency):
                    output.append(value)
        
        return output