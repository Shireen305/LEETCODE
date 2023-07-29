class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
         #print(len(text1),len(text2))
         s = [[0 for j in range(len(text2)+1)] for k in range(len(text1)
         +1)]
         text1='*'+text1
         text2='*'+text2
         for j in range(1,len(text1)):
             for k in range(1,len(text2)):
                 #print(j,k)
                 s[j][k]=max(s[j-1][k],s[j][k-1])
                 if text1[j]==text2[k]:
                     s[j][k]=s[j-1][k-1]+1
         #print(s)
         return s[len(text1)-1][len(text2)-1]
