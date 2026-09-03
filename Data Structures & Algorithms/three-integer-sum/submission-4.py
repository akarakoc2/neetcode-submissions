class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sortNums = sorted(nums) 
        res = []
        for i in range(len(sortNums)-1):

            if sortNums[i] == sortNums[i-1] and i >0:
                continue
            st,rt = i+1, len(sortNums) - 1
            target = -sortNums[i]
            while st < rt:
                    if sortNums[st] + sortNums[rt] < target:
                        st +=1  
                    elif sortNums[st] + sortNums[rt] > target:
                        rt -=1
                    else:
                        res.append([sortNums[i],sortNums[st],sortNums[rt]])
                        st +=1
                        rt -=1
                        while sortNums[st] == sortNums[st - 1] and st < rt:
                            st+=1

        return res


