import pygame

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
            self.position_list.append([circle_instance, pos_rect, [175]]) #the list in thirth position has each one of positions i can move
            posx += 175
        self.position_list[1][2].append(50) #here add more positions aviables
        
        posx = 150
        posy = 550
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [175]])
            posx += 175
        self.position_list[4][2].append(50)
        
        # second en sixth file
        posx = 200
        posy = 250
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [125]])
            posx += 125
        self.position_list[7][2].append(50)
        
        posx = 200
        posy = 500
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [125]])
            posx += 125
        self.position_list[10][2].append(50)
        
        # thirth and fifth file
        posx = 250
        posy = 300
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [75]])
            posx += 75
        self.position_list[13][2].append(50)
        
        posx = 250
        posy = 450
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [75]])
            posx += 75
        self.position_list[16][2].append(50)
        
        # midle file
        posx = 150
        posy = 375
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [50]])
            posx += 50
        self.position_list[18][2].append(175)
        
        self.position_list[19][2].append(125)
        
        self.position_list[20][2].append(75)
        
        posx = 400
        posy = 375
        for e in range(3):
            pos_rect = circle_instance.get_rect(center=(posx, posy))
            self.position_list.append([circle_instance, pos_rect, [50]])
            posx += 50
        self.position_list[21][2].append(75)
        
        self.position_list[22][2].append(125)
        
        self.position_list[23][2].append(175)
    
    
    def draw(self, screem):
        screem.blit(self.image_board, (150, 200))
        
        for i in range(len(self.position_list)):
            screem.blit(self.position_list[i][0], self.position_list[i][1])