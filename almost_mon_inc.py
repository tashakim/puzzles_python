def almostIncreasingSequence(sequence):
    s2 = sorted(sequence)
    index = []

    i = 0
    while i < len(sequence)-1:
        if sequence[i] >= sequence[i+1]:
            index.append(i)
            index.append(i+1)
        i += 1
    
    for i in index:
        print(sequence[:i] + sequence[i+1:])
        print(s2[:i] + s2[i+1:])
        if sequence[:i] + sequence[i+1:] == s2[:i] + sequence[i+1:]:
            return True
        
    return False


if __name__ == "__main__":
    almostIncreasingSequence([1,3,2,1])