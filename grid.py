import pygame

class coordinate:
    x = None
    y = None
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class grid:

class engine:
    WIDTH = 400 # window width
    HEIGHT = 400 # window height
    GRIDSIZE = 10 # grid size
    FPS = 30 # frame rate
    MAX_X = int(WIDTH / GRIDSIZE) # max x index
    MAX_Y = int(HEIGHT / GRIDSIZE) # max y indes
    GRIDMATRIX = [] # stores grid values

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BG_COLOR = BLACK

    def __init__(self):
        global clock, screen # global clock (fps) and display
        for i in range(int(self.WIDTH / self.GRIDSIZE)): # initialize gridmatrix with 0
            self.GRIDMATRIX.append([]) # x value arrays
            for j in range(int(self.HEIGHT / self.GRIDSIZE)): # init x value arrays
                self.GRIDMATRIX[i].append(0)
        pygame.init() # initialize pygame
        
    def start(self): # start the game engine
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH)) # show the screen
        self.clock = pygame.time.Clock() # set the clock

    def refresh_screen(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def draw_rect(self, color, coord):
        if not check_bounds(coord):
            return False
        elif self.GRIDMATRIX[coord.y][coord.x] == 0:
            pygame.draw.rect(self.screen, color, pygame.Rect(coord.x * self.GRIDSIZE, coord.y * self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE)) # draw the square
            self.GRIDMATRIX[coord.y][coord.x] = 1 # record its location
            return True

    def draw_rects(self, )

    def draw_text(self, color, size, text):
        font = pygame.font.SysFont("monospace", size)
        label = font.render(text, 1, color)
        self.screen.blit(label, (100, 100))

    def del_rect(self, coord):
        if not check_bounds(coord):
            return False
        if not self.GRIDMATRIX[coord.y][coord.x] == 0:
            pygame.draw.rect(self.screen, self.BG_COLOR, pygame.Rect(coord.x * self.GRIDSIZE, coord.y * self.GRIDSIZE, self.GRIDSIZE, self.GRIDSIZE)) # draw a black square over the square
            self.GRIDMATRIX[coord.y][coord.x] = 0 # record deletion
            return True
        else:
            return False 

    #def draw_mul_rects(self, rects)

    #def del_mul_rects(self, rects)

    def check_bounds(self, coord):
        if coord.x >= self.MAX_X or coord.y >= self.MAX_Y or coord.y < 0 or coord.x < 0:
            return False
        elif: return True


    def print_matrix(self): # print out all contents of matrix (debug purpose)
        for xarrays in self.GRIDMATRIX:
            for xvals in xarrays:
                print(str(xvals) + "  ", end = "")
            print("")
