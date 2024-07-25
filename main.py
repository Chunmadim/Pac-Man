import pygame
import sys







class Game():
    def __init__(self):
        self.player = Player()
        self.laser = Laser()


    def shoot_laser(self):
        if not self.laser.laser_is_out:
            self.laser.pos_x = self.player.pos_x + self.player.size_x/2
            self.laser.pos_y = self.player.pos_y
            self.laser.laser_is_out = True
            laser_rect = pygame.Rect(self.laser.pos_x,self.laser.pos_y -10,self.laser.laser_size_x,self.laser.laser_size_y)
            pygame.draw.rect(screen,(255,255,255),laser_rect)

    def move_laser(self):
        if self.laser.laser_is_out:
            laser_rect = pygame.Rect(self.laser.pos_x,self.laser.pos_y,self.laser.laser_size_x,self.laser.laser_size_y)
            pygame.draw.rect(screen,(255,255,255),laser_rect)
            self.laser.pos_y -= 5

    def check_laser_hit(self):
        try:
            if self.laser.pos_y + self.laser.laser_size_y < 0:
                self.laser.laser_is_out = False
        except:
            pass



    def ran(self):
        self.player.create_player()
        self.player.update()
        self.check_laser_hit()
        self.move_laser()
        


class Board():
    def __init__(self) -> None:
        pass


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

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.pos_x += self.speed
        elif keys[pygame.K_LEFT]:
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
        pygame.draw.rect(screen,(255,255,255), player_rect)


    def player_inside_window(self):
        if self.pos_x + 5 < width and self.pos_x -5 > 0:
            return True
        





if __name__ == "__main__":
    width = 900
    height = 950
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)
    game = Game()
    






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
                

        
                


        screen.fill((0,0,0))
        game.ran()

        pygame.display.update()
        clock.tick(60)

