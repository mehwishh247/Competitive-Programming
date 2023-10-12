class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        try:
            
            arr1 = queryIP.split(".")
            arr2 = queryIP.split(":")

            
            

            if len(arr1) != 4 and len(arr2) != 8: return "Neither"
            
            if len(arr1)==4: return self.checker4(arr1)
            
            return self.checker6(arr2)
                    
            
        except:
            return "Neither"
        
        
    def checker4(self,ipv4):
        for sub in ipv4:
            if not sub ==str(int(sub)) or not 0<=int(sub)<=255: return "Neither"
        return "IPv4"


        
    def checker6(self,ipv6):
        for sub in ipv6:

            if len(sub)>4 or len(sub)==0: return "Neither"
            for ch in sub:
                
                if "0" <= ch<= "9": continue
                elif "a" <= ch<= "f": continue
                elif "A" <= ch<= "F": continue
            
                return "Neither"
        return "IPv6"     