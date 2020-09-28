import pygame
import sys

from pygame.locals import *

from board import Board
from file import Files
from player import Player
from game import Game


screem = pygame.display.set_mode((650, 700))

def close():
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    
    pygame.display.set_caption("Nine Mens Morris")
    background_image = pygame.image.load("images/background.jpg")
    
    tab = Board()
    tab.make_instances()
    
    file_player_one = Files("images/white_file.png", 40)
    file_player_two = Files("images/black_file.png", 610)
    
    player_one = Player(tab.position_list, file_player_one, screem)
    player_two = Player(tab.position_list, file_player_two, screem)
    
    game = Game(player_one, player_two, screem)
    
    
    file_player_one.make_files()
    file_player_two.make_files()
    
    
    while True:
        screem.blit(background_image, (0,0))
        tab.draw(screem)
        file_player_one.draw(screem)
        file_player_two.draw(screem)
        
        event = pygame.event.wait()
        if event.type == QUIT:
            close()
        
        game.start(event)

        pygame.display.update()


if __name__ == '__main__':
    main()



