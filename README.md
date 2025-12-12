# Tanks – Python Arcade Game

## Description

This is a simple tank simulation game built with the Python Arcade framework.
The player controls a green tank that rotates and moves in the direction of its turret.

The game demonstrates:

* sprite animation for the tank
* movement and rotation using trigonometry
* key press and key release handling

## Requirements

* Python 3.8+
* arcade library (`pip install arcade==2.6.17`)
* image assets:

```
green.png       # tank sprite
background.png  # map background
```

## Controls

| Key | Action            |
| --- | ----------------- |
| ←   | Rotate tank left  |
| →   | Rotate tank right |
| ↑   | Move forward      |
| ↓   | Move backward     |

## Code Structure

### 1. `main.py`

* Main class Game inherits from `arcade.Window`.
* Methods:

  * `on_draw()` - draws the background and tank
  * `on_key_press()` - detects key presses
  * `on_key_release()` - stops movement when key is released
  * `update()` - updates the tank's position

### 2. `green_tank.py`

* Green_Tank class inherits from `arcade.Sprite`.
* Handles tank movement and rotation in the direction of its turret.
* The `update()` method calculates the new position using trigonometry:

```python
self.part_x = math.cos(math.radians(self.angle))
self.part_y = math.sin(math.radians(self.angle))
self.center_x += self.part_x * self.change_x
self.center_y += self.part_y * self.change_y
```

This ensures the tank moves in the direction it is facing.

## How to Run the Game

1. Make sure Python and the `arcade` library are installed:

```bash
pip install arcade==2.6.17
```

2. Place the image assets (`green.png`, `background.png`) in the same folder as `main.py`.

3. Run the game:

```bash
python main.py
```

4. Control the tank using the arrow keys.
