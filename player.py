import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, list_of_instances, file_object, screem):
        pygame.sprite.Sprite.__init__(self)
        
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
        
        self.transport_mills = []
        
        self.rest_num_to_file = 0
        
        self.file_limited = 9
        
        self.boolean_verify = True
        
        self.quit_mills = []
        
        self.cont = 0
    

    def eliminate(self):
        # matrix have all positions where can had a mill
        matrix = [[(150, 200), (325, 200), (500, 200)],
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
        
        
        # this for combine all the files positions and they are stored in "content_mills"
        for first_file in self.list_of_files:
            for second_file in self.list_of_files:
                for thirth_file in self.list_of_files:
                    if first_file != second_file and first_file != thirth_file and second_file != thirth_file:
                        if first_file != [] and second_file != [] and thirth_file != []:
                            self.content_mills.append([first_file, second_file, thirth_file])
                            self.content_mills_position.append([first_file[1].center, second_file[1].center, thirth_file[1].center])

        # in this for id compared all the positions from "matrix" with all the combinations from "content_mills"
        for e in range(len(self.content_mills_position)):
            for confirm in matrix:
                if self.content_mills_position[e] == confirm:
                    #if at least the thirth position of one of mills is empty
                    if not self.content_mills[e][0][2] or not self.content_mills[e][1][2] or not self.content_mills[e][2][2]: 
                        self.transport_mills = self.content_mills[e]                        
                        
                        self.cont += 1
                        
                        self.content_mills_position = []
                        self.content_mills = []
                        return True
    
    
    def put_file(self, event, position_verify, x, y):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # here it is controlled that the index for select the file don't exceed 9
            content_turn = self.turn_put_file
            if content_turn > 8:
                content_turn = 8
                
            if self.list_of_files[content_turn]:
                file = self.list_of_files[content_turn]
                # print(self.turn_put_file - self.rest_num_to_file)
                for instance in self.list_of_instances:
                    if instance[1].collidepoint(x, y):
                        
                        if position_verify and self.boolean_verify:
                                self.my_files.move(file, instance)
                                
                                self.turn_put_file += 1                    
                                break            
    
    
    def select_file(self, event, x, y):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for file_select in self.list_of_files:
                if file_select != []:
                    if file_select[1].collidepoint(x, y):
                        self.file_select_to_move = file_select
                        
                        for instance in self.list_of_instances:
                            if instance[1].collidepoint(x, y):
                                self.position_from_file_select = [instance[1].x, instance[1].y, instance]
                                break
                        break
    
    
    def __move_restrintion(self, instance, x, y):
        for position_aviable in instance[2]:
            if self.position_from_file_select:
                if self.position_from_file_select[0] + position_aviable == x or self.position_from_file_select[0] - position_aviable == x:
                    if self.position_from_file_select[1] == y:
                        return True
                    
                elif self.position_from_file_select[1] + position_aviable == y or self.position_from_file_select[1] - position_aviable == y: 
                    if self.position_from_file_select[0] == x:
                        return True
                
        return False
    
    
    def move_file(self, event, position_verify, x, y):
        three_files = True
        if self.file_limited == 3: #this condition is for when the player has only 3 files
            three_files = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for instance in self.list_of_instances:
                if instance[1].collidepoint(x, y):
                    if three_files:
                        if self.__move_restrintion(instance, instance[1].x, instance[1].y):
                            if position_verify:
                                self.my_files.move(self.file_select_to_move, instance)
                                self.turn_move_file += 1
                                
                                if self.file_select_to_move[2]: #quit the identification of mill from the file
                                    self.file_select_to_move[2].remove(self.file_select_to_move[2][0])
                                
                                
                                self.file_select_to_move = []
                                self.position_from_file_select = []
                                break
                    else:
                        if position_verify:
                            self.my_files.move(self.file_select_to_move, instance)
                            self.turn_move_file += 1
                            
                            if self.file_select_to_move[2]:
                                self.file_select_to_move[2].remove(self.file_select_to_move[2][0])
                            
                            self.file_select_to_move = []
                            self.position_from_file_select = []
                            break