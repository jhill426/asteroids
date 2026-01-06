# Asteroids

A Python implementation of the _classic_ Asteroids arcade game using Pygame.

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

```bash
git clone <repo-url>
cd asteroids
uv sync
```

To install uv if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Running the Game

```bash
uv run python main.py
```

## Controls

| Key      | Action                        |
| -------- | ----------------------------- |
| A        | Rotate ship counter-clockwise |
| D        | Rotate ship clockwise         |
| W        | Move Ship Up                  |
| S        | Move Ship Down                |
| Spacebar | Shoot projecticles            |

## Features

- Classic Asteroids-style physics with momentum
- Screen wrapping for player and asteroids
- Asteroids split into smaller pieces when destroyed
- Shooting cooldown system

## Project Structure

```
asteroids/
├── main.py          # Game loop and initialization
├── player.py        # Player ship logic
├── asteroid.py      # Asteroid behavior
├── asteroidfield.py # Asteroid spawning
├── shot.py          # Bullet mechanics
├── circleshape.py   # Base collision shape
└── constants.py     # Game configuration
```
