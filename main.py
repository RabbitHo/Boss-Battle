
################################################# SORCERERS CLASH #################################################################

#################################################### VARIABLES #####################################################################
import pygame
pygame.init()
import math
import sys
import random

WIDTH = 800
HEIGHT = 800

FPS = 30

BLUE = (0, 0, 255)
LIGHTBLUE = (111, 150, 247)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (252, 211, 3)
PINK = (252, 3, 198)
GREEN = (28, 235, 107)

BUTTON_HOVER_COLOR = (245, 176, 66)
BUTTON_CLICK_COLOR = (255, 64, 239)
BUTTON_COLOR = BLUE

WEAPON_BUTTON_COLOR = RED
BOW_BUTTON_COLOR = RED
BOOMRNG_BUTTON_COLOR = RED
GUIDE_BUTTON_COLOR = BLUE
HOME_BUTTON_COLOR = BLUE
leaveButton_color = BLUE

leftHolding = False
rightHolding = False

button_width = 200
button_height = 75
button_text = "START"
font_size = 50
button_x = 280
button_y = 480
button_clicked = False
button_hover = 0

fromGuide = False
guide_clicked = False
guide_hover = False

home_clicked = False
fromHome = False

X_clicked = False

menu = False
escape_pressed = False
escape_holding = False

title_text = "SORCERERS CLASH"

boss_animation_count = 0
boss_animation_count2 = 5
boss_animation_count3 = 0
bossX2 = 5
bossY2 = 400
boss_flipped = False
sidekickHealth = 100

weapon_choice = 0
SWORD = 1
BOW = 2
BOOMRNG = 3

sword_swing = False
rotation_speed = 3

moving_left = False
moving_right = False

radius = 0

choice = 2

playerSpeed = 10

animation_count = 0
dmg_animation_count = 0

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorcerers Clash")

clock = pygame.time.Clock()

playerImage = pygame.image.load("character.png")

playerWidth = playerImage.get_rect().width
playerHeight = playerImage.get_rect().height

playerX = WIDTH // 2 - playerWidth // 2
playerY = HEIGHT * 3 // 4 + playerHeight // 2

player_pos = (playerX, playerY)

player_rect = playerImage.get_rect(center=player_pos)

gravity = 10
ground_y = playerY
jump_height = 20
jump_speed = 50
jump_count = 0
vel_y = jump_height
fall_speed = 1
falling = False
jumping = False

added_y = 0

hit = False

bow_number = 0
bow_shoot = False
shoot_arrow = False
allow_angle = True

is_fired = False
arrow_speed = 15

arrowUnchanged = pygame.image.load("arrow.png").convert_alpha()
arrowImageUnrotated = pygame.transform.scale(arrowUnchanged, (85, 30))
arrowImage = pygame.transform.rotate(arrowImageUnrotated, 5)

arrow_rect = pygame.Rect(30, 20, 25, 25)

boomrngImage = pygame.image.load("boomerang.png")
boomrng_rect = boomrngImage.get_rect()

boomrngX = playerX
boomrngY = playerY

boomrng_shoot = False
boomrng_spin = 0
boomrng_speed = 15
allow_aim = True
fly_back = False
boomrng_hit = False

spaceHolding = False

playerAnimation = False

backgroundImage = pygame.image.load("background.png")

new_width = 120
new_height = 100

bossImageUnsized = pygame.image.load("boss.png")
bossImage = pygame.transform.scale(bossImageUnsized, (new_width, new_height))

playerFlipped = False

playerHealth = 100
bossHealth = 200

playerGotHit = False

boss_pos = (350, 400)

bossX = 350
bossY = 400

attackChoice = 0
ATTACKLEFT = 2
ATTACKRIGHT = 4
ATTACKUP = 6
ATTACKDOWN = 9
EVERYWHERE = 10
STUNNED = 12

bossFly2 = pygame.image.load("boss.png")
bossRect2 = bossFly2.get_rect(center=(0, 10000))

attackQuantity = 0
stunnedCount = 0
stunnedCooldown = 0
bossStunned_rect = bossFly2.get_rect()

sidekickAlive = True
boss_damaged = False
boss_speed = 5
bossLanded = False
blocked = False
sidekickGotHit = False
bossDeathCount = 0
boss_going_back = False
animationFinished = False
hypoteneuse = 0
fireballCooldown = 0
last_fireball = 0
bossShooting = False
shooting = False
shootingCount = 0
shootAnimation = False
fireball_speed = 10
fireball_vx = 0
fireball_vy = 0
sidekick_animation = 0
fireCooldown = 0
fireCount = 0
spawn_fire = False
explosionCount = 0
exploding = False
explosion_size = 0

player_dead = False
boss_dead = False
playerDeathCount = 0
gameOver = False
leaveButton_width = 200
leaveButton_height = 75
leaveButton_x = 300
leaveButton_y = 500
leaveButton_textSize = 50
leaveButton_rect = pygame.Rect(leaveButton_x, leaveButton_y, leaveButton_width, leaveButton_height)

movingYAmount = 0
movingXAmount = 0
closingAnimation = False
rightVertical = False
stopRightVertical = False
shrink_circle = True
radiusNumber = 0
shrinkRadius = 567    #Square root of (WIDTH ** 2 + HEIGHT ** 2) Then divided by 2
game_screen = True
random_text = False

scroll_map = False
map_confirmed = False
second_map_confirmed = False
third_map_confirmed = False
E_clicked = False
circleWidth = 800
screenX = 0
screenLimitLeft = False
screenLimitRight = False
civilianIdleCount = 0
civilian_interact = False
interaction_next = 0
civilian_running = False
civilianRunCount = 0
civilianX = 600
space_holding = False
endOfGame = False
player_run = True

fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
fireballImageUnrotated = pygame.transform.scale(fireballImageUnsized, (100, 50))
fireball_rect = fireballImageUnrotated.get_rect(topleft=(10000, 0))
fire_rect = fireballImageUnrotated.get_rect(center=(0, 0))

swordRect = swordRect = pygame.Rect(player_rect.centerx + 670, player_rect.centery - 700, 25, 10)

boomrngImage = pygame.image.load("boomerang.png").convert_alpha()
boomrng_rect = boomrngImage.get_rect(center=(boomrngX, boomrngY))
boomrng_rect.center = (boomrngX + 4000, boomrngY + 4000)

last_action_time = pygame.time.get_ticks()

attack_cooldown = 5000
attacking = False

################################################ FUNCTIONS ###################################################

def startGame():
    global attacking, current_time, animationFinished, bossHealth, boss_dead, bossRect, player_dead, gameOver, playerY, playerX
    running = True

    while running:

        if gameOver == False:
            current_time = pygame.time.get_ticks()
            playerImage = pygame.image.load("character.png")
            clock.tick(FPS)
            drawGame()
            findEvents()
            keys = pygame.key.get_pressed()
            handleKeys(keys)
            checkIfJumping()
            checkCollisions()
            bossIdle()
            CheckBossPosition()
            checkForEscape(keys)

            if playerHealth <= 0:
                playerY = 667
                gameOver = True

            if bossHealth <= 0:
                boss_dead = True
                bossRect.center = (-1000, -1000)
                bossStunned_rect.center = (-10000, -10000)
                bossDeath()
                makeArrows()

                if E_clicked == True:
                    playerX = 0
                    scrollMaps()

                if scroll_map == True:
                    playerX = 0
                    scrollMaps()


            if boss_going_back == True and animationFinished == True:
                bossGoBack()
            else:
                bossAttack()

            updateHealthBars()

            if menu == True:
                escapeMenu()

            if moving_left == True:
                leftAnimation()

            elif moving_right == True:
                rightAnimation()

            if weapon_choice == SWORD:
                sword_choice()

            elif weapon_choice == BOW:
                bow_choice()
            
            else:
                boomrng_choice()

            checkIfHit()
            
            if boss_damaged == True:
                bossDamaged()

            pygame.display.update()

        else:
            findEvents()
            playerDeath()

            if player_dead == True:
                closingAnimations()

            if closingAnimation == True:
                gameOverScreen()

            pygame.display.update()

def makeArrows():
    global radius, E_clicked, grow_circle, sign_font
    pygame.draw.line(SCREEN, BLUE, (WIDTH - 40, 700), (WIDTH - 80, 660), 8)
    line_rect = pygame.draw.line(SCREEN, BLUE, (WIDTH - 40, 700), (WIDTH - 80, 740), 8)

    if player_rect.colliderect(line_rect):
        sign_text = "Press 'E' to interact!"
        sign_font = pygame.font.SysFont("Comic Sans MS", 20)

        sign_surface = sign_font.render(sign_text, True, BLACK)
        sign_rect = sign_surface.get_rect(center=(WIDTH - 130, 550))

        SCREEN.blit(sign_surface, sign_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            grow_circle = True
            radius = 0
            while grow_circle == True:
                growCircle()
                pygame.display.update()

            E_clicked = True

    pygame.display.update()

def scrollMaps():
    global playerY, ground_y, playerFlipped, endOfGame, shrink_circle, radiusNumber, moving_left, moving_right
    global endOfGame, civilian_run
    map_scroll = True
    while map_scroll == True:
        clock.tick(FPS)
        findEvents()
        drawMap()
        drawPlayer()
        keys = pygame.key.get_pressed()
        if civilian_interact == False and endOfGame == False:
            checkKeysMap(keys)
            checkIfJumping()
            shrink_circle = True
            radiusNumber = 0
        else:
            moving_left = False
            moving_right = False
            playerFlipped = False
            player_rect.topleft = (playerX, playerY)
            civilianInteraction()

        if endOfGame == True and civilian_run == False:
            while shrink_circle == True:
                clock.tick(FPS)
                findEvents()
                shrinkCircle()
            drawEnding()
        screenScroll()
        createCivilian()
        playerY = 550

        if moving_left == True:
            leftAnimation()

        elif moving_right == True:
            rightAnimation()

        pygame.display.update()

def drawEnding():
    SCREEN.fill(LIGHTBLUE)
    ending_title_font = pygame.font.SysFont("Georgia", 100)
    ending_title_text = "GAME OVER"
    ending_title_surface = ending_title_font.render(ending_title_text, True, BLACK)
    ending_title_rect = ending_title_surface.get_rect(center=(400, 50))

    subtitle_font = pygame.font.SysFont("Georgia", 40)
    subtitle_text = "YOU WIN!"
    subtitle_surface = subtitle_font.render(subtitle_text, True, BLACK)
    subtitle_rect = subtitle_surface.get_rect(center=(400, 120))

    story_text = "Storyline"
    story_surface = subtitle_font.render(story_text, True, BLACK)
    story_rect = story_surface.get_rect(topleft=(50, 200))

    body_font = pygame.font.SysFont("Comic Sans MS", 20)
    body_text1 = "Defeating very few dragons actually won't defeat all of them."
    body_text2 = "However, you managed to defeat the queen dragon which stops the reproduction!"
    body_text3 = "The rest of the dragons can now be handled from other sorcerers."
    body_text4 = "Studies say that this queen dragon has lived for the whole hundred years!"
    body_text5 = "This would mean that there is only one female dragon and you,"
    body_text6 = "have defeated the one and only."
    body_text7 = "You saved the world from chaos and destruction!"
    body_text8 = "Congratulations!"

    body_text_surface = body_font.render(body_text1, True, BLACK)
    body_text_rect = body_text_surface.get_rect(topleft=(30, 250))

    body_text_surface2 = body_font.render(body_text2, True, BLACK)
    body_text_rect2 = body_text_surface2.get_rect(topleft=(30, 270))

    body_text_surface3 = body_font.render(body_text3, True, BLACK)
    body_text_rect3 = body_text_surface3.get_rect(topleft=(30, 290))

    body_text_surface4 = body_font.render(body_text4, True, BLACK)
    body_text_rect4 = body_text_surface4.get_rect(topleft=(30, 310))

    body_text_surface5 = body_font.render(body_text5, True, BLACK)
    body_text_rect5 = body_text_surface5.get_rect(topleft=(30, 330))

    body_text_surface6 = body_font.render(body_text6, True, BLACK)
    body_text_rect6 = body_text_surface6.get_rect(topleft=(30, 350))

    body_text_surface7 = body_font.render(body_text7, True, BLACK)
    body_text_rect7 = body_text_surface7.get_rect(topleft=(30, 370))

    body_text_surface8 = body_font.render(body_text8, True, BLACK)
    body_text_rect8 = body_text_surface8.get_rect(topleft=(30, 390))

    SCREEN.blit(body_text_surface, body_text_rect)
    SCREEN.blit(body_text_surface2, body_text_rect2)
    SCREEN.blit(body_text_surface3, body_text_rect3)
    SCREEN.blit(body_text_surface4, body_text_rect4)
    SCREEN.blit(body_text_surface5, body_text_rect5)
    SCREEN.blit(body_text_surface6, body_text_rect6)
    SCREEN.blit(body_text_surface7, body_text_rect7)
    SCREEN.blit(body_text_surface8, body_text_rect8)
    SCREEN.blit(story_surface, story_rect)
    SCREEN.blit(subtitle_surface, subtitle_rect)
    SCREEN.blit(ending_title_surface, ending_title_rect)

def createCivilian():
    global civilianIdleCount, civilian_rect, civilian_running, endOfGame
    civilianImage = pygame.image.load(f"civilian_idle/{civilianIdleCount}.png").convert_alpha()
    civilian_rect = civilianImage.get_rect(center=(screenX + secondMapWidth + mapWidth + 600, 600))
    civilianIdleCount += 1

    #Draw civilian hitbox
    #pygame.draw.rect(SCREEN, GREEN, civilian_rect, 3)

    if playerX < civilian_rect.centerx:
        civilianImage = pygame.transform.flip(civilianImage, True, False)

    if civilianIdleCount == 17:
        civilianIdleCount = 0

    if player_rect.colliderect(civilian_rect):
        if civilian_interact == False and endOfGame == False:
            interact_text = "Press 'E' to interact!"

            interact_surface = sign_font.render(interact_text, True, BLACK)
            interact_rect = interact_surface.get_rect(center=(playerX + 20, playerY - 50))

            SCREEN.blit(interact_surface, interact_rect)
        
        elif civilian_interact == True:
            interact_text = "Press 'SPACE' to go next!"

            interact_surface = sign_font.render(interact_text, True, BLACK)
            interact_rect = interact_surface.get_rect(center=(playerX + 20, playerY - 50))

            SCREEN.blit(interact_surface, interact_rect)

    if civilian_running == False:
        SCREEN.blit(civilianImage, civilian_rect)

def screenScroll():
    global screenX, playerX, map_rect, screenLimitLeft, secondMap_rect, thirdMap_rect, screenLimitRight
    if playerX >= 600 and moving_right and not moving_left and not screenLimitRight:
        playerX = 600
        screenX -= 25
        screenLimitLeft = False
    
    if playerX <= 200 and moving_left and not moving_right and not screenLimitLeft:
        playerX = 200
        screenX += 5
        screenLimitRight = False
    
    if playerX <= 3:
        playerX = 3
    
    if playerX >= 720:
        playerX = 720

    if map_rect.topleft == (0, 0):
        screenLimitLeft = True

    if thirdMap_rect.topleft <= (0, 0):
        screenLimitRight = True

    map_rect = mapImage.get_rect(topleft=(screenX, 0))
    secondMap_rect = secondMap.get_rect(topleft=(screenX + mapWidth, 0))
    thirdMap_rect = thirdMap.get_rect(topleft=(screenX + secondMapWidth + mapWidth, 0))

def checkKeysMap(keys):
    global playerFlipped, playerX, moving_left, moving_right, playerAnimation, civilian_interact
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and civilian_interact == False:
        playerX -= playerSpeed
        playerFlipped = True
        moving_left = True

    else:
        moving_left = False
        playerAnimation = False

    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and civilian_interact == False:
        playerX += playerSpeed
        playerFlipped = False
        moving_right = True
    
    else:
        moving_right = False
        playerAnimation = False
    
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        playerJump()

    if keys[pygame.K_e]:
        if player_rect.colliderect(civilian_rect):
            civilian_interact = True

def civilianInteraction():
    global civilian_running, interaction_next, space_holding, civilian_interact, endOfGame
    if civilian_running == False:
        pygame.draw.rect(SCREEN, BLACK, (50, 100, 720, 100))
        pygame.draw.rect(SCREEN, WHITE, (50, 100, 720, 100), 10)
    interact_font = pygame.font.SysFont("Georgia", 20)
    interact_text1 = "<Civilian> You really beat the dragons? That's really great! It's finally done!"
    interact_text2 = "<Civilian> I'll go tell the others about this. Thank you!"
    interact_text3 = "<Civilian> I'll say it again. Thank you so much! You saved the world!"

    interact1_surface = interact_font.render(interact_text1, True, WHITE)
    interact1_rect = interact1_surface.get_rect(topleft=(70, 140))

    interact2_surface = interact_font.render(interact_text2, True, WHITE)
    interact2_rect = interact2_surface.get_rect(topleft=(70, 140))

    interact3_surface = interact_font.render(interact_text3, True, WHITE)
    interact3_rect = interact3_surface.get_rect(topleft=(70, 140))

    if interaction_next == 0:
        SCREEN.blit(interact1_surface, interact1_rect)
    
    elif interaction_next == 1:
        SCREEN.blit(interact2_surface, interact2_rect)
    
    elif interaction_next == 2:
        SCREEN.blit(interact3_surface, interact3_rect)
    
    else:
        civilian_running = True
        civilian_interact = False
        endOfGame = True
        civilianRun()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and space_holding == False:
        space_holding = True
        interaction_next += 1

    if not keys[pygame.K_SPACE]:
        space_holding = False

def civilianRun():
    global civilianRunCount, civilianX, endOfGame, civilian_interact, civilian_run
    civilianImage = pygame.image.load(f"civilian_walking/{civilianRunCount}.png").convert_alpha()
    civilianRunCount += 1
    civilian_rect = civilianImage.get_rect(center=(screenX + secondMapWidth + mapWidth + civilianX, 600))
    civilianX += 4
    civilian_run = True

    if civilianRunCount == 24:
        civilianRunCount = 0

    if civilian_rect.centerx >= 800:
        civilian_run = False
    else:
        SCREEN.blit(civilianImage, civilian_rect)

def drawPlayer():
    global playerImage, playerX, playerY, playerRun

    if playerAnimation == False:
        if playerFlipped == False:
            SCREEN.blit(playerImage, (playerX, playerY))

        else:
            flippedPlayerImage = pygame.transform.flip(playerImage, True, False)
            SCREEN.blit(flippedPlayerImage, (playerX, playerY))

    else:
        SCREEN.blit(playerRun, (playerX, playerY))
    
    if civilian_interact == True:
        SCREEN.blit(playerImage, (playerX, playerY))

    player_rect.topleft = (playerX + 50, playerY)

def drawMap():
    global map_confirmed, map_choice, mapImage, map_rect, screenX, mapWidth, second_map_confirmed, secondMap, secondMap_rect, second_map_choice
    global secondMapWidth, thirdMap, third_map_confirmed, thirdMap_rect
    if map_confirmed == False:
        maps = ["grass", "forest", "desert"]
        map_choice = random.choice(maps)
        map_confirmed = True
    
        mapImageUnsized = pygame.image.load(f"{map_choice}.jpg").convert_alpha()
        mapImage = pygame.transform.scale(mapImageUnsized, (1250, 800))
        map_rect = mapImage.get_rect(topleft=(screenX, 0))
        mapWidth = mapImage.get_rect().width

    if second_map_confirmed == False:
        secondMaps = ["grass", "forest", "desert"]
        second_map_choice = random.choice(secondMaps)
        while second_map_choice == map_choice:
            secondMaps = ["grass", "forest", "desert"]
            second_map_choice = random.choice(secondMaps)

        second_map_confirmed = True

        secondMapUnsized = pygame.image.load(f"{second_map_choice}.jpg").convert_alpha()
        secondMap = pygame.transform.scale(secondMapUnsized, (1250, 800))
        secondMap_rect = secondMap.get_rect(topleft=(screenX + mapWidth, 0))
        secondMapWidth = secondMap.get_rect().width

    if third_map_confirmed == False:
        thirdMaps = ["grass", "forest", "desert"]
        third_map_choice = random.choice(thirdMaps)
        while third_map_choice == second_map_choice:
            thirdMaps = ["grass", "forest", "desert"]
            third_map_choice = random.choice(thirdMaps)

        third_map_confirmed = True
        thirdMapUnsized = pygame.image.load(f"{third_map_choice}.jpg").convert_alpha()
        thirdMap = pygame.transform.scale(thirdMapUnsized, (1250, 800))
        thirdMap_rect = thirdMap.get_rect(topleft=(screenX + secondMapWidth + mapWidth, 0))
    
    SCREEN.blit(thirdMap, thirdMap_rect)
    SCREEN.blit(secondMap, secondMap_rect)
    SCREEN.blit(mapImage, map_rect)

def drawGame():
    drawBackground()
    drawCharacters()
    drawHealthBar()

def drawBackground():
    SCREEN.blit(backgroundImage, (0, 0))

def drawCharacters():
    global playerRun, playerX, playerY, playerAnimation, bossFly

    if playerAnimation == False:
        if playerFlipped == False:
            SCREEN.blit(playerImage, (playerX, playerY))

        else:
            flippedPlayerImage = pygame.transform.flip(playerImage, True, False)
            SCREEN.blit(flippedPlayerImage, (playerX, playerY))

    if playerAnimation == True:
        SCREEN.blit(playerRun, (playerX, playerY))

def findEvents():
    global BUTTON_COLOR, BUTTON_CLICK_COLOR, button_clicked, button_hover, button_x, button_y, WEAPON_BUTTON_COLOR, BOW_BUTTON_COLOR, weapon_choice

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            quitGame()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if button_rect.collidepoint(event.pos):
                BUTTON_COLOR = BUTTON_CLICK_COLOR
                WEAPON_BUTTON_COLOR = BUTTON_CLICK_COLOR
                button_clicked = True
                weapon_choice = 1

def closingAnimations():
    global movingYAmount

    if movingYAmount >= 670:
        closeLeftVerticals()
        return
    
    pygame.draw.rect(SCREEN, BLUE, (0, -650 + movingYAmount, WIDTH, 670))

    movingYAmount += 1

def closeLeftVerticals():
    global movingXAmount, rightVertical

    if movingXAmount >= playerX - 100 or rightVertical == True:
        if rightVertical == False:
            movingXAmount = 0
            rightVertical = True

        closeRightVerticals()
        return

    pygame.draw.rect(SCREEN, BLUE, (-100 + movingXAmount, playerY, 200, playerHeight + 50))
    movingXAmount += 1

def closeRightVerticals():
    global movingXAmount, stopRightVertical, closingAnimation

    if WIDTH - movingXAmount <= playerX + playerWidth + 50:
        stopRightVertical = True
        closingAnimation = True

    if stopRightVertical == False:
        pygame.draw.rect(SCREEN, BLUE, (WIDTH - movingXAmount, playerY, 300, playerHeight))
        movingXAmount += 1

def gameOverScreen():
    global shrink_circle, game_screen
    while shrink_circle == True:
        clock.tick(FPS)
        findEvents()
        shrinkCircle()

    while game_screen == True:
        clock.tick(FPS)
        findEvents()
        printGameScreenText()
        createLeaveButton()
        checkClickedButton()

def checkClickedButton():
    global leaveButton_color, leaveButton_rect
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and leaveButton_rect.collidepoint(mouse_pos):
            leaveButton_color = BUTTON_CLICK_COLOR
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
            quitGame()


def createLeaveButton():
    global leaveButton_color, leaveButton_width, leaveButton_height, leaveButton_x, leaveButton_y, leaveButton_textSize, leaveButton_rect
    leaveButton_rect = pygame.Rect(leaveButton_x, leaveButton_y, leaveButton_width, leaveButton_height)
    leaveButton_text = "LEAVE"
    leaveButton_font = pygame.font.SysFont("Comic Sans MS", leaveButton_textSize)
    drawButton(leaveButton_rect, leaveButton_color, leaveButton_text, leaveButton_font, SCREEN)

    mouse_pos = pygame.mouse.get_pos()
    if leaveButton_rect.collidepoint(mouse_pos):
        leaveButton_color = BUTTON_HOVER_COLOR
        leaveButton_width = 237
        leaveButton_height = 112
        leaveButton_x = 275
        leaveButton_y = 475
        leaveButton_textSize = 70
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    else:
        leaveButton_color = BLUE
        leaveButton_width = 200
        leaveButton_height = 75
        leaveButton_x = 300
        leaveButton_y = 500
        leaveButton_textSize = 50
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.update()

def printGameScreenText():
    global random_text, description_text2
    title_font = pygame.font.SysFont("Georgia", 100)
    description_font = pygame.font.SysFont("Comic Sans MS", 20)

    SCREEN.fill(BLACK)

    title_text = "GAME OVER"
    title_text_surface = title_font.render(title_text, True, WHITE)
    title_text_rect = title_text_surface.get_rect(center=(400, 80))

    description_text = "You failed to defeat the dragons..."
    randomText = random.randint(1, 5)

    if random_text == False:
        if randomText == 1:
            description_text2 = "Maybe this job is for someone else."
            random_text = True
        
        elif randomText == 2:
            description_text2 = "We should've called for help when we could."
            random_text = True

        elif randomText == 3:
            description_text2 = "The dragons will now be able to reproduce even more."
            random_text = True

        elif randomText == 4:
            description_text2 = "Maybe choosing another weapon could have helped."
            random_text = True
        
        else:
            description_text2 = "It is what it is."
            random_text = True

    description_text3 = "The question is WHO released them.."

    description_text_surface = description_font.render(description_text, True, WHITE)
    description_text_rect = description_text_surface.get_rect(center=(400, 200))

    description_text2_surface = description_font.render(description_text2, True, WHITE)
    description_text2_rect = description_text2_surface.get_rect(center=(400, 230))

    description_text3_surface = description_font.render(description_text3, True, WHITE)
    description_text3_rect = description_text3_surface.get_rect(center=(400, 260))

    SCREEN.blit(description_text3_surface, description_text3_rect)
    SCREEN.blit(description_text2_surface, description_text2_rect)
    SCREEN.blit(description_text_surface, description_text_rect)
    SCREEN.blit(title_text_surface, title_text_rect)

    pygame.display.update()

def shrinkCircle():
    global radiusNumber, shrinkRadius, shrink_circle

    if endOfGame == False:
        pygame.draw.circle(SCREEN, BLACK, player_rect.center, shrinkRadius + 1000, 800)

    else:
        pygame.draw.circle(SCREEN, LIGHTBLUE, player_rect.center, shrinkRadius + 1000, 800)

    radiusNumber += 0.5
    shrinkRadius -= radiusNumber

    if shrinkRadius + 1000 <= 0:
        shrink_circle = False
        return

    pygame.display.update()

def playerDeath():
    global playerDeathCount, player_dead

    if player_dead:
        return

    SCREEN.fill(BLACK)
    
    playerDeathImage = pygame.image.load(f"player_death/{playerDeathCount}.png").convert_alpha()
    playerDeath_rect = playerDeathImage.get_rect(topleft=(playerX, 650))
    playerDeathCount += 1

    if playerDeathCount == 41:
        playerDeathCount = 0
        player_dead = True

    if playerFlipped == True:
        playerDeathImage = pygame.transform.flip(playerDeathImage, True, False)

    SCREEN.blit(playerDeathImage, playerDeath_rect)

def bossDeath():
    global explosion_size, bossDeathCount

    if bossDeathCount == 16:
        bossRect.center = (-1000, -1000)
        return
    
    bossDeathImageUnsized = pygame.image.load(f"boss_death/{bossDeathCount}.png").convert_alpha()
    bossDeathCount += 1
    bossDeathImage = pygame.transform.scale(bossDeathImageUnsized, (new_width + explosion_size, new_height + explosion_size))
    bossDeath_rect = bossDeathImage.get_rect(center=(bossX, bossY))
    explosion_size += 20

    SCREEN.blit(bossDeathImage, bossDeath_rect)

def bossAttack():
    global attacking, last_action_time, attackChoice, current_time, boss_pos, ATTACKLEFT, ATTACKRIGHT, ATTACKUP, ATTACKDOWN, EVERYWHERE, STUNNED
    global boss_going_back, bossRect2, bossRect, sidekickAlive, hypoteneuse
    global fireballCooldown, last_fireball, attackQuantity, stunnedCooldown, bossStunned_rect

    if attackQuantity == 0:
        bossStunned_rect.center = (-10000, -10000)

    if boss_going_back == True and attackQuantity == 0:
        bossGoBack()
        return

    if sidekickHealth <= 0:
       sidekickAlive = False
       fire_rect.center = (10000, 400)
       sidekickDeath()
       return
    
    if sidekickAlive == False:
       bossRect2 = pygame.Rect(-1000, -1000, bossWidth, bossHeight)

    current_time = pygame.time.get_ticks() 

    if attacking == True and sidekickAlive == False:
        attacking = False
        boss_going_back = True
        attackQuantity += 1
        return

    if attacking == False and boss_dead == False:
        last_fireball = fireballCooldown
        last_action_time = current_time
        attackChoice = random.randint(1, 2)
        if attackQuantity == 0:
            attacking = True
        
        else:
            bossStunned()

    if boss_going_back == False and attackQuantity == 0 and boss_dead == False:
        if attackChoice <= ATTACKLEFT:
            bossAttackLeft()
       
        elif attackChoice <= ATTACKRIGHT and attackChoice > ATTACKLEFT:
            bossAttackRight()

        elif attackChoice <= ATTACKUP and attackChoice > ATTACKRIGHT:
            bossAttackUp()

        elif attackChoice <= ATTACKDOWN and attackChoice > ATTACKUP:
            bossAttackDown()
       
        else:
            bossAttackEverywhere()

def bossStunned():
    global stunnedCount, bossRect, stunnedCooldown, attackQuantity, bossStunned_rect
    current_time = pygame.time.get_ticks()
    if stunnedCooldown == 0:
        stunnedCooldown = pygame.time.get_ticks()

    stunnedImageUnsized = pygame.image.load(f"boss_stunned/{stunnedCount}.png").convert_alpha()
    stunnedCount += 1
    stunnedImage = pygame.transform.scale(stunnedImageUnsized, (new_width, new_height))
    bossStunned_rect = stunnedImage.get_rect(topleft=(bossX, bossY))

    if stunnedCount == 12:
        stunnedCount = 0

    if current_time - stunnedCooldown >= 5000:
        attackQuantity = 0
        stunnedCooldown = 0

    SCREEN.blit(stunnedImage, bossStunned_rect)

def bossAttackLeft():
    global boss_animation_count, bossX, bossY, bossRect, bossLanded
    global boss_animation_count2, bossX2, bossY2, boss_flipped, shoot_arrow, sidekickHealth
    global is_fired, bow_shoot, allow_angle, sidekickGotHit, bossRect2, leftHypoteneuse
    global hit, boomrng_hit, last_fireball, bossShooting, shootAnimation, fireball_rect, fireballImageUnrotated, shooting, fireball_vx, fireball_vy
    global shootingCount, bossFly2

    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))

    if boss_animation_count == 12:
        boss_animation_count = 0

    bossRect = bossFly.get_rect(topleft=(bossX, bossY))

    if bossLanded == False:
        bossX2 = 0

        left_surf = pygame.Surface((50, 50))
        left_rect = left_surf.get_rect(topleft=(120, 160))
        left_rect.topleft = (120, 160)

        leftX = left_rect.centerx
        leftY = left_rect.centery

        run = leftX - bossX
        rise = leftY - bossY

        leftHypoteneuse = math.sqrt(run ** 2 + rise ** 2)

        if leftHypoteneuse == 0:
            return

        boss_x_speed = run/leftHypoteneuse * boss_speed
        boss_y_speed = rise/leftHypoteneuse * boss_speed
        
        bossX += boss_x_speed
        bossY += boss_y_speed

        SCREEN.blit(bossFly, (bossX, bossY))

        if leftHypoteneuse <= boss_speed:
            bossX = leftX
            bossY = leftY
            bossLanded = True

        #Show boss hitbox
        #pygame.draw.rect(SCREEN, (0, 255, 0), bossRect, 2)

        #Show boss destination hitbox
        #pygame.draw.rect(SCREEN, RED, left_rect, 3)

    elif bossLanded == True and sidekickAlive == True:
        SCREEN.blit(bossFly, (bossX, bossY))

        if sidekickGotHit == False:
            bossFlyUnsized2 = pygame.image.load(f"boss_idle2/{boss_animation_count2}.png")
            boss_animation_count2 += 1
            bossFly2 = pygame.transform.scale(bossFlyUnsized2, (new_width, new_height))

            if boss_flipped == False:
                bossFly2 = pygame.transform.flip(bossFly2, True, False)
                bossX2 += 5
                     
            else:
                bossX2 -= 5

        else:
            boss_animation_count2 = 0
            sidekickDamaged()

            if boss_flipped == False:
                bossFly2 = pygame.transform.flip(bossFly2, True, False)
                bossX2 += 5
              
            else:
                bossX2 -= 5

        if boss_animation_count2 == 12:
            boss_animation_count2 = 0

        if bossX2 >= 720:
            boss_flipped = True

        elif bossX2 <= 0:
            boss_flipped = False
       

        bossRect2 = bossFly2.get_rect(center=(bossX2 + 60, bossY2 + 50))

        if weapon_choice == BOW:
            if bossRect2.colliderect(arrow_rect):
                sidekickHealth -= 30
                is_fired = False
                shoot_arrow = False
                bow_shoot = False
                allow_angle = True
                sidekickGotHit = True
                arrow_rect.center = (1000, 1000)

                if sidekickHealth < 0:
                    sidekickHealth = 0
       
        if weapon_choice == SWORD and hit == False:
            if sword_swing and swordRect.colliderect(bossRect2):
                sidekickHealth -= 7
                sidekickGotHit = True
                hit = True

            else:
                hit = False

        if weapon_choice == BOOMRNG and boomrng_hit == False:
            if boomrng_rect.colliderect(bossRect2):
                boomrng_hit = True
                sidekickGotHit = True
                sidekickHealth -= 30
       
        fireballCooldown = pygame.time.get_ticks()
        if fireballCooldown - last_fireball >= 2000 and bossShooting == False:
            last_fireball = fireballCooldown
            bossShooting = True
            shooting = True
       
        if bossShooting == True:
            if shooting == True:
                fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
                fireballImageUnrotated = pygame.transform.scale(fireballImageUnsized, (100, 50))
                fireball_rect = fireballImageUnrotated.get_rect(center=(bossRect2.center))
				
                dx = playerX - fireball_rect.centerx
                dy = playerY - fireball_rect.centery

                distance = math.hypot(dx, dy)

                if distance != 0:
                    fireball_vx = dx / distance * fireball_speed
                    fireball_vy = dy / distance * fireball_speed

                shooting = False
                shootingCount = 0
					
            shootAnimation = True
            shootFireball()

        if spawn_fire:
            createFire()


        if sidekickAlive == True and sidekickHealth > 0 and bossShooting == False:
            SCREEN.blit(bossFly2, (bossX2, bossY2))

        pygame.draw.rect(SCREEN, GREEN, bossRect2, 3)

        if boss_flipped == False:
            pygame.draw.rect(SCREEN, RED, (bossX2 + 20, bossY2 - 20, 100, 15))
            pygame.draw.rect(SCREEN, BLACK, (bossX2 + 20, bossY2 - 20, 100, 15), 3)
            pygame.draw.rect(SCREEN, BLACK, (bossX2 + 20, bossY2 - 20, 100 - sidekickHealth, 15))

        else:
            pygame.draw.rect(SCREEN, RED, (bossX2 - 10, bossY2 - 20, 100, 15))
            pygame.draw.rect(SCREEN, BLACK, (bossX2 - 10, bossY2 - 20, 100, 15), 3)
            pygame.draw.rect(SCREEN, BLACK, (bossX2 - 10, bossY2 - 20, 100 - sidekickHealth, 15))

def shootFireball():
    global fireball_speed, bossShooting, shooting, fireball_rect, fireball_vx, fireball_vy, last_action_time, fireX, fireY, spawn_fire, fireCooldown
    if shootAnimation == True:
        sidekickShoot()

    fireball_rect.centerx += fireball_vx
    fireball_rect.centery += fireball_vy

    fireball_angle = math.degrees(math.atan2(-fireball_vy, fireball_vx))

    fireballImage = pygame.transform.rotate(fireballImageUnrotated, fireball_angle + 180)
    rotated_rect = fireballImage.get_rect(center=fireball_rect.center)

    if fireball_rect.centery >= 770:
        last_action_time = fireCooldown
        fireCooldown = 0
        fireX = fireball_rect.centerx

        fireY = 850
        spawn_fire = True
        last_action_time = pygame.time.get_ticks()
        bossShooting = False
        shooting = True
        fireball_rect.center = (1000, 1000)

    if fireball_rect.centerx >= 800 or fireball_rect.centerx <= 0:
        bossShooting = False
        shooting = True
        fireball_rect.center = (1000, 1000)

    SCREEN.blit(fireballImage, rotated_rect)

def createFire():
    global fireCount, spawn_fire, fireCooldown, fire_rect, fireX, fireY, last_action_time
    #if fireCooldown == 0 and spawn_fire:
    fireCooldown = pygame.time.get_ticks()
    fireImageUnsized = pygame.image.load(f"fire/{fireCount}.png").convert_alpha()
    fireImage = pygame.transform.scale(fireImageUnsized, (100, 100))
    fire_rect = fireImage.get_rect(center=(fireX, fireY - 70))
    fireCount += 1

    if fireCount == 7:
        fireCount = 0

    if fireCooldown - last_action_time <= 2000:
        SCREEN.blit(fireImage, fire_rect)
    
    else:
        fireCooldown = 0
        spawn_fire = False
        fire_rect.center = (1000, 1000)

def sidekickShoot():
    global shootingCount, shootAnimation, bossShooting, sidekick_animation

    if shootingCount == 8:
        sidekickUnsized = pygame.image.load(f"boss_idle2/{sidekick_animation}.png")
        sidekick_animation += 1
        sidekickFly = pygame.transform.scale(sidekickUnsized, (new_width, new_height))

        sidekick_rect = sidekickFly.get_rect(center=(bossX2 + 50, bossY2 + 50))

        if boss_flipped == False:
            sidekickFly = pygame.transform.flip(sidekickFly, True, False)

        if sidekick_animation == 12:
            sidekick_animation = 0

        SCREEN.blit(sidekickFly, sidekick_rect)
    
    else:
        shootingImageUnsized = pygame.image.load(f"boss_attack/{shootingCount}.png").convert_alpha()
        shootingCount += 1


        shootingImage = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shooting_rect = shootingImage.get_rect(topleft=(bossX2, bossY2))

        if playerX > fireball_rect.centerx:
            shootingImage = pygame.transform.flip(shootingImage, True, False)

        SCREEN.blit(shootingImage, shooting_rect)

def bossGoBack():
    global boss_animation_count, bossX, bossY, bossRect, boss_going_back, attacking, animationFinished, hypoteneuse, sidekickAlive, bossLanded

    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))

    if boss_animation_count == 12:
        boss_animation_count = 0

    backX = 350
    backY = 400

    bossX, bossY, hypoteneuse = findHypoteneuse(backX, backY, bossX, bossY, hypoteneuse, boss_speed)

    if hypoteneuse <= boss_speed:
        boss_going_back = False
        attacking = False
        animationFinished = False
        sidekickAlive = True
        bossLanded = False

    bossRect.topleft = (bossX, bossY)
    if boss_dead == False:
        SCREEN.blit(bossFly, bossRect)
    
def findHypoteneuse(targetX, targetY, userX, userY, hypoteneuse, speed):
    run = targetX - userX
    rise = targetY - userY

    hypoteneuse = math.sqrt(run ** 2 + rise ** 2)

    if hypoteneuse == 0:
        return userX, userY
    
    user_x_speed = run/hypoteneuse * speed
    user_y_speed = rise/hypoteneuse * speed

    userX += user_x_speed
    userY += user_y_speed

    return userX, userY, hypoteneuse

def bossAttackRight():
    print("He attacked right...")

def bossAttackUp():
    print("He attacked up...")

def bossAttackDown():
    print("He attacked down...")

def bossAttackEverywhere():
    print("You're cooked...")

def sidekickDamaged():
    global sidekickGotHit, bossFly2, boss_animation_count3, boss_animation_count2

    bossDamageUnsized2 = pygame.image.load(f"boss_damage2/{boss_animation_count3}.png")
    boss_animation_count3 += 1
    bossFly2 = pygame.transform.scale(bossDamageUnsized2, (new_width, new_height))

    if boss_animation_count3 == 4:
       boss_animation_count3 = 0
       sidekickGotHit = False

def sidekickDeath():
    global attacking, bossDeathCount, sidekickHealth, bossRect2, animationFinished, boss_animation_count, bossRect2
    bossRect2.topleft = (-1000, -1000)

    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))

    if boss_animation_count == 12:
        boss_animation_count = 0

    bossDeathUnsized = pygame.image.load(f"sidekick_death/{bossDeathCount}.png")
    bossDeathCount += 1
    bossDeath = pygame.transform.scale(bossDeathUnsized, (new_width, new_height))
    bossDeath_rect = bossDeath.get_rect(topleft=(bossX2, bossY2))

    if bossDeathCount == 6:
        bossDeathCount = 0
        sidekickHealth = 100
        bossRect2 = (1000, 1000)
        animationFinished = True

    SCREEN.blit(bossDeath, bossDeath_rect)
    SCREEN.blit(bossFly, (bossX, bossY))

def updateHealthBars():
    if bossHealth < 200:
        inverse = 200 - bossHealth
        pygame.draw.rect(SCREEN, BLACK, (570, 45, inverse, 30))

def checkBowClicked():
    global BOW_BUTTON_COLOR, BUTTON_CLICK_COLOR, button_clicked, bow_button_rect, button_hover, weapon_choice
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bow_button_rect.collidepoint(event.pos):
                button_hover = 2
                BOW_BUTTON_COLOR = BUTTON_CLICK_COLOR
                button_clicked = True
                weapon_choice = 2

def checkBoomrngClicked():
    global BOOMRNG_BUTTON_COLOR, BUTTON_CLICK_COLOR, button_clicked, boomrng_button_rect, weapon_choice
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boomrng_button_rect.collidepoint(event.pos):
                BOOMRNG_BUTTON_COLOR = BUTTON_CLICK_COLOR
                button_clicked = True
                weapon_choice = 3

def handleKeys(keys):
    global playerX, playerY, playerSpeed, moving_left, moving_right, playerAnimation, spaceHolding, escape_pressed, menu, escape_holding

    moving_left = False
    moving_right = False

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        playerX -= playerSpeed
        moving_left = True

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        playerX += playerSpeed
        moving_right = True

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        playerJump()

    if keys[pygame.K_ESCAPE] and escape_holding == False:
        menu = True
        escape_holding = True
        escapeMenu()

    if spaceHolding == False:
        if keys[pygame.K_SPACE]:
            playerAttack()
            spaceHolding = True

    if not (keys[pygame.K_SPACE]):
        spaceHolding = False

    if not (keys[pygame.K_a] and keys[pygame.K_d]):
      playerAnimation = False

    elif not (keys[pygame.K_a] and keys[pygame.K_RIGHT]):
        playerAnimation = False
    
    elif not(keys[pygame.K_d] and keys[pygame.K_LEFT]):
        playerAnimation = False

def checkForEscape(keys):
    global menu, escape_holding, guide_clicked

    if keys[pygame.K_ESCAPE] and escape_holding == False and menu == False:
        menu = True
        escape_holding = True
        guide_clicked = not guide_clicked

    if keys[pygame.K_ESCAPE] and escape_holding == False and menu == True:
        menu = False
        guide_clicked = False
        escape_holding = True

    if not keys[pygame.K_ESCAPE]:
        escape_holding = False

def escapeMenu():
    global menu, escape_holding
    while menu == True:
        findEvents()

        keys = pygame.key.get_pressed()
        checkForEscape(keys)

        createMenu()
        clock.tick(FPS)

def createMenu():
    global guide_rect, X_rect, home_rect, mouse_rect, fromGuide, menu, GUIDE_BUTTON_COLOR, HOME_BUTTON_COLOR, guide_text
    global home_text, fromHome, X_clicked, guide_clicked, home_clicked

    pygame.draw.rect(SCREEN, GREEN, (30, 20, 738, 735))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse_x, mouse_y, 2, 2)


    font = pygame.font.SysFont("Georgia", 100)
    button_font = pygame.font.SysFont("Comic Sans MS", 100)
    warning_font = pygame.font.SysFont("Georgia", 30)
    escape_font = pygame.font.SysFont("Comic Sans MS", 50)

    menu_text = "Menu"
    menu_surface = font.render(menu_text, True, BLACK)
    menu_rect = menu_surface.get_rect()
    menu_rect.center = (400, 60)

    guide_text = "GUIDE"
    guide_surface = button_font.render(guide_text, True, WHITE)
    guide_rect = guide_surface.get_rect()
    guide_rect.center = (400, 300)

    home_text = "LEAVE"
    home_surface = button_font.render(home_text, True, WHITE)
    home_rect = home_surface.get_rect()
    home_rect.center = (400, 600)

    warning_text = "WARNING: PROGRESS WILL NOT BE SAVED!!"
    warning_surface = warning_font.render(warning_text, True, RED)
    warning_rect = warning_surface.get_rect()
    warning_rect.center = (400, 500)

    escape_text = "Press 'ESC' to leave the menu"
    escape_surf = escape_font.render(escape_text, True, BLACK)
    escape_rect = escape_surf.get_rect()
    escape_rect.center = (400, 130)

    if guide_clicked == False and home_clicked == False:
        drawButton(guide_rect, GUIDE_BUTTON_COLOR, guide_text, button_font, SCREEN)
        drawButton(home_rect, HOME_BUTTON_COLOR, home_text, button_font, SCREEN)

    SCREEN.blit(warning_surface, warning_rect)
    SCREEN.blit(menu_surface, menu_rect)
    SCREEN.blit(escape_surf, escape_rect)

    pygame.draw.rect(SCREEN, BLACK, (30, 20, 738, 735), 3)
    pygame.draw.rect(SCREEN, BLACK, guide_rect, 3)
    pygame.draw.rect(SCREEN, BLACK, home_rect, 3)

    if guide_clicked == True:
        fromGuide = True
        createInstructions()

    if home_clicked == True:
        pygame.quit()
        exit()
        import sys
        sys.exit()

    if X_clicked == True:
        menu = False
        X_clicked = False
        menu = False
        guide_clicked = X_clicked = False

    pygame.display.update()

    checkGuideButton()
    checkHomeButton()

def checkGuideButton():
    global fromGuide, menu, guide_clicked, GUIDE_BUTTON_COLOR, radius, grow_circle, mouse_rect, button_font, guide_hover

    if not(guide_rect.colliderect(mouse_rect)):
        if guide_clicked == False:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
            GUIDE_BUTTON_COLOR = BLUE
            guide_hover = False
            guide_clicked = False

    if guide_rect.colliderect(mouse_rect):
        guide_hover = True
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        GUIDE_BUTTON_COLOR = BUTTON_HOVER_COLOR

        events = pygame.event.get()

        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN and guide_clicked == False:
        
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect(mouse_x, mouse_y, 2, 2)

                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                GUIDE_BUTTON_COLOR = BUTTON_CLICK_COLOR

                drawButton(guide_rect, GUIDE_BUTTON_COLOR, guide_text, button_font, SCREEN)

                radius = 0
                grow_circle = True
                while grow_circle == True:
                    growCircle()

                    pygame.display.update()

                guide_clicked = True

def checkHomeButton():
    global home_clicked, HOME_BUTTON_COLOR, radius, mouse_rect, grow_circle

    events = pygame.event.get()

    if not(home_rect.colliderect(mouse_rect)):
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        HOME_BUTTON_COLOR = BLUE

    if home_rect.colliderect(mouse_rect):
        if guide_clicked == False:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            HOME_BUTTON_COLOR = BUTTON_HOVER_COLOR

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect(mouse_x, mouse_y, 2, 2)

                if guide_clicked == False:

                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    HOME_BUTTON_COLOR = BUTTON_CLICK_COLOR

                    drawButton(home_rect, HOME_BUTTON_COLOR, home_text, button_font, SCREEN)

                    radius = 0
                    grow_circle = True
                    while grow_circle == True:
                        growCircle()

                        pygame.display.update()

                    home_clicked = True

def CheckBossPosition():
    global bossWidth, bossHeight, bossX, bossY, boss_pos, bossImage_rect, bossRect
    bossWidth = bossImage.get_rect().width
    bossHeight = bossImage.get_rect().height
    bossImage_rect = bossFly.get_rect()

def checkIfHit():
    global bossHealth, swordRect, hit, boss_damaged, boss_pos, bossX, bossY, bossFly, bossRect, sword_swing, arrow_rect
    global is_fired, shoot_arrow, bow_shoot, allow_angle, playerHealth, playerX, playerY, playerGotHit, player_rect, boomrng_rect, boomrng_hit
    global shieldTime, blocked, last_action_time, bossShooting, shooting, spawn_fire, exploding
    global swordRect, boomrng_rect
    if sword_swing and swordRect.colliderect(bossRect) and not boss_damaged:
        hit = True

    else: 
        hit = False

    if hit == True:
        bossHealth -= 5
        boss_damaged = True
        print(bossHealth)

    if weapon_choice == BOW:
        if arrow_rect.colliderect(bossRect):
            is_fired = False
            shoot_arrow = False
            bow_shoot = False
            allow_angle = True
            arrow_rect.center = (playerX, playerY)

            if attacking == False:
                bossHealth -= 7
                boss_damaged = True
                print(bossHealth)
            
            else:
                blocked = True
                shieldTime = pygame.time.get_ticks()
                last_action_time = shieldTime

                
    if boomrng_hit == False:
        if weapon_choice == BOOMRNG:
            if boomrng_rect.colliderect(bossRect):
                boomrng_hit = True

                if attacking == False:
                     boss_damaged = True
                     bossHealth -= 100
                     print(bossHealth)

                else:
                    blocked = True
                    shieldTime = pygame.time.get_ticks()
                    last_action_time = shieldTime

    if blocked == True:
       shield = pygame.image.load("shield.png").convert_alpha()
       shield_rect = shield.get_rect(topleft=(bossX - 15, bossY - 10))
       shield = pygame.transform.scale(shield, (bossWidth + 30, bossHeight + 30))

       SCREEN.blit(shield, shield_rect)

       shieldTime = pygame.time.get_ticks()
       if shieldTime - last_action_time >= 1000:
              blocked = False

    if playerGotHit == False:
        if player_rect.colliderect(bossRect) or player_rect.colliderect(bossStunned_rect):
            playerX += 200
            playerY -= 100
            playerGotHit = True
            playerHealth -= 10
            print(playerHealth)
        
        if sidekickAlive and player_rect.colliderect(bossRect2):
              playerX += 200
              playerY -= 50
              playerHealth -= 5
              playerGotHit = True

        if playerX >= 750:
              playerY = 700

    if not (player_rect.colliderect(bossRect)):
        playerGotHit = False

    if exploding == False:
        if arrow_rect.colliderect(fireball_rect) or swordRect.colliderect(fireball_rect) and sword_swing or boomrng_rect.colliderect(fireball_rect) or player_rect.colliderect(fireball_rect):
            exploding = True

        if fireball_rect.colliderect(player_rect):
            playerHealth -= 5
            exploding = True
    else:
        fireballCollide()
        bossShooting = False
        shooting = True


    if fire_rect.colliderect(player_rect):
        playerHealth -= 0.5

def fireballCollide():
    global explosionCount, exploding, is_fired, shoot_arrow, bow_shoot, allow_angle, boomrng_hit, hit, boomrng_rect, swordRect
    explosionImageUnscaled = pygame.image.load(f"fireball_collide/{explosionCount}.png").convert_alpha()
    explosionImage = pygame.transform.scale(explosionImageUnscaled, (100, 100))
    explosionCount += 1
    explosion_rect = explosionImage.get_rect(topleft=(fireball_rect.centerx, fireball_rect.centery))

    if weapon_choice == BOW:
        is_fired = False
        shoot_arrow = False
        bow_shoot = False
        allow_angle = True

    if explosionCount == 5:
        explosionCount = 0
        exploding = False
        fireball_rect.center = (-1000, -1000)

        if weapon_choice == BOW:
            arrow_rect.center = (10000, 1000)

        elif weapon_choice == SWORD:
            if sword_swing and hit == False and not sidekickGotHit:
                hit = True
            
            else:
                hit = False
                swordRect.center = (1000, 1000)

        else:
            if boomrng_hit == False:
                boomrng_rect.center = (1000, 1000)


    SCREEN.blit(explosionImage, explosion_rect)

def bossDamaged():
    global new_width, new_height, dmg_animation_count, bossDmg, boss_damaged, boss_pos
    bossdmgUnsized = pygame.image.load(f"boss_damage/{dmg_animation_count}.png")
    dmg_animation_count += 1

    if dmg_animation_count == 4:
        dmg_animation_count = 0
        boss_damaged = False

    bossDmg = pygame.transform.scale(bossdmgUnsized, (new_width, new_height))

    SCREEN.blit(bossDmg, (bossX, bossY))


def playerAttack():
    if weapon_choice == SWORD:
        sword_attack()

    elif weapon_choice == BOW:
        bow_attack()

    else:
        boomrng_attack()

def sword_attack():
    global sword_swing
    sword_swing = True

def bow_attack():
    global bow_shoot
    bow_shoot = True

def boomrng_attack():
    global boomrng_shoot
    boomrng_shoot = True

def leftAnimation():
    global animation_count, playerAnimation, playerRun, playerFlipped

    playerAnimation = True

    OriginalImage = pygame.image.load(f"animation/{animation_count}.png").convert_alpha()
    playerRun = pygame.transform.flip(OriginalImage, True, False)

    animation_count += 1

    if animation_count > 7:
        animation_count = 0

def rightAnimation():
    global animation_count, playerImage, playerAnimation, playerRun, playerFlipped

    playerAnimation = True

    playerRun = pygame.image.load(f"animation/{animation_count}.png")

    animation_count += 1

    if animation_count > 7:
        animation_count = 0


def playerJump():
    global jumping, playerY, ground_y
    if playerY == ground_y:
        jumping = True

def checkIfJumping():
    global jumping, playerY, vel_y, gravity, jump_height, falling, jump_speed, jump_count, ground_y

    if jumping == True:
        playerY -= jump_speed
        vel_y -= gravity

        if vel_y < -jump_height:
            jumping = False
            vel_y = jump_height

    else:
        falling = True

        if falling == True:
            playerY += gravity + 20

            if playerY >= ground_y:
                playerY = ground_y
                falling = False

def checkCollisions():
    global playerX
    if playerX >= 723:
        playerX = 723
    
    if playerX <= -10:
        playerX = -10

def drawHealthBar():
    font = pygame.font.SysFont("Georgia", 20)
    pygame.draw.rect(SCREEN, BLACK, (30, 45, 200, 30))
    pygame.draw.rect(SCREEN, RED, (30, 45, playerHealth * 2, 30)) 
    pygame.draw.rect(SCREEN, BLACK, (30, 45, 200, 30), 4) 
    text_surface = font.render("Your Health", True, WHITE)
    SCREEN.blit(text_surface, (33, 20))

    if boss_dead == False:
        pygame.draw.rect(SCREEN, RED, (570, 45, 200, 30)) 
    pygame.draw.rect(SCREEN, BLACK, (570, 45, 200, 30), 4)
    text_surface = font.render("Boss Health", True, WHITE)
    SCREEN.blit(text_surface, (655, 20))

    pygame.draw.rect(SCREEN, GREEN, player_rect, 3)

def bossIdle():
    global new_width, new_height, boss_animation_count, bossFly, boss_damaged, boss_pos, bossX, bossY, bossImage_rect, bossRect

    if boss_going_back == True:
        return
    
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    

    if boss_animation_count == 12:
        boss_animation_count = 0

    bossFly = pygame.Surface((new_width, new_height))
    bossRect = bossFly.get_rect(topleft=boss_pos)
    

    bossRect.topleft = boss_pos

    #Draw boss hitbox
    #pygame.draw.rect(SCREEN, (0, 255, 0), bossRect, 2)


    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    if boss_damaged == False and attacking == False and boss_going_back == False and attackQuantity == 0:
        boss_animation_count = 0
        SCREEN.blit(bossFly, (boss_pos))

def checkCursor():
    global mouse_pos, button_rect, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_CLICK_COLOR, button_width, button_height, button_hover, font_size, button_x, button_y, WEAPON_BUTTON_COLOR
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        if BUTTON_COLOR != BUTTON_CLICK_COLOR:
            BUTTON_COLOR = BUTTON_HOVER_COLOR
            button_hover += 1
            if button_hover == 1:
                button_width += 30
                button_height += 30
                font_size += 10
                button_x -= 15
                button_y -= 15
        
        if WEAPON_BUTTON_COLOR != BUTTON_CLICK_COLOR:
            button_hover = 1
            if button_hover == 1:
                WEAPON_BUTTON_COLOR = BUTTON_HOVER_COLOR
    
    else:
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        BUTTON_COLOR = BLUE
        button_width = 200
        button_height = 75
        button_hover = 0
        font_size = 50
        button_x = 280
        button_y = 480
        WEAPON_BUTTON_COLOR = RED

def checkBowHovered():
    global bow_button_rect, BOW_BUTTON_COLOR, BUTTON_CLICK_COLOR, button_hover
    mouse_pos = pygame.mouse.get_pos()

    if bow_button_rect.collidepoint(mouse_pos):
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        if BOW_BUTTON_COLOR != BUTTON_CLICK_COLOR:
            button_hover = 1
            if button_hover == 1:
                BOW_BUTTON_COLOR = BUTTON_HOVER_COLOR
                

    else:
        BOW_BUTTON_COLOR = RED
        button_hover = 0

def checkBoomrngHovered():
    global boomrng_button_rect, BOOMRNG_BUTTON_COLOR, BUTTON_CLICK_COLOR, BUTTON_HOVER_COLOR, button_hover
    mouse_pos = pygame.mouse.get_pos()

    if boomrng_button_rect.collidepoint(mouse_pos):
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        if BOOMRNG_BUTTON_COLOR != BUTTON_CLICK_COLOR:
            button_hover = 1
            if button_hover == 1:
                BOOMRNG_BUTTON_COLOR = BUTTON_HOVER_COLOR

    else:
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        BOOMRNG_BUTTON_COLOR = RED
        button_hover = 0

def sword_choice():
    global sword_swing, rotation_speed, added_y, swordImageUnrotated, swordRect, player_rect, playerX, playerY, bossY

    bossRect = bossFly.get_rect(topleft=(bossX, bossY))
    boss_pos = (bossX, bossY)

    player_pos = (playerX, playerY)
    player_rect = playerImage.get_rect(center=player_pos)
    player_rect.topleft = (playerX, playerY)
    
    swordImageUnrotated = pygame.image.load("sword.png").convert_alpha()
    
    swordWidth = swordImageUnrotated.get_rect().width
    swordHeight = swordImageUnrotated.get_rect().height

    swordX = WIDTH // 2 - swordWidth // 2
    swordY = HEIGHT * 3 // 4 + swordHeight // 2

    if playerFlipped == False:
        swordRect = pygame.Rect(player_rect.centerx + 67, player_rect.centery - 70, 25, 10)
    
    else:
        swordRect = pygame.Rect(player_rect.centerx - 67, player_rect.centery - 70, 25, 10)

    if playerFlipped == False:
        if sword_swing == True:
            sword_top_offset_x = 50
            sword_top_offset_y = -40

            swordRect = pygame.Rect(player_rect.centerx + sword_top_offset_x, player_rect.centery + sword_top_offset_y, 100, 25)

    else:
        if sword_swing == True:
            sword_top_offset_x = -125
            sword_top_offset_y = -40

            swordRect = pygame.Rect(player_rect.centerx + sword_top_offset_x, player_rect.centery + sword_top_offset_y, 100, 25)

    #pygame.draw.rect(SCREEN, (255, 0, 0, 50), swordRect, 25)

    if playerFlipped == False:
        swordImage = pygame.transform.rotate(swordImageUnrotated, -25)

        if sword_swing == False:
            SCREEN.blit(swordImage, (playerX + 5, playerY - 60))

        else:
            
            swordImage = pygame.transform.rotate(swordImageUnrotated, -rotation_speed)

            rotation_speed += 25

            if rotation_speed >= 130:
                sword_swing = False
                rotation_speed = 0
                added_y = 0

            SCREEN.blit(swordImage, (playerX, playerY + added_y))

            added_y += 0.5
    
    else:
        swordImage = pygame.transform.rotate(swordImageUnrotated, 25)

        if sword_swing == False:
            SCREEN.blit(swordImage, (playerX - 70, playerY - 60))

        else:
            swordImage = pygame.transform.rotate(swordImageUnrotated, rotation_speed)

            rotation_speed += 25

            if rotation_speed >= 130:
                sword_swing = False
                rotation_speed = 0
                added_y = 0

            SCREEN.blit(swordImage, (playerX - 100, playerY + added_y))

            added_y += 0.5

def bow_choice():
    global player_rect, bow_number, bow_shoot, shoot_arrow, angle, angle_degrees, arrow_angle, allow_angle, mouse_x, mouse_y, arrow_x_speed, arrow_y_speed, is_fired, arrowX, arrowY
    player_pos = (playerX, playerY)
    player_rect = playerImage.get_rect(center=player_pos)
    player_rect.topleft = (playerX, playerY)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    dx = mouse_x - player_rect.centerx
    dy = mouse_y - player_rect.centery

    angle_radians = math.atan2(-dy, dx)
    angle_degrees = math.degrees(angle_radians)

    if bow_shoot == False:
        angle = angle_degrees - 90
        bowImageUnchanged = pygame.image.load("bow.png")
        bowImageUnrotated = pygame.transform.scale(bowImageUnchanged, (100, 100))
        bowImage = pygame.transform.rotate(bowImageUnrotated, angle + 100)

    else:
        if shoot_arrow == False:
            angle = angle_degrees - 90
            bowImageUnchanged = pygame.image.load(f"bow_shoot/{bow_number}.png").convert_alpha()
            bowImageUnrotated = pygame.transform.scale(bowImageUnchanged, (100, 100))
            bowImage = pygame.transform.rotate(bowImageUnrotated, angle + 100)

            bow_number += 1

            if bow_number == 11:
                bow_shoot = False
                shoot_arrow = True
                bow_number = 0

    if shoot_arrow == True:
        angle = angle_degrees - 90
        bowImageUnchanged = pygame.image.load("bow_shoot/10.png").convert_alpha()
        bowImageUnrotated = pygame.transform.scale(bowImageUnchanged, (100, 100))
        bowImage = pygame.transform.rotate(bowImageUnrotated, angle + 100)

        arrowUnchanged = pygame.image.load("arrow.png").convert_alpha()
        arrowImageUnrotated = pygame.transform.scale(arrowUnchanged, (85, 30))
        arrowImage = pygame.transform.rotate(arrowImageUnrotated, angle)

        if allow_angle == True:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            arrowX = playerX
            arrowY = playerY

            run = mouse_x - arrowX
            rise = mouse_y - arrowY

            hypoteneuse = math.sqrt(run ** 2 + rise ** 2)

            arrow_x_speed = run/hypoteneuse * arrow_speed
            arrow_y_speed = rise/hypoteneuse * arrow_speed

            is_fired = True

            arrow_angle = angle_degrees - 10
            allow_angle = False

        shootArrow()

    bow_rect = bowImage.get_rect(center=player_rect.center)

    SCREEN.blit(bowImage, bow_rect.topleft)

def shootArrow():
    global angle_degrees, arrow_angle, mouse_x, mouse_y, arrowX, arrowY, is_fired, shoot_arrow, bow_shoot, allow_angle, arrow_rect
  
    arrowUnchanged = pygame.image.load("arrow.png").convert_alpha()
    arrowImageUnrotated = pygame.transform.scale(arrowUnchanged, (85, 30))
    arrowImage = pygame.transform.rotate(arrowImageUnrotated, arrow_angle)

    if arrow_angle < 90 and arrow_angle > -180:
        arrow_rect = pygame.Rect(arrowX + 30, arrowY + 20, 25, 25)

    elif arrow_angle > 90 and arrow_angle <= 180:
        arrow_rect = pygame.Rect(arrowX, arrowY, 25, 25)

    arrowX += arrow_x_speed
    arrowY += arrow_y_speed

    if is_fired == False:
        SCREEN.blit(arrowImage, player_rect.center)

    else:
        SCREEN.blit(arrowImage, (arrowX - 20, arrowY))
        #Show arrow hitbox
        #pygame.draw.rect(SCREEN, RED, arrow_rect, 5)

    if arrowY <= 0 or arrowY >= 800:
        is_fired = False
        shoot_arrow = False
        bow_shoot = False
        allow_angle = True

    if arrowX <= 0 or arrowX >= 800:
        is_fired = False
        shoot_arrow = False
        bow_shoot = False
        allow_angle = True
                                                                                                                                                                                                    #easter egg
def boomrng_choice():
    global boomrngImage, boomrng_spin, playerFlipped, boomrngImageUnrotated, boomrngX, boomrngY, mouse_x, mouse_y, allow_aim, mouse_pos, mouse_rect, player_rect, boomrng_hit, boomrng_rect

    player_rect = playerImage.get_rect(center=(playerX + 40, playerY + 60))
    
    boomrngImageUnscaled = pygame.image.load("boomerang.png").convert_alpha()
    boomrngImageUnrotated = pygame.transform.scale(boomrngImageUnscaled, (75, 75))

    if boomrng_shoot == False:
        boomrng_rect.center = (1000, 1000)

    if allow_aim == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        boomrngX = playerX
        boomrngY = playerY
        mouse_pos = (boomrngX, boomrngY)
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 2, 2)

    if boomrng_shoot == False:
        boomrngImage = pygame.transform.rotate(boomrngImageUnrotated, -45)
        boomrng_hit = False

        if playerFlipped == False:
            SCREEN.blit(boomrngImage, (playerX + 40, playerY + 23))

        else:
            boomrngImageFlipped = pygame.transform.flip(boomrngImage, True, False)
            SCREEN.blit(boomrngImageFlipped, (playerX - 70, playerY + 20))

    else:
        allow_aim = False
        spinBoomrng()
        shootBoomrng()

def spinBoomrng():
    global boomrngImageUnrotated, boomrngImage, boomrng_spin, boomrng_rect
    boomrngImage = pygame.transform.rotate(boomrngImageUnrotated, boomrng_spin - 45)

    boomrng_spin -= 25

def shootBoomrng():
    global boomrngX, boomrngY, fly_back, allow_aim, boomrng_shoot, player_rect, boomrng_rect

    boomrng_rect = boomrngImage.get_rect(center=(boomrngX, boomrngY))
    boomrng_rect.center = (boomrngX + 40, boomrngY + 40)

    #pygame.draw.rect(SCREEN, GREEN, boomrng_rect, 3)

    player_rect = playerImage.get_rect(center=(playerX + 40, playerY + 60))

    run = mouse_x - boomrngX
    rise = mouse_y - boomrngY
    distance = (run, rise)

    hypoteneuse = math.sqrt(run ** 2 + rise ** 2)

    boomrng_x_speed = run/hypoteneuse * boomrng_speed
    boomrng_y_speed = rise/hypoteneuse * boomrng_speed

    boomrng_rect = boomrngImage.get_rect(center=(boomrngX, boomrngY))

    if boomrng_rect.colliderect(mouse_rect):
        fly_back = True

    SCREEN.blit(boomrngImage, boomrng_rect.center)

    if fly_back == False:
        boomrngX += boomrng_x_speed
        boomrngY += boomrng_y_speed

    else:
        run = player_rect.centerx - boomrngX
        rise = player_rect.centery - boomrngY
        distance = math.hypot(run, rise)

        if distance != 0:
            boomrng_x_speed = run / distance * boomrng_speed
            boomrng_y_speed = rise / distance * boomrng_speed

            boomrngX += boomrng_x_speed
            boomrngY += boomrng_y_speed

        if boomrng_rect.colliderect(player_rect):
            fly_back = False
            allow_aim = True
            boomrng_shoot = False

#    pygame.draw.rect(SCREEN, GREEN, (boomrngX, boomrngY, 75, 75), 3)


def drawButton(rect, color, text, font, surface):
    pygame.draw.rect(surface, color, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def drawTitle(font, surface, text, rect):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)
    
def growCircle():
    global choose_weapon, grow_circle, radius
    findEvents()
    pygame.draw.circle(SCREEN, BLUE, (375, 350), radius)
    radius += 1
    if radius == 600:
        choose_weapon = True
        grow_circle = False
        return

def quitGame():
    pygame.quit()
    import sys
    sys.exit()

def drawSwordSection():
    pygame.draw.rect(SCREEN, BLUE, (10, 300, 250, 400))
    pygame.draw.rect(SCREEN, BLACK, (10, 300, 250, 400), 3)
    pygame.draw.rect(SCREEN, WHITE, (30, 310, 210, 200))
    pygame.draw.rect(SCREEN, BLACK, (30, 310, 210, 200), 3)
    SCREEN.blit(sword_text_surface, sword_text_rect)

    drawButton(button_rect, WEAPON_BUTTON_COLOR, use_text, button_font, SCREEN)
    pygame.draw.rect(SCREEN, BLACK, (20, 580, 228, 70), 3)

    swordImage = pygame.image.load("sword.png")
    SCREEN.blit(swordImage, (100, 312))

def drawBowSection():
    pygame.draw.rect(SCREEN, ORANGE, (275, 300, 250, 400))
    pygame.draw.rect(SCREEN, BLACK, (275, 300, 250, 400), 3)
    pygame.draw.rect(SCREEN, WHITE, (295, 310, 210, 200))
    pygame.draw.rect(SCREEN, BLACK, (295, 310, 210, 200), 3)
    SCREEN.blit(bow_text_surface, bow_text_rect)

    drawButton(bow_button_rect, BOW_BUTTON_COLOR, use_text, button_font, SCREEN)
    pygame.draw.rect(SCREEN, BLACK, (286, 580, 228, 70), 3)

    bowImageUnscaled = pygame.image.load("bow.png").convert_alpha()

    bowImage = pygame.transform.scale(bowImageUnscaled, (150, 185.5))
    SCREEN.blit(bowImage, (330, 318))

def drawBoomrngSection():
    pygame.draw.rect(SCREEN, PINK, (540, 300, 250, 400))
    pygame.draw.rect(SCREEN, BLACK, (540, 300, 250, 400), 3)
    pygame.draw.rect(SCREEN, WHITE, (560, 310, 210, 200))
    pygame.draw.rect(SCREEN, BLACK, (560, 310, 210, 200), 3)
    SCREEN.blit(boomrng_text_surface, boomrng_text_rect)

    drawButton(boomrng_button_rect, BOOMRNG_BUTTON_COLOR, use_text, button_font, SCREEN)
    pygame.draw.rect(SCREEN, BLACK, (552, 580, 228, 70), 3)

    boomrngImage = pygame.image.load("boomerang.png").convert_alpha()
    SCREEN.blit(boomrngImage, (600, 338))

def checkKeys(keys):
    global choice, leftHolding, rightHolding

    if leftHolding == False:
        if keys[pygame.K_LEFT]:
            choice -= 1
            leftHolding = True
    
    if not (keys[pygame.K_LEFT]):
        leftHolding = False

    if rightHolding == False:
        if keys[pygame.K_RIGHT]:
            choice += 1
            rightHolding = True
    
    if not (keys[pygame.K_RIGHT]):
        rightHolding = False

    if choice == 4:
        choice = 1
    
    if choice == 0:
        choice = 3

    #First Section
    if choice == 1:
        drawSwordSection()
        checkCursor()
    

    #Second Section
    if choice == 2:
        drawBowSection()
        checkBowHovered()
        checkBowClicked()

    #Third Section
    if choice == 3:
        drawBoomrngSection()
        checkBoomrngHovered()
        checkBoomrngClicked()

def checkSpacePress(keys):
    global instructions

    if keys[pygame.K_SPACE]:
        instructions = False

def createInstructions():
    global fromGuide, guide_clicked, menu, escape_holding
    SCREEN.blit(title_background, (-500, 0))


    if fromGuide == True:

        if keys[pygame.K_ESCAPE] and escape_holding == False:
            menu = False
            escape_holding = True
            fromGuide = False
            guide_clicked = False


    instruction_font = pygame.font.SysFont("Georgia", 90)
    guide_font = pygame.font.SysFont("Comic Sans MS", 20)
    controls_font = pygame.font.SysFont("Comic Sans MS", 20)

    instructions_text = "GUIDE"

    guide_text = "Welcome to Sorcerers Clash where you will have to defeat the dragons." 
    guide_text1 = "These dragons have been released 100 years ago!" 
    guide_text2 = "Sadly, no one could defeat them all and the dragons had time to reproduce." 
    guide_text3 = "We need your help to defeating them once and for all." 
    guide_text4 = "To see the controls, it will be right under this."

    if fromGuide == False:
        guide_text5 = "Press 'SPACE' to commence the battle between life and death."

    if fromGuide == True:
        guide_text5 = "Press 'ESC' to continue the battle between life and death."

    instructions_surface = instruction_font.render(instructions_text, True, BLACK)
    instructions_rect = instructions_surface.get_rect()
    instructions_rect.center = (400, 50)

    guide_surface = guide_font.render(guide_text, True, BLACK)
    guide_rect = guide_surface.get_rect()
    guide_rect.center = (400, 200)

    guide_surface1 = guide_font.render(guide_text1, True, BLACK)
    guide_rect1 = guide_surface1.get_rect()
    guide_rect1.center = (400, 230)

    guide_surface2 = guide_font.render(guide_text2, True, BLACK)
    guide_rect2 = guide_surface2.get_rect()
    guide_rect2.center = (400, 260)

    guide_surface3 = guide_font.render(guide_text3, True, BLACK)
    guide_rect3 = guide_surface3.get_rect()
    guide_rect3.center = (400, 290)

    guide_surface4 = guide_font.render(guide_text4, True, BLACK)
    guide_rect4 = guide_surface4.get_rect()
    guide_rect4.center = (400, 320)

    guide_surface5 = guide_font.render(guide_text5, True, BLACK)
    guide_rect5 = guide_surface5.get_rect()
    guide_rect5.center = (400, 350)

    SCREEN.blit(instructions_surface, instructions_rect)
    SCREEN.blit(guide_surface, guide_rect)
    SCREEN.blit(guide_surface1, guide_rect1)
    SCREEN.blit(guide_surface2, guide_rect2)
    SCREEN.blit(guide_surface3, guide_rect3)
    SCREEN.blit(guide_surface4, guide_rect4)
    SCREEN.blit(guide_surface5, guide_rect5)

    #Controls Dialogue

    controls_text0 = "CONTROLS"
    controls_text1 = "Press 'A' to move left"
    controls_text2 = "Press 'D' to move right"
    controls_text3 = "Press 'W' to jump up"
    controls_text4 = "Press 'SPACE' to attack with your weapon!"

    if weapon_choice == SWORD:
        controls_text5 = "You chose a sword! Attack the enemy while facing it!"
        controls_text6 = "Your sword must reach the enemy to deal damage!"

    elif weapon_choice == BOW:
        controls_text5 = "You chose a bow! Attack the enemy using your cursor!"
        controls_text6 = "Press the attack button while holding your mouse to the target!"

    else:
        controls_text5 = "You chose a boomerang! Attack the enemy using your cursor!"
        controls_text6 = "Press the attack button while holding your mouse to the target!"

    controls0_surface = instruction_font.render(controls_text0, True, BLACK)
    controls0_rect = controls0_surface.get_rect()
    controls0_rect.center = (400, 450)

    controls1_surface = controls_font.render(controls_text1, True, BLACK)
    controls1_rect = controls1_surface.get_rect()
    controls1_rect.center = (400, 580)

    controls2_surface = controls_font.render(controls_text2, True, BLACK)
    controls2_rect = controls2_surface.get_rect()
    controls2_rect.center = (400, 610)

    controls3_surface = controls_font.render(controls_text3, True, BLACK)
    controls3_rect = controls3_surface.get_rect()
    controls3_rect.center = (400, 640)

    controls4_surface = controls_font.render(controls_text4, True, BLACK)
    controls4_rect = controls4_surface.get_rect()
    controls4_rect.center = (400, 670)

    controls5_surface = controls_font.render(controls_text5, True, BLACK)
    controls5_rect = controls5_surface.get_rect()
    controls5_rect.center = (400, 700)

    controls6_surface = controls_font.render(controls_text6, True, BLACK)
    controls6_rect = controls6_surface.get_rect()
    controls6_rect.center = (400, 730)

    SCREEN.blit(controls0_surface, controls0_rect)
    SCREEN.blit(controls1_surface, controls1_rect)
    SCREEN.blit(controls2_surface, controls2_rect)
    SCREEN.blit(controls3_surface, controls3_rect)
    SCREEN.blit(controls4_surface, controls4_rect)
    SCREEN.blit(controls5_surface, controls5_rect)
    SCREEN.blit(controls6_surface, controls6_rect)

    pygame.display.update()

############################################### GAME SCREEN ###################################################

introduction = True
while introduction == True:
    clock.tick(FPS)
    if button_hover == True:
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
    else:
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    button_font = pygame.font.SysFont("Comic Sans MS", font_size)
    title_font = pygame.font.SysFont("Georgia", 80)
    title_rect = pygame.Rect(250, 150, 300, 300)

    title_background = pygame.image.load("title_background.png")
    SCREEN.blit(title_background, (-500, 0))

    findEvents()

    checkCursor()

    drawTitle(title_font, SCREEN, title_text, title_rect)
    drawButton(button_rect, BUTTON_COLOR, button_text, button_font, SCREEN)

    if button_clicked == True:
        introduction = False
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        button_hover = 0
        button_x = 0
        button_y = 0
        grow_circle = True
    
    pygame.display.update()

while grow_circle == True:
    growCircle()
    
    pygame.display.update()

choose_weapon = True
button_clicked = False

while choose_weapon == True:
    findEvents()

    SCREEN.blit(title_background, (-500, 0))
    weapon_text = "Choose Your Weapon"
    weapon_rect = pygame.Rect(250, 10, 300, 300)
    drawTitle(title_font, SCREEN, weapon_text, weapon_rect)

    font = pygame.font.SysFont("Comic Sans MS", 30)
    bow_text = "BOW"
    sword_text = "SWORD"
    boomrng_text = "BOOMERANG"
    subtitle_text = "Use Arrow Keys To Interact!"
    use_text = "USE!"

    sword_text_surface = font.render(sword_text, True, WHITE)
    sword_text_rect = sword_text_surface.get_rect()
    sword_text_rect.center = (130, 530)

    bow_text_surface = font.render(bow_text, True, BLACK)
    bow_text_rect = bow_text_surface.get_rect()
    bow_text_rect.center = (400, 530)

    boomrng_text_surface = font.render(boomrng_text, True, WHITE)
    boomrng_text_rect = boomrng_text_surface.get_rect()
    boomrng_text_rect.center = (665, 530)

    button_rect = pygame.Rect(20, 580, 228, 70)
    bow_button_rect = pygame.Rect(286, 580, 228, 70)
    boomrng_button_rect = pygame.Rect(552, 580, 228, 70)
    
    subtitle_surface = font.render(subtitle_text, True, BLACK)
    subtitle_rect = subtitle_surface.get_rect()
    subtitle_rect.center = (400, 225)

    SCREEN.blit(subtitle_surface, subtitle_rect)


    keys = pygame.key.get_pressed()
    checkKeys(keys)

    if button_hover == 0:
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    if button_clicked == True:
        BOW_BUTTON_COLOR = BUTTON_CLICK_COLOR
        BOOMRNG_BUTTON_COLOR = BUTTON_CLICK_COLOR
        checkKeys(keys)
        choose_weapon = False
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        button_hover = 0
        radius = 0
        grow_circle = True

    pygame.display.update()

while grow_circle == True:
    growCircle()

    pygame.display.update()

instructions = True

while instructions:
    findEvents()
    
    keys = pygame.key.get_pressed()
    checkSpacePress(keys)

    createInstructions()

grow_circle = True
radius = 0
while grow_circle == True:
    growCircle()

    pygame.display.update()
############################################### GAME LOGIC ###################################################

startGame()