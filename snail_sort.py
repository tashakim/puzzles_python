def snail(snail_map):
    """Note: needs work
    """
    order = []
    n = len(snail_map) # nxn map
    w, h = n, n
    # while h not 0
    for i in range(0,w):
        if(snail_map[0][i] not in order):
            order.append(snail_map[0][i])
            # decrement h
    for j in range(1,h):
        if(snail_map[j][n-1] not in order):
            order.append(snail_map[j][n-1])
    for k in range(n-1 -1, 0 -1, -1):
        if(snail_map[n-1][k] not in order):
            order.append(snail_map[n-1][k])
    #for l in range(3):
    return order
    

if __name__ == "__main__":
    arr = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    assert(snail(arr) == [1,2,3,6,9,8,7,4,5]), "Wrong answer."
    print("Test passed.")