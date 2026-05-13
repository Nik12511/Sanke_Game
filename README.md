# Simple Snake Game

This project contains a simple Snake game implemented in Python using the `tkinter` GUI library.

## Files

- `simple_page.py` - The main Python file that implements the game.

## Basic Concepts

### 1. Game grid
The game runs on a grid defined by these constants:
- `GRID_SIZE` - size of each square cell in pixels.
- `GRID_WIDTH` - number of cells horizontally.
- `GRID_HEIGHT` - number of cells vertically.
- `DELAY` - the time in milliseconds between snake moves.

The canvas size is calculated as `GRID_WIDTH * GRID_SIZE` by `GRID_HEIGHT * GRID_SIZE`.

### 2. Snake representation
The snake is represented by a list of coordinate tuples called `self.snake`.
- Each tuple is `(x, y)`.
- The first tuple is the snake head.
- New positions are inserted at the front of the list.
- The tail is removed when the snake moves without eating food.

### 3. Food
Food is a single coordinate tuple stored in `self.food`.
- It is placed randomly using `random.randint` within the grid.
- If the food appears on the snake, a new position is chosen.

### 4. Direction and movement
The snake direction is stored in `self.direction`.
- Possible values: `"Up"`, `"Down"`, `"Left"`, `"Right"`.
- The player changes direction with arrow keys.
- The game prevents reversing direction immediately.

## Main Methods

### `__init__(self, root)`
- Initializes the `tkinter` window and canvas.
- Binds keyboard events to `self.on_key_press`.
- Calls `reset_game()` to start the game.
- Starts the movement loop by calling `self.move_snake()`.

### `reset_game(self)`
- Resets the game state.
- Sets the starting snake position and direction.
- Places the first food item.
- Resets the score.
- Clears and redraws the canvas.

### `place_food(self)`
- Chooses a random empty cell for food.
- Ensures the food does not appear on the snake.

### `on_key_press(self, event)`
- Handles key input from the player.
- Updates the snake direction with arrow keys.
- Restarts the game if `Enter` is pressed after game over.

### `move_snake(self)`
- Moves the snake one cell in the current direction.
- Checks for wall collisions or self-collision.
- Ends the game if a collision happens.
- If the snake eats food, the score increases and new food is placed.
- Otherwise, the tail cell is removed to keep the snake length.
- Redraws the game board and schedules the next move.

### `draw_objects(self)`
- Clears the canvas and redraws the score, border, snake, and food.
- Calls `draw_cell()` for each snake segment and the food cell.

### `draw_cell(self, x, y, color)`
- Draws a colored square at grid coordinate `(x, y)`.
- Uses the cell size to convert grid coordinates into pixel positions.

### `game_over(self)`
- Stops the game loop by setting `self.running = False`.
- Displays `Game Over` and restart instructions on the canvas.

## How to Run

Open a terminal in this project folder and run:

```bash
python simple_page.py
```

Use the arrow keys to move the snake.
When the game ends, press `Enter` to restart.
