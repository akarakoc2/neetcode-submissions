class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    st = 0
    rt = len(numbers) - 1

    while st < rt:
      current_sum = numbers[st] + numbers[rt]

      if current_sum > target:
        rt -= 1
      elif current_sum < target:
        st += 1
      else:
        return [st + 1, rt + 1]

    return []