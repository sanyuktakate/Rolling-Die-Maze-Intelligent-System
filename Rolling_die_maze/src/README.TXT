Required software to run this project
--Python 3.5

Run the rdmaze.py program on terminal or command prompt or on any python IDE

Program will ask to enter file name in which Maze Puzzle is written.
(Program expect input to be in specified format "." for path "*" for obstacle
S for start location, G for Goal Location)

Program will print solution for puzzle if there is path else it will print Number of Moves as -1 and will print number of nodes generated and visited for this puzzle

If there is path for given puzzle

Program will first print 3 solution using 3 diffent Heuristic Function 
1) Euclidian
2) Manhattan
3) Diagonal

Program will print step by step path taken by program along the maze.
The maze will have following information for each step 
--Coodinates taken for particular step
--Dice Configuration at that location
--Maze Path using character "O" in maze

When program will reach at Goal Location with 1 value on top 
it will print following information
--The number of moves required to reach at goal location
--The number of nodes generated during process
--The number of nodes visited by algorithm 

Sample Output for Puzzle 

S...G
.....

Enter the file name of puzzle : Puzzle6.txt

 ------EUCLIDEAN------ (Path for Euclidian Heuristic)
['O', '.', '.', '.', 'G'] 
['.', '.', '.', '.', '.']

--The maze and the configurations--
Coordinates: 0   0
configuration of the Dice! 
 Top =  1  East/Right =  3  North/Up =  2 

['O', '.', '.', '.', 'G']
['O', '.', '.', '.', '.']

--The maze and the configurations--
Coordinates: 1   0
configuration of the Dice! 
 Top =  2  East/Right =  3  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', '.', '.', '.']

--The maze and the configurations--
Coordinates: 1   1
configuration of the Dice! 
 Top =  4  East/Right =  2  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', '.', '.']

--The maze and the configurations--
Coordinates: 1   2
configuration of the Dice! 
 Top =  5  East/Right =  4  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', 'O', '.']

--The maze and the configurations--
Coordinates: 1   3
configuration of the Dice! 
 Top =  3  East/Right =  5  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', 'O', 'O']

--The maze and the configurations--
Coordinates: 1   4
configuration of the Dice! 
 Top =  2  East/Right =  3  North/Up =  6 

['O', '.', '.', '.', 'O']
['O', 'O', 'O', 'O', 'O']

--The maze and the configurations--
Coordinates: 0   4
configuration of the Dice! 
 Top =  1  East/Right =  3  North/Up =  2 

The number of moves: 7
Number of nodes Generated: 22
Number of nodes Visited: 15

 ------MANHATTAN------  (Path for Manhattan Heuristic)
['O', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']

--The maze and the configurations--
Coordinates: 0   0
configuration of the Dice! 
 Top =  1  East/Right =  3  North/Up =  2 
['O', '.', '.', '.', 'G']
['O', '.', '.', '.', '.']

--The maze and the configurations--
Coordinates: 1   0
configuration of the Dice! 
 Top =  2  East/Right =  3  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', '.', '.', '.']

--The maze and the configurations--
Coordinates: 1   1
configuration of the Dice! 
 Top =  4  East/Right =  2  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', '.', '.']

--The maze and the configurations--
Coordinates: 1   2
configuration of the Dice! 
 Top =  5  East/Right =  4  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', 'O', '.']

--The maze and the configurations--
Coordinates: 1   3
configuration of the Dice! 
 Top =  3  East/Right =  5  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', 'O', 'O']

--The maze and the configurations--
Coordinates: 1   4
configuration of the Dice! 
 Top =  2  East/Right =  3  North/Up =  6 

['O', '.', '.', '.', 'O']
['O', 'O', 'O', 'O', 'O']

--The maze and the configurations--
Coordinates: 0   4
configuration of the Dice! 
 Top =  1  East/Right =  3  North/Up =  2 

The number of moves: 7
Number of nodes Generated: 22
Number of nodes Visited: 15

 ------DIAGONAL------ (Path for Diagonal Heuristic)
['O', '.', '.', '.', 'G']
['.', '.', '.', '.', '.']

--The maze and the configurations--
Coordinates: 0   0
configuration of the Dice! 
 Top =  1  East/Right =  3  North/Up =  2 

['O', '.', '.', '.', 'G']
['O', '.', '.', '.', '.']

--The maze and the configurations--
Coordinates: 1   0
configuration of the Dice! 
 Top =  2  East/Right =  3  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', '.', '.', '.']

--The maze and the configurations--
Coordinates: 1   1
configuration of the Dice! 
 Top =  4  East/Right =  2  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', '.', '.']

--The maze and the configurations--
Coordinates: 1   2
configuration of the Dice! 
 Top =  5  East/Right =  4  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', 'O', '.']

--The maze and the configurations--
Coordinates: 1   3
configuration of the Dice! 
 Top =  3  East/Right =  5  North/Up =  6 

['O', '.', '.', '.', 'G']
['O', 'O', 'O', 'O', 'O']

--The maze and the configurations--
Coordinates: 1   4
configuration of the Dice! 
 Top =  2  East/Right =  3  North/Up =  6 

['O', '.', '.', '.', 'O']
['O', 'O', 'O', 'O', 'O']

--The maze and the configurations--
Coordinates: 0   4
configuration of the Dice! 
 Top =  1  East/Right =  3  North/Up =  2 

The number of moves: 7
Number of nodes Generated: 22
Number of nodes Visited: 15

