def delete_nth(order,max_e):
    # code here
    temp = [1]*len(order)
    for i in range(1, len(order)):
        for j in range(i):
            if(order[j] == order[i]):
                temp[i] = temp[j] + 1
    l = []
    for k in range(len(order)):
        if(temp[k] <= max_e):
            l.append(order[k])
    return l        