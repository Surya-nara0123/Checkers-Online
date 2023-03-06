import pygame as pyg
import sys

class Menu:
    def __init__(self):
        self.width = self.height = 500
        self.window = pyg.display.set_mode((self.width+220, self.height))
        self.run = True
    def main(self):
        while self.run:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.run = False
                    pyg.quit()
                    sys.exit()
            self.window.fill((255, 255, 255))
            pyg.display.update()

Menu().main()