# radwan ganem 322509951
# bayan kassem 314733296
def base_heuristic(_pancake_state):
    current_h = int(len(_pancake_state.get_state_str())/2 + 1)
    current_h = int(current_h*(current_h+1)/2)
    list1 = _pancake_state.get_state_str().split(',')
    j = len(_pancake_state.get_state_str().split(',')) + 1
    for i in range(0,j-1):
        j -= 1
        if int(list1[i]) == j:
            current_h = current_h - int(list1[i])
        else:
            return current_h
    return current_h

def advanced_heuristic(_pancake_state):
    current_h = int(len(_pancake_state.get_state_str())/2 + 1)
    list1 = [str(current_h)]
    current_h = int(current_h*(current_h+1)/2)
    list1 =  list1 + _pancake_state.get_state_str().split(',')
    j = len(list1)
    length = int(len(list1)/2) + 1
    for i in range(0,j-2):
        j -= 1
        if int(list1[i+1]) == j:
            current_h = current_h - int(list1[i])
            if(abs(int(list1[i+1]) - int(list1[i])) != 1):
                  current_h -= length + 1
        else:
            if(abs(int(list1[i+1]) - int(list1[i])) != 1):
                  current_h += length - 3
            return current_h - int(list1[-1]) + 2
    return current_h