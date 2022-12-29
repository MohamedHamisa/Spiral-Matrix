class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

#matrix.pop(0) is usually a tuple (since zip creates a list of tuples). And "tuple+list" is not allowed, so I need to convert each tuple to a list.
