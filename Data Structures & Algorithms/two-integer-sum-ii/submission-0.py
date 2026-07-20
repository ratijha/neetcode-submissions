class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right = right -1 
            elif sum < target:
                left = left + 1

# if the array is unsorted 
def twoSumUnsorted(numbers, target):
    # Map to store: key = number_needed, value = its_0_indexed_position
    seen = {}
    
    for i, num in enumerate(numbers):
        complement = target - num
        
        if complement in seen:
            # Found the pair! Convert to 1-indexed before returning
            return [seen[complement] + 1, i + 1]
        
        # Store current number's index
        seen[num] = i
