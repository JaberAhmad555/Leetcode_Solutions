class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        for ch in s:
            arr.append(ch)
        count = 0
        s=False
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == ' ' and not s:
                continue
            if arr[i] == ' ' and s:
                break
            s=True

            count += 1
        return count
