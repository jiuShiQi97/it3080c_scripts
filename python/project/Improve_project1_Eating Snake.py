import pygame,sys,time,random
from pygame.locals import *

# define color
ballColour = pygame.Color(245,0,0)
#bgColour = pygame.Color(0,0,0)
snakeColour = pygame.Color(255,255,255)
wordColour = pygame.Color(255,255,255)

# define game over fanction
# def gameOver(playSurface):
#     gameOverFont = pygame.font.Font('Times New Roman .fon',120)
#     gameOverSurf = gameOverFont.render('Game Over', True, wordColour)
#     gameOverRect = gameOverSurf.get_rect()
#     gameOverRect.midtop = (320, 100)
#     playSurface.blit(gameOverSurf, gameOverRect)
#     pygame.display.flip()
#     time.sleep(5)
#     pygame.quit()
#     sys.exit()

# find a better way to define gameOver fanction
def gameOver(playSurface,score):
    gameOverFont = pygame.font.SysFont('Times New Roman .fon',120) #font and size
    gameOverSurf = gameOverFont.render('Game Over!', True, wordColour) #game over
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (695, 10) #show position
    playSurface.blit(gameOverSurf, gameOverRect)
    scoreFont = pygame.font.SysFont('Times New Roman .fon',60) #show score
    scoreSurf = scoreFont.render('Score:'+str(score), True, wordColour)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (695, 100)
    playSurface.blit(scoreSurf, scoreRect)
    pygame.display.flip() #reflesh
    time.sleep(5) #Sleep 5s and exit
    pygame.quit()
    sys.exit()

# difine main fanction
def main():
    # init pygame
    pygame.init()
    #setting = Settings()
    pygame.mixer.init()
    fpsClock = pygame.time.Clock()
    # create pygame layer
    playSurface = pygame.display.set_mode((1391,780))
    pygame.display.set_caption('Wenhan Eating Snake')
    #New! Add background
    screen = pygame.display.set_mode((1391,780))
    bg = pygame.image.load('bg.jpg')
    #screen = pygame.display.set_mode(())
    # New! Add game icon
    image = pygame.image.load('icon.ico')
    pygame.display.set_icon(image)
    # New! Add bgm
    pygame.mixer.music.load("bgm.mp3")

    # Initialize variable
    snakePosition = [100,100]
    snakeSegments = [[100,100],[80,100],[60,100]]
    ballPosition = [300,300] #init ball position
    ballSpawned = 1 #number
    direction = 'right' #init derection
    changeDirection = direction
    score = 0 #init score
    while True:
        # New! play music!
        if pygame.mixer.music.get_busy()==False:
            pygame.mixer.music.play()
        # New! Add bg
        screen.blit(bg,(0,0))
        # check pygame action
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # input keyboard action
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # determine if the wrong derection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        # change derection
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
        # increase snake length
        snakeSegments.insert(0,list(snakePosition))
        # detemine eat ball
        if snakePosition[0] == ballPosition[0] and snakePosition[1] == ballPosition[1]:
            ballSpawned = 0
        else:
            snakeSegments.pop()
        # reborn balls
        if ballSpawned == 0:
            x = random.randrange(1,30)
            y = random.randrange(1,23)
            ballPosition = [int(x*20),int(y*20)]
            ballSpawned = 1
            score += 1
        # drew pygame layer
        #playSurface.fill(bgColour)
        for position in snakeSegments:
            pygame.draw.rect(playSurface,snakeColour,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,ballColour,Rect(ballPosition[0], ballPosition[1],20,20))

        # reflesh pygame layer
        pygame.display.flip()

        # determine dead
        if snakePosition[0] > 1391 or snakePosition[0] < 0:
            gameOver(playSurface,score)
        if snakePosition[1] > 780 or snakePosition[1] < 0:
            gameOver(playSurface,score)
        for snakeBody in snakeSegments[1:]:#if reach itself
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface,score)

        # New!! Game speed increases with the length of the snake
        if len(snakeSegments) < 40:
            speed = 6 + len(snakeSegments) // 2
        else:
            speed = 16
        fpsClock.tick(speed)

if __name__ == "__main__":
    main()
