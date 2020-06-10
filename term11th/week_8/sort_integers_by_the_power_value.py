class Solution:
    def get_power(self, num):
        result = 0
        while num != 1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3 * num + 1
            result += 1
        return result
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_nums = []
        power_dict = dict()
        
        for i in range(lo, hi+1):
            current_power = self.get_power(i)
            if current_power in power_dict.keys():
                power_dict[current_power].append(i)
                power_dict[current_power].sort()
            else:
                power_dict[current_power] = list()
                power_dict[current_power].append(i)
                power_nums.append(current_power)
        power_nums.sort()
        current = 1
        result = None
        
        for num in power_nums:
            cur_nums = power_dict[num]
            
            for cur_num in cur_nums:
                if current == k:
                    result = cur_num
                    break
                current += 1
            if result:
                break
        return result