def collapse_list(ls, empty='.'):
    """
    Concatena todas las cadenas de la lista en una sola cadena
    """
    string = ''
    for item in ls:
        if item == None:
            string = string + empty
        else:
            string = string + item
    return string

def collapse_matrix(matrix, empty='.', separator='|'):
    """ 
    Contatena todas las listas en una sola cadena separada por |
    """
    string = ''
    for ls in matrix:
        string = string + collapse_list(ls, empty) + separator
    return string[:-1]

def explode_string(string):
    return list(string)

def explode_list_of_strings(list_of_strings):
    matrix = []
    for string in list_of_strings:
        matrix.append(explode_string(string))
    return matrix

def replace_all_in_list(ls,old,new):
    result = []
    for element in ls:
        if element == old:
            result.append(new)
        else: #element != old
            result.append(element)
    return result

def replace_all_in_matrix(matrix,old,new):
    result = []
    for ls in matrix:
        result.append(replace_all_in_list(ls, old, new))
    return result