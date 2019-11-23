from foundation import Node
from foundation import State
from foundation import Block

from random import shuffle
import timeit
import queue
import heapq

class SearchMethods:

    def __init__(self, startNode, finishState):
        self.startNode = startNode
        self.finishState = finishState
        self.path = []


    def BFS(self):
        path = []
        startTime = timeit.timeit()

        #initialize queue and dictionary and add Start Node to it
        q = queue.Queue()
        q.put(self.startNode)

        visited = {self.startNode: True}

        while not q.empty():
            #pops first element from the queue and checks what moves can be made
            currentNode = q.get()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")

            if(currentNode.state.isEqual(self.finishState)):
                time = timeit.timeit() - startTime
                self.printResults('Breadth First', currentNode, visited, time)
                break

            else:
                possibleMoves = currentNode.checkPossibleMoves()
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        q.put(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")

    def DFS(self):
        path = []
        startTime = timeit.timeit()
        
        #initializes stack and dictionary and add Start Node to it
        s = []
        s.append(self.startNode)
        
        visited = {self.startNode: True}
        
        while len(s) > 0:
            currentNode = s.pop()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")
            
            if(currentNode.state.isEqual(self.finishState)):
                time = startTime - timeit.timeit()
                self.printResults('Depth First', currentNode, visited, time)
                break
                
            else:
                possibleMoves = currentNode.checkPossibleMoves()
                shuffle(possibleMoves)
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        s.append(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")

    def iterativeDeepening(self):
        maxDepth = 0

        startTime = timeit.timeit()

        #initializes stack and dictionary and add Start Node to it
        s = []
        s.append(self.startNode)

        visited = {self.startNode: True}

        while len(s) > 0:
            currentNode = s.pop()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")

            if(currentNode.state.isEqual(self.finishState)):
                time = startTime - timeit.timeit()
                self.printResults('Iterative Deepening', currentNode, visited, time)
                break

            elif currentNode.depth < maxDepth:
                possibleMoves = currentNode.checkPossibleMoves()
                shuffle(possibleMoves)
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        s.append(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")




    def aStar(self):
        path = []
        startTime = timeit.timeit()
        
        #iitializes a priority queue and dictionary and add Start Node to it
        pq = PriorityQueue(self.startNode)
        visited = {self.startNode: True}
        
        while not pq.isEmpty():
            currentNode = pq.pop()

            print("Visiting:")
            currentNode.state.printGrid()
            print("")
            
            if(currentNode.state.isEqual(self.finishState)):
                time = timeit.timeit() - startTime
                self.printResults('A*', currentNode, visited, time)
                break
                
            else:
                possibleMoves = currentNode.checkPossibleMoves()
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        pq.push(nextNode, nextNode.getHeuristicEstimate(Node(self.finishState, None, None)))
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")
        

    def printResults(self, searchType, currentNode, visited, time):
        print ('{} Search Complete'.format(searchType))
        
        print ('Start State:')
        self.startNode.state.printGrid()
        print ('\nFinal State:')
        currentNode.state.printGrid()

        if not currentNode.parent is None:
            print ('\nDepth: {}\nHeuristic Estimate: {}\nMoves Performed: {}\nAmount visited: {}\nTime Taken: {}'.format(currentNode.depth, self.startNode.getHeuristicEstimate(currentNode), currentNode.getPath(), len(visited), time))

class PriorityQueue:

    def __init__(self, item):
        self.queue = [(item, 0)]


    def push(self, item, priority):
        i = 0
        # Searching for the position 
        for i in range(0, len(self.queue)): 
            if self.queue[i][1] < priority: 
                break
      
        self.queue = self.queue[:i] + [(item, priority)] + self.queue[i:]

    def pop(self):
        return self.queue.pop(len(self.queue) - 1)[0]

    def isEmpty(self):
        if len(self.queue) == 0: return True
        else: return False




