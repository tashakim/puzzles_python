import math

def primeFactors(n):
    """Returns the prime factor decomposition of n. 
    Result is a string of the form:  "(p1**n1)(p2**n2)...(pk**nk)".
    """
    factors = []
    for i in range(2, math.ceil(math.sqrt(n))):
        if(n%i == 0):
            factors.append("("+str(i)+")")
            index = factors.index("("+str(i)+")")
            n = n/i
            p = 2
            while(n%i == 0):
                factors[index] = "("+str(i)+"**"+str(p)+")"
                n = n/i
                p +=1
    res = "".join(factors)
    return res


def better_sol(n):
    i = 2
    factors = []
    while i*i <= n:
        if(n%i):
            i+=1
        else:
            n//=i
            factors.append(i)
    if(n>1):
        factors.append(n)
    return factors # call factor_rep(factors)


def factor_rep(factors):
    """String representation. 
    """
    """res = ""
                for i in factors:
                    res.join(""("+str(i)+")"")
                print(res)
                return res"""
    return


if __name__ == "__main__":
    print(better_sol(7775460))