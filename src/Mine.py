import pygame

# Object class
class Mine(pygame.sprite.Sprite):
    def __init__(self, surfaceColor, height, width):
        super().__init__()
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.brown = (150, 75, 0)

        self.image = pygame.Surface([width, height])
        self.image.fill(surfaceColor)
        # self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image, self.brown, pygame.Rect((width/2)-1, 5, 2.5, height/2))
        #Blackbol
        pygame.draw.circle(self.image, self.black, (height/2, width/2+5), (height/2)-7.5)

        self.rect = self.image.get_rect()
        self.rect.center = [width, height]


# pygame.init()
#
# surfaceColor = (255,255,255)
#
# WIDTH = 500
# HEIGHT = 500
#
# size = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Creating Sprite")
#
all_sprites_list = pygame.sprite.Group()

# object_ = Mine(surfaceColor, 30, 30)
# object_.rect.x = 200
# object_.rect.y = 400
#
# object_2 = Mine((122,122,122), 30, 30)
# object_2.rect.x = 20
# object_2.rect.y = 40
#
# all_sprites_list.add(object_)
# all_sprites_list.add(object_2)
#
# exit = True
# clock = pygame.time.Clock()
#
# while exit:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit = False
#
#     all_sprites_list.update()
#     screen.fill(surfaceColor)
#
#     all_sprites_list.draw(screen)
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()