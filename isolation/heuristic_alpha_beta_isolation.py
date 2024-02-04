import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth):
    global h
    h = _heuristic
    alpha=-math.inf
    beta=math.inf
    return maximin(current_game,depth,alpha,beta)


def alphabeta_min_h(current_game, _heuristic, depth):
    global h
    h = _heuristic
    # add code here
    alpha=-math.inf
    beta=math.inf
    return minimax(current_game,depth,alpha,beta)


def maximin(current_game, depth,alpha,beta):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    my_alpha=alpha
    my_beta=beta
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1,my_alpha,my_beta)
        if v < mx:
            v = mx
            best_move = move
        my_alpha = max(v, my_alpha)
        if my_beta <= my_alpha:  # pruning
            return v, None
    return v, best_move


def minimax(current_game, depth,alpha,beta):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    my_alpha=alpha
    my_beta = beta
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1,my_alpha,my_beta)
        if v > mx:
            v = mx
            best_move = move
        my_beta = min(my_beta, v)
        if my_beta <= my_alpha:
            return v, None
    return v, best_move
