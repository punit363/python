# Find the shortest path in a maze
# using breadth first algorithm
# create a maze using '#' -> obstacles, '" "' -> path, "O" -> start and "X" -> end
# create two functions to find start and end positions
# create a function to find neighbours of current positions
# create a function to find the shortest path
# in the shortest path function start with putting a tuple in the queue with the starting_position and path_list 
# start processing the queue
# processing:- 
# check if it is the end and return path
# else find its immediate neighbours
# reject # and if present in visited set
# if " " add to queue with path extended with this address
# reprocess the queue
# use curse and reprint the maze after each iteration


import queue
import curses
from curses import wrapper
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i, j*2, "+", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)

def find_start(maze, start):
    for i, rows in enumerate(maze):
        for j, value in enumerate(rows):
            if value == start :
                return i, j
      
def find_neighbors(maze, row, col):
    neighbours = []

    # UP
    if row > 0:
        neighbours.append((row - 1, col))
    # DOWN
    if row < len(maze):
        neighbours.append((row + 1, col))
    # LEFT
    if col > 0:
        neighbours.append((row, col - 1))
    # RIGHT
    if col < len(maze):
        neighbours.append((row, col + 1))

    return neighbours
            
def find_shortest_path(maze, stdscr):
    start = "O"
    end = "X"

    starting_position = find_start(maze,start)

    q = queue.Queue()

    q.put((starting_position,[starting_position]))

    visited = set()

    while not q.empty():
        position, shortest_path = q.get()
        row, col = position

        stdscr.clear()
        print_maze(maze, stdscr, shortest_path)    
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return shortest_path
            
        neighbors = find_neighbors(maze, row, col)

        for neighbor in neighbors:

            if neighbor in visited:
                continue

            neighbor_row, neighbor_col = neighbor

            if maze[neighbor_row][neighbor_col] == "#":
                continue

            new_shorteset_path = shortest_path + [neighbor]
            q.put((neighbor,new_shorteset_path))
            visited.add(neighbor)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    find_shortest_path(maze, stdscr)
    stdscr.getch()

wrapper(main)