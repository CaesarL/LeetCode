from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_idx = [0]*26
        for idx, ch in enumerate(s):
            last_idx[ord(ch) - ord("a")] = idx
        
        start_idx, end_idx = 0,0
        ans_list = []
        for idx, ch in enumerate(s):
            end_idx = max(end_idx, last_idx[ord(ch) - ord("a")])
            if idx == end_idx:
                ans_list.append(idx - start_idx + 1)
                start_idx = idx + 1
        return ans_list
