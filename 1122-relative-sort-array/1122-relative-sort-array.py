class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        count = {}

        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []

        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0

        remaining = []

        for num in count:
            if count[num] > 0:
                remaining.extend([num] * count[num])

        remaining.sort()

        result.extend(remaining)

        return result