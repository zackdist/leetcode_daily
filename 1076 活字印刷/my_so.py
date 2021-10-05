

class Solution:
    def numTilePossibilities(self, tiles: str):
        str_count = {}

        for i in tiles:
            if(i not in str_count):
                str_count[i] = tiles.count(i)

        def call_back(str_count):
            num = 0
            for i in str_count:
                if( str_count[i]!=0):
                    num += 1
                    str_count[i] = str_count[i] -1
                    num += call_back(str_count)
                    str_count[i] = str_count[i] +1
            return num

        res = call_back(str_count)
        print(res)


so = Solution()
so.numTilePossibilities("AAB")
