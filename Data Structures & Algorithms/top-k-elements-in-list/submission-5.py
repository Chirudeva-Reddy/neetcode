class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dic = defaultdict(int)
        n = len(nums)
        ans = []
        for val in nums:
            count_dic[val]+=1
        sorted_count_dic = sorted(count_dic.items(), key=lambda item: item[1], reverse=True)    
        for i in range(k):
            ans.append(sorted_count_dic[i][0])
        return ans
