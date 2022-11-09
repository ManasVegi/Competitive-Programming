class StockSpanner:

    def __init__(self):
        self.spans = []
        self.prices = []

    def next(self, price: int) -> int:
        self.spans.append(1)
        self.prices.append(price)
        prev = len(self.prices) - 2
        while prev >= 0 and price >= self.prices[prev]:
            self.spans[-1] += self.spans[prev]
            prev -= self.spans[prev]
        return self.spans[-1]
#need to follow greedy strategy and replace all the spanned stocks with a single stock
#this is possible because we are looking at the CONSECUTIVE stocks starting from today.
class StockSpannerBetter:

    def __init__(self):
        self.spans = []
        self.prices = []

    def next(self, price: int) -> int:
        span = 1
        while len(self.spans) > 0 and price >= self.prices[-1]:
            span += self.spans[-1]
            self.spans.pop()
            self.prices.pop()
        self.spans.append(span)
        self.prices.append(price)
        return self.spans[-1]