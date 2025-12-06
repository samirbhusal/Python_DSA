from typing import List


class TwoSumSolution:
    def twoSum(self, nums: List[int], target) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hash_map:
                return [hash_map[diff], i]

            hash_map[n] = i


twoSumSol = TwoSumSolution()
print(twoSumSol.twoSum(nums=[2, 15, 11, 7], target=9))
