class solution():

    def lcs(self,idx1,idx2):
        if idx1 == 0 or idx1 == 0:
            return 0
        elif self.s1[idx1-1] == self.s2[idx2-1]:
            return self.lcs(idx1-1, idx2-1)+1
        else:
            return max(self.lcs(idx1,idx2-1), self.lcs(idx1-1,idx2))

    def lcs_max_num(self,s1,s2):
        
        self.s1 = s1
        self.s2 = s2
        return self.lcs(len(s1),len(s2))

print(solution().lcs_max_num("abcdef","abcdefg"))