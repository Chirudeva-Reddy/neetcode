class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dic = defaultdict(int)
        freq = [[]for i in range(len(nums)+1)]

        for val in nums:
            count_dic[val]+= 1
                                        #        (key,freq)
        for key,c in count_dic.items():   # tuple: (1,2),(2,1)
            freq[c].append(key)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res