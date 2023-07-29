class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        s = [[0 for j in range(len(coins)
         +1)] for k in range(amount
         +1)]
        coins.insert(0,-1)
        #print(coins)
        for k in range(1,len(coins)):
            s[0][k]=1
        for j in range(1,amount+1):
            for k in range(1,len(coins)):
                s[j][k]=s[j][k-1]
                if j>=coins[k]:
                    s[j][k]+=s[j-coins[k]][k]

                #print(j,k,s[j][k],s[j][k-1],s[j-coins[k]][k],coins[k])
        
        return s[amount][len(coins)-1]