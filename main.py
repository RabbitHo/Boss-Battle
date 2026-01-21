
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
fireballY2 = 0
fireballX3 = 0
fireballY3 = 0
fireballX4 = 0
fireballY4 = 0
fireballX5 = 0
fireballY5 = 0
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
civilian_sound = pygame.mixer.Sound("sounds/civilian_talking.mp3")
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
    global sound

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
            sound = 0
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

    #If the time difference is more than 7500 and less than or equal to 10500 milliseconds
    elif time_difference > 7500 and time_difference <= 10500:
        last_surf4 = last_font.render(last_text4, True, WHITE)
        last_rect4 = last_surf4.get_rect(center=(400, 400))
        SCREEN.blit(last_surf4, last_rect4) 

    #If the time difference is more than 10500 and less than or equal to 13500 milliseconds
    elif time_difference > 10500 and time_difference <= 13500:
        last_surf5 = last_font.render(last_text5, True, WHITE)
        last_rect5 = last_surf5.get_rect(center=(400, 400))
        SCREEN.blit(last_surf5, last_rect5)

    #If the time difference is more than 13500 milliseconds
    else:
        quitGame()

def checkForExit():
    global endGame
    #Find the keys the player presses
    keys = pygame.key.get_pressed()
    #If the player pressed the 'SPACE' or 'ESC' key
    if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
        #Set the variable to true
        endGame = True

def drawEnding():
    #Fill the screen with the color light blue
    SCREEN.fill(LIGHTBLUE)
    #The font for the title and the text
    ending_title_font = pygame.font.SysFont("Georgia", 100)
    ending_title_text = "GAME OVER"
    ending_title_surface = ending_title_font.render(ending_title_text, True, BLACK)
    ending_title_rect = ending_title_surface.get_rect(center=(400, 50))

    #The font for the subtitle and the text
    subtitle_font = pygame.font.SysFont("Georgia", 40)
    subtitle_text = "YOU WIN!"
    subtitle_surface = subtitle_font.render(subtitle_text, True, BLACK)
    subtitle_rect = subtitle_surface.get_rect(center=(400, 120))

    #The text for the 'Storyline' text
    story_text = "Storyline"
    story_surface = subtitle_font.render(story_text, True, BLACK)
    story_rect = story_surface.get_rect(topleft=(50, 200))

    #The text for the paragraph for the story
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

    #Converts the body text to a text
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

    #Create the text on the screen
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
    #Create the civilian image and animating it
    civilianImage = pygame.image.load(f"civilian_idle/{civilianIdleCount}.png").convert_alpha()
    civilian_rect = civilianImage.get_rect(center=(screenX + secondMapWidth + mapWidth + 600, 600))
    civilianIdleCount += 1

    #Draw civilian hitbox
    #pygame.draw.rect(SCREEN, GREEN, civilian_rect, 3)

    #If the player's x coordinates is over the civilian's
    if playerX < civilian_rect.centerx:
        #Flip the civilian to face the player
        civilianImage = pygame.transform.flip(civilianImage, True, False)

    #If the civilian has gone through all the idle animation, reset the animation
    if civilianIdleCount == 17:
        civilianIdleCount = 0

    #If the player touches the civilian
    if player_rect.colliderect(civilian_rect):
        #If the player has not interacted with the civilian
        if civilian_interact == False and endOfGame == False:
            interact_text = "Press 'E' to interact!"

            interact_surface = sign_font.render(interact_text, True, BLACK)
            interact_rect = interact_surface.get_rect(center=(playerX + 20, playerY - 50))
            
            #Create the interacting instructions text
            SCREEN.blit(interact_surface, interact_rect)
        
        #If the player has interacted with the civilian
        elif civilian_interact == True:
            interact_text = "Press 'SPACE' to go next!"

            interact_surface = sign_font.render(interact_text, True, BLACK)
            interact_rect = interact_surface.get_rect(center=(playerX + 20, playerY - 50))

            #Create the interacting instructions text
            SCREEN.blit(interact_surface, interact_rect)

    #If the civilian's interaction is not over
    if civilian_running == False:
        SCREEN.blit(civilianImage, civilian_rect)

def screenScroll():
    global screenX, playerX, map_rect, screenLimitLeft, secondMap_rect, thirdMap_rect, screenLimitRight
    #If the player's X coordinates is over 600 and is moving right and the screen limit for right is not reached
    if playerX >= 600 and moving_right and not moving_left and not screenLimitRight:
        playerX = 600
        screenX -= 7
        screenLimitLeft = False
    
    #If the player's X coordinates is under 200 and is moving left and the screen limit for left is not reached
    if playerX <= 200 and moving_left and not moving_right and not screenLimitLeft:
        playerX = 200
        screenX += 7
        screenLimitRight = False
    
    #If the player's X coordinates is under 3
    if playerX <= 3:
        playerX = 3
    
    #If the player's X coordinates is over 720
    if playerX >= 720:
        playerX = 720

    #If the first map is on the coordinates (0, 0) which is the top corner on the left 
    if map_rect.topleft == (0, 0):
        #Set the screen limit of left true
        screenLimitLeft = True

    #If the third map is on the coordinates (0, 0)
    if thirdMap_rect.topleft <= (0, 0):
        #Set the screen limit of right true
        screenLimitRight = True

    #Create the three map's coordinates
    map_rect = mapImage.get_rect(topleft=(screenX, 0))
    secondMap_rect = secondMap.get_rect(topleft=(screenX + mapWidth, 0))
    thirdMap_rect = thirdMap.get_rect(topleft=(screenX + secondMapWidth + mapWidth, 0))

def checkKeysMap(keys):
    global playerFlipped, playerX, moving_left, moving_right, playerAnimation, civilian_interact
    #If the player presses the 'A' or 'LEFT' key and has not interacted with the civilian
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and civilian_interact == False:
        playerX -= playerSpeed
        playerFlipped = True
        moving_left = True

    #If the player has interacted with the civilian
    else:
        moving_left = False
        playerAnimation = False

    #If the player presses the 'D' or 'RIGHT' key and has not interacted with the civilian
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and civilian_interact == False:
        playerX += playerSpeed
        playerFlipped = False
        moving_right = True
    
    #If the player has interacted with the civilian
    else:
        moving_right = False
        playerAnimation = False

    #If the player presses the 'E' key and is touching the civilian
    if keys[pygame.K_e]:
        if player_rect.colliderect(civilian_rect):
            civilian_interact = True

def civilianInteraction():
    global civilian_running, interaction_next, space_holding, civilian_interact, endOfGame, sound

    #If the interaction is not over
    if civilian_running == False:
        pygame.draw.rect(SCREEN, BLACK, (50, 100, 720, 100))
        pygame.draw.rect(SCREEN, WHITE, (50, 100, 720, 100), 10)

    #If no sound is playing (except the background music)
    if sound == 0:
        #Play the civilian talking sound
        civilian_sound = pygame.mixer.Sound("sounds/civilian_talking.mp3")
        civilian_sound.play()
        sound = 1

    #Create the interaction font and text
    interact_font = pygame.font.SysFont("Georgia", 20)
    interact_text1 = "<Civilian> You really beat the dragons? That's really great! It's finally done!"
    interact_text2 = "<Civilian> I'll go tell the others about this. Thank you!"
    interact_text3 = "<Civilian> I'll say it again. Thank you so much! You saved the world!"

    #Create the text and coordinates
    interact1_surface = interact_font.render(interact_text1, True, WHITE)
    interact1_rect = interact1_surface.get_rect(topleft=(70, 140))

    interact2_surface = interact_font.render(interact_text2, True, WHITE)
    interact2_rect = interact2_surface.get_rect(topleft=(70, 140))

    interact3_surface = interact_font.render(interact_text3, True, WHITE)
    interact3_rect = interact3_surface.get_rect(topleft=(70, 140))

    #Define the clicking sound of the interaction when going to the next dialogue
    click_sound = pygame.mixer.Sound("sounds/click_civilian_sound.wav")

    #If the player presses 'SPACE' and the interaction goes next
    if interaction_next == 0:
        SCREEN.blit(interact1_surface, interact1_rect)
    
    elif interaction_next == 1:
        SCREEN.blit(interact2_surface, interact2_rect)
    
    elif interaction_next == 2:
        SCREEN.blit(interact3_surface, interact3_rect)
    
    else:
        sound = 1
        #Stop the civilian from speaking
        civilian_sound.stop()
        civilian_running = True
        civilian_interact = False
        endOfGame = True
        civilianRun()       #Function to make the civilian run

    #Define the key the player presses
    keys = pygame.key.get_pressed()
    #If the player presses the 'SPACE' key and is not holding
    if keys[pygame.K_SPACE] and space_holding == False:
        space_holding = True
        interaction_next += 1
        #Play the clicking sound
        click_sound.play()
        sound = 0

    #If the player is not pressing space
    if not keys[pygame.K_SPACE]:
        space_holding = False

def civilianRun():
    global civilianRunCount, civilianX, endOfGame, civilian_interact, civilian_run
    #Sets the civilian's image and it's idle animation
    civilianImage = pygame.image.load(f"civilian_walking/{civilianRunCount}.png").convert_alpha()
    civilianRunCount += 1
    #Set the civilian's coordinates on the map
    civilian_rect = civilianImage.get_rect(center=(screenX + secondMapWidth + mapWidth + civilianX, 600))
    civilianX += 4
    #Set the variable civilian_run to true for 'if' statements in the 'while' loop
    civilian_run = True

    #If the civilian's animation is over, reset it
    if civilianRunCount == 24:
        civilianRunCount = 0

    #If the civilian is beyond the screen and outside of it
    if civilian_rect.centerx >= 800:
        #Set the variable to false for 'if' statements in the 'while' loop
        civilian_run = False
    #If the civilian has not made it out of the screen
    else:
        #Create the civilian image and its coordinates
        SCREEN.blit(civilianImage, civilian_rect)

def drawPlayer():
    global playerImage, playerX, playerY, playerRun, playerFlipped

    #If the player not moving left or right and not animating
    if playerAnimation == False:
        #If the player is facing to the right
        if playerFlipped == False:
            #Create the normal player image
            SCREEN.blit(playerImage, (playerX, playerY))

        #If the player is facing to the left
        else:
            #Flip the image and create the flipped player's image
            flippedPlayerImage = pygame.transform.flip(playerImage, True, False)
            SCREEN.blit(flippedPlayerImage, (playerX, playerY))

    #If the player is moving left or right and is animating
    else:
        #Create the running animation
        SCREEN.blit(playerRun, (playerX, playerY))
    
    #If the player is interacting with the civilian
    if civilian_interact == True:
        #Set the player's image to the normal image
        SCREEN.blit(playerImage, (playerX, playerY))

    #Set the player's hitbox to the player
    player_rect.topleft = (playerX + 50, playerY)

def drawMap():
    global map_confirmed, map_choice, mapImage, map_rect, screenX, mapWidth, second_map_confirmed, secondMap, secondMap_rect, second_map_choice
    global secondMapWidth, thirdMap, third_map_confirmed, thirdMap_rect
    #If map is not chosen yet
    if map_confirmed == False:
        #List of maps that can be used
        maps = ["grass", "forest", "desert"]
        #Random the list of maps
        map_choice = random.choice(maps)
        #Set the map to be confirmed and has been chosen
        map_confirmed = True
    
        #Create the map with the randomized map and it's coordinates
        mapImageUnsized = pygame.image.load(f"{map_choice}.jpg").convert_alpha()
        mapImage = pygame.transform.scale(mapImageUnsized, (1250, 800))
        map_rect = mapImage.get_rect(topleft=(screenX, 0))
        mapWidth = mapImage.get_rect().width

    #Create a second map
    if second_map_confirmed == False:
        secondMaps = ["grass", "forest", "desert"]
        second_map_choice = random.choice(secondMaps)
        #Forces it to become a different map choice
        while second_map_choice == map_choice:
            secondMaps = ["grass", "forest", "desert"]
            second_map_choice = random.choice(secondMaps)

        second_map_confirmed = True

        #Create the second map
        secondMapUnsized = pygame.image.load(f"{second_map_choice}.jpg").convert_alpha()
        secondMap = pygame.transform.scale(secondMapUnsized, (1250, 800))
        secondMap_rect = secondMap.get_rect(topleft=(screenX + mapWidth, 0))
        secondMapWidth = secondMap.get_rect().width

    #Create a third map
    if third_map_confirmed == False:
        thirdMaps = ["grass", "forest", "desert"]
        third_map_choice = random.choice(thirdMaps)
        #Forces it to be different from the second map
        while third_map_choice == second_map_choice:
            thirdMaps = ["grass", "forest", "desert"]
            third_map_choice = random.choice(thirdMaps)

        third_map_confirmed = True
        #Create the third map and its coordinates
        thirdMapUnsized = pygame.image.load(f"{third_map_choice}.jpg").convert_alpha()
        thirdMap = pygame.transform.scale(thirdMapUnsized, (1250, 800))
        thirdMap_rect = thirdMap.get_rect(topleft=(screenX + secondMapWidth + mapWidth, 0))
    
    #Create all maps on the screen
    SCREEN.blit(thirdMap, thirdMap_rect)
    SCREEN.blit(secondMap, secondMap_rect)
    SCREEN.blit(mapImage, map_rect)

def drawGame():
    drawBackground()    #Function to draw the background
    drawCharacters()    #Function to draw the characters
    drawHealthBar()     #Function to draw the health bars for both the boss and the player

def drawBackground():
    #Create the background on the screen
    SCREEN.blit(backgroundImage, (0, 0))

def drawCharacters():
    global playerRun, playerX, playerY, playerAnimation, bossFly, playerFlipped

    #If player is not moving
    if playerAnimation == False:
        #If player is facing right
        if playerFlipped == False:
            #Create the normal player image
            SCREEN.blit(playerImage, (playerX, playerY))

        #If player is facing left
        else:
            #Flip the image and create the flipped player image
            flippedPlayerImage = pygame.transform.flip(playerImage, True, False)
            SCREEN.blit(flippedPlayerImage, (playerX, playerY))

    #If player is not moving left or right
    if playerAnimation == True:
        #Create the running animation
        SCREEN.blit(playerRun, (playerX, playerY))

def findEvents():
    global BUTTON_COLOR, BUTTON_CLICK_COLOR, button_clicked, button_hover, button_x, button_y, WEAPON_BUTTON_COLOR, BOW_BUTTON_COLOR, weapon_choice

    #Define the events in a variable
    events = pygame.event.get()

    #Find the event seperately in the variable
    for event in events:
        #If the event is the player quitting the program
        if event.type == pygame.QUIT:
            quitGame()      #Function to exit the program

        #If the event is when the player clicks down
        if event.type == pygame.MOUSEBUTTONDOWN:
            #If the cursor is overlapping the button
            if button_rect.collidepoint(event.pos):
                #Sets the button color to the button click color
                BUTTON_COLOR = BUTTON_CLICK_COLOR
                WEAPON_BUTTON_COLOR = BUTTON_CLICK_COLOR
                button_clicked = True
                weapon_choice = 1

def closingAnimations():
    global movingYAmount

    #If the variable is over or equal to 670
    if movingYAmount >= 670:
        closeLeftVerticals()      #Function to do the animation for closing on the left
        return
    
    #Draw the rectangle
    pygame.draw.rect(SCREEN, BLUE, (0, -650 + movingYAmount, WIDTH, 670))

    movingYAmount += 1

def closeLeftVerticals():
    global movingXAmount, rightVertical

    #If the variable is equal to or more than the player's X coordinates minus 100 and the variable is True
    if movingXAmount >= playerX - 100 or rightVertical == True:
        #If the rightVertical variable is false
        if rightVertical == False:
            movingXAmount = 0
            rightVertical = True

        closeRightVerticals()       #Function to start the animation for closing on the right
        return

    #Draw the rectangle
    pygame.draw.rect(SCREEN, BLUE, (-100 + movingXAmount, playerY, 200, playerHeight + 50))
    movingXAmount += 1

def closeRightVerticals():
    global movingXAmount, stopRightVertical, closingAnimation

    #If the width minus the variable is below or equal to the player's X coordinates added with the player's width add with 50
    if WIDTH - movingXAmount <= playerX + playerWidth + 50:
        stopRightVertical = True
        closingAnimation = True

    if stopRightVertical == False:
        #Draw the rectangle
        pygame.draw.rect(SCREEN, BLUE, (WIDTH - movingXAmount, playerY, 300, playerHeight))
        movingXAmount += 1

def gameOverScreen():
    global shrink_circle, game_screen
    #Forces the circle to shrink until it the variable is set to false
    while shrink_circle == True:
        clock.tick(FPS)
        findEvents()
        shrinkCircle()

    #Forces the game screen to keep going until the variable is set to false
    while game_screen == True:
        clock.tick(FPS)
        findEvents()    #Function to find what the player does
        printGameScreenText()   #Function to create the ending screen
        createLeaveButton()     #Function to create the leave button
        checkClickedButton()    #Function to check if the player clicked the button

def checkClickedButton():
    global leaveButton_color, leaveButton_rect
    #Define a variable for the events that the player does
    events = pygame.event.get()
    #Define each individual event the player does
    for event in events:
        #If the event is the player clicking and the cursor is overlaping the button
        if event.type == pygame.MOUSEBUTTONDOWN and leaveButton_rect.collidepoint(mouse_pos):
            leaveButton_color = BUTTON_CLICK_COLOR
            #Set the cursor's arrow to the arrow
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
            quitGame()  #Function to exit the program


def createLeaveButton():
    global leaveButton_color, leaveButton_width, leaveButton_height, leaveButton_x, leaveButton_y, leaveButton_textSize, leaveButton_rect
    #Create the button's hitbox
    leaveButton_rect = pygame.Rect(leaveButton_x, leaveButton_y, leaveButton_width, leaveButton_height)
    #Create the button's text
    leaveButton_text = "LEAVE"
    #Create the text font
    leaveButton_font = pygame.font.SysFont("Comic Sans MS", leaveButton_textSize)
    #Function to draw the button
    drawButton(leaveButton_rect, leaveButton_color, leaveButton_text, leaveButton_font, SCREEN)
    
    #Store the mouse position to the variable
    mouse_pos = pygame.mouse.get_pos()
    #If the cursor is overlapping with the button
    if leaveButton_rect.collidepoint(mouse_pos):
        #Update the button
        leaveButton_color = BUTTON_HOVER_COLOR
        leaveButton_width = 237
        leaveButton_height = 112
        leaveButton_x = 275
        leaveButton_y = 475
        leaveButton_textSize = 70
        #Set the cursor to a hand
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    #If the cursor is not overlapping with the button
    else:
        #Update the button
        leaveButton_color = BLUE
        leaveButton_width = 200
        leaveButton_height = 75
        leaveButton_x = 300
        leaveButton_y = 500
        leaveButton_textSize = 50
        #Set the cursor to an arrow
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    #Update the game
    pygame.display.update()

def printGameScreenText():
    global random_text, description_text2
    #Set the font for the title and description
    title_font = pygame.font.SysFont("Georgia", 100)
    description_font = pygame.font.SysFont("Comic Sans MS", 20)

    #Fill the screen with black
    SCREEN.fill(BLACK)

    #Set the title's text and create the text
    title_text = "GAME OVER"
    title_text_surface = title_font.render(title_text, True, WHITE)
    title_text_rect = title_text_surface.get_rect(center=(400, 80))

    #Set the description text and randomize the next text
    description_text = "You failed to defeat the dragons..."
    randomText = random.randint(1, 5)

    #If the random text is not confirmed
    if random_text == False:
        #If the random text is 1
        if randomText == 1:
            description_text2 = "Maybe this job is for someone else."
            random_text = True
        
        #If the random text is 2
        elif randomText == 2:
            description_text2 = "We should've called for help when we could."
            random_text = True

        #If the random text is 3
        elif randomText == 3:
            description_text2 = "The dragons will now be able to reproduce even more."
            random_text = True

        #If the random text is 4
        elif randomText == 4:
            description_text2 = "Maybe choosing another weapon could have helped."
            random_text = True
        
        #If the random text is 5
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

    #Create the text and put it in the screen
    SCREEN.blit(description_text3_surface, description_text3_rect)
    SCREEN.blit(description_text2_surface, description_text2_rect)
    SCREEN.blit(description_text_surface, description_text_rect)
    SCREEN.blit(title_text_surface, title_text_rect)

    #Update the game
    pygame.display.update()

def shrinkCircle():
    global radiusNumber, shrinkRadius, shrink_circle
    #If the variable is false and the other variable is true
    if endOfGame == False or endGame == True:
        #Draw the circle
        pygame.draw.circle(SCREEN, BLACK, player_rect.center, shrinkRadius + 1000, 800)

    #If the variable is ture an the other variable is false
    elif endOfGame == True and endGame == False:
        #Draw a different circle in a different color
        pygame.draw.circle(SCREEN, LIGHTBLUE, player_rect.center, shrinkRadius + 1000, 800)

    #Shrink the radius
    radiusNumber += 0.5
    shrinkRadius -= radiusNumber

    #If the radius added with 1000 is lower or equal to 0
    if shrinkRadius + 1000 <= 0:
        shrink_circle = False
        return

    #Update the game
    pygame.display.update()

def playerDeath():
    global playerDeathCount, player_dead, playerFlipped

    #If player is dead and animation is finished
    if player_dead:
        return

    #Fill the screen with black
    SCREEN.fill(BLACK)
    
    #Animate the player's dead animation
    playerDeathImage = pygame.image.load(f"player_death/{playerDeathCount}.png").convert_alpha()
    playerDeath_rect = playerDeathImage.get_rect(topleft=(playerX, 650))
    playerDeathCount += 1

    #If the animation count is 41, set the variable to true
    if playerDeathCount == 41:
        playerDeathCount = 0
        player_dead = True

    #If player is flipped and facing left
    if playerFlipped == True:
        #Flip the image
        playerDeathImage = pygame.transform.flip(playerDeathImage, True, False)

    #Create the flipped or non flipped image
    SCREEN.blit(playerDeathImage, playerDeath_rect)

def bossDeath():
    global explosion_size, bossDeathCount, sound
    #If no sound is playing
    if sound == 0:
        #Play the explosion sound
        explosion_sound.play()
        sound = 1
    
    #If the boss's death animation count is 16
    if bossDeathCount == 16:
        bossRect.center = (-1000, -1000)    #Move the boss away off-screen
        explosion_sound.stop()
        pygame.mixer.music.stop()       #Stop all sounds
        return
    
    #Animate the boss's death
    bossDeathImageUnsized = pygame.image.load(f"boss_death/{bossDeathCount}.png").convert_alpha()
    bossDeathCount += 1
    bossDeathImage = pygame.transform.scale(bossDeathImageUnsized, (new_width + explosion_size, new_height + explosion_size))
    bossDeath_rect = bossDeathImage.get_rect(center=(bossX, bossY))
    explosion_size += 20

    #Create the boss's death animation
    SCREEN.blit(bossDeathImage, bossDeath_rect)

def bossAttack():
    global attacking, last_action_time, attackChoice, current_time, boss_pos, ATTACKLEFT, ATTACKRIGHT, ATTACKUP, ATTACKDOWN, EVERYWHERE, STUNNED
    global boss_going_back, bossRect2, bossRect, sidekickAlive, hypoteneuse
    global fireballCooldown, last_fireball, attackQuantity, stunnedCooldown, bossStunned_rect

    #If the boss has not attacked
    if attackQuantity == 0:
        #Get the stunned boss hitbox away from screen
        bossStunned_rect.center = (-10000, -10000)

    #If the boss has finished attacking
    if boss_going_back == True and attackQuantity == 0:
        bossGoBack()
        return

    #If the sidekick's health is 0 or below
    if sidekickHealth <= 0:
       sidekickAlive = False
       fire_rect.center = (10000, 400)
       sidekickDeath()  #Function to animate the death of the sidekick
       return
    
    #If the sidekick is not alive
    if sidekickAlive == False:
       #Set the sidekick's hitbox off screen
       bossRect2 = pygame.Rect(-1000, -1000, bossWidth, bossHeight)

    #Get the current time in milliseconds
    current_time = pygame.time.get_ticks() 

    #If the boss is attacking and the side kick is not alive
    if attacking == True and sidekickAlive == False:
        attacking = False
        boss_going_back = True
        attackQuantity += 1
        return

    #If the boss is not attacking and the boss is not dead
    if attacking == False and boss_dead == False:
        last_fireball = fireballCooldown
        last_action_time = current_time
        #Randomize the attack decision
        attackChoice = random.randint(1, 10)
        #If the boss has not attacked yet
        if attackQuantity == 0:
            attacking = True
        
        #If the boss has finished attacking
        else:
            bossStunned()

    #If the boss is not going back from attacking and the boss is not dead
    if boss_going_back == False and attackQuantity == 0 and boss_dead == False:
        #If the attack choice is equal to or below the variable
        if attackChoice <= ATTACKLEFT:
            bossAttackLeft()        #Function to get the boss to attack left
       
        #If the attack choice is equal to or below the variable and above the attackleft variable
        elif attackChoice <= ATTACKUP and attackChoice > ATTACKLEFT:
            bossAttackUp()          #Function to get the boss to attack up

        #If the attack choice is equal to or below the variable and above the attackup variable
        elif attackChoice <= ATTACKRIGHT and attackChoice > ATTACKUP:
            bossAttackRight()       #Function to get the boss to attack right

        #If the attack choice is equal to or below the variable and above the attackright variable
        elif attackChoice <= ATTACKDOWN and attackChoice > ATTACKRIGHT:
            bossAttackDown()        #Function to get the boss to attack down
       
        #If the attack choice is none of them
        else:
            bossAttackEverywhere()  #Function to get the boss to attack everywhere

def bossStunned():
    global stunnedCount, bossRect, stunnedCooldown, attackQuantity, bossStunned_rect
    #Get the current time
    current_time = pygame.time.get_ticks()
    #Set the cooldown once
    if stunnedCooldown == 0:
        stunnedCooldown = pygame.time.get_ticks()

    #Animate the boss stunned animation
    stunnedImageUnsized = pygame.image.load(f"boss_stunned/{stunnedCount}.png").convert_alpha()
    stunnedCount += 1
    stunnedImage = pygame.transform.scale(stunnedImageUnsized, (new_width, new_height))
    bossStunned_rect = stunnedImage.get_rect(topleft=(bossX, bossY))

    #If the animation is finished, reset the animation
    if stunnedCount == 12:
        stunnedCount = 0

    #If the current time minus the cooldown is more than or equal to 5000 milliseconds
    if current_time - stunnedCooldown >= 5000:
        attackQuantity = 0
        stunnedCooldown = 0

    #Create the stunned animation
    SCREEN.blit(stunnedImage, bossStunned_rect)

def bossAttackLeft():
    global boss_animation_count, bossX, bossY, bossRect, bossLanded
    global boss_animation_count2, bossX2, bossY2, boss_flipped, shoot_arrow, sidekickHealth
    global is_fired, bow_shoot, allow_angle, sidekickGotHit, bossRect2, leftHypoteneuse
    global hit, boomrng_hit, last_fireball, bossShooting, shootAnimation, fireball_rect, fireballImageUnrotated, shooting, fireball_vx, fireball_vy
    global shootingCount, bossFly2

    #Animate the boss
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))

    #If the animation is finished, reset the animation
    if boss_animation_count == 12:
        boss_animation_count = 0

    #Keep the boss's hitbox on the boss
    bossRect = bossFly.get_rect(topleft=(bossX, bossY))
    
    #If the boss has not reached its destination
    if bossLanded == False:
        bossX2 = 0

        #Make a destination area hitbox
        left_surf = pygame.Surface((50, 50))
        left_rect = left_surf.get_rect(topleft=(120, 160))
        leftX = left_rect.centerx
        leftY = left_rect.centery
        run = leftX - bossX
        rise = leftY - bossY
        #Find the hypoteneuse
        leftHypoteneuse = math.sqrt(run ** 2 + rise ** 2)

        #If the hypoteneuse is 0
        if leftHypoteneuse == 0:
            return      #Return to prevent crashing

        #Move the boss towards the destination
        boss_x_speed = run/leftHypoteneuse * boss_speed
        boss_y_speed = rise/leftHypoteneuse * boss_speed
        bossX += boss_x_speed
        bossY += boss_y_speed

        #Create the boss on the screen
        SCREEN.blit(bossFly, (bossX, bossY))

        #If the boss has made it to the destination
        if leftHypoteneuse <= boss_speed:
            bossX = leftX
            bossY = leftY
            bossLanded = True

        #Show boss hitbox
        #pygame.draw.rect(SCREEN, (0, 255, 0), bossRect, 2)

        #Show boss destination hitbox
        #pygame.draw.rect(SCREEN, RED, left_rect, 3)

    #If the boss has made it to it's destination and the sidekick is alive
    elif bossLanded == True and sidekickAlive == True:
        #Create the boss's fly animation
        SCREEN.blit(bossFly, (bossX, bossY))

        #If the sidekick did not get hit
        if sidekickGotHit == False:
            #Animate the sidekick's animation
            bossFlyUnsized2 = pygame.image.load(f"boss_idle2/{boss_animation_count2}.png")
            boss_animation_count2 += 1
            bossFly2 = pygame.transform.scale(bossFlyUnsized2, (new_width, new_height))

            #If the sidekick is not flipped
            if boss_flipped == False:
                #Flip the boss image
                bossFly2 = pygame.transform.flip(bossFly2, True, False)
                bossX2 += 5
            
            #If the sidekick is flipped
            else:
                bossX2 -= 5

        #If the sidekick got hit from the player
        else:
            boss_animation_count2 = 0
            sidekickDamaged()       #Function to animate the sidekicks damaged animation

            #If the sidekick is not flipped
            if boss_flipped == False:
                #Flip the image
                bossFly2 = pygame.transform.flip(bossFly2, True, False)
                bossX2 += 5
        
            #If the sidekick is flipped
            else:
                bossX2 -= 5

        #If the sidekick's animation is finished, reset it
        if boss_animation_count2 == 12:
            boss_animation_count2 = 0

        #If the boss hits the right wall, flip it
        if bossX2 >= 720:
            boss_flipped = True

        #If the boss hits the left wall, flip it
        elif bossX2 <= 0:
            boss_flipped = False
       
        #Center the sidekicks hitbox to the sidekick
        bossRect2 = bossFly2.get_rect(center=(bossX2 + 60, bossY2 + 50))

        #If the player's weapon is the bow
        if weapon_choice == BOW:
            #If the arrow touches the boss
            if bossRect2.colliderect(arrow_rect):
                #Rearm the arrow and animate the sidekick
                #Subtract the sidekick's health
                sidekickHealth -= 30
                is_fired = False
                shoot_arrow = False
                bow_shoot = False
                allow_angle = True
                sidekickGotHit = True
                arrow_rect.center = (1000, 1000)

                #If the sidekick's health is below 0, set it back to 0
                if sidekickHealth < 0:
                    sidekickHealth = 0

        #If the player's weapon is the sword and is not hitting the sidekick
        if weapon_choice == SWORD and hit == False:
            #If the sword is swinging and touches the boss
            if sword_swing and swordRect.colliderect(bossRect2):
                #Animate the sidekick and subtract its health
                sidekickHealth -= 7
                sidekickGotHit = True
                hit = True

            #If the sword is not swinging
            else:
                hit = False

        #If the player's weapon is the boomerang and is not hitting the sidekick
        if weapon_choice == BOOMRNG and boomrng_hit == False:
            #If the boomerang touches the sidekick
            if boomrng_rect.colliderect(bossRect2):
                boomrng_hit = True
                sidekickGotHit = True
                sidekickHealth -= 30

        #Get the fireball's cooldown
        fireballCooldown = pygame.time.get_ticks()
        #If the fireball's cooldown minus the last fireball is over 2000 milliseconds and the sidekick is not shooting
        if fireballCooldown - last_fireball >= 2000 and bossShooting == False:
            last_fireball = fireballCooldown
            bossShooting = True
            shooting = True
       
        #If the sidekick is shooting
        if bossShooting == True:
            if shooting == True:
                #Play the fireball sound
                shoot_sound = pygame.mixer.Sound("sounds/fireball_shoot.mp3")
                shoot_sound.play()
                #Create the fireball image
                fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
                fireballImageUnrotated = pygame.transform.scale(fireballImageUnsized, (100, 50))
                fireball_rect = fireballImageUnrotated.get_rect(center=(bossRect2.center))
				
                #Make the fireball go towards the player's direction
                dx = playerX - fireball_rect.centerx
                dy = playerY - fireball_rect.centery

                distance = math.hypot(dx, dy)
                #Find the distance

                if distance != 0:
                    fireball_vx = dx / distance * fireball_speed
                    fireball_vy = dy / distance * fireball_speed

                shooting = False
                shootingCount = 0
					
            shootAnimation = True
            shootFireball()     #Function to get the sidekick to shoot the fireball

        #If the fire is being spawned
        if spawn_fire:
            createFire()        #Function to animate and create the fire

        #If the sidekick is alive and is not shooting
        if sidekickAlive == True and sidekickHealth > 0 and bossShooting == False:
            #Create the boss's image on the screen
            SCREEN.blit(bossFly2, (bossX2, bossY2))

        #Show sidekick hitbox during attack left
        #pygame.draw.rect(SCREEN, GREEN, bossRect2, 3)

        #If the boss is not flipped, create the sidekick's health bar
        if boss_flipped == False:
            pygame.draw.rect(SCREEN, RED, (bossX2 + 20, bossY2 - 20, 100, 15))
            pygame.draw.rect(SCREEN, BLACK, (bossX2 + 20, bossY2 - 20, 100, 15), 3)
            pygame.draw.rect(SCREEN, BLACK, (bossX2 + 20, bossY2 - 20, 100 - sidekickHealth, 15))

        #If the boss is flipped
        else:
            pygame.draw.rect(SCREEN, RED, (bossX2 - 10, bossY2 - 20, 100, 15))
            pygame.draw.rect(SCREEN, BLACK, (bossX2 - 10, bossY2 - 20, 100, 15), 3)
            pygame.draw.rect(SCREEN, BLACK, (bossX2 - 10, bossY2 - 20, 100 - sidekickHealth, 15))

def shootFireball():
    global fireball_speed, bossShooting, shooting, fireball_rect, fireball_vx, fireball_vy, last_action_time, fireX, fireY, spawn_fire, fireCooldown
    #If the sidekick is shooting a fireball
    if shootAnimation == True:
        sidekickShoot()         #Function to animate the sidekick

    #Get the fireball to move
    fireball_rect.centerx += fireball_vx
    fireball_rect.centery += fireball_vy
    fireball_angle = math.degrees(math.atan2(-fireball_vy, fireball_vx))
    fireballImage = pygame.transform.rotate(fireballImageUnrotated, fireball_angle + 180)
    rotated_rect = fireballImage.get_rect(center=fireball_rect.center)

    #If the fireball's Y coordinates is over or equal to 770
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

    #If the fireballs' X coordinates is over or equal to 800 or under or equal to 0
    if fireball_rect.centerx >= 800 or fireball_rect.centerx <= 0:
        bossShooting = False
        shooting = True
        fireball_rect.center = (1000, 1000)

    #Create the fireball image
    SCREEN.blit(fireballImage, rotated_rect)

def createFire():
    global fireCount, spawn_fire, fireCooldown, fire_rect, fireX, fireY, last_action_time, fire_sound, fireSound
    #If the fire sound is not being played
    if fireSound == 0:
        #Play the fire sound
        fire_sound.play()
        fireSound = 1
    
    #Get the fire cooldown and animate it
    fireCooldown = pygame.time.get_ticks()
    fireImageUnsized = pygame.image.load(f"fire/{fireCount}.png").convert_alpha()
    fireImage = pygame.transform.scale(fireImageUnsized, (100, 100))
    fire_rect = fireImage.get_rect(center=(fireX, fireY - 70))
    fireCount += 1

    #If the animation is over, reset the animation
    if fireCount == 7:
        fireCount = 0

    #If the fire is animating for less than 2000 milliseconds
    if fireCooldown - last_action_time <= 2000:
        #Create the image
        SCREEN.blit(fireImage, fire_rect)
    
    #If the fire is animating for more than 2000 milliseconds
    else:
        #Stop the sound and stop the fire
        fire_sound.stop()
        fireSound = 0
        fireCooldown = 0
        spawn_fire = False
        fire_rect.center = (1000, 1000)

def sidekickShoot():
    global shootingCount, shootAnimation, bossShooting, sidekick_animation
    #If the shooting animation count is 8
    if shootingCount == 8:
        #Animate it's idle animation
        sidekickUnsized = pygame.image.load(f"boss_idle2/{sidekick_animation}.png")
        sidekick_animation += 1
        sidekickFly = pygame.transform.scale(sidekickUnsized, (new_width, new_height))

        sidekick_rect = sidekickFly.get_rect(center=(bossX2 + 50, bossY2 + 50))

        if boss_flipped == False:
            sidekickFly = pygame.transform.flip(sidekickFly, True, False)

        if sidekick_animation == 12:
            sidekick_animation = 0

        #Create the animation image
        SCREEN.blit(sidekickFly, sidekick_rect)
    
    #If the shooting animation is still going
    else:
        #Get the shooting image and animate it
        shootingImageUnsized = pygame.image.load(f"sidekick_attack/{shootingCount}.png").convert_alpha()
        shootingCount += 1
        shootingImage = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shooting_rect = shootingImage.get_rect(topleft=(bossX2, bossY2))

        #If the player's X coordinates is more than the fireball
        if playerX > fireball_rect.centerx:
            #Flip the shooting image
            shootingImage = pygame.transform.flip(shootingImage, True, False)

        #Create the image
        SCREEN.blit(shootingImage, shooting_rect)

def bossGoBack():
    global boss_animation_count, bossX, bossY, bossRect, boss_going_back, attacking, animationFinished, hypoteneuse, sidekickAlive, bossLanded
    global revert_explosion, stopExplosion, bigFireball_rect, fireball_shoot, shoot_number, attackQuantity, bigFireballY, fireCooldown, fireball_rect
    global fireballShower, bossFlipped, fireballMovement, fireballMovement2, setFireballMovement, setFireballMovement2
    global fireballY5
    #Animate the boss in it's idle animation
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect.topleft = (bossX, bossY)
    if boss_animation_count == 12:
        boss_animation_count = 0

    #Set the attacking to false so the player can hit it
    attacking = False

    backX = 350
    backY = 400
    #Find the hypoteneuse of the boss and the destination
    bossX, bossY, hypoteneuse = findHypoteneuse(backX, backY, bossX, bossY, hypoteneuse, boss_speed)

    #If the boss made it towards the destination, reset the attacks variables depending on the attack choice 
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
            fires_sound.stop()
            attacking = False
            boss_going_back = False
            bossLanded = False
            fireballShower = False
            fireball_shoot = False
            attackQuantity += 1
            fireballY5 = 0

        if attackChoice <= EVERYWHERE and attackChoice > ATTACKDOWN:
            fires_sound.stop()
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

    #If boss is not dead
    if boss_dead == False:
        #Create the image
        SCREEN.blit(bossFly, bossRect)
    
def findHypoteneuse(targetX, targetY, userX, userY, hypoteneuse, speed):
    #Find the rise and run of the target and user
    run = targetX - userX
    rise = targetY - userY

    #Find the hypoteneuse of it
    hypoteneuse = math.sqrt(run ** 2 + rise ** 2)

    if hypoteneuse == 0:
        return userX, userY
    
    #Move the userX and userY
    user_x_speed = run/hypoteneuse * speed
    user_y_speed = rise/hypoteneuse * speed
    userX += user_x_speed
    userY += user_y_speed

    return userX, userY, hypoteneuse

def bossAttackUp():
    global boss_animation_count, bossX, bossY, fireball_shoot, fireballMovement, bossLanded, bossShootCount, shoot_number, bossRect, shoot_spot
    global bigFireballY, bigFireballX, bigExplosionCount, bigExplosionSize, stopExplosion, revert_explosion, boss_going_back, playerX, playerY, playerHealth
    global fire_animation_count, fire_rect, fireballSound, fireball_sound, bigFireball_sound

    #Set the boss animation idle position
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png").convert_alpha()
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect = bossFly.get_rect(topleft=(bossX, bossY))
    if shoot_number == 4:
        fireball_shoot = True

    if boss_animation_count == 12:
        boss_animation_count = 0

    #If the boss has not landed
    if bossLanded == False:
        fireballSound = 0 
        up_surf = pygame.Surface((50, 50))
        up_rect = up_surf.get_rect(center=(400, 100))

        upX = up_rect.centerx
        upY = up_rect.centery
        run = upX - bossX
        rise = upY - bossY

        #Find the hypoteneuse
        upHypoteneuse = math.sqrt(run ** 2 + rise ** 2)

        if upHypoteneuse == 0:
            return

        #Move the boss
        boss_x_speed = run/upHypoteneuse * boss_speed
        boss_y_speed = rise/upHypoteneuse * boss_speed
        bossX += boss_x_speed
        bossY += boss_y_speed

        #Create the boss image
        SCREEN.blit(bossFly, (bossX, bossY))

        if upHypoteneuse <= boss_speed:
            bossX = upX
            bossY = upY
            bossLanded = True

    #If the boss made it to it's destination
    elif bossLanded == True and fireball_shoot == False and shoot_number <= 5:
        #Animate the shooting animation
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImageRotated = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shootingImage = pygame.transform.rotate(shootingImageRotated, -90)   
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))

        #If the animation is finished, set the variable fireball_shoot to true
        if bossShootCount == 24:
            fireball_shoot = True

        #Create the shooting image
        SCREEN.blit(shootingImage, shooting_rect)

    #If fireball_shoot is true from the animation
    if fireball_shoot == True:
        #If the number of shots is under or equal to 3
        if shoot_number <= 3:
            if fireballSound == 0:
                #Play the fireball sound
                fireball_sound.play()
                fireballSound = 1
            #Create the fireball image
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

            #Randomize the big fireball's X coordinates
            bigFireballX = random.randint(50, 700)

            #Create the fireball image
            SCREEN.blit(fireballImage, fireball_rect)

        else:
            #If the big fireball's Y coordinates minus 200 is under or equal to 800
            if bigFireballY - 200 <= 800:
                #Create the big fireball image and it's hitboxes
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

                #Create the big fireball image
                SCREEN.blit(bigFireballImage, bigFireball_rect)

                #If the fireball left side touches the player
                if bigFireballLeft.colliderect(player_rect):
                    playerX -= 500
                    playerY -= 300
                    playerHealth -= 20

                #If the fireball's right side touches the player
                elif bigFireballRight.colliderect(player_rect):
                    playerX += 500
                    playerY -= 300
                    playerHealth -= 20

            #If the fireball has reached the ground
            else:
                if fireballSound == 0:
                    #Play the fire ball sound
                    bigFireball_sound.play()
                    fireballSound = 1
                
                #If the explosion animation is 0 and the explosion is not finished 
                if bigExplosionCount == 0 and revert_explosion == True:
                    bigExplosionCount = 0
                    stopExplosion = True
                    boss_going_back = True
                    fireballSound = 0
                
                #If boss has finished attacking
                if boss_going_back == True:
                    bossGoBack()        #Function to move the boss back

                #If the explosion is finished
                if stopExplosion == True:
                    fire_rect.center = (50000, 2000)
                
                #If the explosion is not finised
                else:
                    if fireballSound == 0:
                        fireballSound = 1
                        #Play the explosion sound
                        explosion_sound.play()
                    
                    #Create the explosion image
                    bigExplosionUnsized = pygame.image.load(f"bigFireball_collide/{bigExplosionCount}.png").convert_alpha()
                    if revert_explosion == False:
                        bigExplosionCount += 1

                    #Once the explosion animation is finished, reverse it
                    if bigExplosionCount == 16 or revert_explosion == True:
                        revert_explosion = True
                        bigExplosionCount -= 1

                    bigExplosion = pygame.transform.scale(bigExplosionUnsized, (bigExplosionSize + 598, bigExplosionSize + 500))
                    
                    if revert_explosion == False:
                        bigExplosionSize += 5
                    else:
                        bigExplosionSize -= 5
                    bigExplosion_rect = bigExplosion.get_rect(center=(bigFireballX, bigFireballY - 300))

                    #If explosion is reversing
                    if revert_explosion == True:
                        #Create a fire image
                        largeFireImageUnsized = pygame.image.load(f"fire/{fire_animation_count}.png").convert_alpha()
                        largeFireImage = pygame.transform.scale(largeFireImageUnsized, (367, 250))
                        fire_animation_count += 1
                        if fire_animation_count == 7:
                            fire_animation_count = 0

                        fire_rect = largeFireImage.get_rect(center=(bigFireballX, bigFireballY - 300))

                        #Create the fire image
                        SCREEN.blit(largeFireImage, fire_rect)
                    #Create the explosion image
                    SCREEN.blit(bigExplosion, bigExplosion_rect)
        #Create the boss's image
        SCREEN.blit(bossFly, (bossX, bossY))

def bossAttackRight():
    global boss_animation_count, bossX, bossY, shoot_number, bigFireballX, fireball_shoot, bossLanded, bossShootCount, fireballMovement
    global idleCount, platformX, jumping, falling, ground_y, on_platform, playerY, platform_rect, bigFireball_rect, boss_going_back, playerHealth
    global fireballSound, fireball_sound
    #Set the boss's animation to it's idle animatoin
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png").convert_alpha()
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect.topleft = (bossX, bossY)
    #If the animation is finished, reset it
    if boss_animation_count == 12:
        boss_animation_count = 0

    #If the bigfireball's X coordinates is over or equal to 1000
    if bigFireballX - 1100 >= 1000:
        #Reset everything for attacking right
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

    #If the boss finished attacking
    if boss_going_back == True:
        bossGoBack()        #Function to get the boss going back
        return
    
    #If the boss has not landed at it's destination
    if bossLanded == False:
        #Move the boss towards the destination
        fireballSound = 0
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

        #If the boss made it to it's destination
        if rightHypoteneuse <= boss_speed:
            bossX = rightX
            bossY = rightY
            bossLanded = True

        #Create the boss's image
        SCREEN.blit(bossFly, (bossX, bossY))

    #If the boss has made it to it's destination
    elif bossLanded == True and fireball_shoot == False:
        #Make the boss shooting animation
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImage = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))

        #If the animation is finished
        if bossShootCount == 24:
            bossShootCount = 0
            fireball_shoot = True
        
        #Create the shooting image
        SCREEN.blit(shootingImage, shooting_rect)

    #If the boss shot a fireball
    if fireball_shoot == True:
        #Animate the boss with the idle animation
        bossIdleImageUnsized = pygame.image.load(f"boss_idle/{idleCount}.png").convert_alpha()
        idleCount += 1
        bossIdleImage = pygame.transform.scale(bossIdleImageUnsized, (new_width, new_height))
        idle_rect = bossIdleImage.get_rect(topleft=(bossX, bossY))
        if idleCount == 12:
            idleCount = 0

        #Create the animation
        SCREEN.blit(bossIdleImage, idle_rect)

        #If the quantity of shots is equal to or under 2
        if shoot_number <= 2:
            if fireballSound == 0:
                #Play the fireball sound
                fireball_sound.play()
                fireballSound = 1
            
            #Make the fireball image
            fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
            fireballImage = pygame.transform.scale(fireballImageUnsized, (150, 100))
            fireball_rect = fireballImage.get_rect(center=(bossX + fireballMovement, bossY + 50))
            fireballMovement -= 20

            #If the fireball reaches outside of the screen
            if fireball_rect.centerx <= 0:
                shoot_number += 1
                fireballMovement = 0
                fireball_shoot = False
                fireballSound = 0

            #Create the fireball image
            SCREEN.blit(fireballImage, fireball_rect)

        #If the quantity of shots is over 2
        else:
            if fireballSound == 0:
                fireballSound = 1
                #Play the big fireball sound
                bigFireball_sound.play()
            
            #Create the big fireball image
            fireballImageUnsized = pygame.image.load("fireball.png").convert_alpha()
            bigFireballImageUnflipped = pygame.transform.scale(fireballImageUnsized, (750, 500))
            bigFireballImage = pygame.transform.flip(bigFireballImageUnflipped, True, False)
            bigFireball_rect = bigFireballImage.get_rect(center=(bigFireballX - 1000, 750))
            bigFireballHitbox = pygame.Rect(bigFireballX - 1300, bigFireballY + 650, bigFireball_rect.width - 130, bigFireball_rect.height)
            bigFireballX += 10

            #Create the big fireball image on the screen
            SCREEN.blit(bigFireballImage, bigFireball_rect)

            #Create the platform image
            platformImageUnsized = pygame.image.load("platform.png").convert_alpha()
            platformImage = pygame.transform.scale(platformImageUnsized, (269, 100))
            if platformX == 0:
                platformX = random.randint(200, 750)
            platform_rect = platformImage.get_rect(center=(platformX, 650))
            platform_rectTop = pygame.Rect(platform_rect.centerx - 100, platform_rect.centery - 75, platform_rect.width - 50, 10)
            
            #Show platform hitbox
            #pygame.draw.rect(SCREEN, RED, platform_rect, 3)
            #pygame.draw.rect(SCREEN, GREEN, platform_rectTop, 3)

            #If the player touches the platform's top
            if player_rect.colliderect(platform_rectTop):
                player_rect.bottom = platform_rectTop.bottom
                on_platform = True
                jumping = False
                falling = True

            #If the player is not touching the platform's top
            if not player_rect.colliderect(platform_rectTop) and on_platform == True:
                ground_y = 667
                falling = True
                on_platform = False

            #If the player is touching the platform
            if player_rect.colliderect(platform_rect):
                falling = True

            #If the player is touching the big fireball
            if player_rect.colliderect(bigFireballHitbox):
                playerY -= 300
                playerHealth -= 10

            #Show fireball hitbox for attacking up
            #pygame.draw.rect(SCREEN, RED, bigFireballHitbox, 3)

            #Create the platform image
            SCREEN.blit(platformImage, platform_rect)

def bossAttackDown():
    global fireballY, fireballX, fireballY2, fireballX2, fireballY3, fireballX3, fireballY4, fireballX4, fireballY5, fireballX5
    global fireballShower, bossLanded, bossX, bossY, fireball_shoot, fireballShower, bossShootCount, idleCount
    global boss_wait_time, fireballImage, fireball_cooldown, boss_going_back, playerX, playerY, playerHealth
    global fireball_rect, fireball_rect2, fireball_rect3, fireball_rect4, fireball_rect5, exploding, fireball_cooldown
    global fireballHitbox, fireball2Hitbox, fireball3Hitbox, fireball4Hitbox, fireball5Hitbox, fires_sound, fireballSound
    bossRect.topleft = (bossX, bossY)

    #If the boss has finished attacking
    if boss_going_back == True:
        bossGoBack()        #Function to move the boss back
        return
    
    #If the boss has not arrived at it's destination
    if bossLanded == False:
        #Move the boss towards the destination
        fireballSound = 0
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

        #If the boss made it to it's destination
        if downHypoteneuse <= boss_speed:
            bossX = downX
            bossY = downY
            bossLanded = True
        
        #Create the boss's image
        SCREEN.blit(bossFly, (bossX, bossY))
    
    #If the boss has made it to it's destination and is not shooting
    elif bossLanded == True and fireball_shoot == False:
        #Create the boss's shooting image
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImage = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))

        #If the animation is finished
        if bossShootCount == 24:
            bossShootCount = 0
            fireball_shoot = True
        
        #Create the shooting boss image
        SCREEN.blit(shootingImage, shooting_rect)

        #Get the time in milliseconds
        boss_wait_time = pygame.time.get_ticks()

    #If the boss is shooting the fireball
    if fireball_shoot == True:
        #Get the current time in milliseconds
        current_time = pygame.time.get_ticks()
        #If the current time minus the boss wait time is equal to or below 2000 milliseconds
        if current_time - boss_wait_time >= 2000:
            #Set the fireball shower to be true
            fireballShower = True

        #Animate the boss's idle animation
        bossIdleImageUnsized = pygame.image.load(f"boss_idle/{idleCount}.png").convert_alpha()
        idleCount += 1
        bossIdleImage = pygame.transform.scale(bossIdleImageUnsized, (new_width, new_height))
        idle_rect = bossIdleImage.get_rect(topleft=(bossX, bossY))
        if idleCount == 12:
            idleCount = 0
        
        #Create the idle animation on the screen
        SCREEN.blit(bossIdleImage, idle_rect)
        #If the fireballs are not defined yet
        if fireballX2 == 0:
            #Random the X position of the fireballs
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
            #Get the current time in milliseconds
            fireball_cooldown = pygame.time.get_ticks()  

    #If the fireball shower has begun
    if fireballShower == True:
        #If the fireball cooldown is not defined yet
        if fireball_cooldown == 0:
            #Get the current time
            fireball_cooldown = pygame.time.get_ticks()

        #Define all the other fireball images to be the same as the orginal fireball image
        fireballImage2 = fireballImage
        fireballImage3 = fireballImage
        fireballImage4 = fireballImage
        fireballImage5 = fireballImage
        #Get the current time in milliseconds
        current_time = pygame.time.get_ticks()

        #Move the first fireball's X coordinates
        fireball_rect = fireballImage.get_rect(center=(fireballX, fireballY - 50))
        fireballHitbox = pygame.Rect(fireballX - 50, fireballY - 50, 75, 75)
        fireballY += 15
        fireballX -= 5

        #If the time has been 4 seconds long
        if current_time - fireball_cooldown >= 4000:
            if fireballSound == 0:
                #Play the sound
                fires_sound.play()
                fireballSound = 1
            
            #Move the second fireball
            fireball2Hitbox = pygame.Rect(fireballX2 - 50, fireballY2 - 50, 75, 75)
            fireball_rect2 = fireballImage2.get_rect(center=(fireballX2, fireballY2 - 50))
            fireballY2 += 15
            fireballX2 -= 5

            #Create the second fireball
            SCREEN.blit(fireballImage2, fireball_rect2)

        #If the time has been 5 seconds long
        if current_time - fireball_cooldown >= 5000:
            #Move the third fireball
            fireball3Hitbox = pygame.Rect(fireballX3 - 50, fireballY3 - 50, 75, 75)
            fireball_rect3 = fireballImage3.get_rect(center=(fireballX3, fireballY3 - 50))
            fireballY3 += 15
            fireballX3 -= 5

            #Create the third fireball
            SCREEN.blit(fireballImage3, fireball_rect3)

        #If the time has been 6 seconds long
        if current_time - fireball_cooldown >= 6000:
            #Move the fourth fireball
            fireball4Hitbox = pygame.Rect(fireballX4 - 50, fireballY4 - 50, 75, 75)
            fireball_rect4 = fireballImage4.get_rect(center=(fireballX4, fireballY4 - 50))
            fireballY4 += 15
            fireballX4 -= 5

            #Create the fourth fireball
            SCREEN.blit(fireballImage4, fireball_rect4)

        #If the time has been 7 seconds long
        if current_time - fireball_cooldown >= 7000:
            #Move the fifth fireball
            fireball5Hitbox = pygame.Rect(fireballX5 - 50, fireballY5 - 50, 75, 75)
            fireball_rect5 = fireballImage5.get_rect(center=(fireballX5, fireballY5 - 50))
            fireballY5 += 15
            fireballX5 -= 5
            #Create the fifth fireball
            SCREEN.blit(fireballImage5, fireball_rect5)
        
        #If the fifth fireball go off-screen
        if fireballY5 >= 800:
            boss_going_back = True
            fireballY5 = 0
            fireballX2 = 0
            fireballSound = 0
        
        #If the fourth fireball goes off-screen
        elif fireballY4 >= 800:
            fireball_rect4.center = (10000, 10234)
            fireballX4 = -1000
        
        #If the third fireball goes off-screen
        elif fireballY3 >= 800:
            fireball_rect3.center = (245, 1000)
            fireballX3 = -1000

        #If the second fireball goes off-screen
        elif fireballY2 >= 800:
            fireball_rect2.center = (245, 1000)
            fireballX2 = -1000

        #If the first fireball goes off-screen
        elif fireballY >= 800:
            fireball_rect.center = (245, 1000)
            fireballX = -1000

        #If the player touches any fireball
        if player_rect.colliderect(fireballHitbox) or player_rect.colliderect(fireball2Hitbox) or player_rect.colliderect(fireball3Hitbox) or player_rect.colliderect(fireball4Hitbox) or player_rect.colliderect(fireball5Hitbox):
            playerX += 300
            playerY -= 200
            playerHealth -= 5

        #Create the first fireball
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
    #Animate the boss's idle animation
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png").convert_alpha()
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    bossRect.topleft = (bossX, bossY)
    #If animation is finished, reset it
    if boss_animation_count == 12:
        boss_animation_count = 0

    #If the boss finishes attacking
    if boss_going_back == True:
        bossGoBack()        #Function to make the boss go back
        return
    
    #If the boss is not at it's destination
    if bossLanded == False:
        #Move the boss towards it's destination
        fireballSound = 0
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

        #Create the boss on screen
        SCREEN.blit(bossFly, (bossX, bossY))

    #If the boss made it to it's destination
    elif bossLanded == True:
        #Animate the boss's shooting animation
        shootingImageUnsized = pygame.image.load(f"boss_attack/{bossShootCount}.png").convert_alpha()
        bossShootCount += 1
        shootingImageUnrotated = pygame.transform.scale(shootingImageUnsized, (new_width, new_height))
        shootingImage = pygame.transform.rotate(shootingImageUnrotated, 90)
        #If the boss is flipped
        if bossFlipped == True:
            #Flip the image
            shootingImage = pygame.transform.flip(shootingImage, True, False)
        shooting_rect = shootingImage.get_rect(topleft=(bossX, bossY))

        #If the animation is finished
        if bossShootCount == 24:
            bossShootCount = 0
            fireball_shoot = True

        #Create the shooting boss image
        SCREEN.blit(shootingImage, shooting_rect)
        #If the boss's X position is equal to or under 20 and is not flipped
        if bossX <= 20 and bossFlipped == False:
            bossFlipped = True

        #If the boss's X position is equal to or more than 750 and is flipped 
        if bossX >= 750 and bossFlipped == True:
            boss_going_back = True
            fireballSound = 0

        #If boss is flipped
        if bossFlipped == True:
            #Move it to the right
            bossX += 5
        #If the boss is not flipped
        else:
            #Move it to the left
            bossX -= 5

    #If the boss is shooting it's fireball
    if fireball_shoot == True:
        #If fireball's X position equal to or under 0
        if fireballX <= 0:
            fireballX = bossX + 50
        #If the second fireball's X position is equal to or under 0
        elif fireballX2 <= 0:
            fireballX2 = bossX + 50
        
        #If no fireball sound is playing
        if fireballSound == 0:
            #Play the fireball sound
            fires_sound.play()
            fireballSound = 1
        
        #Create the first fireball and it's hitbox
        #Move the first fireball downwards
        fireballImageUnrotated = pygame.image.load("fireball.png").convert_alpha()
        fireballImageUnsized = pygame.transform.rotate(fireballImageUnrotated, 90)
        fireballImage = pygame.transform.scale(fireballImageUnsized, (100, 150))
        fireball_rect = fireballImage.get_rect(center=(fireballX, bossY + fireballMovement))
        fireballHitbox = pygame.Rect(fireballX - 20, bossY + fireballMovement, 50, 50)
        fireballMovement += 30

        #Create the second fireball and it's hitbox
        #Move the second fireball downwards
        fireballImageUnrotated2 = pygame.image.load("fireball.png").convert_alpha()
        fireballImageUnsized2 = pygame.transform.rotate(fireballImageUnrotated2, 90)
        fireballImage2 = pygame.transform.scale(fireballImageUnsized2, (100, 150))
        fireball_rect2 = fireballImage.get_rect(center=(fireballX2, bossY + fireballMovement2))
        fireballHitbox2 = pygame.Rect(fireballX2 - 20, bossY + fireballMovement2, 50, 50)
        fireballMovement2 += 30

        #If the first fireball's Y position is equal to or more than 550
        if fireball_rect.centery >= 550:
            if setFireballMovement2 == True:
                fireballMovement2 = 0
                setFireballMovement2 = False
                setFireballMovement = True
                fireballX2 = -100
            #Get the second fireball to the boss                
            fireball_rect2 = fireballImage.get_rect(center=(fireballX2, bossY + fireballMovement2))

        #If the second fireball's Y position is equal to ore more than 550
        if fireball_rect2.centery >= 550:
            if setFireballMovement == True:
                fireballMovement = 0
                setFireballMovement = False
                setFireballMovement2 = True
                fireballX = -100

            #Get the first fireball to the boss
            fireball_rect.center = (fireballX, bossY + fireballMovement)

        #If the player touches the fireballs
        if player_rect.colliderect(fireballHitbox) or player_rect.colliderect(fireballHitbox2):
            #If the boss is flipped
            if bossFlipped == True:
                #Move the player to the right
                playerX += 200
                playerY -= 50
                playerHealth -= 4
            #If the boss is not flipped
            else:
                #Move the player to the left
                playerX -= 200
                playerY -= 50
                playerHealth -= 4

        #Show fireball hitboxes
        # pygame.draw.rect(SCREEN, RED, fireballHitbox, 3)
        # pygame.draw.rect(SCREEN, GREEN, fireballHitbox2, 3)

        #Create the fireball's image
        SCREEN.blit(fireballImage2, fireball_rect2)
        SCREEN.blit(fireballImage, fireball_rect)

def sidekickDamaged():
    global sidekickGotHit, bossFly2, boss_animation_count3, boss_animation_count2
    #Create the sidekick's damaged animation
    bossDamageUnsized2 = pygame.image.load(f"boss_damage2/{boss_animation_count3}.png")
    boss_animation_count3 += 1
    bossFly2 = pygame.transform.scale(bossDamageUnsized2, (new_width, new_height))

    #If the animation is finished
    if boss_animation_count3 == 4:
       boss_animation_count3 = 0
       sidekickGotHit = False

def sidekickDeath():
    global attacking, bossDeathCount, sidekickHealth, bossRect2, animationFinished, boss_animation_count, bossRect2
    #Move the sidekick's hitbox off-screen
    bossRect2.topleft = (-1000, -1000)

    #Create the boss's idle animation
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))

    #If the animation is finished, reset it
    if boss_animation_count == 12:
        boss_animation_count = 0

    #Create the sidekick's death animation
    bossDeathUnsized = pygame.image.load(f"sidekick_death/{bossDeathCount}.png")
    bossDeathCount += 1
    bossDeath = pygame.transform.scale(bossDeathUnsized, (new_width, new_height))
    bossDeath_rect = bossDeath.get_rect(topleft=(bossX2, bossY2))

    #If the death animation is over
    if bossDeathCount == 6:
        bossDeathCount = 0
        sidekickHealth = 100
        bossRect2 = (1000, 1000)
        animationFinished = True

    #Create both images
    SCREEN.blit(bossDeath, bossDeath_rect)
    SCREEN.blit(bossFly, (bossX, bossY))

def updateHealthBars():
    #If the boss's health is under 200
    if bossHealth < 200:
        inverse = 200 - bossHealth
        #Makes a black rectangle to cover the red health bar
        pygame.draw.rect(SCREEN, BLACK, (570, 45, inverse, 30))

def checkBowClicked():
    global BOW_BUTTON_COLOR, BUTTON_CLICK_COLOR, button_clicked, bow_button_rect, button_hover, weapon_choice
    #Find the events that the player does
    events = pygame.event.get()
    #Find individual events
    for event in events:
        #If the event is the player clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            #If the cursor is overlapping the bow button
            if bow_button_rect.collidepoint(event.pos):
                button_hover = 2
                BOW_BUTTON_COLOR = BUTTON_CLICK_COLOR
                button_clicked = True
                weapon_choice = BOW

def checkBoomrngClicked():
    global BOOMRNG_BUTTON_COLOR, BUTTON_CLICK_COLOR, button_clicked, boomrng_button_rect, weapon_choice
    #Find the events that the player does
    events = pygame.event.get()
    #Find individual events
    for event in events:
        #If the event is the player clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            #If the cursor is overlapping with the boomerang button
            if boomrng_button_rect.collidepoint(event.pos):
                BOOMRNG_BUTTON_COLOR = BUTTON_CLICK_COLOR
                button_clicked = True
                weapon_choice = BOOMRNG

def handleKeys(keys):
    global playerX, playerY, playerSpeed, moving_left, moving_right, playerAnimation, spaceHolding, escape_pressed, menu, escape_holding
    global playerFlipped
    #Set the player to not move
    moving_left = False
    moving_right = False

    #If the player presses 'A' or 'LEFT' key
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        #Move the player left
        playerX -= playerSpeed
        playerFlipped = True
        moving_left = True

    #If the player presses 'D' or 'RIGHT' key
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        #Move the player right
        playerX += playerSpeed
        playerFlipped = False
        moving_right = True

    #If the player presses 'W' or 'UP' key
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        playerJump()        #Function to make the player jump

    #If the player presses the 'ESC' key and is not holding it
    if keys[pygame.K_ESCAPE] and escape_holding == False:
        menu = True
        escape_holding = True
        escapeMenu()        #Function to open a menu

    #If the player is not holding space
    if spaceHolding == False:
        #If the player presses the 'SPACE' key
        if keys[pygame.K_SPACE]:
            playerAttack()      #Function to get the player to attack
            spaceHolding = True

    #If the player is not pressing the 'SPACE' key
    if not (keys[pygame.K_SPACE]):
        spaceHolding = False

    #If the player is not pressing the 'A' and 'D' key at the same time
    if not (keys[pygame.K_a] and keys[pygame.K_d]):
        playerAnimation = False

    #If the player is not pressing the 'A' or 'RIGHT' key
    elif not (keys[pygame.K_a] and keys[pygame.K_RIGHT]):
        playerAnimation = False
    
    #If the player is not pressing the 'D' or 'LEFT' key
    elif not(keys[pygame.K_d] and keys[pygame.K_LEFT]):
        playerAnimation = False

def checkForEscape(keys):
    global menu, escape_holding, guide_clicked

    #If the player presses the 'ESC' key and is not holding it and the menu is not open
    if keys[pygame.K_ESCAPE] and escape_holding == False and menu == False:
        menu = True
        escape_holding = True
        guide_clicked = not guide_clicked

    #If the player presses the 'ESC' key and is not holding it and menu is open
    if keys[pygame.K_ESCAPE] and escape_holding == False and menu == True:
        menu = False
        guide_clicked = False
        escape_holding = True

    #If the palyer is not pressing the 'ESC' key
    if not keys[pygame.K_ESCAPE]:
        escape_holding = False

def escapeMenu():
    global menu, escape_holding
    #Play a clicking sound
    click_sound.play()
    #Loop the menu, stopping everything else or pausing the program
    while menu == True:
        findEvents()        #Function to check if the player quits the game

        #Find what keys the player pressed
        keys = pygame.key.get_pressed()
        checkForEscape(keys)    #Function to check if the player presses the 'ESC' key

        createMenu()            #Function to create the menu
        clock.tick(FPS)         #Set the frames per second

def createMenu():
    global guide_rect, home_rect, mouse_rect, fromGuide, menu, GUIDE_BUTTON_COLOR, HOME_BUTTON_COLOR, guide_text
    global home_text, fromHome, guide_clicked, home_clicked, sound
    #Create the menu background
    pygame.draw.rect(SCREEN, GREEN, (30, 20, 738, 735))

    #Get the mouse position and hitbox
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse_x, mouse_y, 2, 2)

    #Get the fonts for the texts that the menu uses
    font = pygame.font.SysFont("Georgia", 100)
    button_font = pygame.font.SysFont("Comic Sans MS", 100)
    warning_font = pygame.font.SysFont("Georgia", 30)
    escape_font = pygame.font.SysFont("Comic Sans MS", 50)

    #Define the menu's title text
    menu_text = "Menu"
    menu_surface = font.render(menu_text, True, BLACK)
    menu_rect = menu_surface.get_rect()
    menu_rect.center = (400, 60)

    #Define the guide button text
    guide_text = "GUIDE"
    guide_surface = button_font.render(guide_text, True, WHITE)
    guide_rect = guide_surface.get_rect()
    guide_rect.center = (400, 300)

    #Define the leave button text
    home_text = "LEAVE"
    home_surface = button_font.render(home_text, True, WHITE)
    home_rect = home_surface.get_rect()
    home_rect.center = (400, 600)

    #Define the warning text
    warning_text = "WARNING: PROGRESS WILL NOT BE SAVED!!"
    warning_surface = warning_font.render(warning_text, True, RED)
    warning_rect = warning_surface.get_rect()
    warning_rect.center = (400, 500)

    #Define the subtitle text
    escape_text = "Press 'ESC' to leave the menu"
    escape_surf = escape_font.render(escape_text, True, BLACK)
    escape_rect = escape_surf.get_rect()
    escape_rect.center = (400, 130)
    
    #If the buttons are not clicked yet
    if guide_clicked == False and home_clicked == False:
        drawButton(guide_rect, GUIDE_BUTTON_COLOR, guide_text, button_font, SCREEN)
        drawButton(home_rect, HOME_BUTTON_COLOR, home_text, button_font, SCREEN)

    #Create the text
    SCREEN.blit(warning_surface, warning_rect)
    SCREEN.blit(menu_surface, menu_rect)
    SCREEN.blit(escape_surf, escape_rect)

    #Create the outline of the menu and buttons
    pygame.draw.rect(SCREEN, BLACK, (30, 20, 738, 735), 4)
    pygame.draw.rect(SCREEN, BLACK, guide_rect, 3)
    pygame.draw.rect(SCREEN, BLACK, home_rect, 3)

    #If the guide button is clicked
    if guide_clicked == True:
        fromGuide = True
        createInstructions()

    #If the leave button is clicked
    if home_clicked == True:
        pygame.quit()
        exit()
        import sys
        sys.exit()

    #Update the game
    pygame.display.update()

    #Functions that check if a button is clicked
    checkGuideButton()
    checkHomeButton()

def checkGuideButton():
    global fromGuide, menu, guide_clicked, GUIDE_BUTTON_COLOR, radius, grow_circle, mouse_rect, button_font, guide_hover
    global sound

    #If the cursor is not overlapping with the guide button
    if not(guide_rect.colliderect(mouse_rect)):
        if guide_clicked == False:
            #Set the cursor to an arrow
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
            #Set the button's color to blue
            GUIDE_BUTTON_COLOR = BLUE
            guide_hover = False
            guide_clicked = False

    #If the cursor is overlapping with the guide button
    if guide_rect.colliderect(mouse_rect):
        guide_hover = True
        #Set the cursor to a hand
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        #Set the button's color to the button hover color
        GUIDE_BUTTON_COLOR = BUTTON_HOVER_COLOR

        #Get the events the player does
        events = pygame.event.get()

        #Get individual events
        for event in events:
            #If the event is a click and the guide button is not clicked
            if event.type == pygame.MOUSEBUTTONDOWN and guide_clicked == False:
                #Get the mouse's position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect(mouse_x, mouse_y, 2, 2)
                #Set the cursor to an arrow
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                #Set the guide button to the click color
                GUIDE_BUTTON_COLOR = BUTTON_CLICK_COLOR

                #Draw the guide button
                drawButton(guide_rect, GUIDE_BUTTON_COLOR, guide_text, button_font, SCREEN)

                radius = 0
                grow_circle = True
                if sound == 0:
                    sound = 1
                    #Play the click sound
                    click_sound.play()
                
                #Start the growing circle animation until the variable is false
                while grow_circle == True:
                    growCircle()

                    #Update the game
                    pygame.display.update()

                guide_clicked = True

def checkHomeButton():
    global home_clicked, HOME_BUTTON_COLOR, radius, mouse_rect, grow_circle, sound

    #Get the event the player does
    events = pygame.event.get()

    #If the cursor is not overlapping the leave button
    if not(home_rect.colliderect(mouse_rect)):
        #Set the cursor to an arrow
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        #Set the button to blue
        HOME_BUTTON_COLOR = BLUE

    #If the cursor is overlapping with the leave button
    else:
        #If the guide button is not clicked
        if home_clicked == False:
            #Set the cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            #Set the button to the hover color
            HOME_BUTTON_COLOR = BUTTON_HOVER_COLOR

        #Get a individual event
        for event in events:
            #If player clicks on their mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Get the cursor's position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect(mouse_x, mouse_y, 2, 2)

                #If the leave button is not clicked
                if home_clicked == False:
                    #Set the cursor to an arrow
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    #Set the leave button to the click color
                    HOME_BUTTON_COLOR = BUTTON_CLICK_COLOR

                    #Draw the new button
                    drawButton(home_rect, HOME_BUTTON_COLOR, home_text, button_font, SCREEN)

                    radius = 0
                    grow_circle = True
                    if sound == 0:
                        sound = 1
                        #Play the click sound
                        click_sound.play()
                    #Animate the growing circle until the variable is false
                    while grow_circle == True:
                        growCircle()

                        #Update the game
                        pygame.display.update()

                    home_clicked = True

def CheckBossPosition():
    global bossWidth, bossHeight, bossX, bossY, boss_pos, bossImage_rect, bossRect
    #Get the boss's position, width, and height
    bossWidth = bossImage.get_rect().width
    bossHeight = bossImage.get_rect().height
    bossImage_rect = bossFly.get_rect()

def checkIfHit():
    global bossHealth, swordRect, hit, boss_damaged, boss_pos, bossX, bossY, bossFly, bossRect, sword_swing, arrow_rect
    global is_fired, shoot_arrow, bow_shoot, allow_angle, playerHealth, playerX, playerY, playerGotHit, player_rect, boomrng_rect, boomrng_hit
    global shieldTime, blocked, last_action_time, bossShooting, shooting, spawn_fire, exploding
    global swordRect, boomrng_rect
    #If the sword is swinging and it touches the boss and the boss is not damaged yet
    if sword_swing and swordRect.colliderect(bossRect) and not boss_damaged:
        hit = True

    else: 
        hit = False

    #If the sword hit the boss
    if hit == True:
        bossHealth -= 5
        boss_damaged = True

    #If the player's weapon is the bow
    if weapon_choice == BOW:
        #If the arrow touches the boss
        if arrow_rect.colliderect(bossRect):
            #Reset the arrow and rearm the player
            is_fired = False
            shoot_arrow = False
            bow_shoot = False
            allow_angle = True
            arrow_rect.center = (playerX, playerY)

            #If the boss is not attacking
            if attacking == False:
                bossHealth -= 7
                boss_damaged = True
            
            #If the boss is attacking, block it
            else:
                blocked = True
                shieldTime = pygame.time.get_ticks()
                last_action_time = shieldTime

    #If the boomerang did not hit the boss yet
    if boomrng_hit == False:
        #If the player's weapon is a boomerang
        if weapon_choice == BOOMRNG:
            #If the boomerang hit the boss
            if boomrng_rect.colliderect(bossRect):
                boomrng_hit = True

                #If the boss is not attacking
                if attacking == False:
                     boss_damaged = True
                     bossHealth -= 10

                #If the boss is attacking, block it
                else:
                    blocked = True
                    shieldTime = pygame.time.get_ticks()
                    last_action_time = shieldTime

    #If the boss blocked the player's projectile
    if blocked == True:
       #Create the shield
       shield = pygame.image.load("shield.png").convert_alpha()
       shield_rect = shield.get_rect(topleft=(bossX - 15, bossY - 10))
       shield = pygame.transform.scale(shield, (bossWidth + 30, bossHeight + 30))

       #Draw the shield on the boss
       SCREEN.blit(shield, shield_rect)

       shieldTime = pygame.time.get_ticks()
       #If the shield appeared for 1 second
       if shieldTime - last_action_time >= 1000:
              blocked = False

    #If player did not get hit
    if playerGotHit == False:
        #If player touches the boss or stunned boss
        if player_rect.colliderect(bossRect) or player_rect.colliderect(bossStunned_rect):
            playerX += 200
            playerY -= 100
            playerGotHit = True
            playerHealth -= 10
        
        #If the sidekick is alive and player touches the sidekick
        if sidekickAlive and player_rect.colliderect(bossRect2):
              playerX += 200
              playerY -= 50
              playerHealth -= 5
              playerGotHit = True

        #If the player's X over or equal to 750
        if playerX >= 750:
              playerY = 700

    #If the player is not touching the boss
    if not (player_rect.colliderect(bossRect)):
        playerGotHit = False

    #If the small explosion has not exploded
    if exploding == False:
        #If the arrow or sword or boomerang touches the fireball
        if arrow_rect.colliderect(fireball_rect) or swordRect.colliderect(fireball_rect) and sword_swing or boomrng_rect.colliderect(fireball_rect) or player_rect.colliderect(fireball_rect):
            exploding = True
        
        #If the fireball touches the player
        if fireball_rect.colliderect(player_rect):
            playerHealth -= 5
            exploding = True
    #If the small explosion exploded
    else:
        fireballCollide()       #Function to create the small explosion
        bossShooting = False
        shooting = True

    #If the fire touches the player
    if fire_rect.colliderect(player_rect):
        playerHealth -= 0.5

def fireballCollide():
    global explosionCount, exploding, is_fired, shoot_arrow, bow_shoot, allow_angle, boomrng_hit, hit, boomrng_rect, swordRect
    #Create the explosion image and animation
    explosionImageUnscaled = pygame.image.load(f"fireball_collide/{explosionCount}.png").convert_alpha()
    explosionImage = pygame.transform.scale(explosionImageUnscaled, (100, 100))
    explosionCount += 1
    explosion_rect = explosionImage.get_rect(topleft=(fireball_rect.centerx, fireball_rect.centery))

    #If the player's weapon is the bow
    if weapon_choice == BOW:
        #Rearm the player with an arrow
        is_fired = False
        shoot_arrow = False
        bow_shoot = False
        allow_angle = True

    #If the explosion animation is finished
    if explosionCount == 5:
        explosionCount = 0
        exploding = False
        fireball_rect.center = (-1000, -1000)

        #If the player's weapon is a bow
        if weapon_choice == BOW:
            arrow_rect.center = (10000, 1000)

        #If the player's weapon is a sword
        elif weapon_choice == SWORD:
            #If the sword is swinging and is not hitting the boss and the sidekick is not hit
            if sword_swing and hit == False and not sidekickGotHit:
                hit = True
            
            else:
                hit = False
                swordRect.center = (1000, 1000)

        #If the player's weapon is a boomerang
        else:
            if boomrng_hit == False:
                boomrng_rect.center = (1000, 1000)
    #Draw the explosion image on screen
    SCREEN.blit(explosionImage, explosion_rect)

def bossDamaged():
    global new_width, new_height, dmg_animation_count, bossDmg, boss_damaged, boss_pos
    #Create the boss's damaged animation
    bossdmgUnsized = pygame.image.load(f"boss_damage/{dmg_animation_count}.png")
    dmg_animation_count += 1

    #If the animation is finished
    if dmg_animation_count == 4:
        dmg_animation_count = 0
        boss_damaged = False
    #Rescale the image
    bossDmg = pygame.transform.scale(bossdmgUnsized, (new_width, new_height))
    #Draw the boss's damaged animation image on screen
    SCREEN.blit(bossDmg, (bossX, bossY))


def playerAttack():
    #If the player's weapon is the sword
    if weapon_choice == SWORD:
        sword_attack()      #Function to swing the sword

    #If the player's weapon is the bow
    elif weapon_choice == BOW:
        bow_attack()        #Function to shoot an arrow

    #If the player's weapon is the boomerang
    else:
        boomrng_attack()    #Function to throw the boomerang

def sword_attack():
    global sword_swing
    #Set the variable sword_swing to true
    sword_swing = True

def bow_attack():
    global bow_shoot
    #Set the variable bow_shoot to true
    bow_shoot = True

def boomrng_attack():
    global boomrng_shoot
    #Set the variable boomrng_shoot to true
    boomrng_shoot = True

def leftAnimation():
    global animation_count, playerAnimation, playerRun, playerFlipped
    #Set the variable to true for other conditional statements to function
    playerAnimation = True

    #Create the player's walking animation and flip
    originalImage = pygame.image.load(f"animation/{animation_count}.png").convert_alpha()
    playerRun = pygame.transform.flip(originalImage, True, False)
    animation_count += 1

    #If the animation is finished, reset it
    if animation_count > 7:
        animation_count = 0

def rightAnimation():
    global animation_count, playerImage, playerAnimation, playerRun, playerFlipped
    #Set the variable to true for otehr conditional statements to function
    playerAnimation = True

    #Create the player's walking animation
    playerRun = pygame.image.load(f"animation/{animation_count}.png")
    animation_count += 1

    #If the animation is finished, reset it
    if animation_count > 7:
        animation_count = 0


def playerJump():
    global jumping, playerY, ground_y
    #If the player is on the ground and is not on the platform
    if playerY == ground_y and on_platform == False:
        jumping = True

def checkIfJumping():
    global jumping, playerY, vel_y, gravity, jump_height, falling, jump_speed, jump_count, ground_y

    #If the player is not on the paltform
    if on_platform == False:
        #If the player is jumping
        if jumping == True:
            #Minus the player's Y coordinates
            playerY -= jump_speed
            vel_y -= gravity

            #If the velocity is under the negative jump height
            if vel_y < -jump_height:
                jumping = False
                vel_y = jump_height

        #If jumping is false
        else:
            #Set the falling to be true
            falling = True

            #If the player is falling
            if falling == True:
                playerY += gravity + 20

                #If the player's Y coordinates is more or equal to the ground's Y coordinates 
                if playerY >= ground_y:
                    playerY = ground_y
                    falling = False

def checkCollisions():
    global playerX
    #If the player's X coordinates is over or equal to 723
    if playerX >= 723:
        playerX = 723
    
    #If the player's X coordinates is under or equal to 10
    if playerX <= -10:
        playerX = -10

def drawHealthBar():
    #Set the font for the player's health bar's text
    #Create the player's health bar
    font = pygame.font.SysFont("Georgia", 20)
    pygame.draw.rect(SCREEN, BLACK, (30, 45, 200, 30))
    pygame.draw.rect(SCREEN, RED, (30, 45, playerHealth * 2, 30)) 
    pygame.draw.rect(SCREEN, BLACK, (30, 45, 200, 30), 4) 
    text_surface = font.render("Your Health", True, WHITE)
    SCREEN.blit(text_surface, (33, 20))

    #Create the boss's health bar
    #Set the font for the boss's health bar's text
    pygame.draw.rect(SCREEN, RED, (570, 45, 200, 30)) 
    pygame.draw.rect(SCREEN, BLACK, (570, 45, 200, 30), 4)
    text_surface = font.render("Boss Health", True, WHITE)
    SCREEN.blit(text_surface, (655, 20))

    #Show player hitbox during battle
    #pygame.draw.rect(SCREEN, GREEN, player_rect, 3)

def bossIdle():
    global new_width, new_height, boss_animation_count, bossFly, boss_damaged, boss_pos, bossX, bossY, bossImage_rect, bossRect
    #If the boss is going back
    if boss_going_back == True:
        return
    
    #Create the boss's idle animation image
    bossFlyUnsized = pygame.image.load(f"boss_idle/{boss_animation_count}.png")
    boss_animation_count += 1
    
    #If the animation is finished, reset it
    if boss_animation_count == 12:
        boss_animation_count = 0

    bossFly = pygame.Surface((new_width, new_height))
    bossRect = bossFly.get_rect(topleft=boss_pos)
    
    bossRect.topleft = boss_pos

    #Draw boss hitbox
    #pygame.draw.rect(SCREEN, (0, 255, 0), bossRect, 2)

    bossFly = pygame.transform.scale(bossFlyUnsized, (new_width, new_height))
    #If boss is not damaged from the player and the boss is not attacking and the boss is not going back from attacking
    if boss_damaged == False and attacking == False and boss_going_back == False and attackQuantity == 0:
        boss_animation_count = 0
        #Create the boss's flying animation
        SCREEN.blit(bossFly, (boss_pos))

def checkCursor():
    global mouse_pos, button_rect, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_CLICK_COLOR, button_width, button_height, button_hover, font_size, button_x, button_y, WEAPON_BUTTON_COLOR
    #Get the mouse's position
    mouse_pos = pygame.mouse.get_pos()
    #If the cursor is overlapping the button
    if button_rect.collidepoint(mouse_pos):
        #Set the cursor to a hand
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        #If the button's color is not the button's click color
        if BUTTON_COLOR != BUTTON_CLICK_COLOR:
            BUTTON_COLOR = BUTTON_HOVER_COLOR
            button_hover += 1
            if button_hover == 1:
                button_width += 30
                button_height += 30
                font_size += 10
                button_x -= 15
                button_y -= 15
        
        #If the weapon's button color is not the button's click color
        if WEAPON_BUTTON_COLOR != BUTTON_CLICK_COLOR:
            button_hover = 1
            if button_hover == 1:
                WEAPON_BUTTON_COLOR = BUTTON_HOVER_COLOR
    
    #If the mouse's position is not overlapping the button
    else:
        #Set the cursor to an arrow
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
    #Get the mouse's position
    mouse_pos = pygame.mouse.get_pos()

    #If the cursor is overlapping the bow button
    if bow_button_rect.collidepoint(mouse_pos):
        #Set the cursor to a hand
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        #If the button's color is not the click color
        if BOW_BUTTON_COLOR != BUTTON_CLICK_COLOR:
            button_hover = 1
            if button_hover == 1:
                BOW_BUTTON_COLOR = BUTTON_HOVER_COLOR
    
    #If the cursor is not overlapping the bow button
    else:
        BOW_BUTTON_COLOR = RED
        button_hover = 0

def checkBoomrngHovered():
    global boomrng_button_rect, BOOMRNG_BUTTON_COLOR, BUTTON_CLICK_COLOR, BUTTON_HOVER_COLOR, button_hover
    #Get the mouse's position
    mouse_pos = pygame.mouse.get_pos()

    #If the cursor is overlapping the boomerang button
    if boomrng_button_rect.collidepoint(mouse_pos):
        #Set the cursor to a hand
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        #If the button's color is not the click color
        if BOOMRNG_BUTTON_COLOR != BUTTON_CLICK_COLOR:
            button_hover = 1
            if button_hover == 1:
                BOOMRNG_BUTTON_COLOR = BUTTON_HOVER_COLOR
    #If the cursor is not overlapping the boomerang button
    else:
        #Set the cursor to an arrow
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        BOOMRNG_BUTTON_COLOR = RED
        button_hover = 0

def sword_choice():
    global sword_swing, rotation_speed, added_y, swordImageUnrotated, swordRect, player_rect, playerX, playerY, bossY, playerFlipped
    global sword_sound, sound
    #Get the player's and hitbox's position
    player_pos = (playerX, playerY)
    player_rect = playerImage.get_rect(center=player_pos)
    player_rect.topleft = (playerX, playerY)
    
    #Get the sword image
    swordImageUnrotated = pygame.image.load("sword.png").convert_alpha()

    #If player is not flipped
    if playerFlipped == False:
        #Create the sword tilting right
        swordRect = pygame.Rect(player_rect.centerx + 67, player_rect.centery - 70, 25, 10)
    
    #If player is flipped
    else:
        #Create the sword tilting left
        swordRect = pygame.Rect(player_rect.centerx - 67, player_rect.centery - 70, 25, 10)

    #If player is not flipped
    if playerFlipped == False:
        #If the sword is swinging
        if sword_swing == True:
            sword_top_offset_x = 50
            sword_top_offset_y = -40

            #Create the sword's hitbox
            swordRect = pygame.Rect(player_rect.centerx + sword_top_offset_x, player_rect.centery + sword_top_offset_y, 100, 25)

    #If player is flipped
    else:
        #If the sword is swinging
        if sword_swing == True:
            sword_top_offset_x = -125
            sword_top_offset_y = -40
            
            #Create the sword's hitbox
            swordRect = pygame.Rect(player_rect.centerx + sword_top_offset_x, player_rect.centery + sword_top_offset_y, 100, 25)

    #pygame.draw.rect(SCREEN, (255, 0, 0, 50), swordRect, 25)

    #If player is not flipped
    if playerFlipped == False:
        #Rotate the sword's image
        swordImage = pygame.transform.rotate(swordImageUnrotated, -25)

        #If sword is not swinging
        if sword_swing == False:
            #Draw the sword out
            SCREEN.blit(swordImage, (playerX + 5, playerY - 60))

        #If the sword is swinging
        else:
            if sound == 0:
                #Play the sword swinging sound
                sword_sound.play()
                sound = 1
            #Rotate the sword's image
            swordImage = pygame.transform.rotate(swordImageUnrotated, -rotation_speed)
            rotation_speed += 25

            #If the rotation speed is more than or equal to 130
            if rotation_speed >= 130:
                sword_swing = False
                rotation_speed = 0
                added_y = 0
                sound = 0

            #Draw the sword swinging image
            SCREEN.blit(swordImage, (playerX, playerY + added_y))

            added_y += 0.5
    #If the player is flipped
    else:
        #Rotate the sword image
        swordImage = pygame.transform.rotate(swordImageUnrotated, 25)

        #If the sword is not swinging
        if sword_swing == False:
            #Draw the sword
            SCREEN.blit(swordImage, (playerX - 70, playerY - 60))

        #If the sword is swinging
        else:
            if sound == 0:
                #Play the sword swinging sound
                sword_sound.play()
                sound = 1
            #Rotate the sword
            swordImage = pygame.transform.rotate(swordImageUnrotated, rotation_speed)
            rotation_speed += 25
            
            #If the rotation speed is more than or equal to 130
            if rotation_speed >= 130:
                sword_swing = False
                rotation_speed = 0
                added_y = 0
                sound = 0
            
            #Draw the swinging sword image
            SCREEN.blit(swordImage, (playerX - 100, playerY + added_y))

            added_y += 0.5

def bow_choice():
    global player_rect, bow_number, bow_shoot, shoot_arrow, angle, angle_degrees, arrow_angle, allow_angle, mouse_x, mouse_y, arrow_x_speed, arrow_y_speed, is_fired, arrowX, arrowY
    global sound, arrow_sound
    #Get the player's and hitbox's position
    player_pos = (playerX, playerY)
    player_rect = playerImage.get_rect(center=player_pos)
    player_rect.topleft = (playerX, playerY)

    #Get the mouse positions
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #Get the hypoteneuse of the cursor and the bow
    dx = mouse_x - player_rect.centerx
    dy = mouse_y - player_rect.centery
    angle_radians = math.atan2(-dy, dx)
    angle_degrees = math.degrees(angle_radians)

    #If bow is not shooting
    if bow_shoot == False:
        #Create the bow image and rotate it towards the mouse's position
        angle = angle_degrees - 90
        bowImageUnchanged = pygame.image.load("bow.png")
        bowImageUnrotated = pygame.transform.scale(bowImageUnchanged, (100, 100))
        bowImage = pygame.transform.rotate(bowImageUnrotated, angle + 100)

    #If bow is shooting
    else:
        #If the arrow is not shot yet
        if shoot_arrow == False:
            sound = 0
            angle = angle_degrees - 90
            #Animate the bow for shooting
            bowImageUnchanged = pygame.image.load(f"bow_shoot/{bow_number}.png").convert_alpha()
            bowImageUnrotated = pygame.transform.scale(bowImageUnchanged, (100, 100))
            bowImage = pygame.transform.rotate(bowImageUnrotated, angle + 100)
            bow_number += 1

            #If the animation is finished, shoot the arrow
            if bow_number == 11:
                bow_shoot = False
                shoot_arrow = True
                bow_number = 0

    #If the arrow is shot
    if shoot_arrow == True:
        if sound == 0:
            #Play the shooting sound
            arrow_sound.play()
            sound = 1
        
        #Create the empty bow image while rotating it towards the mouse
        angle = angle_degrees - 90
        bowImageUnchanged = pygame.image.load("bow_shoot/10.png").convert_alpha()
        bowImageUnrotated = pygame.transform.scale(bowImageUnchanged, (100, 100))
        bowImage = pygame.transform.rotate(bowImageUnrotated, angle + 100)

        #If the arrow can change it's angle
        if allow_angle == True:
            #Get the mouse's position 
            #Move the arrow towards the mouse's shooting position
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
    global instructions, sound

    if keys[pygame.K_SPACE]:
        if sound == 0:
            sound = 1
            click_sound.play()
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