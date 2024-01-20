from collections import deque

class RecentCounter(object):
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Remove requests older than 3000 milliseconds
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # Add the current request to the queue
        self.requests.append(t)

        # Return the number of requests within the time frame
        return len(self.requests)

# Example usage:
recentCounter = RecentCounter()
print(recentCounter.ping(1))     # Output: 1
print(recentCounter.ping(100))   # Output: 2
print(recentCounter.ping(3001))  # Output: 3
print(recentCounter.ping(3002))  # Output: 3
