class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Initialize prefix and suffix product arrays
        prefix_products = [1] * n
        suffix_products = [1] * n
        result = [0] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix_product
            suffix_product *= nums[i]

        # Calculate the final result by multiplying prefix and suffix products
        for i in range(n):
            result[i] = prefix_products[i] * suffix_products[i]

        return result

# Example usage:
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1,1,0,-3,3]))  # Output: [0, 0, 9, 0, 0]
