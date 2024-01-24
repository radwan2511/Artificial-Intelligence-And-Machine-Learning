from search import print_path, search
from pancake_state import pancake_state
from heuristics import *
import time
if __name__ == '__main__':
    goal_state = "9,8,7,6,5,4,3,2,1"
    pancake_input = "8,4,9,3,5,7,2,6,1"
    pancake_state1 = pancake_state(pancake_input)
    pancake_state2 = pancake_state(pancake_input)

    t1 = time.time()
    search_result = search(pancake_state1, base_heuristic, goal_state)
    t2 = time.time()
    # search_result2 = search(pancake_state2, advanced_heuristic, goal_state)
    # t3 = time.time()
    
    print_path(search_result)
    print(t2-t1)
    # print(t2-t1,t3-t2)
    # print_path(search_result2)