####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

import pygame
import random
pygame.init()
random.seed()

config = {
    'description': 'Hierarchy',
    'author': 'Adam Stiles and Ryan McKay',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

class gui(object):
    resolution = res_width, res_height = (1280, 720)    
    def __init__(self):
        #set window screen res - pixels 
        self.display = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('Hierarchy')
    def fill_color(self, screen, color, position):
    	screen.fill(color)
    	self.display.blit(screen, position)
    def write_text(self, size, message, color, location):
    	font = pygame.font.Font(None, size)
    	text = font.render(message, 1, color)
    	textpos = text.get_rect()
    	textpos.center = location
    	self.display.blit(text, textpos)
    def intro_display(self, queue):
        #set up intro surface
        intro_screen_position = (0, 0)
        intro_screen = pygame.Surface(self.resolution)
        #fill black
        black = (0,0,0)
        self.fill_color(intro_screen, black, intro_screen_position)
        #draw title
        t_size = 108
        t_color = (255, 255, 255)
        t_message = 'Hierarchy'
        t_location = (self.display.get_width()/3, self.display.get_height()/4)
        self.write_text(t_size, t_message, t_color, t_location)
        #draw to display
        pygame.display.flip()
    def map_display(self):
        #Divide Map
        map_screen_dim = map_positionx, map_positiony, map_width, map_height  = (0, 0, 3*self.res_width/4, self.res_height)
        map_screen_position = pygame.Rect(map_screen_dim)
        map_sub_screen = self.display.subsurface(map_screen_position)
        # Divide Stats screen
        stats_screen_dim = stats_positionx, stats_positiony, stats_width, stats_height = (map_width, 0, self.res_width/4, self.res_height)
        stats_screen_position = pygame.Rect(stats_screen_dim)
        stats_sub_screen = self.display.subsurface(stats_screen_position)
        #Initiate map surface - pixels
        whole_map_dim = ((10000, 10000))
        whole_map = pygame.Surface(whole_map_dim)
        #fill some_colour
        some_colour = (245,165,44)
        whole_map.fill(some_colour)
        #Mount a section of the map surfacen the map screen
        map_segment_dim = segment_posx, segment_posy, segment_width, segment_height = (0, 0, map_width, map_height)
        map_segment = pygame.Rect(map_segment_dim)
        map_sub_screen.blit(whole_map.subsurface(map_segment), (0,0))
        #Draw to display
        pygame.display.flip()



class event_loop(object):
    def player_input(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #exit_game()
                    raise SystemExit
                elif event.key == pygame.K_SPACE:
                    screen.map_display()


def main():
    queue = event_loop()
    screen = gui()
    screen.intro_display(queue)
    while True:
        queue.player_input(screen)


if __name__ == "__main__":
    main()




# class map (object):

#     def __init__(self):
#         #initilise 2d array

# class map_tile(map):

#     self.map[x][y].id_num = 0
