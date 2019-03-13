from square import *

class Grid:

    def __init__(self, x_amount, y_amount):
        self.grid = [[Square(x, y, 10, 10) for x in range(x_amount)] for y in range(y_amount)]
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                if y > 0:
                    cell.neighbours.append(self.grid[y-1][x])
                if y < y_amount - 1:
                    cell.neighbours.append(self.grid[y+1][x])
                if x > 0:
                    cell.neighbours.append(self.grid[y][x-1])
                if x < x_amount - 1:
                    cell.neighbours.append(self.grid[y][x+1])

    def show(self):
        pass