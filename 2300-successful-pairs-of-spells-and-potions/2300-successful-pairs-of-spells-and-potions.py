class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n = len(spells)
        m = len(potions)

        # Create an array of tuples (value, original index) for spells
        spells_with_indices = [(spells[i], i) for i in range(n)]

        # Sort spells based on values
        spells_with_indices.sort()

        # Sort potions
        potions.sort()

        result = [0] * n
        j = m - 1

        for i in range(n):
            spell_value, original_index = spells_with_indices[i]

            while j >= 0 and spell_value * potions[j] >= success:
                j -= 1

            result[original_index] = m - 1 - j

        return result
