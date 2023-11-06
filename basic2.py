import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("My Pygame Image")

# Load the image
image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\pygame\\sunnyday.png")

# Set the initial position of the image
x, y = 0,0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Handle user input or game logic here

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with a black background

    # Blit the image onto the screen
    screen.blit(image, (x, y))

    # Update the display
    pygame.display.update()

# Clean up and quit
pygame.quit()
sys.exit()
