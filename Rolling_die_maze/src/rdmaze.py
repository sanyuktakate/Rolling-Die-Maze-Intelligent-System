""" Author : Amit Jagannath Magar
           : Sanyukta Sanjay Kate

Version 1.0

Problem Definition:-

You will implement A* search in Python to solve rolling-die mazes.
In a rolling-die maze, the objective is to "roll" a die along its edges
through a grid until a goal location is reached. The initial state of
the search is given by the die location and the orientation of the die faces.
Rolling die mazes contain obstacles, along with restrictions on which numbers may face 'up.'

Constraints:
1. The die begins with 1 on top, 2 facing up/north, and 3 facing right/east.
2. All opposite die faces add to 7 (for example: 1 on top + 6 on bottom = 7).
3. The number 6 should never be on top of the die facing 'up' (away from the grid).
4. The number 1 must be on top of the die when the goal location is reached.
"""

import math




class Dice:
    _slot_="north","south","east","west","top","bottom"
    def __init__(self):
        """
        This is constructor for Dice Object. Dice object represent Dice values on 6
        different direction. Top, Bottom, North, East, West, South
        Initially on Top will have 1, North will have 2 and East will have 3 value
        """
        self.north=2
        self.south=5
        self.east=3
        self.west=4
        self.top=1
        self.bottom=6

    def turn_right(self):
        """
        This function rotates dice to right direction
        :return: Nothing
        """
        temp1,temp2=self.west,self.east
        self.west,self.east=self.bottom,self.top
        self.top,self.bottom=temp1,temp2

    def turn_left(self):
        """
        This function rotates dice to left direction
        :return: Nothing
        """
        temp1,temp2=self.west,self.east
        self.west,self.east=self.top,self.bottom
        self.top,self.bottom=temp2,temp1

    def straight(self):
        """
        This function rotates dice in straight direction
        :return: Nothing
        """
        temp1,temp2=self.north,self.south
        self.north,self.south=self.top,self.bottom
        self.top,self.bottom=temp2,temp1

    def back(self):
        """
        This function rotates dice in backward direction
        :return: Nothing
        """
        temp1,temp2=self.north,self.south
        self.north, self.south=self.bottom,self.top
        self.top, self.bottom=temp1,temp2

    def copy(self,other):
        """
        This is copy function. Which copies values from dice object to 'other' dice object
        :param other: Dice Object
        :return: Nothing
        """
        other.north,other.south,other.west,other.east,other.top,other.bottom=\
            self.north,self.south,self.west,self.east,self.top,self.bottom

    def __eq__(self, other):
        """
        This function overrides equal function of python object. It checks if dice object
        has same directional configuration as 'other' dice object passed to function
        :param other: Dice object
        :return: Nothing
        """
        other.north, other.south, other.west, other.east, other.top, other.bottom == \
        self.north, self.south, self.west, self.east, self.top, self.bottom

    def __str__(self):
        """
        This function implements to string function of dice
        :return:
        """
        return "top ="+str(self.top)+" bottom ="+str(self.bottom)+" north = " \
                ""+str(self.north)+" south = "+str(self.south)+" west = "\
               +str(self.west)+" east = "+str(self.east)


class Node:

    _slot_="row","coll","dice","hCost","gCost","cost"


    def __init__(self,row,coll,actual_cost,hueristic_cost,dice):
        """
        This constructor initializes Node object. Which represents Each location in maze
        with Row, Column, Dice Configuration and different cost
        :param row: row of maze
        :param coll: column of maze
        :param actual_cost: Actual cost to reach at particular node from start location
        :param hueristic_cost: Hueristic cost from current node to Goal location
        :param dice: Dice configuration at that particular location
        """
        self.row=row
        self.coll=coll
        self.dice=dice
        self.gCost=actual_cost
        self.hCost=hueristic_cost
        self.cost=actual_cost+hueristic_cost


    ## Checking if two given objects are same
    def __eq__(self, other):
        return self.row==other.row and self.coll==other.coll and self.dice.__eq__(other.dice)

    def __str__(self):
        return str(self.row)+" "+str(self.coll)+" "+str(self.dice)
    ##



class Frontier:
    _slot_="heap","lookup","nodegenerated","visited"
    def __init__(self):
        self.heap=[]
        self.lookup={}
        self.nodegenerated=0
        self.visited=0

    def add(self,node):
        ## check if object is present in lookup
        flag = False
        if self.lookup.__contains__(str(node)):
            temp=self.lookup[str(node)]
            if temp.cost>node.cost:
                # remove node from heap
                self.lookup[str(node)] = node
                self.heap.remove(temp)
                for i in range(0, len(self.heap)):
                    if (self.heap[i].cost > node.cost):
                        self.heap.insert(i, node)
                        self.lookup[str(node)] = node
                        flag=True
                        break
                if flag is False:
                    self.heap.append(node)
                    self.lookup[str(node)] = node
                    self.nodegenerated = self.nodegenerated + 1
            else:
                return
        else:
            for i in range(0,len(self.heap)):
                if(self.heap[i].cost>node.cost):
                    self.heap.insert(i,node)
                    self.nodegenerated = self.nodegenerated + 1
                    self.lookup[str(node)]=node

                    flag=True
                    break
            if flag is False:
                self.heap.append(node)
                self.lookup[str(node)]=node
                self.nodegenerated=self.nodegenerated+1

    def isEmpty(self):
        return len(self.heap)==0

    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp= self.heap.pop(0)
            self.lookup.__delitem__(str(temp))
            self.visited=self.visited+1
            return temp


    def display(self):
        for temp in self.heap:
            print (temp)





front=Frontier()
visited ={}
parent = {}



## Heuristic Function
def heuristic(x1, y1, x2, y2, hName):
    '''/
    The heuristic distance is calculated - Euclidean distance
    :param x1: the x cordinate of the current node
    :param y1: the y coordinate of the current node
    :param x2: the x coordinate of the goal node
    :param y2: the y coordinate of the goal node
    :return: returns the heuristic value (euclidean distance)
    '''

    if hName == 1: #euclidean
        return math.sqrt(((x1-x2)**2)+(y1-y2)**2)
    elif hName == 2: #Manhatten
        return abs(x2-x1)+abs(y2-y1)
    else:
        return max(abs(x2-x1), abs(y2-y1))


## Finding The Start and End Location
def findStartGoalCoordinates(maze):
    '''
    This function is used for finding the START and GOAL coordinates.
    :param maze: Puzzle in the form of list
    :return: return a list with start and goal coordinates
    '''
    for row in range(0, len(maze)):
        for column in range(0, len(maze[row])):
            if maze[row][column]=='S':
                startRow = row
                startColumn = column
            if maze[row][column] == 'G':
                goalRow = row
                goalColumn = column

    return [startRow, startColumn, goalRow, goalColumn]

## Reading the Maze
def readPuzzle(maze1):
    #make a list of list to store the maze

    maze=[]

    #open the file
    file = open(maze1, 'r')

    #start reading the contents in it by looping it over the file
    for everyline in file:
        temp = []
        for everyValue in everyline:
            if everyValue!='\n':
                temp.append(everyValue)
        maze.append(temp)

    return maze

##Applying A*
def startPuzzle(startRow, startColumn, goalRow, goalColumn, maze, heuristicName):
    numberOfNodesvisited = 0

    IsGoal = False
    #front = Frontier()
    # for starting node, the g(n) will be 0 whereas the h(n) for starting node will be the euclidean distance
    # Calculate heuristic h(n) for the starting node by sending its coordinates to the heuristic function
    hCost = heuristic(startRow, startColumn, goalRow, goalColumn,heuristicName )
    gCost = 0

    # createNode of the Start Values given along with other values
    startNode = Node(startRow, startColumn, gCost, hCost, Dice())
    #print(Thedice.__str__())

    #add the start node into the priority queue(heap)
    front.add(startNode)

    #now, loop over the priority queue
    while len(front.heap) is not 0:
        #pop the smallest element from the priority queue
        poppedNode = front.pop()
        numberOfNodesvisited+=1
        visited[str(poppedNode)] = poppedNode

        #when you pop out, check if that is equal to the goal
        #if(checkForGoal(poppedNode, goalNode)):
        flag = checkForGoal(poppedNode, goalRow, goalColumn)


        if(flag):
            IsGoal=True
            break

        #now, check the north, south, east, west of this heap
        #first check if the coordinates are valid first for N, then S, then E, then W and then
        #find out there fCost and everything and then create a node and add it

        #---Checking validity of the popped node's children
        #North is row-1, column=column

        findAdjacentNodes(poppedNode, poppedNode.row-1, poppedNode.coll, maze, goalRow, goalColumn, "north", heuristicName)
        #Easta
        findAdjacentNodes(poppedNode, poppedNode.row, poppedNode.coll+1, maze, goalRow, goalColumn, "east", heuristicName)
        #West
        findAdjacentNodes(poppedNode, poppedNode.row, poppedNode.coll - 1, maze, goalRow, goalColumn, "west", heuristicName)
        #South
        findAdjacentNodes(poppedNode, poppedNode.row+1, poppedNode.coll, maze, goalRow, goalColumn, "south", heuristicName)

    if IsGoal:
        #bactract
        backTrack(poppedNode, startNode, maze)
        print("Number of nodes Generated:", front.nodegenerated)
        print("Number of nodes Visited:", front.visited)
        return True
    else:
        print("Number of moves: ", -1)
        print("Number of nodes generated:", front.nodegenerated)
        print("Number of nodes Visited:", front.visited)


    return False

def findAdjacentNodes(poppedNode, row, column, maze, goalRow, goalColumn, direction, hName):
    #check if present in visited
    #IsVisited = checkInVisited(row, column)
    #if IsVisited is False:
        #goalFound=False

    IsVisited = False
    IsValid = checkValidity(row, column, maze)

    #valid coordinates
    if IsValid:
        if maze[row][column]!='*':
            newDice = Dice()
            poppedNode.dice.copy(newDice)

            #check the direction first, north or south or east..blah blah
            if direction is "north":
                newDice.straight()
            if direction is "east":
                newDice.turn_right()
            if direction is "west":
                newDice.turn_left()
            if direction is "south":
                newDice.back()

        #IsVisited = checkInVisited(row, column, newDice)
            if newDice.top is not 6:
                #find the hCost and the gCost
                gCost = 1+poppedNode.gCost
                hCost = heuristic(row, column, goalRow, goalColumn, hName)

            #create the node here and add it into the heap(priority queue)
                newNode = Node(row, column,gCost, hCost,newDice)
                IsVisited=checkInVisited(newNode)
                    #first check if it is a goal node-->if goal node, then goal found, else add the node in the heap
                    #now add this newNode into the priority queue
                if(IsVisited is False):
                    front.add(newNode)
                    #make the row and column of newNode as string ans add it into the parent dictionary
                    addIntoParent(newNode, poppedNode)
                    #if newNode not in parent:
                else:
                    temp = visited[str(newNode)]
                    if temp.cost>newNode.cost:
                        front.add(newNode)
                        visited[str(newNode)]=newNode

    return IsVisited

def backTrack(goalNode, startNode, maze):

    numberOfMoves = 0
    stack = []
    temp = goalNode

    stack.append(str(goalNode))

    while str(temp)!=str(startNode):
        temp = parent[str(temp)]
        stack.append(temp)
        numberOfMoves+=1
    numberOfMoves+=1

    # node is str. Go to the visisted, take every node, convert into str, and check with its contents, if
    # found then then break it out, and use that node from the visited to print the maze.
    #stack.pop()
    while len(stack) != 0:
        # stack has str values of nodes
        val = stack.pop()
        temp = visited[str(val)]
        maze[temp.row][temp.coll] = 'O'
        displayMaze(temp,maze)

    print("The number of moves:", numberOfMoves)

def displayMaze(node, maze):

    for r in range(0, len(maze)):
        temp=[]
        for c in range(0, len(maze[0])):
            temp.append(maze[r][c])
        print(temp)

    print("\n--The maze and the configurations--")
    print("Coordinates:", node.row, " ", node.coll)
    print("configuration of the Dice!", "\n", "Top = ",node.dice.top, " East/Right = ", node.dice.east, " North/Up = ", node.dice.north, "\n")


def checkForGoal(poppedNode, goalRow, goalColumn):
    return poppedNode.row==goalRow and poppedNode.coll==goalColumn and poppedNode.dice.top==1

def addIntoParent(newNode, poppedNode):
    parent[str(newNode)]=str(poppedNode)

def checkInVisited( node):
    return visited.__contains__(str(node))

def checkValidity(row, column, maze):
    if row>=0 and row<len(maze) and column>=0 and column<len(maze[0]):
        return True
    else:
        return False

## Checking if solution Exist
def main():
    global front,parent,visited

    my_file=input('Enter the file name of puzzle : ')


    maze=readPuzzle(my_file)
    maze2=readPuzzle(my_file)
    maze3=readPuzzle(my_file)

    startRow, startColumn, goalRow, goalColumn = findStartGoalCoordinates(maze)
    # euclidean

    print("\n ------EUCLIDEAN------")
    goalFound = startPuzzle(startRow, startColumn, goalRow, goalColumn, maze, 1)
    #print(goalFound)


    #Manhatten
    #maze = readPuzzle()
    print("\n ------MANHATTAN------")

    front = Frontier()
    visited = {}
    parent = {}

    goalFound1 = startPuzzle(startRow, startColumn, goalRow, goalColumn, maze2, 2)
    #print(goalFound1)

    #Diagonal
    #maze = readPuzzle()
    print("\n ------DIAGONAL------")
    front = Frontier()
    visited = {}
    parent = {}
    goalFound2 = startPuzzle(startRow, startColumn, goalRow, goalColumn, maze3, 3)
    #print(goalFound2)


if __name__=='__main__':
    main()