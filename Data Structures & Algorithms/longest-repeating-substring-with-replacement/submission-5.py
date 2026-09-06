class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for i in range(len(s)):
            # 1. Cleaner frequency increment
            count[s[i]] = count.get(s[i], 0) + 1

            # 2. Window length is already (i - l + 1); no need to sum the dictionary
            window_len = i - l + 1
            check = window_len - max(count.values())

            if check <= k:
                res = max(res, window_len)
            else:
                count[s[l]] -= 1
                l += 1

        return res