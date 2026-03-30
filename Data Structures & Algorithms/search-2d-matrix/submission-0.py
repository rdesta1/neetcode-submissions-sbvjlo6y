class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flat_matrix = [element for row in matrix for element in row]

        l, r = 0, len(flat_matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if target < flat_matrix[m]:
                r = m - 1
            elif target > flat_matrix[m]:
                l = m + 1
            else:
                return True

        return False