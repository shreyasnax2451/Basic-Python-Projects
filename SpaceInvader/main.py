import pygame as py, random, math
from pygame import mixer

py.init()

screen = py.display.set_mode((800, 600))

def player(x_cor, y_cor):
    screen.blit(player_icon, (x_cor, y_cor))

def enemy(x_cor, y_cor,i):
    screen.blit(enemy_icon[i], (x_cor, y_cor))

def fire_bullet(x_cor, y_cor):
    global bullet_state
    bullet_state = 'Fire'
    screen.blit(bullet_icon, (x_cor + 16, y_cor + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX-enemyX,2) + math.pow(bulletY-enemyY,2))
    if distance < 27:
        return True
    return False

def show_score(x, y):
    final_score = text_font.render('Score : ' + str(score), True, (255, 255, 255))
    screen.blit(final_score, (x, y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


py.display.set_caption('Space Invader')
py.display.set_icon(py.image.load('SpaceInvader/startup.png'))
background = py.image.load('SpaceInvader/wepik-export-20240202190506pT4D.jpeg')

mixer.music.load('SpaceInvader/background.wav')
mixer.music.play(-1)

player_icon = py.image.load('SpaceInvader/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

enemy_icon = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemy_icon.append(py.image.load('SpaceInvader/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.15)
    enemyY_change.append(30)

bullet_icon = py.image.load('SpaceInvader/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.6
bullet_state = 'Ready'

score = 0
text_font = py.font.Font('freesansbold.ttf',32)
game_over_font = py.font.Font('freesansbold.ttf',64)

textX = 10
textY =10

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 

        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                playerX_change = -0.3
            if event.key == py.K_RIGHT:
                playerX_change = 0.3

            if event.key == py.K_UP:
                playerY_change = -0.3
            if event.key == py.K_DOWN:
                playerY_change = 0.3
            
            if event.key == py.K_SPACE:
                if bullet_state == 'Ready':
                    bullet_sound = mixer.Sound('SpaceInvader/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT or event.key == py.K_UP or event.key == py.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    for i in range(number_of_enemies):

        if enemyY[i] > 450:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.15
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.15
            enemyY[i] += enemyY_change[i]
        
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('SpaceInvader/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = 'Ready'
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'Ready'

    if bullet_state == 'Fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    py.display.update()