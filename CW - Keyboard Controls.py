import pgzrun
import random

score = 0

WIDTH = 800
HEIGHT = 450
TITLE = 'Bee Game'

bee = Actor('bee')
bee.pos = (100, 100)

flower = Actor('flower')
flower.pos = (200, 400)

isGameOver = False

def flowerPos():
    flower.pos = (random.randint(50, 750), random.randint(50, 400))

def update():
    global score
    
    if keyboard.left:
        bee.x -= 5
    elif keyboard.right:
        bee.x += 5
    elif keyboard.up:
        bee.y -= 5
    elif keyboard.down:
        bee.y += 5
    
    isCollided = bee.colliderect(flower)
    #print(isCollided)

    if isCollided:
        flowerPos()
        score += 1

def endGame():
    global isGameOver
    isGameOver = True

def draw():
    screen.blit('background', (0, 0))

    bee.draw()
    flower.draw()

    screen.draw.text(f'Score: {score}', (50, 50))

    if isGameOver:
        screen.fill('black')
        screen.draw.text(f'GAME OVER, YOUR SCORE IS {score}', (300, 225))

clock.schedule(endGame, 60)
pgzrun.go()