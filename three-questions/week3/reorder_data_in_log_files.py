class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alphas = []
        digits = []
        
        for log in logs:
            split_arr = log.split(" ")
            head, tail = split_arr[0], " ".join(split_arr[1:])
            
            if tail[0].isalpha():
                alphas.append([tail, head])
            else:
                digits.append(" ".join([head, tail]))
        alphas.sort()
        alphas = [" ".join(elem[::-1]) for elem in alphas]
        return alphas + digits