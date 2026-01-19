
################################################# SORCERERS CLASH #################################################################

#################################################### VARIABLES #####################################################################
#Imports the needed functions for this game
import pygame
pygame.mixer.init()
pygame.init()
import math
import random

#Width and Height of the screen
WIDTH = 800
HEIGHT = 800

#The frames per second for the game
FPS = 30

#Colors used in the game
BLUE = (0, 0, 255)
LIGHTBLUE = (111, 150, 247)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (252, 211, 3)
PINK = (252, 3, 198)
GREEN = (28, 235, 107)
YELLOW = (245, 245, 66)

#Colors used for buttons for when being clicked, hovered, or none
BUTTON_HOVER_COLOR = (245, 176, 66)
BUTTON_CLICK_COLOR = (255, 64, 239)
BUTTON_COLOR = BLUE
WEAPON_BUTTON_COLOR = RED
BOW_BUTTON_COLOR = RED
BOOMRNG_BUTTON_COLOR = RED
GUIDE_BUTTON_COLOR = BLUE
HOME_BUTTON_COLOR = BLUE
leaveButton_color = BLUE

#Variable for checking if the left or right arrow key is being held
leftHolding = False
rightHolding = False

#Variables for buttons being used
button_width = 200
button_height = 75
button_text = "START"
font_size = 50
button_x = 280
button_y = 480
button_clicked = False
button_hover = 0

#Variables for menu buttons
fromGuide = False
guide_clicked = False
guide_hover = False
home_clicked = False
fromHome = False

#Variables to check if 'ESC' is being pressed or held
menu = False
escape_pressed = False
escape_holding = False

#Defines the text of the title on the title screen
title_text = "SORCERERS CLASH"

#Variables the boss would need for animation and movement
boss_animation_count = 0
boss_animation_count2 = 5
boss_animation_count3 = 0
bossX2 = 5
bossY2 = 400
boss_flipped = False
sidekickHealth = 100

#Defines the choice of weapon the player decides
weapon_choice = 0
SWORD = 1
BOW = 2
BOOMRNG = 3

#Variables to check if sword is swinging and it's rotation speed
sword_swing = False
rotation_speed = 3

#Variables to check if player is moving left or right or none
moving_left = False
moving_right = False

#Defines radius for a circle in further use
radius = 0

#Defines the choice for the weaponry the player must decide to use
choice = 2

#Defines the player's speed for it's movement
playerSpeed = 10

#Defines the animation for being damaged or others
animation_count = 0
dmg_animation_count = 0

#Set the screen to it's height and weight (800, 800)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#Set the game captions to be the game name, "Sorcerers Clash"
pygame.display.set_caption("Sorcerers Clash")

#Defines the variable to be the "clock" of the game
clock = pygame.time.Clock()

#Sets the player's character's image
playerImage = pygame.image.load("character.png")

#Defines the player's width and height
playerWidth = playerImage.get_rect().width
playerHeight = playerImage.get_rect().height

#Defines the x and y coordinates of the player
playerX = WIDTH // 2 - playerWidth // 2
playerY = HEIGHT * 3 // 4 + playerHeight // 2
player_pos = (playerX, playerY)

#Make the hitbox of the player using their position
player_rect = playerImage.get_rect(center=player_pos)

#Variables for when the player presses 'W' or 'UP' to jump
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

#Variables for when the player's sword hits the boss
hit = False

#Variables for when the player shoots their bow
bow_number = 0
bow_shoot = False
shoot_arrow = False
allow_angle = True
is_fired = False
arrow_speed = 15

#Sets the arrow's image
arrowUnchanged = pygame.image.load("arrow.png").convert_alpha()
arrowImageUnrotated = pygame.transform.scale(arrowUnchanged, (85, 30))
arrowImage = pygame.transform.rotate(arrowImageUnrotated, 5)
arrow_rect = pygame.Rect(30, 20, 25, 25)

#Sets the boomerang's image and it's coordinates
boomrngImage = pygame.image.load("boomerang.png")
boomrng_rect = boomrngImage.get_rect()
boomrngX = playerX
boomrngY = playerY

#Variables to check for when the player uses the boomerang
boomrng_shoot = False
boomrng_spin = 0
boomrng_speed = 15
allow_aim = True
fly_back = False
boomrng_hit = False

#Variable to check if the player is holding space
spaceHolding = False

#Variable to check if the player's animation is being used
playerAnimation = False

#Sets the background image
backgroundImage = pygame.image.load("background.png")

#Variables for the new width and height for the boss
new_width = 120
new_height = 100

#Sets the boss's image
bossImageUnsized = pygame.image.load("boss.png")
bossImage = pygame.transform.scale(bossImageUnsized, (new_width, new_height))

#Variable to check if player is going left(flipped) or right(not flipped)
playerFlipped = False

#Sets the player's and boss's inital health
playerHealth = 100
bossHealth = 200

#Variable to check if the player got hit from the boss when in contact with the boss
playerGotHit = False

#Defines the position of where the boss will initially be
boss_pos = (350, 400)
bossX = 350
bossY = 400

#Variables to check which attack will the boss "choose"
attackChoice = 0
ATTACKLEFT = 2
ATTACKUP = 4
ATTACKRIGHT = 6
ATTACKDOWN = 8
EVERYWHERE = 10

#Sets the boss fly image
bossFly2 = pygame.image.load("boss.png")
bossRect2 = bossFly2.get_rect(center=(0, 10000))

#Variables to check if the boss has attacked for it to be stunned
attackQuantity = 0
stunnedCount = 0
stunnedCooldown = 0
bossStunned_rect = bossFly2.get_rect()

#Variables for when the boss atacks. Checks if:
sidekickAlive = True        # sidekick is alive or not
boss_damaged = False        # the boss is damaged or not
boss_speed = 5              #Defines the boss's speed to it's destination
bossLanded = False          # the boss has arrived at it's destination
blocked = False             # the boss blocked a projectile
sidekickGotHit = False      # the sidekick got hit from the player
bossDeathCount = 0          #Defines the animation for the boss
boss_going_back = False     # the boss is going back to it's inital position
animationFinished = False   # the animation for the boss has finished
hypoteneuse = 0             #Defines the hypoteneuse for globalizing
fireballCooldown = 0        #Defines the fireball's cooldown for globalizing
last_fireball = 0           #Defines the previous fireball for globalizing
bossShooting = False        # the boss is shooting or not
shooting = False            # the boss is shooting or not
shootingCount = 0           #Defines the shooting animation for the boss
shootAnimation = False      # the boss animation is over or not
fireball_speed = 10         #Defines the speed of the fireball
fireball_vx = 0             #Defines the fireball's X movement
fireball_vy = 0             #Defines the fireball's Y movement
sidekick_animation = 0      #Defines the sidekick's animation
fireCooldown = 0            #Defines the cooldown for the fire
fireCount = 0               #Defines the animation for the fire
spawn_fire = False          #Variable to check if the fire is spawned
explosionCount = 0          #Defines the explosion's animation
exploding = False           #Variable to check if the explosion is et
explosion_size = 0          #Defines the explosion's size

#Variables that check whether or not the player or the boss is dead
player_dead = False
boss_dead = False

#Define's the player's death animation
playerDeathCount = 0

#Variable to check if the player is dead or not
gameOver = False

#Variables for the leave button after player dies
leaveButton_width = 200
leaveButton_height = 75
leaveButton_x = 300
leaveButton_y = 500
leaveButton_textSize = 50
leaveButton_rect = pygame.Rect(leaveButton_x, leaveButton_y, leaveButton_width, leaveButton_height)

#Variables for the closing animation when player dies
movingYAmount = 0
movingXAmount = 0
closingAnimation = False
rightVertical = False
stopRightVertical = False
shrink_circle = True
radiusNumber = 0
shrinkRadius = 567    #Calculated using square root of (WIDTH ** 2 + HEIGHT ** 2) Then divided by 2
game_screen = True
random_text = False

#Variables to check if player defeats the boss
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
endGame = False
last_text_time = 0

#Sets the fireball image for the boss's projectile
fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
fireballImageUnrotated = pygame.transform.scale(fireballImageUnsized, (100, 50))
fireball_rect = fireballImageUnrotated.get_rect(topleft=(10000, 0))
fire_rect = fireballImageUnrotated.get_rect(center=(0, 0))
fireball_rect2 = pygame.Rect(0, 0, 0, 0)
fireballImage2 = pygame.image.load("fireball.png")

#Variables to define the projectiles of the boss
fireballX = 0
fireballY = 0
fireballX2 = 0
fireball_cooldown = 0
fireballMovement = 0
fireballMovement2 = 0
setFireballMovement = True
setFireballMovement2 = True
bossFlipped = False
shoot_number = 0
bossLanded = False
fireball_shoot = False
bossShootCount = 0
shoot_spot = 0
bigFireballX = 0
bigFireballY = 0
bigExplosionCount = 0
bigExplosionSize = 0
revert_explosion = False
stopExplosion = False
bigFireball_rect = pygame.Rect(0, 0, 0, 0)
fire_animation_count = 0
idleCount = 0
platformX = 0
on_platform = False
platform_rect = pygame.Rect(0, 0, 0, 0)
bigFireball_rect = pygame.Rect(0, 0, 0, 0)
fireballShower = False
swordRect = swordRect = pygame.Rect(player_rect.centerx + 670, player_rect.centery - 700, 25, 10)

#Sets the second fireball image and it's hitbox
fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
fireballImageUnrotated = pygame.transform.scale(fireballImageUnsized, (150, 100))
fireballImage = pygame.transform.rotate(fireballImageUnrotated, 45)
fireballX2 = 0
#Sets other fireball hitboxes
fireballHitbox = pygame.Rect(0, 0, 0, 0)
fireball2Hitbox = pygame.Rect(0, 0, 0, 0)
fireball3Hitbox = pygame.Rect(0, 0, 0, 0)
fireball4Hitbox = pygame.Rect(0, 0, 0, 0)
fireball5Hitbox = pygame.Rect(0, 0, 0, 0)

#Sets the boomerang image
boomrngImage = pygame.image.load("boomerang.png").convert_alpha()
boomrng_rect = boomrngImage.get_rect(center=(boomrngX, boomrngY))
boomrng_rect.center = (boomrngX + 4000, boomrngY + 4000)

#Sets the variable to become the last action time
last_action_time = pygame.time.get_ticks()

#Variable to check if the boss is attacking or not
attacking = False

#Variables that checks if sound is played
sound = 0
fireballSound = 0
fireSound = 0

#Sets the background music
pygame.mixer.music.load("sounds/background_music.mp3")
pygame.mixer.music.play(-1)

#Sounds that will be used for the game
spinning_sound = pygame.mixer.Sound("sounds/boomrng_throw.wav")
arrow_sound = pygame.mixer.Sound("sounds/arrow_shoot.wav")
fire_sound = pygame.mixer.Sound("sounds/fire_sound.wav")
sword_sound = pygame.mixer.Sound("sounds/sword_sound.wav")
fireball_sound = pygame.mixer.Sound("sounds/fireball_shoot.mp3")
bigFireball_sound = pygame.mixer.Sound("sounds/bigFireball_sound.wav")
explosion_sound = pygame.mixer.Sound("sounds/explosion_sound.wav")
fires_sound = pygame.mixer.Sound("sounds/fires_sound.wav")
################################################ FUNCTIONS ###################################################

#Function to start the game
def startGame():
    global attacking, current_time, animationFinished, bossHealth, boss_dead, bossRect, player_dead, gameOver, playerY, playerX
    running = True
    #Sets the running loop so it remains forever until something closes it
    while running:
        #If the player is still alive
        if gameOver == False:
            #If the player has not clicked on the 'ESC' key
            if endGame == False:
                current_time = pygame.time.get_ticks() #Sets the current time for further usage
            clock.tick(FPS)                     #Sets the frames per second to be the defined variable, FPS(30)
            drawGame()                          #Draw the game, background, characters, health bars
            findEvents()                        #Check if the player presses the exit button or the play button
            keys = pygame.key.get_pressed()
            handleKeys(keys)                    #Checks what keys the player presses
            checkIfJumping()                    #Checks if the player jumping
            checkCollisions()                   #Checks if the player hits the wall so it does not go off-screen
            bossIdle()                          #Function to animate the boss flying
            CheckBossPosition()                 #Checks where the boss is for the game
            checkForEscape(keys)                #Checks if the player presses 'ESC' key

            #If the player's health is 0 or below
            if playerHealth <= 0:
                #Sets the Y coordinates of the player to be on the ground in case the player jumped
                playerY = 667
                gameOver = True

            #If the boss's health is 0 or below
            if bossHealth <= 0:
                boss_dead = True
                #Sets the boss's hitbox away from the game screen
                bossRect.center = (-1000, -1000)
                bossStunned_rect.center = (-10000, -10000)
                bossDeath()     #Function to animate the boss's death
                makeArrows()    #Function draw arrows the guide the player in the game

                #If the player clicks 'E' or if the variable scroll_map is true
                if E_clicked == True or scroll_map == True:
                    #Set the X coordinates of the player to be 0
                    playerX = 0
                    scrollMaps()    #Function to create a new map

            if boss_going_back == True and animationFinished == True:
                bossGoBack()        #Function to make the boss fly back to it's inital possition
            else:
                bossAttack()        #Function to make the boss attack the player

            updateHealthBars()      #Function to update player's and boss's health bars if damaged 

            #If player presses 'ESC'
            if menu == True:
                escapeMenu()        #Function to create a menu

            #If player is moving to the left
            if moving_left == True:
                leftAnimation()     #Function to animate the player walking left

            #If the player is moving to the right
            elif moving_right == True:
                rightAnimation()    #Function to animate the player walking right

            #If the player chooses their weapon as a sword
            if weapon_choice == SWORD:
                sword_choice()      #Function to create the sword and sword swinging animation

            #If the player chooses their weapon as a bow
            elif weapon_choice == BOW:
                bow_choice()        #Function to create the bow and the animation for the shooting
            
            #If the player chooses their weapon as a boomerang
            else:
                boomrng_choice()    #Function to create the boomerang and the animation of the throw

            #Check if the boss gets hit by the player's weapon or if the player gets hit by the boss
            checkIfHit()
            
            #If the boss is damaged from the player
            if boss_damaged == True:
                bossDamaged()       #Function to animate the boss getting damaged

            #Updates the game
            pygame.display.update()

        #If the player is defeated
        else:
            #Stop the current music and play the ending music
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/ending_sound.mp3")
            pygame.mixer.music.play(-1)
            #Function to check if the player closes the program
            findEvents()
            #Function to animate the player's death
            playerDeath()

            #If the player's death animation is finished
            if player_dead == True:
                closingAnimations()     #Function to create a animation to conclude the game

            #If the closing animation has ended
            if closingAnimation == True:
                gameOverScreen()        #Function to create the game over menu

            #Updates the program
            pygame.display.update()

def makeArrows():
    global radius, E_clicked, grow_circle, sign_font
    #Draws an arrow pointing a direction on the right
    pygame.draw.line(SCREEN, BLUE, (WIDTH - 40, 700), (WIDTH - 80, 660), 8)
    line_rect = pygame.draw.line(SCREEN, BLUE, (WIDTH - 40, 700), (WIDTH - 80, 740), 8)

    #If the player touches the lower line
    if player_rect.colliderect(line_rect):
        sign_text = "Press 'E' to interact!"
        sign_font = pygame.font.SysFont("Comic Sans MS", 20)

        sign_surface = sign_font.render(sign_text, True, BLACK)
        sign_rect = sign_surface.get_rect(center=(WIDTH - 130, 550))

        #Create the text for the player to see
        SCREEN.blit(sign_surface, sign_rect)

        keys = pygame.key.get_pressed()
        #If the player presses the 'E' key
        if keys[pygame.K_e]:
            grow_circle = True
            radius = 0
            #Make an animation of a circle growing
            while grow_circle == True:
                growCircle()
                pygame.display.update()

            E_clicked = True

def scrollMaps():
    global playerY, ground_y, playerFlipped, endOfGame, shrink_circle, radiusNumber, moving_left, moving_right
    global endOfGame, civilian_run, endGame, last_text_time, current_time
    map_scroll = True
    #Play the new background music
    pygame.mixer.music.load("sounds/final_background_music.mp3")
    pygame.mixer.music.play(-1)
    #Loops the new map
    while map_scroll == True:
        #Set the frames per second to FPS(30)
        clock.tick(FPS)
        findEvents()        #Function to check if the player exits the program
        drawMap()           #Draws the new map and updates if the player moves
        drawPlayer()        #Create the player and its animation

        keys = pygame.key.get_pressed()
        #If the player did not interact with the civilian
        if civilian_interact == False and endOfGame == False:
            checkKeysMap(keys)      #Function to check what keys the player presses
            shrink_circle = True
            radiusNumber = 0
        #If the player has interacted with the civilian
        else:
            #Set the movement to false and initiate the interaction
            moving_left = False
            moving_right = False
            playerFlipped = False
            player_rect.topleft = (playerX, playerY)
            civilianInteraction()   #Function to interact with the civilian

        #If the interaction with the civilian is over and civilian stops running
        if endOfGame == True and civilian_run == False:
            #Make an animation of shrinking the circle
            while shrink_circle == True:
                clock.tick(FPS)
                findEvents()
                shrinkCircle()
            
            if endGame == False:
                drawEnding()        #Function to draw the ending after the interaction with the civilian
                checkForExit()      #Check if the player has pressed the 'ESC' or 'SPACE' key
                shrink_circle = True
                #Check for the last time the text has appeared
                last_text_time = pygame.time.get_ticks()
            else:
                endingText()        #Function to create a cliffhanger for the player

        screenScroll()      #Function to create the screen to move when the player reaches a limit or wall
        createCivilian()    #Function to create the civilian and move along the screen
        playerY = 550       #Keep the player's Y coordinates to be 550

        #If the player moves left
        if moving_left == True:
            leftAnimation()     #Function to animate the player walking left

        #If the player moves right
        elif moving_right == True:
            rightAnimation()    #Function to animate the player walking right

        #Updates the game
        pygame.display.update()

def endingText():
    global last_text_time, current_time, sound
    #Fill the screen with black
    SCREEN.fill(BLACK) 
    #Find the current time 
    current_time = pygame.time.get_ticks()
    pygame.mixer.music.stop()
    if sound == 0:
        pygame.mixer.music.load("sounds/ending_sound.mp3")
        pygame.mixer.music.play(-1)
        sound = 1
    
    #Create the font of the text and the text itself
    last_font = pygame.font.SysFont("Georgia", 20)
    last_text = '<Unknown> "My queen dragon has been defeated, huh?"'
    last_text2 = '<Unknown> "I see."'
    last_text3 = '<Unknown> "How dare they slay such beauty."'
    last_text4 = '<Unknown> "With this royalty, I summon"'
    last_text5 = '<Unknown> "The Dragon King."'

    #Find the time difference between the current time and the first text time
    time_difference = current_time - last_text_time

    #If the time difference is less than or equal to 3000 milliseconds
    if time_difference <= 3000:
        last_surf = last_font.render(last_text, True, WHITE)
        last_rect = last_surf.get_rect(center=(400, 400))
        SCREEN.blit(last_surf, last_rect)
    
    #If the time difference is more than 3000 and less than or equal to 5000 milliseconds
    elif time_difference > 3000 and time_difference <= 5000:
        last_surf2 = last_font.render(last_text2, True, WHITE)
        last_rect2 = last_surf2.get_rect(center=(400, 400))
        SCREEN.blit(last_surf2, last_rect2)
    
    #If the time difference is more than 5000 and less than or equal to 7500 milliseconds
    elif time_difference > 5000 and time_difference <= 7500:
        last_surf3 = last_font.render(last_text3, True, WHITE)
        last_rect3 = last_surf3.get_rect(center=(400, 400))
        SCREEN.blit(last_surf3, last_rect3)

    
    elif time_difference > 7500 and time_difference <= 10500:
        last_surf4 = last_font.render(last_text4, True, WHITE)
        last_rect4 = last_surf4.get_rect(center=(400, 400))
        SCREEN.blit(last_surf4, last_rect4) 

    elif time_difference > 10500 and time_difference <= 13500:
        last_surf5 = last_font.render(last_text5, True, WHITE)
        last_rect5 = last_surf5.get_rect(center=(400, 400))
        SCREEN.blit(last_surf5, last_rect5)

    else:
        quitGame()

def checkForExit():
    global endGame
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
        endGame = True

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
    exit_text = "Press 'ESC' or 'SPACE' to exit!"

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

    exit_text_surface = subtitle_font.render(exit_text, True, BLACK)
    exit_text_rect = exit_text_surface.get_rect(center=(400, 600))

    SCREEN.blit(body_text_surface, body_text_rect)
    SCREEN.blit(body_text_surface2, body_text_rect2)
    SCREEN.blit(body_text_surface3, body_text_rect3)
    SCREEN.blit(body_text_surface4, body_text_rect4)
    SCREEN.blit(body_text_surface5, body_text_rect5)
    SCREEN.blit(body_text_surface6, body_text_rect6)
    SCREEN.blit(body_text_surface7, body_text_rect7)
    SCREEN.blit(body_text_surface8, body_text_rect8)
    SCREEN.blit(exit_text_surface, exit_text_rect)
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
        screenX -= 7
        screenLimitLeft = False
    
    if playerX <= 200 and moving_left and not moving_right and not screenLimitLeft:
        playerX = 200
        screenX += 7
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

    if keys[pygame.K_e]:
        if player_rect.colliderect(civilian_rect):
            civilian_interact = True

def civilianInteraction():
    global civilian_running, interaction_next, space_holding, civilian_interact, endOfGame, sound, civilian_sound
    if civilian_running == False:
        pygame.draw.rect(SCREEN, BLACK, (50, 100, 720, 100))
        pygame.draw.rect(SCREEN, WHITE, (50, 100, 720, 100), 10)

    if sound == 0:
        civilian_sound = pygame.mixer.Sound("sounds/civilian_talking.mp3")
        civilian_sound.play()

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
        sound = 1
        civilian_sound.stop()
        civilian_running = True
        civilian_interact = False
        endOfGame = True
        civilianRun()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and space_holding == False:
        space_holding = True
        interaction_next += 1
        click_sound = pygame.mixer.Sound("sounds/click_civilian_sound.wav")
        click_sound.play()

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
    global playerImage, playerX, playerY, playerRun, playerFlipped

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
    global playerRun, playerX, playerY, playerAnimation, bossFly, playerFlipped

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

    if endOfGame == False or endGame == True:
        pygame.draw.circle(SCREEN, BLACK, player_rect.center, shrinkRadius + 1000, 800)

    elif endOfGame == True and endGame == False:
        pygame.draw.circle(SCREEN, LIGHTBLUE, player_rect.center, shrinkRadius + 1000, 800)

    radiusNumber += 0.5
    shrinkRadius -= radiusNumber

    if shrinkRadius + 1000 <= 0:
        shrink_circle = False
        return

    pygame.display.update()

def playerDeath():
    global playerDeathCount, player_dead, playerFlipped

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
    global explosion_size, bossDeathCount, sound

    explosion_sound.play()

    if bossDeathCount == 16:
        bossRect.center = (-1000, -1000)
        explosion_sound.stop()
        pygame.mixer.music.stop()
        sound = 0
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
        attackChoice = random.randint(1, 10)
        if attackQuantity == 0:
            attacking = True
        
        else:
            bossStunned()

    if boss_going_back == False and attackQuantity == 0 and boss_dead == False:
        if attackChoice <= ATTACKLEFT:
            bossAttackLeft()
       
        elif attackChoice <= ATTACKUP and attackChoice > ATTACKLEFT:
            bossAttackUp()

        elif attackChoice <= ATTACKRIGHT and attackChoice > ATTACKUP:
            bossAttackRight()

        elif attackChoice <= ATTACKDOWN and attackChoice > ATTACKRIGHT:
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
                shoot_sound = pygame.mixer.Sound("sounds/fireball_shoot.mp3")
                shoot_sound.play()
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

        #Show sidekick hitbox during attack left
        #pygame.draw.rect(SCREEN, GREEN, bossRect2, 3)

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
    global fireCount, spawn_fire, fireCooldown, fire_rect, fireX, fireY, last_action_time, fire_sound, fireSound
    if fireSound == 0:
        fire_sound.play()
        fireSound = 1
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
        fire_sound.stop()
        fireSound = 0
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
        shootingImageUnsized = pygame.image.load(f"sidekick_attack/{shootingCount}.png").convert_alpha()
        shootingCount += 1


        shootingImage = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shooting_rect = shootingImage.get_rect(topleft=(bossX2, bossY2))

        if playerX > fireball_rect.centerx:
            shootingImage = pygame.transform.flip(shootingImage, True, False)

        SCREEN.blit(shootingImage, shooting_rect)

def bossGoBack():
    global boss_animation_count, bossX, bossY, bossRect, boss_going_back, attacking, animationFinished, hypoteneuse, sidekickAlive, bossLanded
    global revert_explosion, stopExplosion, bigFireball_rect, fireball_shoot, shoot_number, attackQuantity, bigFireballY, fireCooldown, fireball_rect
    global fireballShower, bossFlipped, fireballMovement, fireballMovement2, setFireballMovement, setFireballMovement2
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect.topleft = (bossX, bossY)
    if boss_animation_count == 12:
        boss_animation_count = 0
    
    attacking = False

    backX = 350
    backY = 400
    bossX, bossY, hypoteneuse = findHypoteneuse(backX, backY, bossX, bossY, hypoteneuse, boss_speed)

    if hypoteneuse <= boss_speed:
        if attackChoice <= ATTACKLEFT:
            boss_going_back = False
            animationFinished = False
            sidekickAlive = True
            bossLanded = False
            fireCooldown = 5000
            fireball_rect.center = (1000, 1000)

        if attackChoice <= ATTACKUP and attackChoice > ATTACKLEFT:
            boss_going_back = False
            bossLanded = False
            revert_explosion = False
            stopExplosion = False
            fireball_shoot = False
            bigFireball_rect.center = (50000, 2000)
            shoot_number = 0
            attackQuantity += 1
            bigFireballY = 0
    
        if attackChoice <= ATTACKRIGHT and attackChoice > ATTACKUP:
            attacking = False
            boss_going_back = False
            bossLanded = False
            attackQuantity += 1
        
        if attackChoice <= ATTACKDOWN and attackChoice > ATTACKRIGHT:
            attacking = False
            boss_going_back = False
            bossLanded = False
            fireballShower = False
            fireball_shoot = False
            attackQuantity += 1

        if attackChoice <= EVERYWHERE and attackChoice > ATTACKDOWN:
            attacking = False
            boss_going_back = False
            bossLanded = False
            bossFlipped = False
            fireball_shoot = False
            fireball_rect.center = (-1000, 1000)
            fireball_rect2.center = (-1000, 1000)
            fireballMovement = 0
            fireballMovement2 = 0
            setFireballMovement = True
            setFireballMovement2 = True
            attackQuantity += 1

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

def bossAttackUp():
    global boss_animation_count, bossX, bossY, fireball_shoot, fireballMovement, bossLanded, bossShootCount, shoot_number, bossRect, shoot_spot
    global bigFireballY, bigFireballX, bigExplosionCount, bigExplosionSize, stopExplosion, revert_explosion, boss_going_back, playerX, playerY, playerHealth
    global fire_animation_count, fire_rect, fireballSound, fireball_sound, bigFireball_sound

    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png").convert_alpha()
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect = bossFly.get_rect(topleft=(bossX, bossY))
    if shoot_number == 4:
        fireball_shoot = True

    if boss_animation_count == 12:
        boss_animation_count = 0

    if bossLanded == False:
        up_surf = pygame.Surface((50, 50))
        up_rect = up_surf.get_rect(center=(400, 100))

        upX = up_rect.centerx
        upY = up_rect.centery

        run = upX - bossX
        rise = upY - bossY

        upHypoteneuse = math.sqrt(run ** 2 + rise ** 2)

        if upHypoteneuse == 0:
            return

        boss_x_speed = run/upHypoteneuse * boss_speed
        boss_y_speed = rise/upHypoteneuse * boss_speed
        bossX += boss_x_speed
        bossY += boss_y_speed

        SCREEN.blit(bossFly, (bossX, bossY))

        if upHypoteneuse <= boss_speed:
            bossX = upX
            bossY = upY
            bossLanded = True

    elif bossLanded == True and fireball_shoot == False and shoot_number <= 5:
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImageRotated = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shootingImage = pygame.transform.rotate(shootingImageRotated, -90)   
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))

        if bossShootCount == 24:
            fireball_shoot = True

        SCREEN.blit(shootingImage, shooting_rect)

    if fireball_shoot == True:
        if shoot_number <= 3:
            if fireballSound == 0:
                fireball_sound.play()
                fireballSound = 1
            fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
            fireballImageUnrotated = pygame.transform.scale(fireballImageUnsized, (150, 100))
            fireballImage = pygame.transform.rotate(fireballImageUnrotated, -90)
            fireball_rect = fireballImage.get_rect(center=(bossX + 40, bossY - fireballMovement))
            fireballMovement += 10

            if bossY - fireballMovement <= -20:
                fireballMovement = 0
                bossShootCount = 0
                shoot_number += 1
                if shoot_number != 3:
                    fireball_shoot = False
                    fireballSound = 0
                else:
                    fireball_shoot = True

            bigFireballX = random.randint(50, 700)

            SCREEN.blit(fireballImage, fireball_rect)

        else:

            if bigFireballY - 200 <= 800:
                fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
                fireballImageUnrotated = pygame.transform.scale(fireballImageUnsized, (750, 500))
                bigFireballImage = pygame.transform.rotate(fireballImageUnrotated, 90)
                bigFireball_rect = bigFireballImage.get_rect(center=(bigFireballX, bigFireballY - 200))
                bigFireballY += 10
                bigFireballRight = pygame.Rect(bigFireball_rect.centerx + 100, bigFireball_rect.centery + 50, 100, 200)
                bigFireballLeft = pygame.Rect(bigFireball_rect.centerx - 100, bigFireball_rect.centery + 50, 100, 200)

                #Draw big fire ball hitbox
                #pygame.draw.rect(SCREEN, GREEN, bigFireballLeft, 3)
                #pygame.draw.rect(SCREEN, RED, bigFireballRight, 3)

                SCREEN.blit(bigFireballImage, bigFireball_rect)

                if bigFireballLeft.colliderect(player_rect):
                    playerX -= 500
                    playerY -= 300
                    playerHealth -= 20

                elif bigFireballRight.colliderect(player_rect):
                    playerX += 500
                    playerY -= 300
                    playerHealth -= 20

            else:
                if fireballSound == 0:
                    bigFireball_sound.play()
                    fireballSound = 1
                if bigExplosionCount == 0 and revert_explosion == True:
                    bigExplosionCount = 0
                    stopExplosion = True
                    boss_going_back = True
                    fireballSound = 0
                
                if boss_going_back == True:
                    bossGoBack()

                if stopExplosion == True:
                    fire_rect.center = (50000, 2000)

                if stopExplosion == False:
                    if fireballSound == 0:
                        fireballSound = 1
                        explosion_sound.play()
                    bigExplosionUnsized = pygame.image.load(f"bigFireball_collide/{bigExplosionCount}.png").convert_alpha()
                    if revert_explosion == False:
                        bigExplosionCount += 1

                    if bigExplosionCount == 16 or revert_explosion == True:
                        revert_explosion = True
                        bigExplosionCount -= 1


                    bigExplosion = pygame.transform.scale(bigExplosionUnsized, (bigExplosionSize + 598, bigExplosionSize + 500))
                    if revert_explosion == False:
                        bigExplosionSize += 5
                    else:
                        bigExplosionSize -= 5
                    bigExplosion_rect = bigExplosion.get_rect(center=(bigFireballX, bigFireballY - 300))

                    if revert_explosion == True:
                        largeFireImageUnsized = pygame.image.load(f"fire/{fire_animation_count}.png").convert_alpha()
                        largeFireImage = pygame.transform.scale(largeFireImageUnsized, (367, 250))
                        fire_animation_count += 1
                        if fire_animation_count == 7:
                            fire_animation_count = 0

                        fire_rect = largeFireImage.get_rect(center=(bigFireballX, bigFireballY - 300))

                        SCREEN.blit(largeFireImage, fire_rect)

                    SCREEN.blit(bigExplosion, bigExplosion_rect)

        SCREEN.blit(bossFly, (bossX, bossY))

def bossAttackRight():
    global boss_animation_count, bossX, bossY, shoot_number, bigFireballX, fireball_shoot, bossLanded, bossShootCount, fireballMovement
    global idleCount, platformX, jumping, falling, ground_y, on_platform, playerY, platform_rect, bigFireball_rect, boss_going_back, playerHealth
    global fireballSound, fireball_sound
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png").convert_alpha()
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect.topleft = (bossX, bossY)
    if boss_animation_count == 12:
        boss_animation_count = 0

    if bigFireballX - 1100 >= 1000:
        fireballSound = 0
        shoot_number = 0
        bigFireballX = 0
        fireball_shoot = False
        platform_rect.center = (100, 50000)
        bigFireball_rect.center = (0, 5000)
        boss_going_back = True
        on_platform = False
        falling = True
        platformX = 0

    if boss_going_back == True:
        bossGoBack()
        return
    
    if bossLanded == False:
        right_surf = pygame.Surface((50, 50))
        right_rect = right_surf.get_rect(center=(600, 100))

        rightX = right_rect.centerx
        rightY = right_rect.centery
        run = rightX - bossX
        rise = rightY - bossY

        rightHypoteneuse = math.sqrt(run ** 2 + rise ** 2)
        if rightHypoteneuse == 0:
            return
        
        boss_x_speed = run/rightHypoteneuse * boss_speed
        boss_y_speed = rise/rightHypoteneuse * boss_speed
        bossX += boss_x_speed
        bossY += boss_y_speed

        if rightHypoteneuse <= boss_speed:
            bossX = rightX
            bossY = rightY
            bossLanded = True

        SCREEN.blit(bossFly, (bossX, bossY))

    elif bossLanded == True and fireball_shoot == False:
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImage = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))

        if bossShootCount == 24:
            bossShootCount = 0
            fireball_shoot = True
        
        SCREEN.blit(shootingImage, shooting_rect)

    if fireball_shoot == True:
        bossIdleImageUnsized = pygame.image.load(f"boss_idle/{idleCount}.png").convert_alpha()
        idleCount += 1
        bossIdleImage = pygame.transform.scale(bossIdleImageUnsized, (new_width, new_height))
        idle_rect = bossIdleImage.get_rect(topleft=(bossX, bossY))
        if idleCount == 12:
            idleCount = 0

        SCREEN.blit(bossIdleImage, idle_rect)

        if shoot_number <= 2:
            if fireballSound == 0:
                fireball_sound.play()
                fireballSound = 1
            fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
            fireballImage = pygame.transform.scale(fireballImageUnsized, (150, 100))
            fireball_rect = fireballImage.get_rect(center=(bossX + fireballMovement, bossY + 50))
            fireballMovement -= 20

            if fireball_rect.centerx <= 0:
                shoot_number += 1
                fireballMovement = 0
                fireball_shoot = False
                fireballSound = 0

            SCREEN.blit(fireballImage, fireball_rect)

        else:
            if fireballSound == 0:
                fireballSound = 1
                bigFireball_sound.play()
            fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
            bigFireballImageUnflipped = pygame.transform.scale(fireballImageUnsized, (750, 500))
            bigFireballImage = pygame.transform.flip(bigFireballImageUnflipped, True, False)
            bigFireball_rect = bigFireballImage.get_rect(center=(bigFireballX - 1000, 750))
            bigFireballHitbox = pygame.Rect(bigFireballX - 1300, bigFireballY + 650, bigFireball_rect.width - 130, bigFireball_rect.height)
            bigFireballX += 10

            SCREEN.blit(bigFireballImage, bigFireball_rect)

            platformImageUnsized = pygame.image.load("platform.png").convert_alpha()
            platformImage = pygame.transform.scale(platformImageUnsized, (269, 100))
            if platformX == 0:
                platformX = random.randint(200, 750)
            platform_rect = platformImage.get_rect(center=(platformX, 650))
            platform_rectTop = pygame.Rect(platform_rect.centerx - 100, platform_rect.centery - 75, platform_rect.width - 50, 10)
            
            #Show platform hitbox
            #pygame.draw.rect(SCREEN, RED, platform_rect, 3)
            #pygame.draw.rect(SCREEN, GREEN, platform_rectTop, 3)

            if player_rect.colliderect(platform_rectTop):
                player_rect.bottom = platform_rectTop.bottom
                on_platform = True
                jumping = False
                falling = True

            if not player_rect.colliderect(platform_rectTop) and on_platform == True:
                ground_y = 667
                falling = True
                on_platform = False

            if player_rect.colliderect(platform_rect):
                falling = True

            if player_rect.colliderect(bigFireballHitbox):
                playerY -= 300
                playerHealth -= 10

            #Show fireball hitbox for attacking up
            #pygame.draw.rect(SCREEN, RED, bigFireballHitbox, 3)

            SCREEN.blit(platformImage, platform_rect)

def bossAttackDown():
    global fireballY, fireballX, fireballY2, fireballX2, fireballY3, fireballX3, fireballY4, fireballX4, fireballY5, fireballX5
    global fireballShower, bossLanded, bossX, bossY, fireball_shoot, fireballShower, bossShootCount, idleCount
    global boss_wait_time, fireballImage, fireball_cooldown, boss_going_back, playerX, playerY, playerHealth
    global fireball_rect, fireball_rect2, fireball_rect3, fireball_rect4, fireball_rect5, exploding, fireball_cooldown
    global fireballHitbox, fireball2Hitbox, fireball3Hitbox, fireball4Hitbox, fireball5Hitbox, fires_sound, fireballSound
    bossRect.topleft = (bossX, bossY)

    if boss_going_back == True:
        bossGoBack()
        return
    
    if bossLanded == False:
        down_surf = pygame.Surface((50, 50))
        down_rect = down_surf.get_rect(center=(400, 100))
        downX = down_rect.centerx
        downY = down_rect.centery
        run = downX - bossX
        rise = downY - bossY

        downHypoteneuse = math.sqrt(run ** 2 + rise ** 2)
        if downHypoteneuse == 0:
            return
        
        boss_x_speed = run/downHypoteneuse * boss_speed
        boss_y_speed = rise/downHypoteneuse * boss_speed
        bossX += boss_x_speed
        bossY += boss_y_speed

        if downHypoteneuse <= boss_speed:
            bossX = downX
            bossY = downY
            bossLanded = True
        
        SCREEN.blit(bossFly, (bossX, bossY))
    
    elif bossLanded == True and fireball_shoot == False:
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImage = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))

        if bossShootCount == 24:
            bossShootCount = 0
            fireball_shoot = True
        
        SCREEN.blit(shootingImage, shooting_rect)
        boss_wait_time = pygame.time.get_ticks()

    if fireball_shoot == True:
        current_time = pygame.time.get_ticks()
        if current_time - boss_wait_time >= 2000:
            fireballShower = True
        bossIdleImageUnsized = pygame.image.load(f"boss_idle/{idleCount}.png").convert_alpha()
        idleCount += 1
        bossIdleImage = pygame.transform.scale(bossIdleImageUnsized, (new_width, new_height))
        idle_rect = bossIdleImage.get_rect(topleft=(bossX, bossY))
        if idleCount == 12:
            idleCount = 0
        
        SCREEN.blit(bossIdleImage, idle_rect)
        if fireballX2 == 0:
            fireballX = random.randint(300, 750)
            fireballX2 = random.randint(300, 650)
            fireballX3 = random.randint(500, 850)
            fireballX4 = random.randint(200, 950)
            fireballX5 = random.randint(0, 950)
            fireballY = random.randint(-200, -50)
            fireballY2 = random.randint(-300, -10)
            fireballY3 = random.randint(-400, -100)
            fireballY4 = random.randint(-300, -10)
            fireballY5 = random.randint(-500, -10)
            fireball_cooldown = pygame.time.get_ticks()  

    if fireballShower == True:
        if fireball_cooldown == 0:
            fireball_cooldown = pygame.time.get_ticks()
        fireballImage2 = fireballImage
        fireballImage3 = fireballImage
        fireballImage4 = fireballImage
        fireballImage5 = fireballImage
        current_time = pygame.time.get_ticks()

        fireball_rect = fireballImage.get_rect(center=(fireballX, fireballY - 50))
        fireballHitbox = pygame.Rect(fireballX - 50, fireballY - 50, 75, 75)
        fireballY += 15
        fireballX -= 5

        if current_time - fireball_cooldown >= 4000:
            if fireballSound == 0:
                fires_sound.play()
                fireballSound = 1
            fireball2Hitbox = pygame.Rect(fireballX2 - 50, fireballY2 - 50, 75, 75)
            fireball_rect2 = fireballImage2.get_rect(center=(fireballX2, fireballY2 - 50))
            fireballY2 += 15
            fireballX2 -= 5
            SCREEN.blit(fireballImage2, fireball_rect2)

        if current_time - fireball_cooldown >= 5000:
            fireball3Hitbox = pygame.Rect(fireballX3 - 50, fireballY3 - 50, 75, 75)
            fireball_rect3 = fireballImage3.get_rect(center=(fireballX3, fireballY3 - 50))
            fireballY3 += 15
            fireballX3 -= 5
            SCREEN.blit(fireballImage3, fireball_rect3)

        if current_time - fireball_cooldown >= 6000:
            fireball4Hitbox = pygame.Rect(fireballX4 - 50, fireballY4 - 50, 75, 75)
            fireball_rect4 = fireballImage4.get_rect(center=(fireballX4, fireballY4 - 50))
            fireballY4 += 15
            fireballX4 -= 5
            SCREEN.blit(fireballImage4, fireball_rect4)

        if current_time - fireball_cooldown >= 7000:
            fireball5Hitbox = pygame.Rect(fireballX5 - 50, fireballY5 - 50, 75, 75)
            fireball_rect5 = fireballImage5.get_rect(center=(fireballX5, fireballY5 - 50))
            fireballY5 += 15
            fireballX5 -= 5
            SCREEN.blit(fireballImage5, fireball_rect5)
        
        if fireballY5 >= 800:
            boss_going_back = True
            fireballY5 = 0
            fireballX2 = 0
            fireballSound = 0
        
        elif fireballY4 >= 800:
            fireball_rect4.center = (10000, 10234)
            fireballX4 = -1000
        
        elif fireballY3 >= 800:
            fireball_rect3.center = (245, 1000)
            fireballX3 = -1000

        elif fireballY2 >= 800:
            fireball_rect2.center = (245, 1000)
            fireballX2 = -1000

        elif fireballY >= 800:
            fireball_rect.center = (245, 1000)
            fireballX = -1000

        if player_rect.colliderect(fireballHitbox) or player_rect.colliderect(fireball2Hitbox) or player_rect.colliderect(fireball3Hitbox) or player_rect.colliderect(fireball4Hitbox) or player_rect.colliderect(fireball5Hitbox):
            playerX += 300
            playerY -= 200
            playerHealth -= 5

        SCREEN.blit(fireballImage, fireball_rect)
        #Show fireballs hitbox for attacking down
        # pygame.draw.rect(SCREEN, RED, fireballHitbox, 3)
        # pygame.draw.rect(SCREEN, RED, fireball2Hitbox, 3)
        # pygame.draw.rect(SCREEN, RED, fireball3Hitbox, 3)
        # pygame.draw.rect(SCREEN, RED, fireball4Hitbox, 3)
        # pygame.draw.rect(SCREEN, RED, fireball5Hitbox, 3)

def bossAttackEverywhere():
    global boss_animation_count, bossLanded, fireball_shoot, bossShootCount, fireballMovement
    global bossX, bossY, fireballMovement2, fireball_rect2, setFireballMovement, setFireballMovement2
    global fireballImage2, fireballX, fireballX2, bossFlipped, boss_going_back, playerX, playerY, playerHealth, fireballSound

    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png").convert_alpha()
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect.topleft = (bossX, bossY)
    if boss_animation_count == 12:
        boss_animation_count = 0

    if boss_going_back == True:
        bossGoBack()
        return
    
    if bossLanded == False:
        evrwhere_surf = pygame.Surface((50, 50))
        evrwhere_rect = evrwhere_surf.get_rect(center=(600, 100))
        evrwhereX = evrwhere_rect.centerx
        evrwhereY = evrwhere_rect.centery

        run = evrwhereX - bossX
        rise = evrwhereY - bossY
        evrwhereHypoteneuse = math.sqrt(run ** 2 + rise ** 2)
        if evrwhereHypoteneuse == 0:
            return
        
        boss_x_speed = run/evrwhereHypoteneuse * boss_speed
        boss_y_speed = rise/evrwhereHypoteneuse * boss_speed
        bossX += boss_x_speed
        bossY += boss_y_speed

        if evrwhereHypoteneuse <= boss_speed:
            bossX = evrwhereX
            bossY = evrwhereY
            bossLanded = True

        SCREEN.blit(bossFly, (bossX, bossY))

    elif bossLanded == True:
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImageUnrotated = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shootingImage = pygame.transform.rotate(shootingImageUnrotated, 90)
        if bossFlipped == True:
            shootingImage = pygame.transform.flip(shootingImage, True, False)
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))
        if bossShootCount == 24:
            bossShootCount = 0
            fireball_shoot = True

        SCREEN.blit(shootingImage, shooting_rect)
        if bossX <= 20 and bossFlipped == False:
            bossFlipped = True

        if bossX >= 750 and bossFlipped == True:
            boss_going_back = True
            fireballSound = 0

        if bossFlipped == True:
            bossX += 5
        else:
            bossX -= 5

    if fireball_shoot == True:
        if fireballX <= 0:
            fireballX = bossX + 50
        elif fireballX2 <= 0:
            fireballX2 = bossX + 50
        
        if fireballSound == 0:
            fires_sound.play()
            fireballSound = 1
        fireballImageUnrotated = pygame.image.load("fireball.png").convert_alpha()
        fireballImageUnsized = pygame.transform.rotate(fireballImageUnrotated, 90)
        fireballImage = pygame.transform.scale(fireballImageUnsized, (100, 150))
        fireball_rect = fireballImage.get_rect(center=(fireballX, bossY + fireballMovement))
        fireballHitbox = pygame.Rect(fireballX - 20, bossY + fireballMovement, 50, 50)
        fireballMovement += 30

        fireballImageUnrotated2 = pygame.image.load("fireball.png").convert_alpha()
        fireballImageUnsized2 = pygame.transform.rotate(fireballImageUnrotated2, 90)
        fireballImage2 = pygame.transform.scale(fireballImageUnsized2, (100, 150))
        fireball_rect2 = fireballImage.get_rect(center=(fireballX2, bossY + fireballMovement2))
        fireballHitbox2 = pygame.Rect(fireballX2 - 20, bossY + fireballMovement2, 50, 50)
        fireballMovement2 += 30

        if fireball_rect.centery >= 550:
            if setFireballMovement2 == True:
                fireballMovement2 = 0
                setFireballMovement2 = False
                setFireballMovement = True
                fireballX2 = -100
                
            fireball_rect2 = fireballImage.get_rect(center=(fireballX2, bossY + fireballMovement2))

        if fireball_rect2.centery >= 550:
            if setFireballMovement == True:
                fireballMovement = 0
                setFireballMovement = False
                setFireballMovement2 = True
                fireballX = -100

            fireball_rect.center = (fireballX, bossY + fireballMovement)

        if player_rect.colliderect(fireballHitbox) or player_rect.colliderect(fireballHitbox2):
            if bossFlipped == True:
                playerX += 200
                playerY -= 50
                playerHealth -= 4
            else:
                playerX -= 200
                playerY -= 50
                playerHealth -= 4

        #Show fireball hitboxes
        # pygame.draw.rect(SCREEN, RED, fireballHitbox, 3)
        # pygame.draw.rect(SCREEN, GREEN, fireballHitbox2, 3)
        SCREEN.blit(fireballImage2, fireball_rect2)
        SCREEN.blit(fireballImage, fireball_rect)

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
    global playerFlipped
    moving_left = False
    moving_right = False

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        playerX -= playerSpeed
        playerFlipped = True
        moving_left = True

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        playerX += playerSpeed
        playerFlipped = False
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
                     bossHealth -= 10

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
    if playerY == ground_y and on_platform == False:
        jumping = True

def checkIfJumping():
    global jumping, playerY, vel_y, gravity, jump_height, falling, jump_speed, jump_count, ground_y

    if on_platform == False:
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

    #Show player hitbox during battle
    #pygame.draw.rect(SCREEN, GREEN, player_rect, 3)

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
    global sword_swing, rotation_speed, added_y, swordImageUnrotated, swordRect, player_rect, playerX, playerY, bossY, playerFlipped
    global sword_sound, sound
    player_pos = (playerX, playerY)
    player_rect = playerImage.get_rect(center=player_pos)
    player_rect.topleft = (playerX, playerY)
    
    swordImageUnrotated = pygame.image.load("sword.png").convert_alpha()

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
            if sound == 0:
                sword_sound.play()
                sound = 1
            swordImage = pygame.transform.rotate(swordImageUnrotated, -rotation_speed)

            rotation_speed += 25

            if rotation_speed >= 130:
                sword_swing = False
                rotation_speed = 0
                added_y = 0
                sound = 0

            SCREEN.blit(swordImage, (playerX, playerY + added_y))

            added_y += 0.5
    
    else:
        swordImage = pygame.transform.rotate(swordImageUnrotated, 25)

        if sword_swing == False:
            SCREEN.blit(swordImage, (playerX - 70, playerY - 60))

        else:
            if sound == 0:
                sword_sound.play()
                sound = 1
            swordImage = pygame.transform.rotate(swordImageUnrotated, rotation_speed)

            rotation_speed += 25

            if rotation_speed >= 130:
                sword_swing = False
                rotation_speed = 0
                added_y = 0
                sound = 0

            SCREEN.blit(swordImage, (playerX - 100, playerY + added_y))

            added_y += 0.5

def bow_choice():
    global player_rect, bow_number, bow_shoot, shoot_arrow, angle, angle_degrees, arrow_angle, allow_angle, mouse_x, mouse_y, arrow_x_speed, arrow_y_speed, is_fired, arrowX, arrowY
    global sound, arrow_sound
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
            sound = 0
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
        if sound == 0:
            arrow_sound.play()
            sound = 1
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
    global sound, spinning_sound

    player_rect = playerImage.get_rect(center=(playerX + 40, playerY + 60))
    
    boomrngImageUnscaled = pygame.image.load("boomerang.png").convert_alpha()
    boomrngImageUnrotated = pygame.transform.scale(boomrngImageUnscaled, (75, 75))

    if boomrng_shoot == False:
        boomrng_rect.center = (1000, 1000)
        spinning_sound.stop()
        sound = 0

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
    global boomrngImageUnrotated, boomrngImage, boomrng_spin, boomrng_rect, sound, spinning_sound
    if sound == 0:
        spinning_sound.play()
        sound = 1
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
    SCREEN.blit(difficulty_sword_surface, difficulty_sword_rect)

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
    SCREEN.blit(difficulty_bow_surface, difficulty_bow_rect)

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
    SCREEN.blit(difficulty_boomrng_surface, difficulty_boomrng_rect)

    drawButton(boomrng_button_rect, BOOMRNG_BUTTON_COLOR, use_text, button_font, SCREEN)
    pygame.draw.rect(SCREEN, BLACK, (552, 580, 228, 70), 3)

    boomrngImage = pygame.image.load("boomerang.png").convert_alpha()
    SCREEN.blit(boomrngImage, (600, 338))

def checkKeys(keys):
    global choice, leftHolding, rightHolding
    swipe_sound = pygame.mixer.Sound("sounds/swipe_sound.mp3")
    if leftHolding == False:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            choice -= 1
            leftHolding = True
            swipe_sound.play()
    
    if not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        leftHolding = False

    if rightHolding == False:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            choice += 1
            rightHolding = True
            swipe_sound.play()
    
    if not (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
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
        click_sound = pygame.mixer.Sound("sounds/button_click.wav")
        click_sound.play()
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
    difficulty_font = pygame.font.SysFont("Georgia", 20)
    bow_text = "BOW"
    sword_text = "SWORD"
    boomrng_text = "BOOMERANG"
    subtitle_text = "Use Arrow Keys To Interact!"
    use_text = "USE!"
    difficulty_bow_text = "Difficulty: Medium"
    difficulty_sword_text = "Difficulty: HARD"
    difficulty_boomrng_text = "Difficulty: Easy"

    difficulty_bow_surface = difficulty_font.render(difficulty_bow_text, True, BLACK)
    difficulty_bow_rect = difficulty_bow_surface.get_rect(center=(400, 560))

    difficulty_sword_surface = difficulty_font.render(difficulty_sword_text, True, BLACK)
    difficulty_sword_rect = difficulty_sword_surface.get_rect(center=(130, 560))

    difficulty_boomrng_surface = difficulty_font.render(difficulty_boomrng_text, True, BLACK)
    difficulty_boomrng_rect = difficulty_boomrng_surface.get_rect(center=(665, 560))

    sword_text_surface = font.render(sword_text, True, BLACK)
    sword_text_rect = sword_text_surface.get_rect()
    sword_text_rect.center = (130, 530)

    bow_text_surface = font.render(bow_text, True, BLACK)
    bow_text_rect = bow_text_surface.get_rect()
    bow_text_rect.center = (400, 530)

    boomrng_text_surface = font.render(boomrng_text, True, BLACK)
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
        click_sound.play()
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