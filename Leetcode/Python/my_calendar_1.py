class MyCalendar: 
    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        def getPos():
            if len(self.books) == 0:
                return -1
            left, right = 0, len(self.books) - 1
            while left <= right:
                mid = (left + right )// 2
                if self.books[mid][0] == start:
                    return mid - 1
                elif self.books[mid][0] < start:
                    left = mid + 1
                else:
                    right = mid - 1
            if left >= len(self.books):
                left = len(self.books) - 1
            return left if self.books[left][0] <= start else left - 1
        pos = getPos()
        leftS, leftE = (float('-inf'), float('-inf')) if pos < 0 else self.books[pos]
        rightS, rightE = (float('inf'), float('inf')) if pos >= (len(self.books) - 1) else self.books[pos + 1]
        if start >= leftE and end <= rightS:
            self.books = self.books[: pos + 1] + [(start, end)] + self.books[pos + 1:]
            return True
        else:
            return False