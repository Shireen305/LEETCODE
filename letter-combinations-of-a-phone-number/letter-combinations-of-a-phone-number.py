class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def comb(i,subset):
            if len(subset)==len(digits):
                res.append(subset[:])
                return
            for c in digitToChar[digits[i]]:
                comb(i+1, subset + c)
                
            
            return res
        
        if digits:
            return comb(0,"")