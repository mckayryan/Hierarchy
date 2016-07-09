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
	#the object that prints to the screen
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
    def intro_display(self):
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
    #the object that manages events and time, using screen as an input
    def add_gui(self, gui):
        self.display = gui
    # def game_map_input():
    def control_input(self, action):
    #takes the input from the control, as a string and does stuff
        if action == 'escape':
            raise SystemExit
    # def player_input():
    # def game_map_output():
    # def player_output():
    def gui_output(self, x):
    #takes an integer as an argument and displays
        if x == 1: 
            self.display.intro_display()
        else:
            self.display.map_display()
    # def objects_output():

class game_map(object):
    #storage of updatable *4 pixel object map
    #also includes structural map at *64 pixel
    def events_input():
        pass
    # def player_input():
    # def objects_input():
    def events_output():
        pass
    # def player_output():
    # def objects_output():

def generate_map(game_map):
    #fills an empty game map with the starting game state
    pass

class control_input(object):
    #management of player input
    def add_event_loop(self, event_loop):
        self.event_queue = event_loop
    def watch_keys(self):
        #monitors for key input and reports back to event loop
        #OUTPUT to EVENT QUEUE
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.event_queue.control_input('escape')
                elif event.key == pygame.K_SPACE:
                    #go from intro screen to game screen
                    self.event_queue.gui_output(2)

# class player_character(object):
# 	#storage for player attributes
# 	def map_input():
# 	def events_input():
# 	def objects_input():
# 	def map_output():
# 	def objects_output():
# 	def events_output():

# class game_objects(object):
# 	#all objects on the map
# 	def events_input():
# 	def map_input():
# 	def player_input():
# 	def events_output():
# 	def map_output():
# 	def player_output():



def main():
	#initialise modules
    screen = gui()
    queue = event_loop()
    queue.add_gui(screen)
    controls = control_input()
    controls.add_event_loop(queue)
    queue.gui_output(1)
    while True:
        controls.watch_keys()


if __name__ == "__main__":
    main()




# class map (object):

#     def __init__(self):
#         #initilise 2d array

# class map_tile(map):

#     self.map[x][y].id_num = 0
