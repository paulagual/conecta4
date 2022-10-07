

def find_one(list, needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle en list
    """
    # for item in list:
    #     if item == needle:
    #         return True
    # return False
    return find_n(list, needle, 1) #find_one refactorizado con find_n

def find_n(list, needle, n):
    """
    Devuelve True si encuentra n o más ocurrencias de needle en una en list
    False si hay menos o si n < 0
    """
    if n >= 0:
        n_times = 0
        for item in list:
            if item == needle:
                n_times += 1
                if n_times == n:
                    return True
        return n_times >= n
    else: 
        return False

def find_streak(list, needle, streak):
    """
    Devuelve True si encuentra n o más ocurrencias seguidas de needle en una en list
    False si hay menos o si n < 0
    """
    if streak >= 0:
        count = 0
        for item in list:
            if item == needle:
                count += 1
                if count == streak:
                    return True
            else:
                count = 0
        return count == streak
    else: 
        return False

def first_elements(list_of_lists):
    """
    Transpone una matriz (lista de listas), y devuelve la primera columna de la matriz transpuesta.
    """
    return nth_elements(list_of_lists, 0)

def nth_elements(list_of_lists, n):
    """
    Transpone una matriz (lista de listas), y devuelve la enesima columna de la matriz transpuesta.
    """
    return [ls[n] for ls in list_of_lists]

def transpose(matrix):
    """
    Transpone una matriz (lista de listas), y devuelve la matriz transpuesta.
    """    
    return [nth_elements(matrix, i) for i in range(len(matrix[0]))]

def displace(ls, distance, filler=None):
    if (distance == 0) or (len(ls) == 0):
        return ls
    elif distance  > 0:
        filling = [filler] * distance
        res = filling + ls
        res = res[:-distance]
        return res
    else: #distance < 0
        filling = [filler] * abs(distance)
        res = ls + filling
        res = res[abs(distance):]
        return res    

def displace_matrix(matrix, filler=None):
    m = []
    for i in range(len(matrix)):
        m.append(displace(matrix[i], i-1, filler))
    return m

def reverse_list(ls):
    return list(reversed(ls))

def reverse_matrix(matrix):
    m = []
    for l in matrix:
        m.append(reverse_list(l))
    return m

def all_same(ls):
    is_same = True
    for i in range(len(ls)):
        if ls[i] != ls[0]:
            is_same = False
            break
    return is_same
