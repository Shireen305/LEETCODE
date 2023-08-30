class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        fin=[]
        for i in range(len(searchWord)):
            res=[]
            for product in products:
                if searchWord[0:i+1]==product[0:i+1]:
                    if len(res)==3:
                        break
                    else:
                        res.append(product)  
            fin.append(res)  
        return fin
            

