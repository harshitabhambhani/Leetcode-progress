from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the frequency of each character
        counts = Counter(s)
        
        # Sort the characters based on their frequency in decreasing order
        sorted_chars = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        
        # Construct the sorted string
        sorted_str = ''.join(char * counts[char] for char in sorted_chars)
        
        return sorted_str

        