class Solution:
    def avoidFlood(self, rains):
        day_sun = []
        lake_dict = {}

        for i in range(len(rains)):
            # 如果为晴天
            if(rains[i]==0):
                day_sun.append(i)
                rains[i] = 1
                continue
            else:
                if(rains[i] in lake_dict):
                    for day in day_sun:
                        if(day>lake_dict[rains[i]]):
                            rains[day] = rains[i]
                            day_sun.remove(day)
                            lake_dict[rains[i]] = i
                            break
                    if(lake_dict[rains[i]]!=i):
                        return []
                else:
                    lake_dict[rains[i]] = i
            rains[i] =  -1
        return rains

so = Solution()
res = so.avoidFlood([69,0,0,0,69])
print(res)