class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dic = defaultdict(int)
        n = len(nums)
        ans = []
        for val in nums:
            count_dic[val]+=1
        sorted_count_dic = sorted(count_dic.items(),reverse = True, key = lambda x: x[1])    
        for i in range(k):
            ans.append(sorted_count_dic[i][0])
        return ans