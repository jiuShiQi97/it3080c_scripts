# My Github repo for IT3038C

### LAB 7 
hi
Here is how you can run a Python script that I created, which uses a plugin called Pygame. 
First, let's create a Virtual ENV called scripts. You can call it whatever you want.

```bash
virtualenv ~/venv/pygame
source ~/venv/scripts/bin/activate
pip install (PyGame -1.9.6-cp37-cp37m-win_amd64.whl)"
```
(The parentheses are for the version of PyGame you installed)

Now, you can use pygame to create and decorate your game! You can use it for define color, set Fonts, create game playSurface and set time for your game.

First, in Python, run the following code
```python
import pygame
from pygame.locals import *
```

The syntax above will load the pygame and all your needs. Now we can run several commands to define colors. You just need to put the value of the RGB color in the following parentheses, like this:
```python
ballColour = pygame.Color(0,245,0)
```

Let's set our game Over Font for example:
```python
gameOverFont = pygame.font.SysFont('Times New Roman .fon',120) #font and size
```

We also can add time clock for our game:
```python
def main():
    # init pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
```

Finally, we can add them all in a playSurface and when we quit then gameover:

```python
playSurface = pygame.display.set_mode((1000,800))
ballPosition = [300,300] #init ball position
ballSpawned = 1 #number
  for event in pygame.event.get():
            if event.type == QUIT:
            gameOver(playSurface)
        # Clock
        fpsClock.tick(5)
```

I hope that was fun. Don't forget to deactivate your virtualenv when you're done.
```bash
quit()
deactivate
```
