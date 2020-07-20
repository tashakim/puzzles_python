class Solution:
    """Purpose: Returns correct English words from an 
    alien dictionary. 
    Note: This is a really inefficient solution.
    """
    def freqAlphabets(self, s: str) -> str:
        mydict = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10#':'j', '11#':'k', '12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u', '22#':'v', '23#':'w','24#':'x','25#':'y', '26#':'z'}
        let = []
        
        for i in range(len(s)):
            let.append(s[i])
            if s[i] == '#':
                for x in range(3):
                    let.pop()
                let.append(s[i-2:i+1])
        s = ""
        for x in let:
            s += mydict[x]
        return s