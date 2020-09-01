class ThisTime:
    def largestTimeFromDigits(self, A: List[int]) -> str:
    """Purpose: Returns the largest time (24:00) that can be 
    composed of input array of digits.
    """
        perm = list(sorted(itertools.permutations(A), reverse = True))
        
        for possible_time in perm:            
            a,b,c,d = possible_time
            hr = (a*10+b)
            mins = (c*10+d) 

            if hr < 24 and mins <60:
                return  f"{a}{b}:{c}{d}"
                
        return ''