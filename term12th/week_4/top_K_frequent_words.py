class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        word_dict = defaultdict(lambda: 0)
        for word in words:
            word_dict[word] += 1
        
        need_value = sorted(word_dict.values(), reverse=True)[:k]

        result = []
        for key, value in word_dict.items():
            if value in need_value:
                result.append(key)
        return result