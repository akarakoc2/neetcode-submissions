class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = dict()

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        nums_sorted = sorted(freq, key= lambda x: freq[x], reverse = True)
        print(nums_sorted)

        top_freq = list()

        return nums_sorted[:k]
        
        

            


        
        