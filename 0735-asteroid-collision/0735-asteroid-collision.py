class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # Collisions happen, compare sizes
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:
                # No collision, add the asteroid to the stack
                stack.append(asteroid)

        return stack

# Example usage:
solution = Solution()
print(solution.asteroidCollision([5, 10, -5]))  # Output: [5, 10]
print(solution.asteroidCollision([8, -8]))  # Output: []
print(solution.asteroidCollision([10, 2, -5]))  # Output: [10]

        