import numpy as np

def consecutive_combo(lst1, lst2):
    newar = np.concatenate((lst1, lst2), axis=None)
    newar = np.sort(newar, axis= -1, kind=None, order=None)
    for x in range(len(newar)-1):
        if newar[x] != newar[x+1]-1:
            return False
        
    return True
            
                


	
consecutive_combo([7, 4, 5, 1], [2, 3, 6])