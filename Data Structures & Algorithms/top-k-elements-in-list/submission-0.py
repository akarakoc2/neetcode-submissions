class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = dict()

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        nums_sorted = sorted(freq, key= lambda x: freq[x], reverse = True)

        top_freq = list()

        for i in range(k):
            top_freq.append(nums_sorted[i])
        

        return top_freq
        

            


        
        