class Solution:
    def func(self, i, j, s, p):
        if i == len(s) and j == len(p):
            return True

        if j >= len(p):
            return False

        if i == len(s):  # s exhausted but pattern isn't → only True if remaining pattern is x* pairs
            while j <= len(p) - 1:
                if j+1 <= len(p) - 1 and p[j+1] == '*':
                    j += 2
                else:
                    return False
            return True

        if j+1 <= (len(p) - 1) and p[j+1] == '*':
            if p[j] != '.': 

                # x* takes up 0 case
                zeroCase = self.func(i, j+2, s, p)
                if zeroCase == True:
                    return True

                char = p[j]

                # loop that goes thru all possibilities 
                # of x*, x* takes up 1, x* takes up 2, x* takes up 2
                iHelper = 0
                while (i + iHelper) <= (len(s) - 1) and s[i + iHelper] == char:
                    checker = self.func(i + iHelper + 1, j + 2, s, p)
                    if checker == True:
                        return True  
                    iHelper += 1

                return False

            elif p[j] == '.':
                # x* takes up 0 case
                zeroCase = self.func(i, j+2, s, p)
                if zeroCase == True:
                    return True
                

                # loop that goes thru all possibilities 
                # of x*, x* takes up 1, x* takes up 2, x* takes up 2
                iHelper = 0
                while (i + iHelper) <= (len(s) - 1):
                    print('i + iHelper + 1: ', i + iHelper + 1)
                    checker = self.func(i + iHelper + 1, j + 2, s, p)
                    if checker == True:
                        return True  
                    iHelper += 1

                return False

        # match
        if s[i] == p[j] or p[j] == '.':
            return self.func(i+1, j+1, s, p)

        # not match
        if s[i] != p[j]:
            return False
            
                

    def isMatch(self, s: str, p: str) -> bool:
        return self.func(0, 0, s, p)
        #similar to wildcard matching
        