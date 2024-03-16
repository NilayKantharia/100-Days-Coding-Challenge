class Solution:
    def sameFreq(self, s):
        hashDic={}
        for i in s:
            if i in hashDic:
                hashDic[i]+=1
            else:
                hashDic[i]=1
        f=0
        temp=list(hashDic.values())
        temp.sort()
        if len(temp)>1:
            if temp[0]!=temp[1] and temp[0]==1:
                del temp[0]
                if temp[0]==temp[-1]:
                    return True
                return False
        for i in range(len(temp)-1):
            if temp[i+1]-temp[i]>1:
                return False
            if temp[i+1]-temp[i]==1:
                if not f:
                    f+=1
                    temp[i+1]-=1
                else:
                    return False
        if temp[0]==temp[-1]:
            return True
        else:
            return False
            
