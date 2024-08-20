import random

class Grid:
    def __init__(self, grid_size: int):
        self.grid = [[0] * grid_size for _ in range(grid_size)]
        self.grid_size = grid_size

    def spawn_random(self):
        empty_cells = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size) if self.grid[x][y] == 0]
        if not empty_cells:
            return
        pos_x, pos_y = random.choice(empty_cells)
        value = 4 if random.random() <= 0.10 else 2
        self.grid[pos_x][pos_y] = value

    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.grid_size - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(self.grid_size - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(self):
        for i in range(self.grid_size):
            self.grid[i] = self.compress(self.grid[i])
            self.grid[i] = self.merge(self.grid[i])
            self.grid[i] = self.compress(self.grid[i])

    def move_right(self):
        for i in range(self.grid_size):
            self.grid[i] = self.compress(self.grid[i][::-1])
            self.grid[i] = self.merge(self.grid[i])
            self.grid[i] = self.compress(self.grid[i])
            self.grid[i] = self.grid[i][::-1]

    def move_up(self):
        self.grid = [list(row) for row in zip(*self.grid)]
        self.move_left()
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_down(self):
        self.grid = [list(row) for row in zip(*self.grid)]
        self.move_right()
        self.grid = [list(row) for row in zip(*self.grid)]

    def move(self, direction: chr):
        if direction == 'l':
            self.move_left()
        elif direction == 'r':
            self.move_right()
        elif direction == 'u':
            self.move_up()
        elif direction == 'd':
            self.move_down()
        else:
            print("Unknown direction " + direction)

    def print(self):
        for row in self.grid:
            print(row)

