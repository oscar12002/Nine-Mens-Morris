import pygame

class Files(pygame.sprite.Sprite):
    def __init__(self, file_image, first_pos_x):
        pygame.sprite.Sprite.__init__(self)
        
        self.first_pos_x = first_pos_x #position in x where the files will be drawing the first time
        
        self.image_file = pygame.image.load(file_image)
        self.image_file = pygame.transform.scale(self.image_file, (35, 35))
        
        self.file_quantly = 9
        
        self.file_list = []
    
    
    def make_files(self):
        posY = 210
        for i in range(self.file_quantly):
            file_rect = self.image_file.get_rect(center=(self.first_pos_x, posY))
            # the array in thirth position store a number to know then this file is in a mill
            # the array in fourth position is changed for a number to identify the three files that are in the same mill
            self.file_list.append([self.image_file, file_rect, [], []])
            posY += 40
    
    
    def move(self, file_of_list, instace_of_list):
        file_of_list[1].center = instace_of_list[1].center
    
    
    def draw(self, screem):
        for e in range(len(self.file_list)):
            if self.file_list[e]:
                screem.blit(self.file_list[e][0], self.file_list[e][1])