from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant_queue = deque()
        dire_queue = deque()
        n = len(senate)

        for i, party in enumerate(senate):
            if party == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while radiant_queue and dire_queue:
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()

            if radiant_index < dire_index:
                radiant_queue.append(radiant_index + n)
            else:
                dire_queue.append(dire_index + n)

        return "Radiant" if radiant_queue else "Dire"

# Example usage:
solution = Solution()
print(solution.predictPartyVictory("RD"))  # Output: "Radiant"
print(solution.predictPartyVictory("RDD"))  # Output: "Dire"

