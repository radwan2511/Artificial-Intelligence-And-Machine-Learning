import heapq
from search_node import search_node


class My_Structure():
    def __init__(self, heap,dict):
        self.heap = heap
        self.dict = dict


def create_open_set():
    return My_Structure([],dict())


def create_closed_set():
    return dict()


def add_to_open(vn, open_set):
    open_set.dict[vn.state.state_str] = vn
    #heapq.heappush(open_set, (vn.f, vn))
    heapq.heappush(open_set.heap,vn)


def open_not_empty(open_set):
    return len(open_set.heap) != 0


def get_best(open_set):
    return_me=heapq.heappop(open_set.heap)
#    open_set.dict.pop(return_me.state.state_str)
    return return_me


def add_to_closed(vn, closed_set):
    closed_set[vn.state.get_state_str()]=vn

#returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
#remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    if vn.state.get_state_str() in open_set.dict:
            if  open_set.dict[vn.state.get_state_str()].g<=vn.g :
                return True
            else:
                return False
    return False


#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
#remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    if vn.state.get_state_str() in closed_set:
        if vn.g >= closed_set[vn.state.get_state_str()].g:
            return True
        else:
            return False
    return False


def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    # print(f"[{path[-1].state.get_state_str()}]")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if current.state.get_state_str() == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None




