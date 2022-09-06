

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
