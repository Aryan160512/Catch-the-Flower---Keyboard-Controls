import pgzrun
import random

score = 0

WIDTH = 800
HEIGHT = 600
TITLE = 'Catch the Villian Game'

spiderman = Actor('spiderman')
spiderman.pos = (50, 550)

greenGoblin = Actor('green goblin')
greenGoblin.pos = (300, 200)

isGameOver = False

def greenGoblinPos():
    greenGoblin.pos = (random.randint(50, 750), random.randint(50, 550))

def update():
    global score

    if keyboard.a:
        spiderman.x -= 5
    elif keyboard.d:
        spiderman.x += 5
    elif keyboard.w:
        spiderman.y -= 5
    elif keyboard.s:
        spiderman.y += 5

    isCollided = spiderman.colliderect(greenGoblin)

    if isCollided:
        greenGoblinPos()
        score += 1

def endGame():
    global isGameOver
    isGameOver = True

def draw():
    screen.blit('cityscape', (0, 0))

    spiderman.draw()
    greenGoblin.draw()

    screen.draw.text(f'Score: {score}', (50, 50), color='black')

    if isGameOver:
        screen.fill('black')
        screen.draw.text(f'GAME OVER, YOUR SCORE IS {score}', (300, 225))

clock.schedule(endGame, 60)
pgzrun.go()

