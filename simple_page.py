import random
import tkinter as tk

GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
DELAY = 100


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Snake Game")
        self.canvas = tk.Canvas(
            root,
            width=GRID_WIDTH * GRID_SIZE,
            height=GRID_HEIGHT * GRID_SIZE,
            bg="black",
        )
        self.canvas.pack()
        self.root.bind("<KeyPress>", self.on_key_press)
        self.reset_game()
        self.running = True
        self.move_snake()

    def reset_game(self):
        self.direction = "Right"
        self.snake = [(5, 10), (4, 10), (3, 10)]
        self.place_food()
        self.score = 0
        self.canvas.delete("all")
        self.draw_objects()

    def place_food(self):
        while True:
            self.food = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1),
            )
            if self.food not in self.snake:
                break

    def on_key_press(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Return" and not self.running:
            self.running = True
            self.reset_game()
            self.move_snake()

    def move_snake(self):
        if not self.running:
            return
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1
        elif self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1

        new_head = (head_x, head_y)

        if (
            head_x < 0
            or head_x >= GRID_WIDTH
            or head_y < 0
            or head_y >= GRID_HEIGHT
            or new_head in self.snake
        ):
            self.game_over()
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

        self.draw_objects()
        self.root.after(DELAY, self.move_snake)

    def draw_objects(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            8,
            8,
            anchor="nw",
            text=f"Score: {self.score}",
            fill="white",
            font=("Arial", 12, "bold"),
        )
        self.canvas.create_rectangle(
            1,
            1,
            GRID_WIDTH * GRID_SIZE - 1,
            GRID_HEIGHT * GRID_SIZE - 1,
            outline="#303030",
        )

        for x, y in self.snake:
            self.draw_cell(x, y, "lime")

        food_x, food_y = self.food
        self.draw_cell(food_x, food_y, "red")

    def draw_cell(self, x, y, color):
        self.canvas.create_rectangle(
            x * GRID_SIZE,
            y * GRID_SIZE,
            x * GRID_SIZE + GRID_SIZE,
            y * GRID_SIZE + GRID_SIZE,
            fill=color,
            outline="#101010",
        )

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            GRID_WIDTH * GRID_SIZE / 2,
            GRID_HEIGHT * GRID_SIZE / 2 - 20,
            text="Game Over",
            fill="red",
            font=("Arial", 28, "bold"),
        )
        self.canvas.create_text(
            GRID_WIDTH * GRID_SIZE / 2,
            GRID_HEIGHT * GRID_SIZE / 2 + 20,
            text="Press Enter to restart",
            fill="white",
            font=("Arial", 14),
        )


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()
