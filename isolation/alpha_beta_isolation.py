# radwan ganem 322509951
# bayan kassem 314733296

import math


def alphabeta_max(current_game):
    #now i am max - current player is max
    alpha=-math.inf
    beta=math.inf
    return maximin(current_game,alpha,beta)


def alphabeta_min(current_game):
    # now i am min - current player is min
    alpha=-math.inf
    beta=math.inf
    return minimax(current_game,alpha,beta)



def maximin(current_game,alpha,beta):
    # now i am max - current player is max
    if current_game.is_terminal():
        return current_game.get_score(), None
    my_alpha=alpha
    v = -math.inf
    my_beta=beta
    best_move=None
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move,my_alpha,my_beta)
        if v < mx:
            v = mx
            best_move = move
        my_alpha=max(v,my_alpha)
        if my_beta<=my_alpha:  #pruning
             return v,None
    return v, best_move


def minimax(current_game,alpha,beta):
    #now i am min - current player is min
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    my_alpha=alpha
    my_beta = beta
    best_move = None
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move,my_alpha,my_beta)
        if v > mx:
            v = mx
            best_move = move
        my_beta=min(my_beta,v)
        if my_beta <= my_alpha:
            return v,None
    return v, best_move
