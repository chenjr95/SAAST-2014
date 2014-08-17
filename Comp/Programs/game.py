'''
    # Game loop
    while True:
        #update game state
        # draw game to screen

    Model-view-controller
      ^     ^     ^
      ^     ^     ^
     sims   ^    input
           graphics

PyGame - provide a bunch of common classes for quickly prototyping games
'''
import pygame

WIDTH = 1024
HEIGHT = 768

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.displya.set_caption('Pong!')

    while True:
        update()                 # Update the model
        render()                 # Draw the model
        pygame.display.update()  # Pygame: "update yourself"


main()
