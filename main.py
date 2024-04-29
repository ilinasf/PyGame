import pygame

class Window:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.fps = 60

        self.__init_window()

    def __init_window(self):
        pygame.init()
        pygame.mixer.init()

    
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Моя игра')
        clock = pygame.time.Clock()

class EventHandler:
    def __init__(self):
        while self.running:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    running = False
                    pygame.quit()

class Run(Window, EventHandler):
    def __init__(self):
        super().__init__()
        self.running = True
        while True:
            self.screen.fill((0,0,255))
            pygame.display.flip()

class Render:
    def __init__(self):
        pass

k = Run()