# import util
# import copy
# from util import Stack, Queue, PriorityQueue, PriorityQueueWithFunction
#
#
# class SearchProblem:
#     """
#     This class outlines the structure of a search problem, but doesn't implement
#     any of the methods (in object-oriented terminology: an abstract class).
#     You do not need to change anything in this class, ever.
#     """
#
#     def getStartState(self):
#         """
#         Returns the start state for the search problem.
#         """
#         util.raiseNotDefined()
#
#     def isGoalState(self, state):
#         """
#           state: Search state
#         Returns True if and only if the state is a valid goal state.
#         """
#         util.raiseNotDefined()
#
#     def getSuccessors(self, state):
#         """
#           state: Search state
#         For a given state, this should return a list of triples, (successor,
#         action, stepCost), where 'successor' is a successor to the current
#         state, 'action' is the action required to get there, and 'stepCost' is
#         the incremental cost of expanding to that successor.
#         """
#         util.raiseNotDefined()
#
#     def getCostOfActions(self, actions):
#         """
#          actions: A list of actions to take
#         This method returns the total cost of a particular sequence of actions.
#         The sequence must be composed of legal moves.
#         """
#         util.raiseNotDefined()
#
#
# def tinyMazeSearch(problem):
#     """
#     Returns a sequence of moves that solves tinyMaze.  For any other maze, the
#     sequence of moves will be incorrect, so only use this for tinyMaze.
#     """
#     from game import Directions
#     s = Directions.SOUTH
#     w = Directions.WEST
#     return [s, s, w, s, w, w, s, w]
#
#
# '''HELPER FUNCTIONS'''
#
#
# def find_child(paths, node):
#     '''checks if a node(state) is in a path'''
#     for path in paths:
#         if node in path:
#             return (path, True)
#     return ("", False)
#
#
# '''CYCLE CHECKING FUNCTIONS'''
#
#
# def path_index(path, state):
#     '''returns the list index in the path where the state is'''
#     # print 'path boi ', path
#     c = 0
#     for s in path:
#         if s == state:
#             return c
#         c += 1
#     return -1
#
#
# def update_path(node, new_node):
#     '''update the path, cost and direction with the new node'''
#     # print 'node ', node
#     index_state = path_index(node[0], new_node[0][-1])
#     return [new_node[0] + node[0][index_state + 1:], [new_node][1] + node[1][index_state + 1:],
#             [new_node][2] + node[2][index_state + 1:]]
#
#
# def update_all(stack, new_node):
#     for index in range(len(nodes)):
#         nodes[index] = update_path(nodes[index], new_node)
#     return True
#
#
# def check_costs(node, opt_costs):
#     states = node[0]
#     costs = node[2]
#     for index in range(len(states)):
#         if states[index] in costs:
#             if (sum(costs[:index + 1]) < opt_costs[states[index]]):
#                 return False
#     return True
#
#
# '''
# def update(n,v,stack):
# 	copy = list(n)
#     copy.append(v)
#     stack.push(copy)
# '''
#
#
# def depthFirstSearch(problem):
#     """
#     Search the deepest nodes in the search tree first.
#     Your search algorithm needs to return a list of actions that reaches the
#     goal. Make sure to implement a graph search algorithm.
#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:
#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
#     """
#     "*** YOUR CODE HERE ***"
#     # util.raiseNotDefined()
#     visited, paths = list(), list()
#     stack = Stack()
#     stack.push([[problem.getStartState()], []])
#     while not stack.isEmpty():
#         n = stack.pop()  # remove node from stack
#         paths.append(n)
#         state = n[0][-1]
#         if problem.isGoalState(state):
#             return n[1]
#         if state not in visited:  # expand only once
#             visited.append(state)
#             for child in problem.getSuccessors(state):
#                 if not find_child(paths, child)[1]:  # path check
#                     cp = copy.deepcopy(n)
#                     cp[0].append(child[0])
#                     cp[1].append(child[1])
#                     stack.push(cp)
#
#     return []
#
#
# def breadthFirstSearch(problem):
#     """Search the shallowest nodes in the search tree first."""
#     "*** YOUR CODE HERE ***"
#     # util.raiseNotDefined()
#
#     visited = list()
#     stack = Queue()
#     stack.push([[problem.getStartState()], []])
#
#     while not stack.isEmpty():
#         n = stack.pop()  # remove node from stack
#         state = n[0][-1]
#         if problem.isGoalState(state):
#             return n[1]
#         if state not in visited:  # expand only once
#             visited.append(state)
#             for child in problem.getSuccessors(state):
#                 if child[0] not in visited:  # path check
#                     cp = copy.deepcopy(n)
#                     cp[0].append(child[0])
#                     cp[1].append(child[1])
#                     stack.push(cp)
#
#     return []
#
#
# def uniformCostSearch(problem):
#     """Search the node of least total cost first."""
#     "*** YOUR CODE HERE ***"
#     visited = list()
#     stack = PriorityQueue()
#     stack.push([[problem.getStartState()], [], [0]], 0)
#     while not stack.isEmpty():
#         n = stack.pop()  # remove node from stack
#         state = n[0][-1]
#         if problem.isGoalState(state):
#             return n[1]
#         if state not in visited:  # expand only once
#             visited.append(state)
#             for child in problem.getSuccessors(state):
#                 if child[0] not in visited:  # path check
#                     current_priority = sum(n[2]) + child[2]
#                     # print 'p ',p,'child[2] ', child[2], 'sum(p) ',sum(p) ,'current priority ',current_priority,
#                     cp = copy.deepcopy(n)
#                     cp[0].append(child[0])
#                     cp[1].append(child[1])
#                     cp[2].append(child[2])
#                     stack.push(cp, current_priority)
#
#     # print 'priorities', priorities.heap
#
#
# def nullHeuristic(state, problem=None):
#     """
#     A heuristic function estimates the cost from the current state to the nearest
#     goal in the provided SearchProblem.  This heuristic is trivial.
#     """
#     return 0
#
#
# def aStarSearch(problem, heuristic=nullHeuristic):
#     """Search the node that has the lowest combined cost and heuristic first."""
#     "*** YOUR CODE HERE ***"
#     costs = dict()
#     stack = PriorityQueueWithFunction(lambda x: sum(x[2]) + heuristic(x[0][-1], problem))
#     # intialize
#     start = problem.getStartState()
#     initial_cost = 0
#     stack.push([[start], [], [initial_cost]])
#     costs[start] = heuristic(start, problem)
#
#     while not stack.isEmpty():
#         n = stack.pop()  # remove node from stack
#         # print 'chosen ', n
#         state = n[0][-1]
#         # print 'state ',state ,'heuristic ', heuristic(state,problem), 'total_cost', sum(n[2])
#         # sum(n[2]) <= costs[state]
#         if sum(n[2]) + heuristic(state, problem) <= costs[state]:  # expand only if cheapest
#             if problem.isGoalState(state):
#                 return n[1]
#             for child in problem.getSuccessors(state):
#                 sum_new = heuristic(child[0], problem) + child[2]
#                 cp = copy.deepcopy(n)
#                 if child[0] not in costs or sum_new + sum(n[2]) < costs[child[0]]:  # path check
#                     costs[child[0]] = sum(cp[2]) + sum_new
#                     cp[0].append(child[0])
#                     cp[1].append(child[1])
#                     cp[2].append(child[2])
#                     # print 'cp ', cp
#                     stack.push(cp)
#                 # update cost
#
#                 # need to update every path
#     return False
#
#
# '''
# chosen  [['S'], [], [6.0]]
# chosen  [['S', 'A'], ['0'], [6.0, 4.5]]
# chosen  [['S', 'D'], ['2'], [6.0, 6.0625]]
# chosen  [['S', 'D', 'C'], ['2', '1'], [6.0, 6.0625, 2.125]]
# chosen  [['S', 'D', 'C'], ['2', '1'], [6.0, 6.0625, 2.125]]
# chosen  [['S', 'B'], ['1'], [6.0, 8.25]]
# chosen  [['S', 'A', 'C'], ['0', '0'], [6.0, 4.5, 4.125]]
# chosen  [['S', 'D', 'C', 'G'], ['2', '1', '2'], [6.0, 6.0625, 2.125, 2.0]]
# '''
#
# # Abbreviations
# bfs = breadthFirstSearch
# dfs = depthFirstSearch
# astar = aStarSearch
# ucs = uniformCostSearch
import pdb
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    closed = set()
    fringe = util.Stack()
    fringe.push([problem.getStartState(),[]])

    while True:
        if fringe.isEmpty():
            print "Cannot reach goal state."
            return None
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.add(node[0])
            for successor, action, cost in problem.getSuccessors(node[0]):
                accumActions = node[1][:]
                accumActions.append(action)
                childNode = [successor, accumActions]
                fringe.push(childNode)



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    closed = set()
    fringe = util.Queue()
    fringe.push([problem.getStartState(),[]])

    while True:
        if fringe.isEmpty():
            print "Cannot reach goal state."
            return None
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.add(node[0])
            for successor, action, cost in problem.getSuccessors(node[0]):
                accumActions = node[1][:]
                accumActions.append(action)
                childNode = [successor, accumActions]
                fringe.push(childNode)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    closed = set()
    fringe = util.PriorityQueue()
    fringe.push([problem.getStartState(),[]],0)

    while True:
        if fringe.isEmpty():
            print "Cannot reach goal state."
            return None
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.add(node[0])
            for successor, action, cost in problem.getSuccessors(node[0]):
                accumActions = node[1][:]
                accumActions.append(action)
                childNode = [successor, accumActions]
                g = problem.getCostOfActions(accumActions)
                fringe.push(childNode, g)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    closed = set()
    fringe = util.PriorityQueue()
    fringe.push([problem.getStartState(), []], 0)

    while True:
        if fringe.isEmpty():
            print "Cannot reach goal state."
            return None
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.add(node[0])
            for successor, action, cost in problem.getSuccessors(node[0]):
                accumActions = node[1][:]
                accumActions.append(action)
                childNode = [successor, accumActions]
                g = problem.getCostOfActions(accumActions)
                h = heuristic(successor, problem)
                f = g + h
                fringe.push(childNode, f)

def greedySearch(problem, heuristic=nullHeuristic):
    closed = set()
    fringe = util.PriorityQueue()
    fringe.push([problem.getStartState(),[]],0)
    while True:
        if fringe.isEmpty():
            print "Cannot reach goal state."
            return None
        node = fringe.pop()
        if problem.isGoalState(node[0]):
            return node[1]
        if node[0] not in closed:
            closed.add(node[0])
            for successor, action, cost in problem.getSuccessors(node[0]):
                accumActions = node[1][:]
                accumActions.append(action)
                childNode = [successor, accumActions]
                h = heuristic(successor, problem)
                fringe.push(h)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
greedy = greedySearch
