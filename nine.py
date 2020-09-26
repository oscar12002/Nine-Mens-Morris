import pygame
import sys
import time
import random
from pygame.locals import *


class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image_board = pygame.image.load("images/tab.jpg")
        self.position_list = []
    
    
    def make_instances(self):
        circle_instance = pygame.image.load("images/instance.png")
        
        # first and last file
        posx = 150
        posy = 200
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [175], []])
            posx += 175
        self.position_list[1][2].append(50)
        
        posx = 150
        posy = 550
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [175], []])
            posx += 175
        self.position_list[4][2].append(50)
        
        # second en sixth file
        posx = 200
        posy = 250
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [125], []])
            posx += 125
        self.position_list[7][2].append(50)
        
        posx = 200
        posy = 500
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [125], []])
            posx += 125
        self.position_list[10][2].append(50)
        
        # thirth and fifth file
        posx = 250
        posy = 300
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [75], []])
            posx += 75
        self.position_list[13][2].append(50)
        
        posx = 250
        posy = 450
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [75], []])
            posx += 75
        self.position_list[16][2].append(50)
        
        # midle file
        posx = 150
        posy = 375
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [50], []])
            posx += 50
        self.position_list[18][2].append(175)
        
        self.position_list[19][2].append(125)
        
        self.position_list[20][2].append(75)
        
        posx = 400
        posy = 375
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [50], []])
            posx += 50
        self.position_list[21][2].append(75)
        
        self.position_list[22][2].append(125)
        
        self.position_list[23][2].append(175)
    
    
    def draw(self, screem):
        screem.blit(self.image_board, (150, 200))
        
        for i in range(len(self.position_list)):
            screem.blit(self.position_list[i][0], self.position_list[i][1])


class Files(pygame.sprite.Sprite):
    def __init__(self, file_image, first_pos_x):
        pygame.sprite.Sprite.__init__(self)
        
        self.first_pos_x = first_pos_x
        
        self.image_file = pygame.image.load(file_image)
        self.image_file = pygame.transform.scale(self.image_file, (35, 35))
        
        self.file_quantly = 4
        
        self.file_list = []
    
    
    def make_files(self):
        posY = 210
        for i in range(self.file_quantly):
            file_rect = self.image_file.get_rect(center=(self.first_pos_x, posY))
            self.file_list.append([self.image_file, file_rect, []])
            posY += 40
    
    
    def move(self, file_of_list, instace_of_list):
        file_of_list[1].center = instace_of_list[1].center
    
    def delete(self, file, list_of_file):
        list_of_file.remove(file)
        
    
    def draw(self, screem):
        for e in range(len(self.file_list)):
            if self.file_list[e]:
                screem.blit(self.file_list[e][0], self.file_list[e][1])


class Player(pygame.sprite.Sprite):
    def __init__(self, list_of_instances, file_object, screem):
        pygame.sprite.Sprite.__init__(self)
        
        self.screem = screem
        
        self.my_files = file_object
        
        self.list_of_instances = list_of_instances
        
        self.list_of_files = self.my_files.file_list
        
        self.cont_turn_put_file = 0
        self.turn_put_file = 0
        
        self.cont_turn_move_file = 0
        self.turn_move_file = 0
        
        self.file_select_to_move = []
        self.position_from_file_select = []
        
        self.content_mills = []
        self.content_mills_position = []
        
        self.cont_files = 9
        self.cont_files_2 = 9
        
        self.indice = True
        
        self.klk = 0
    

    def eliminate(self):
        matr = [[(150, 200), (325, 200), (500, 200)],
                [(200, 250), (325, 250), (450, 250)],
                [(250, 300), (325, 300), (400, 300)],
                [(150, 375), (200, 375), (250, 375)],
                [(400, 375), (450, 375), (500, 375)],
                [(250, 450), (325, 450), (400, 450)],
                [(200, 500), (325, 500), (450, 500)],
                [(150, 550), (325, 550), (500, 550)],
                
                [(150, 200), (150, 375), (150, 550)],
                [(200, 250), (200, 375), (200, 500)],
                [(250, 300), (250, 375), (250, 450)],
                [(325, 200), (325, 250), (325, 300)],
                [(325, 450), (325, 500), (325, 550)],
                [(400, 300), (400, 375), (400, 450)],
                [(450, 250), (450, 375), (450, 500)],
                [(500, 200), (500, 375), (500, 550)]]
        
        for first_file in self.list_of_files:
            for second_file in self.list_of_files:
                for thirth_file in self.list_of_files:
                    if first_file != second_file and first_file != thirth_file and second_file != thirth_file:
                        self.content_mills.append([first_file, second_file, thirth_file])
                        self.content_mills_position.append([first_file[1].center, second_file[1].center, thirth_file[1].center])

        for e in range(len(self.content_mills_position)):
            for confirm in matr:
                if self.content_mills_position[e] == confirm:
                    if self.content_mills[e][0][2] != [1] and self.content_mills[e][1][2] != [1] and self.content_mills[e][2][2] != [1]:
                        self.indice = self.content_mills[e]
                        return True
    
    
    def put_file(self, event, position_verify, x, y):
        if event.type == pygame.MOUSEBUTTONDOWN:
            file = self.list_of_files[self.turn_put_file - self.klk]
            for instance in self.list_of_instances:
                if instance[1].collidepoint(x, y):
                    
                    if position_verify:
                        self.my_files.move(file, instance)
                        
                        self.turn_put_file += 1                    
                        break            
    
    
    def select_file(self, event, x, y):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for file_select in self.list_of_files:
                if file_select[1].collidepoint(x, y):
                    self.file_select_to_move = file_select                                                                
                    
                    for instance in self.list_of_instances:
                        if instance[1].collidepoint(x, y):
                            self.position_from_file_select = [instance[1].x, instance[1].y, instance]
                            break
                    break
    
    
    def __move_restrintion(self, instance, x, y):
        for position_aviable in instance[2]:
            if self.position_from_file_select[0] + position_aviable == x or self.position_from_file_select[0] - position_aviable == x:
                if self.position_from_file_select[1] == y:
                    return True
                
            elif self.position_from_file_select[1] + position_aviable == y or self.position_from_file_select[1] - position_aviable == y: 
                if self.position_from_file_select[0] == x:
                    return True
                
        return False
    
    
    def move_file(self, event, position_verify, x, y):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for instance in self.list_of_instances:
                if instance[1].collidepoint(x, y):
                    if self.__move_restrintion(instance, instance[1].x, instance[1].y):
                        if position_verify:
                            self.my_files.move(self.file_select_to_move, instance)
                            self.turn_move_file += 1
                            
                            self.file_select_to_move = []
                            self.position_from_file_select = []
                            break


class Game:
    def __init__(self, player_one, player_two, screem):
        self.player_one = player_one
        self.player_two = player_two
        
        self.file_black = pygame.image.load("images/black_file.png")
        self.file_black = pygame.transform.scale(self.file_black, (35, 35))
        
        self.file_white = pygame.image.load("images/white_file.png")
        self.file_white = pygame.transform.scale(self.file_white, (35, 35))
        
        
        self.mouse_pos_x = 0
        self.mouse_pos_y = 0
        
        self.screem = screem

        self.almacen = 0

    def __get_click_position(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_pos_x = pygame.mouse.get_pos()[0]
            self.mouse_pos_y = pygame.mouse.get_pos()[1]


    def __verify_position(self, event):
        self.__get_click_position(event)
        for white_file in self.player_one.list_of_files:
            if white_file[1].collidepoint(self.mouse_pos_x, self.mouse_pos_y):
                return False
                
        for black_file in self.player_two.list_of_files:                
            if black_file[1].collidepoint(self.mouse_pos_x, self.mouse_pos_y):
                return False
                
        return True

    def select_file(self, event, player, player_me):
        self.__get_click_position(event)
        
        for file in player.list_of_files:
            if file[1].collidepoint(self.mouse_pos_x, self.mouse_pos_y):
                if file[2] != [1]:
                    player.list_of_files.remove(file)                    
                    
                    player_me.indice[0][2] = [1]
                    player_me.indice[1][2] = [1]
                    player_me.indice[2][2] = [1]
                    
                    player.klk += 1
                    
                    if (self.player_one.cont_turn_put_file < 4) or (self.player_two.cont_turn_put_file < 4):
                        self.player_one.cont_turn_put_file = self.player_one.turn_put_file
                    else:
                        self.player_one.cont_turn_move_file = self.player_one.turn_move_file
                    break


    def __turn_put_file(self, event):
        if self.player_one.cont_turn_put_file == self.player_two.cont_turn_put_file:
            
            self.__print_turn_player(self.file_white)
            
            self.player_one.put_file(event, self.__verify_position(event), self.mouse_pos_x, self.mouse_pos_y)            
            
            if self.player_one.eliminate():
                self.select_file(event, self.player_two, self.player_one)
            else:
                self.player_one.cont_turn_put_file = self.player_one.turn_put_file
            
        elif self.player_one.cont_turn_put_file > self.player_two.cont_turn_put_file:
            
            self.__print_turn_player(self.file_black)
            
            self.player_two.put_file(event, self.__verify_position(event), self.mouse_pos_x, self.mouse_pos_y)
            
            if self.player_two.eliminate():
                self.select_file(event, self.player_one, self.player_two)
            else:
                self.player_two.cont_turn_put_file = self.player_two.turn_put_file


    def __turn_move_file(self, event):
        if self.player_one.cont_turn_move_file == self.player_two.cont_turn_move_file:
            self.__get_click_position(event)
            
            self.__print_turn_player(self.file_white)
            
            self.player_one.select_file(event, self.mouse_pos_x, self.mouse_pos_y)                
            
            if self.player_one.file_select_to_move != []:
                
                self.player_one.move_file(event, self.__verify_position(event), self.mouse_pos_x, self.mouse_pos_y)
                
                if self.player_one.eliminate():
                    self.select_file(event, self.player_two, self.player_one)
                else:
                    self.player_one.cont_turn_move_file = self.player_one.turn_move_file
            
        elif self.player_one.cont_turn_move_file > self.player_two.cont_turn_move_file:
            self.__get_click_position(event)
            
            self.__print_turn_player(self.file_black)
            
            self.player_two.select_file(event, self.mouse_pos_x, self.mouse_pos_y)
            
            if self.player_two.file_select_to_move != []:
                
                self.player_two.move_file(event, self.__verify_position(event), self.mouse_pos_x, self.mouse_pos_y)
                
                if self.player_two.eliminate():
                    self.select_file(event, self.player_one, self.player_two)
                else:
                    self.player_two.cont_turn_move_file = self.player_two.turn_move_file
    
    
    def __print_turn_player(self, file):
        font = pygame.font.Font(None, 50)
        text_player = font.render("Turn", 0, (255, 255, 255))
        
        pygame.draw.rect(self.screem, (0, 0, 0), [160, 585, 330, 60], 1)
        ret = pygame.Surface((330, 60))
        ret.set_alpha(100)
        ret.fill((0, 0, 0))
        self.screem.blit(ret, (160, 585))
        
        self.screem.blit(text_player, (245, 600))
        self.screem.blit(file, (360, 600))
        
        
    def __print_instructions(self, text, x):
        font = pygame.font.Font(None, 45)
        text_player = font.render(text, 0, (255, 255, 255))
        
        self.screem.blit(text_player, (x, 120))
    
    
    def start(self, event):
        if (self.player_one.cont_turn_put_file < 4) or (self.player_two.cont_turn_put_file < 4):
            self.__print_instructions("Set your file on the board", 140)       
            self.__turn_put_file(event)
            
            
        else:
            self.__print_instructions("Move your file to create a Mill", 110)
            self.__turn_move_file(event)


def close():
    pygame.quit()
    sys.exit()

screem = pygame.display.set_mode((650, 700))
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



