import pygame

class Button():
    def __init__(self, position_x, position_y, width, height, text, color):

        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont(None, 30)

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.position_x, self.position_y, self.width, self.height))
        text = self.font.render(self.text, True, (255, 255, 255))
        window.blit(text, (self.position_x + (self.width/2 - text.get_width()/2), self.position_y + (self.height/2 - text.get_height()/2)))

    def on_button(self, position):
        if position[0] > self.position_x and position[0] < self.position_x + self.width and position[1] > self.position_y and position[1] < self.position_y + self.height:
            return True
        else:
            return False

class Label():
    def __init__(self, position_x, position_y, text):
        self.position_x = position_x
        self.position_y = position_y
        self.text = text
        self.font = pygame.font.SysFont(None, 30)

    def change_text(self, text):
        self.text = text

    def draw(self, window):
        text = self.font.render(self.text, True, (255, 255, 255))
        window.blit(text, (self.position_x - text.get_width()/2, self.position_y - text.get_height()/2))
