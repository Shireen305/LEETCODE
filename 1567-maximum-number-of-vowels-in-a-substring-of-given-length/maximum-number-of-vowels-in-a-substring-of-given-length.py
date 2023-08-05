class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=0
        max_vowel=0
        left=0
        right=0
        while(right<=len(s)-1):
            if s[right]=='a' or s[right]=='e'or s[right]=='i' or s[right]=='o' or s[right]=='u':
                vowel+=1
            if right-left==k-1:
                max_vowel=max(vowel,max_vowel)
                if s[left]=='a' or s[left]=='e'or s[left]=='i' or s[left]=='o' or s[left]=='u':
                    vowel-=1
                left+=1
            right+=1
        return max_vowel

