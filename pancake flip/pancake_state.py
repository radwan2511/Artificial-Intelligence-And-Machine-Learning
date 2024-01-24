class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data stractures to improve the search

    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        neighbors = []
        current_state_in_list = self.state_str.split(',')
        lenght = len(current_state_in_list)
        flip_all_cost = int((lenght * (lenght + 1)) / 2)
        # neighbors.append((current_state_in_list[::-1], flip_all_cost)) pancake_state(pancake_input)
        neighbors.append((pancake_state(','.join(current_state_in_list[::-1])), flip_all_cost))
        unflipped_pancakes = int(current_state_in_list[0])
        for i in range(len(current_state_in_list) - 2):
            neighbors.append((pancake_state(','.join(current_state_in_list[0:i + 1] + current_state_in_list[i + 1:][::-1])),
                              flip_all_cost - unflipped_pancakes))
            unflipped_pancakes = unflipped_pancakes + int(current_state_in_list[i + 1])
        return neighbors



    #you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str


    def get_state_str(self):
        return self.state_str
