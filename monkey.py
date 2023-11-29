



import random
class Room:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['.' for _ in range(cols)] for _ in range(rows)]
        self.monkey_row = random.randint(0, rows - 1)
        self.monkey_col = random.randint(0, cols - 1)
        self.banana_row = random.randint(0, rows - 1)
        self.banana_col = random.randint(0, cols - 1)
        self.chair_row = random.randint(0, rows - 1)
        self.chair_col = random.randint(0, cols - 1)
        self.grid[self.monkey_row][self.monkey_col] = 'M'
        self.grid[self.banana_row][self.banana_col] = 'B'
        self.grid[self.chair_row][self.chair_col] = 'C'
    def print_room(self):
        for row in self.grid:
            print(' '.join(row))
        print()
    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    def move_monkey(self, direction):
        new_monkey_row = self.monkey_row
        new_monkey_col = self.monkey_col
        if direction == 'up':
            new_monkey_row -= 1
        elif direction == 'down':
            new_monkey_row += 1
        elif direction == 'left':
            new_monkey_col -= 1
        elif direction == 'right':
            new_monkey_col += 1
        if self.is_valid_move(new_monkey_row, new_monkey_col):
            self.grid[self.monkey_row][self.monkey_col] = ' '
            self.monkey_row = new_monkey_row
            self.monkey_col = new_monkey_col
            self.grid[self.monkey_row][self.monkey_col] = 'M'

def main():
    rows = int(input("Enter Width of Room :"))
    cols = int(input("Enter Length of Room :"))
    room = Room(rows, cols)
    print("Monkey and Banana Problem!")
    steps = 0
    while (room.monkey_row, room.monkey_col) != (room.chair_row, room.chair_col):
        print("Current Room:")
        room.print_room()
        move = input("Enter your Move : ").lower()
        if move in ['up', 'down', 'left', 'right']:
            room.move_monkey(move)
            steps += 1
        else:
            print("Invalid Move!!")
    if (room.monkey_row, room.monkey_col) == (room.chair_row, room.chair_col):
        print("Monkey reached the Chair!")
        print(f"Steps taken : {steps}")
    while (room.monkey_row, room.monkey_col) != (room.banana_row, room.banana_col):
        print("Current Room:")
        room.print_room()
        move = input("Enter your Move : ").lower()
        if move in ['up', 'down', 'left', 'right']:
            room.move_monkey(move)
            steps += 1
        else:
            print("Invalid move!!")
    if (room.monkey_row, room.monkey_col) == (room.banana_row, room.banana_col):
        print("Congratulations, Monkey collected the Banana!!")
        print(f"Total Steps taken : {steps}")
if __name__ == "__main__":
    main()
