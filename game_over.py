import pygame

class GameOver:
    def __init__(self, width, height, text="Game Over", font_size=36, color=(255, 255, 255)):
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=(self.width // 2, self.height // 2))

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Background color (black in this case)
        screen.blit(self.text_surface, self.text_rect)