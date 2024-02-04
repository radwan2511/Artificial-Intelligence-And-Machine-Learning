import numpy as np

def base_heuristic(curr_state):
    player_locations=curr_state.get_player_locations()
    player_1_location=player_locations[1]
    player_2_location = player_locations[2]
    moves1 = []
    moves2 = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            curr_state.add_moves_in_direction(player_1_location, (i, j), moves1)
            curr_state.add_moves_in_direction(player_2_location, (i, j), moves2)
    return len(moves1) - len(moves2)
    

def advanced_heuristic(curr_state):
    g = curr_state.get_grid()
    height = len(g)
    width = len(g[0])
    num_zeros = np.count_nonzero(g == 0)
    round = (height*width - num_zeros)
    player_locations=curr_state.get_player_locations()
    player_1_location=player_locations[1]
    player_2_location = player_locations[2]

    moves1 = []
    moves2 = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            curr_state.add_moves_in_direction(player_1_location, (i, j), moves1)
            curr_state.add_moves_in_direction(player_2_location, (i, j), moves2)

    avg = round/(height*width)
    if avg <= 0.5:
        return len(moves1) - (2*len(moves2))
    else:
        return (2*len(moves1)) - len(moves2)
