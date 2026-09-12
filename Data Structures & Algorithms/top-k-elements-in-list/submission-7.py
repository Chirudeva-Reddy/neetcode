class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dic = defaultdict(int)
        n = len(nums)
        ans = []
        for val in nums:
            count_dic[val]+=1
        sorted_count_dic = sorted(count_dic, key = count_dic.get, reverse=True)    
        return sorted_count_dic[:k]
