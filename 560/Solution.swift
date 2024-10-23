class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var remainingNumbers = [Int](nums)
        var numSequences = 0
        while !remainingNumbers.isEmpty {
            var sum = 0
            for number in remainingNumbers {
                sum += number
                if sum == k {
                    numSequences += 1
                }
            }
            remainingNumbers.removeFirst()
        }
        
        return numSequences
    }
}