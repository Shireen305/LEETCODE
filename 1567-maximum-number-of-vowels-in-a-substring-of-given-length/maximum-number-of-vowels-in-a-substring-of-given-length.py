class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=0
        max_vowel=0
        left=0
        right=0
        vowela="aeiou"
        while(right<=len(s)-1):
            if s[right] in vowela:
                vowel+=1
            if right-left==k-1:
                max_vowel=max(vowel,max_vowel)
                if s[left] in vowela:
                    vowel-=1
                left+=1
            right+=1
        return max_vowel

