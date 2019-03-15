class Pile:
    def __init__(self):
        self.cells = []

    def add_block(self, block):
        for cell in block.cells:
            self.cells.append(cell)
            cell.piled = True