class StockSpanner(object):
    def __init__(self):
        self.prices = []  # List to store the prices
        self.spans = []   # List to store the spans

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1  # Initialize span to 1
        while self.prices and price >= self.prices[-1]:
            # Pop elements from the stack while the current price is greater than or equal to the last element
            span += self.spans.pop()
            self.prices.pop()

        # Append the current price and its corresponding span to the stack
        self.prices.append(price)
        self.spans.append(span)

        return span

# Example usage:
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # Output: 1
print(stockSpanner.next(80))   # Output: 1
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(70))   # Output: 2
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(75))   # Output: 4
print(stockSpanner.next(85))   # Output: 6
