import pygame
import sys
import random







class Game():
    def __init__(self):
        self.allice_lst = []
        self.obsticle_lst = []
        self.allins_laser_lst = []
        self.player = Player()
        self.laser = Laser()
        self.number_of_aliens = 55
        self.spawn_alliens()
        self.create_obsticles()

        self.red = pygame.image.load("red.png")
        self.yellow = pygame.image.load("yellow.png")
        self.green = pygame.image.load("green.png")

        self.font = pygame.font.Font(None,45)
        self.score = 0
        music = pygame.mixer.Sound("music.wav")
        music.set_volume(0.1)
        music.play(loops= -1)

        self.laser_sound = pygame.mixer.Sound("laser.wav")
        self.laser_sound.set_volume(0.3)
        self.explosion_sound = pygame.mixer.Sound("explosion.wav")
        self.laser_sound.set_volume(0.3)



    def display_score(self):
        score_rect = pygame.Rect(100,50,100,20)
        score_surface = self.font.render(str(self.score),True,(255,255,255))
        screen.blit(score_surface,score_rect)
        



    def shoot_laser(self):
        if not self.laser.laser_is_out:
            self.laser.pos_x = self.player.pos_x + self.player.size_x/2
            self.laser.pos_y = self.player.pos_y
            self.laser.laser_is_out = True
            laser_rect = pygame.Rect(self.laser.pos_x,self.laser.pos_y -10,self.laser.laser_size_x,self.laser.laser_size_y)
            pygame.draw.rect(screen,(255,255,255),laser_rect)
            self.laser_sound.play()

    def move_laser(self):
        if self.laser.laser_is_out:
            laser_rect = pygame.Rect(self.laser.pos_x,self.laser.pos_y,self.laser.laser_size_x,self.laser.laser_size_y)
            pygame.draw.rect(screen,(255,255,255),laser_rect)
            self.laser.pos_y -= 15
        

    def check_laser_hit(self):
        try:
            if self.laser.pos_y + self.laser.laser_size_y < 0:
                self.laser.laser_is_out = False
            for obsticle in self.obsticle_lst:
                if obsticle.pos_x - self.laser.pos_x < 0 and abs(obsticle.pos_x - self.laser.pos_x) <= obsticle.size:
                    if obsticle.pos_y - self.laser.pos_y > 0 and (obsticle.pos_y - self.laser.pos_y) <= obsticle.size:
                        obsticle.strenght -= 1
                        self.check_obsiticle_strenght(obsticle)
                        
                        self.laser = Laser()
            
            for allien in self.allice_lst:
                if allien.pos_x - self.laser.pos_x < 0 and abs(allien.pos_x - self.laser.pos_x) <= allien.size_x:
                    if allien.pos_y - self.laser.pos_y > 0 and (allien.pos_y - self.laser.pos_y) <= allien.size_y:
                        self.allice_lst.remove(allien)
                        self.explosion_sound.play()
                        self.score += allien.score
                        self.laser = Laser()

        except:
            pass

    def spawn_alliens(self):
        x = 50
        y = 100
        for i in range(self.number_of_aliens):
            if x + 350 > width:
                x = 50
                y += 40
            if i <= 10:
                allien = Aliens(x,y,"red")
            elif i > 10 and i <= 32:
                allien = Aliens(x,y,"yellow")
            else:
                allien = Aliens(x,y,"green")
            self.allice_lst.append(allien)
            x += 50

    def draw_alliens(self):
        count = 0
        for i in self.allice_lst:

            allien_rect = pygame.Rect(i.pos_x,i.pos_y,i.size_x,i.size_y)
            if i.colour == "red":
                screen.blit(self.red,allien_rect)
            elif i.colour == "yellow":
                screen.blit(self.yellow,allien_rect)
            else:
                screen.blit(self.green,allien_rect)

            count += 1

    def move_alliens(self):
        if self.allice_lst[0].move_left:
            most_left_one_x = self.allice_lst[0].pos_x
            for i in self.allice_lst:
                if i.pos_x < most_left_one_x:
                    most_left_one_x = i.pos_x
            if most_left_one_x < 50:
                for item in self.allice_lst:
                    item.pos_y += 20
                    item.move_left = False
            else:
                for item in self.allice_lst:
                    item.pos_x -= 1.0
        else:
            most_right_one_x = self.allice_lst[0].pos_x
            for i in self.allice_lst:
                if i.pos_x > most_right_one_x:
                    most_right_one_x = i.pos_x
            if most_right_one_x + 100 > width:
                for item in self.allice_lst:
                    item.pos_y += 20
                    item.move_left = True
            else:
                for item in self.allice_lst:
                    item.pos_x += 1.0



    def create_obsticles(self):
        obsticle_range_x = 40

        for i in range(4):
            obsticle_range_y = 0
            for row in range(3):
                if row == 2:
                    obsticle = Obsticles(obsticle_range_x + 150,height- 350+obsticle_range_y)
                    obsticle2 = Obsticles(obsticle_range_x + 210,height- 350+obsticle_range_y)
                    self.obsticle_lst.append(obsticle)
                    self.obsticle_lst.append(obsticle2)
                    obsticle_range_y += 40
                else:
                    obsticle = Obsticles(obsticle_range_x + 150,height- 350 +obsticle_range_y)
                    obsticle2 = Obsticles(obsticle_range_x + 170,height- 350+obsticle_range_y)
                    obsticle3 = Obsticles(obsticle_range_x + 190,height- 350+obsticle_range_y)
                    obsticle4 = Obsticles(obsticle_range_x + 210,height- 350+obsticle_range_y)
                    self.obsticle_lst.append(obsticle)
                    self.obsticle_lst.append(obsticle2)
                    self.obsticle_lst.append(obsticle3)
                    self.obsticle_lst.append(obsticle4)
                    obsticle_range_y +=20
            obsticle_range_x += 150
        

    def draw_obsticles(self):
        for i in self.obsticle_lst:
            obsticle_rect = pygame.Rect(i.pos_x,i.pos_y,i.size,i.size)
            if i.strenght == 3:
                pygame.draw.rect(screen,i.colour_3,obsticle_rect)
            elif i.strenght == 2:
                pygame.draw.rect(screen,i.colour_2,obsticle_rect)
            else:
                pygame.draw.rect(screen,i.colour_1,obsticle_rect)



    def alliens_shoot_back(self):
        most_up_one = self.allice_lst[0].pos_y
        for i in self.allice_lst:
            if i.pos_y == most_up_one:
                if random.randint(0,750) == 9:
                    laser = Laser()
                    laser.pos_x = i.pos_x + i.size_x/2
                    laser.pos_y = i.pos_y + i.size_y
                    self.allins_laser_lst.append(laser)
                    self.laser_sound.play()


    def move_allien_lasers(self):
        for i in self.allins_laser_lst:
            laser_rect = pygame.Rect(i.pos_x,i.pos_y,i.laser_size_x,i.laser_size_y)
            pygame.draw.rect(screen,(255,255,255),laser_rect)

            i.pos_y += 10
            if i.pos_y > height:
                self.allins_laser_lst.remove(i)

        


    def check_obsiticle_strenght(self,obsticle):
        if obsticle.strenght == 0:
            self.obsticle_lst.remove(obsticle)
            self.explosion_sound.play()


    def check_collision_for_allien_laser(self):
        for laser in self.allins_laser_lst:
            for obsticle in self.obsticle_lst:
                if obsticle.pos_x - laser.pos_x < 0 and abs(obsticle.pos_x - laser.pos_x) <= obsticle.size:
                    if obsticle.pos_y - laser.pos_y > 0 and (obsticle.pos_y - laser.pos_y) <= obsticle.size:
                        obsticle.strenght -= 1
                        self.check_obsiticle_strenght(obsticle)
                        self.allins_laser_lst.remove(laser)
            if self.player.pos_x - laser.pos_x < 0 and abs(self.player.pos_x - laser.pos_x) <= self.player.size_x:
                if self.player.pos_y - laser.pos_y > 0 and (self.player.pos_y - laser.pos_y) <= self.player.size_y:
                    self.allins_laser_lst.remove(laser)
                    self.player.health -= 1
                    self.explosion_sound.play()


    def victory_message(self):
        if len(self.allice_lst) == 0:
            victory_surf = self.font.render("You won",True, "white")
            victory_rect = victory_surf.get_rect(center = (width / 2,height/2))
            screen.blit(victory_surf,victory_rect)


    def check_game_over(self):
        if self.player.health ==0:
            defeat_surf = self.font.render("You lost, ghosari",True, "white")
            defeat_rect = defeat_surf.get_rect(center = (width / 2,height/2))
            screen.blit(defeat_surf,defeat_rect)
 
        if self.allice_lst[-1].pos_y >height -290:
            defeat_surf = self.font.render("You lost, ghosari",True, "white")
            defeat_rect = defeat_surf.get_rect(center = (width / 2,height/2))
            screen.blit(defeat_surf,defeat_rect)

    def ran(self):

        self.player.create_player()
        self.player.update()
        self.draw_obsticles()
        self.move_alliens()
        self.draw_alliens()
        self.alliens_shoot_back()
        self.move_allien_lasers()
        self.check_laser_hit()
        self.check_collision_for_allien_laser()
        self.move_laser()
        self.check_game_over()
        self.display_score()
        self.victory_message()
        self.player.show_health()

    
class Obsticles():
    def __init__(self,pos_x,pos_y) -> None:
        self.strenght = 3
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = 20
        self.colour_3 = (255,0,5)
        self.colour_2 = (255, 254, 64)
        self.colour_1 = (84,251,13)

    
        


class Aliens():
    def __init__(self,pos_x,pos_y,colour):
        self.size_x = 40
        self.size_y = 30
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.move_left = False
        self.colour = colour
        if self.colour == "red": self.score = 1000
        elif self.colour == "yellow": self.score = 500
        else: self.score = 100

        


class Laser():
    def __init__(self) -> None:
        self.laser_size_x = 4
        self.laser_size_y = 20
        self.laser_is_out = False
        self.pos_x = None
        self.pos_y = None



class Player():
    def __init__(self) -> None:
        self.size_x = 50
        self.size_y = 25
        self.pos_x = width /2
        self.pos_y = height - 50
        self.speed = 5
        self.health = 3
        self.player_image = pygame.image.load("player.png")



    def show_health(self):
        range_x = 0
        for i in range(self.health):
            rect = pygame.Rect(width - 100 - range_x, 50, self.size_x,self.size_y)
            screen.blit(self.player_image,rect)
            range_x += 80


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.player_inside_window(1):
            self.pos_x += self.speed
        elif keys[pygame.K_LEFT] and self.player_inside_window(0):
            self.pos_x -= self.speed


    def update(self):
        self.get_input()


    def move_player(self,index):
        if index == 0:
            self.pos_x += 5
        else:
            self.pos_x -= 5



    def create_player(self):

        player_rect = pygame.Rect(self.pos_x,self.pos_y,self.size_x,self.size_y)
        screen.blit(self.player_image,player_rect)



    def player_inside_window(self,index):
        if self.pos_x + 115 < width and index ==1:
            return True
        
        elif self.pos_x -50 > 0 and index == 0:
            return True
        
        else:
            return False
        





if __name__ == "__main__":
    width = 900
    height = 950
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)
    game = Game()
    rect = pygame.Rect(50,height-15,width -105, 5 )
    



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT and game.player.player_inside_window():
                #    game.player.move_player(1)
                #elif event.key == pygame.K_RIGHT and game.player.player_inside_window():
                #    game.player.move_player(0)
                if event.key == pygame.K_SPACE:
                    game.shoot_laser()
                

        
                

        background = pygame.Rect(0,0,width,height)
        screen.fill((0,0,0))
        game.ran()
        pygame.draw.rect(screen, (38,87,16), rect)
        pygame.display.update()
        clock.tick(60)

