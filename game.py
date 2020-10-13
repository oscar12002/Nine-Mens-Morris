import pygame

class Game:
    def __init__(self, player_one, player_two, screem):
        self.player_one = player_one
        self.player_two = player_two
        
        self.file_black = pygame.image.load("images/black_file.png")
        self.file_black = pygame.transform.scale(self.file_black, (35, 35))
        
        self.file_white = pygame.image.load("images/white_file.png")
        self.file_white = pygame.transform.scale(self.file_white, (35, 35))
        
        self.background = pygame.image.load("images/background.jpg")
        
        
        self.mouse_pos_x = 0
        self.mouse_pos_y = 0
        
        self.screem = screem


    def __get_click_position(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_pos_x = pygame.mouse.get_pos()[0]
            self.mouse_pos_y = pygame.mouse.get_pos()[1]


    def __verify_position(self, event):
        self.__get_click_position(event)
        for white_file in self.player_one.list_of_files:
            if white_file != []:
                if white_file[1].collidepoint(self.mouse_pos_x, self.mouse_pos_y):
                    return False
                
        for black_file in self.player_two.list_of_files:  
            if black_file != []:
                if black_file[1].collidepoint(self.mouse_pos_x, self.mouse_pos_y):
                    return False
                
        return True

    def __select_file_to_delete(self, event, player, player_me):
        self.__get_click_position(event)

        player_me.boolean_verify = False
        for i in range(len(player.list_of_files)):
            if player.list_of_files[i] != []:
                if player.list_of_files[i][1].collidepoint(self.mouse_pos_x, self.mouse_pos_y):
                    # if not player.list_of_files[i][2]:
                        player.list_of_files[i] = []                    
                        
                        player_me.boolean_verify = True
                        
                        player_me.transport_mills[0][2].append(1)
                        player_me.transport_mills[1][2].append(1)
                        player_me.transport_mills[2][2].append(1)
                        
                        player.file_limited -= 1
                        
                        if (self.player_one.cont_turn_put_file < self.player_one.my_files.file_quantly) or (self.player_two.cont_turn_put_file < self.player_two.my_files.file_quantly):
                            self.player_one.cont_turn_put_file = self.player_one.turn_put_file
                        else:
                            self.player_one.cont_turn_move_file = self.player_one.turn_move_file
                        break


    def __turn_put_file(self, event):
        if self.player_one.cont_turn_put_file == self.player_two.cont_turn_put_file:
            
            self.__print_turn_player(self.file_white)
            
            self.player_one.put_file(event, self.__verify_position(event), self.mouse_pos_x, self.mouse_pos_y)            
            
            if self.player_one.eliminate():
                self.__eliminate_indication()
                self.__select_file_to_delete(event, self.player_two, self.player_one)
            else:
                self.player_one.cont_turn_put_file = self.player_one.turn_put_file
            
        elif self.player_one.cont_turn_put_file > self.player_two.cont_turn_put_file:
            
            self.__print_turn_player(self.file_black)
            
            self.player_two.put_file(event, self.__verify_position(event), self.mouse_pos_x, self.mouse_pos_y)
            
            if self.player_two.eliminate():
                self.__eliminate_indication()
                self.__select_file_to_delete(event, self.player_one, self.player_two)
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
                    self.__eliminate_indication()
                    self.__select_file_to_delete(event, self.player_two, self.player_one)
                else:
                    self.player_one.cont_turn_move_file = self.player_one.turn_move_file
            
        elif self.player_one.cont_turn_move_file > self.player_two.cont_turn_move_file:
            self.__get_click_position(event)
            
            self.__print_turn_player(self.file_black)
            
            self.player_two.select_file(event, self.mouse_pos_x, self.mouse_pos_y)
            
            if self.player_two.file_select_to_move != []:
                
                self.player_two.move_file(event, self.__verify_position(event), self.mouse_pos_x, self.mouse_pos_y)
                
                if self.player_two.eliminate():
                    self.__eliminate_indication()
                    self.__select_file_to_delete(event, self.player_one, self.player_two)
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
    
    def __eliminate_indication(self):
        font = pygame.font.Font(None, 45)
        text_player = font.render("select file to eliminate", 0, (0, 0, 255))
        
        self.screem.blit(text_player, (160, 650))
    
    def __last_scene(self, winner):
        self.screem.blit(self.background, (0, 0))
        
        font = pygame.font.Font(None, 50)
        text_end = font.render("THE GAME FINISHED", 0, (255, 255, 25))
        
        text_player = font.render(winner, 0, (0, 0, 0))
        
        self.screem.blit(text_end, (130, 100))
        
        self.screem.blit(text_player, (170, 250))
    
    
    def start(self, event):
        if (self.player_one.cont_turn_put_file < self.player_one.my_files.file_quantly) or (self.player_two.cont_turn_put_file < self.player_two.my_files.file_quantly):
            self.__print_instructions("Set your file on the board", 140)       
            self.__turn_put_file(event)
            
        else:
            self.__print_instructions("Move your file to create a Mill", 110)
            self.__turn_move_file(event)
        # when a player has 2 files the game end
        if self.player_one.file_limited == 2:
            self.__last_scene("PLAYER 2 WIM")
            
        elif self.player_two.file_limited == 2:
            self.__last_scene("PLAYER 1 WIM")