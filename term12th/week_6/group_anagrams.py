class Solution:
    # time exceed
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1:
            return strs
        
        from collections import defaultdict, deque
        total_dict = {}
        
        for word in strs:
            total_dict[word] = defaultdict(lambda:0)
            for w in word:
                total_dict[word][w] += 1
        
        strs_q = deque(strs)
        result = []
        while strs_q:
            cur = strs_q.popleft()
            cur_arr = [cur]
            strs_cp = strs_q.copy()
            for word in strs_cp:
                if total_dict[cur] == total_dict[word]:
                    strs_q.popleft()
                    cur_arr.append(word)
                else:
                    cur_tar = strs_q.popleft()
                    strs_q.append(cur_tar)
            result.append(cur_arr)
        return result
    
    # accept
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1:
            return strs
        
        from collections import defaultdict
        total_dict = defaultdict(lambda:[])
        for word in strs:
            key = "".join(sorted(word))
            total_dict[key].append(word)
        
        result = [value for key, value in total_dict.items()]
        return result
