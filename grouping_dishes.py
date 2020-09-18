def groupingDishes(dishes):
    """Purpose: Given list of lists with [dish, ingredient1, ingredient2, ...],
    return a list of lists starting with each ingredient that appears more than twice,
    followed by all dishes that can be made from it.
    """
    d = {}
        
        for l in dishes:
            dish = l[0]
            for i in l[1:]:
                if i not in d:
                    d[i] = [dish]
                else:
                    d[i] += [dish]
                    
        print(d)
        
        out = []
        
        for i in sorted(d):
            if len(d[i]) > 1:
                out += [[i] + sorted(d[i])]
                
        return out