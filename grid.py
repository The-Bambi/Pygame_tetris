from cell import *

class Grid:

    def __init__(self, x_amount, y_amount, screen):
        self.grid = [[Cell(x*29, y*29, 30, 30, screen) for x in range(x_amount)] for y in range(y_amount)]
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                if y > 0:
                    cell.up = self.grid[y-1][x]
                if y < y_amount - 1:
                    cell.down = self.grid[y+1][x]
                if x > 0:
                    cell.left = self.grid[y][x-1]
                if x < x_amount - 1:
                    cell.right = self.grid[y][x+1]

    def show(self):
        for line in self.grid:
            for cell in line:
                cell.show()