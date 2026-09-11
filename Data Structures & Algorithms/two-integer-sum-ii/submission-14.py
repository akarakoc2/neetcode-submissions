class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        st = 0
        rt = len(numbers) - 1
        i = 0
        while (i < (len(numbers))-1):

            left = numbers[st]
            right = numbers[rt]

            if (left + right) > target:
                rt -= 1
            elif (left + right) < target:
                st += 1
            i+=1
        return [(1+st),(rt+1)]




            
