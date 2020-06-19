def snail(snail_map):
    """Note: needs work
    """
    order = []
    n = len(snail_map) # nxn map
    w, h = n, n
    
    for i in range(0,w):
        if(snail_map[0][i] not in order):
            order.append(snail_map[0][i])
    for j in range(1,h):
        if(snail_map[j][n-1] not in order):
            order.append(snail_map[j][n-1])
    for k in range(n-1 -1, 0 -1, -1):
        if(snail_map[n-1][k] not in order):
            order.append(snail_map[n-1][k])
    #for l in range(3):
    return order