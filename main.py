from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index

    return []
