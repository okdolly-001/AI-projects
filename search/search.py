
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
