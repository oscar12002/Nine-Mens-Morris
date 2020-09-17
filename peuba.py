# def multiplo(n):
#     suma = 0
#     for e in range(n):
#         if e % 3 == 0:
#             suma += e
#             continue
#         if e % 5 == 0:
#             suma += e
#     print(suma)
    
    
# multiplo(1000)

# def fibonacci(n):
#     num1 = 0
#     num2 = 1
#     list_fibo = []
#     suma = 0
#     for e in range(n):
#         num3 = num1 + num2
#         list_fibo.append(num3)
#         num1 = num2
#         num2 = num3
#     for num in list_fibo:
#         if num % 2 == 0:
#             suma += num
#     print(suma)
    
# fibonacci(32)

# def primo(n):
#     list_primos = []
#     hay = 0
#     for numero in range(1, n):
#         if n % numero == 0 and numero != 1 and numero != n:
#             list_primos.append(numero)
            
#     print(list_primos)
    
# primo(600851475143)
                
                
# lis = [1,2,5,4,7,9]
# print(lis)
# key = 5
# for e in range(len(lis)):
#     if key == lis[e]:
#         lis[e] = 500
        
# print(lis)
# if key in lis:
#     indice = lis.index(key)
#     lis[indice] = 500

# print(lis)







    # def __select_file_to_delete(self, event, enemi_player):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         self.__get_click_position(event)
            
    #         for file in enemi_player.list_of_files:
    #             if file[1].collidepoint(self.mouse_pos_x, self.mouse_pos_y):
    #                 enemi_player.list_of_files.remove(file)
    #                 break
    
    
    # def __delete_file(self, event):
    #     if (self.player_one.cont_turn_putFile < 9) or (self.player_two.cont_turn_putFile < 9):  
            
    #         if self.player_one.cont_turn_putFile == self.player_two.cont_turn_putFile:
    #             self.__select_file_to_delete(event, self.player_two)
    #         elif self.player_one.cont_turn_putFile > self.player_two.cont_turn_putFile:
    #             self.__select_file_to_delete(event, self.player_one)
            
    #     else:
    #         if self.player_one.cont_turn_move_file == self.player_two.cont_turn_move_file:
    #             self.__select_file_to_delete(event, self.player_two)
    #         elif self.player_one.cont_turn_move_file > self.player_two.cont_turn_move_file:
    #             self.__select_file_to_delete(event, self.player_one)
    
    
    
    
    
    
    
    
    
    
    
        # def eliminate_file(self):
        #     first = False
        # second = False
        # thirth = False
        # for e in range(0, len(self.list_of_instances), 3):
        #     for file in self.list_of_files:
        #         if file[1].center == self.list_of_instances[e+0][1].center:
        #             if file[2] == []:                        
        #                 first = True
        #                 # file[2].append(1)
        #             continue
        #         elif file[1].center == self.list_of_instances[e+1][1].center:   
        #             if file[2] == []:
        #                 second = True
        #                 # file[2].append(1)
        #             continue
        #         elif file[1].center == self.list_of_instances[e+2][1].center:
        #             if file[2] == []:
        #                 thirth = True
        #                 # file[2].append(1)
                        
        #                 break
        #     break
        
        # if first:
        #     if second:
        #         if  thirth:
        #             print("Gg")
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False
        # else:
        #     return False
        
matr = [[(150, 200), (325, 200), (500, 200)],
        [(200, 250), (325, 250), (450, 250)],
        [(250, 300), (325, 300), (400, 300)],
        [(150, 375), (200, 375), (250, 375)],
        [(400, 375), (450, 375), (500, 375)],
        [(250, 450), (325, 450), (400, 450)],
        [(200, 500), (325, 500), (450, 500)],
        [(150, 550), (325, 550), (500, 550)]]

aped = [1,2,3,4,5,6,7,8,9]
contenedor = []

cambio = 0
indice = aped[cambio]

for y in range(1, len(aped)+1):
    for i in range(1, len(aped)+1):
        for e in range(1, len(aped)+1):
            if y != i and y != e and i != e:
                contenedor.append([y, i, e])
            

for parte in contenedor:
    print(parte)
print(len(contenedor))