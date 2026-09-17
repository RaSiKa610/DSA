class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        # min_lens[i] will store the minimum length of a valid subarray ending at or before i
        min_lens = [float('inf')] * n
        best_so_far = float('inf')
        ans = float('inf')
        
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            # If we found a subarray that matches the target
            if current_sum == target:
                curr_len = right - left + 1
                
                # If there's a valid non-overlapping subarray before this one, evaluate the total length
                if left > 0 and min_lens[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_lens[left - 1])
                
                # Update the best (shortest) length seen so far
                best_so_far = min(best_so_far, curr_len)
            
            # Store the shortest length found up to the current index
            min_lens[right] = best_so_far
            
        return ans if ans != float('inf') else -1
