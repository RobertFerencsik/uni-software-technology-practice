# Snake Game (Python)

The project is the classic snake game in python.

## Description

The purpose of this game is to control the snake and collect as much as food as possible without hitting a wall or yourself.

The project was made in Python with the use of the Pygame library.

## Functions

- Controllable snake
- Randomly appearing food
- Randomly appearing powerups
- Score calculation
- Snake growth after eating food
- Collision detection
- Game Over screen
- Restart option

## Setup the Game and Execution

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
- Clone the Repository:
        git clone https://github.com/RobertFerencsik/uni-software-technology-practice.git

Then navigate into the project folder:
        cd uni-software-technology-practice


OR

- Manual Download:
1. Visit the repository link in your browser.
2. Click the blue "<> Code" button.
3. Select "Download ZIP".
4. Extract the ZIP file to your preferred location.

- Install the required dependencies:

        pip install -r requirements.txt

### Running the Game
        python main.py

### Controls
W, A, S, D - Move the snake (Up, Down, Left, Right)

P - Pause/Unpause the game

R - Restart the game (during play or after Game Over)

ESC - Exit the game

### Gameplay Features and Power-ups
#### Food
- Color: Red
- Effect: Increases the snake's length and score.
- Spawning: Appears at a random empty position on the board.

#### Power-ups
The game attempts to spawn a power-up every 100 ticks. A maximum of 2 power-ups can be active on the field at once.

- Shorten (Shrink)
    - Color: Gold/Orange
    - Effect: Instantly reduces the snake's current length by 30%.

- Slow
    - Color: Blue
    - Effect: Slows down the game logic for 10 seconds, making the snake easier to control.

### Testing
The project uses pytest for unit testing the core logic (movement, collisions, rendering). To run the tests, use:
            pytest

## Screenshots

<img width="1290" height="765" alt="image" src="https://github.com/user-attachments/assets/5c9a0cae-1575-4217-928f-f97e4b701869" />

<img width="1293" height="772" alt="image" src="https://github.com/user-attachments/assets/a4a6cc4c-6ea7-4fb4-964a-6f35e0c26edc" />

<img width="1288" height="764" alt="image" src="https://github.com/user-attachments/assets/2b59ece2-949f-48f9-aa7b-a4a89b2a97a0" />


## Authors
- Csáki Gergely
- Ferencsik Róbert
- Gyöngyösi Dóra Imola
- Krusó Panna
- Marót Máté
