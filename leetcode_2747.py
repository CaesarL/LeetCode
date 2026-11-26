from typing import List
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries:List[int]) -> List[int]:
        len_log = len(logs)
        sort_log = sorted(logs, key=lambda x: x[1])
        idx_sort = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        cnt = [0] * (n + 1)
        sorted(queries)
        right = left = resp = 0
        for idx in idx_sort:
            query = queries[idx]
            while right < len_log and sort_log[right][1] <= query:
                server_id = sort_log[right][0]
                if cnt[server_id] == 0:
                    resp += 1
                cnt[server_id] += 1
                right += 1
            while left < right and sort_log[left][1] < query - x:
                server_id = sort_log[left][0]
                cnt[server_id] -= 1
                if cnt[server_id] == 0:
                    resp -= 1
                left += 1    
            ans[idx] = n - resp
        return ans
