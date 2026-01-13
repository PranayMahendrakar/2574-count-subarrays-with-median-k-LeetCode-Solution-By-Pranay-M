class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find position of k
        pos = nums.index(k)
        n = len(nums)
        
        # Transform: elements < k become -1, elements > k become +1, k becomes 0
        # A valid subarray has balance 0 or 1 (for odd/even length)
        
        # Count balances on the right side of k (inclusive)
        right_count = {0: 1}
        balance = 0
        for i in range(pos + 1, n):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1
            right_count[balance] = right_count.get(balance, 0) + 1
        
        # Count valid subarrays by iterating from k to the left
        result = right_count.get(0, 0) + right_count.get(1, 0)
        balance = 0
        for i in range(pos - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1
            # Need right balance such that total is 0 or 1
            result += right_count.get(-balance, 0) + right_count.get(1 - balance, 0)
        
        return result