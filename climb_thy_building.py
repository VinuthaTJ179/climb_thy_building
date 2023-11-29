import pygame
import sys
import time
import button
# Initialize Pygame
pygame.init()

# Set the dimensions of your screen
screen_width = 1920
screen_height = 1080

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Text and Image Animation")

start_img = pygame.image.load("C:\\Users\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\start_img.png").convert_alpha()
exit_img = pygame.image.load("C:\\Users\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\exit_img.png").convert_alpha()


# Creating a player**************************************************************************
class Player():
    def __init__(self, x, y):
        img = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\guy-removebg-preview.png")
        self.image = pygame.transform.scale(img, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Draw player onto screen
        screen.blit(self.image, self.rect)


#Create button instances

start_button = button.Button(840,450,start_img,0.8)
exit_button = button.Button(855,600,exit_img,0.8)

# Load the images
splash_image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\cityskyline.png")
second_screen_image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\bluemoon.png")

x, y = 0, 0

# Define a font and initial text
font = pygame.font.Font("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\pixelmix.ttf", 60)  # None uses the default system font
text_color = (255, 255, 255)  # White, in (R, G, B) format
text = "Hello, Pygame!"
text_surface = font.render('', True, text_color)

# Calculate the position to place the text at the center of the screen
text_x = 610
text_y = 500

# *********************************************************************************
SPLASH_SCREEN = 0
SECOND_SCREEN = 1
current_state = SPLASH_SCREEN

# Timer to control the splash screen duration
transition_duration = 5000  # Duration of the transition in milliseconds (5 seconds)
start_time = pygame.time.get_ticks()
alpha = 255  # Initial alpha value for fading (fully opaque)
fade_speed = 2

# *********************************************************************************

# Initialize variables for the animation
animation_text = "Climb thy building"
animation_speed = 7  # Number of letters displayed per second
current_letter_index = 0
time_last_letter_displayed = time.time()



# ****************************************************************
def start_platformer_game(screen):
    # screen_width = 1920  # No need to redefine screen dimensions here
    # screen_height = 1080

    # screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    # load images
    bg_img = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\sunnyday.png")

    grid_size = 100

    def draw_grid():
        # Set the grid parameters
        grid_size = 100  # Adjust this value to change the grid cell size
        grid_color = (255, 255, 255)  # White color for the grid lines
        # Draw horizontal lines
        for y in range(0, screen_height, grid_size):
            pygame.draw.line(screen, grid_color, (0, y), (screen_width, y))

        # Draw vertical lines
        for x in range(0, screen_width, grid_size):
            pygame.draw.line(screen, grid_color, (x, 0), (x, screen_height))

        # Update the display
        pygame.display.flip()

    class World():
        def __init__(self, data):
            self.tile_list = []
            # load images
            building1 = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\dirt1.jpg")
            building2 = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\dirt2.jpg")
            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(building1, (grid_size, grid_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * grid_size
                        img_rect.y = row_count * grid_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    elif tile == 2:
                        img = pygame.transform.scale(building2, (grid_size, grid_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * grid_size
                        img_rect.y = row_count * grid_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
            
    world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

       
    world = World(world_data)
    player = Player(180,700)
    #player = Player(100,screen_height - 130)

    running = True

    while running:
        screen.fill((0,0,0))

        screen.blit(bg_img,(0,0))

        world.draw()

        draw_grid()
        
        player.update()

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

    pygame.quit()
#******************************************************




# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    if current_state == SPLASH_SCREEN:
        # Clear the screen
        screen.fill((0, 0, 0))  # Black background
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= transition_duration:
            current_state = SECOND_SCREEN
        # Blit (draw) the image onto the screen
        screen.blit(splash_image, (x, y))

        # Calculate the time since the last letter was displayed
        time_now = time.time()
        time_since_last_display = time_now - time_last_letter_displayed

        # Display the letters one by one with the defined animation speed
        if current_letter_index < len(animation_text) and time_since_last_display >= 1 / animation_speed:
            text_surface = font.render(animation_text[:current_letter_index + 1], True, text_color)
            time_last_letter_displayed = time_now
            current_letter_index += 1

        # Blit (draw) the text surface at the center of the screen
        screen.blit(text_surface, (text_x, text_y))
    elif current_state == SECOND_SCREEN:
        screen.fill((0, 0, 0))  # Black background

        # Blit (draw) the second screen image
        screen.blit(second_screen_image, (x, y))
        if start_button.draw(screen) == True:
            print('START')
            start_platformer_game(screen)
        if exit_button.draw(screen) == True:
            running = False

        if alpha > 0:
            overlay = pygame.Surface((screen_width, screen_height))
            overlay.set_alpha(alpha)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            alpha = max(0, alpha - fade_speed)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
