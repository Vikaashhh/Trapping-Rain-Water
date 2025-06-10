class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n <= 2:
            return 0  # Sirf 2 ya usse kam blocks honge toh pani trap nahi hoga

        left = 0
        right = n - 1
        left_max = 0  # Left side ka max height
        right_max = 0  # Right side ka max height
        water = 0  # Total trapped water

        while left < right:
            if arr[left] < arr[right]:
                # Left side choti hai, toh left se calculate karenge
                if arr[left] >= left_max:
                    left_max = arr[left]  # Update left max
                else:
                    water += left_max - arr[left]  # Pani trap hoga
                left += 1
            else:
                # Right side choti hai, toh right se calculate karenge
                if arr[right] >= right_max:
                    right_max = arr[right]  # Update right max
                else:
                    water += right_max - arr[right]  # Pani trap hoga
                right -= 1

        return water
