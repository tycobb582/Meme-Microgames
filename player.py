import pygame.image
import pygame.mixer
pygame.init()


class Player:
    def __init__(self, player_num):
        self.keybinds = {}
        if player_num == 1:
            self.p_num = 1
            self.__class__ = Ye
        else:
            self.p_num = 2
            self.__class__ = Drake

    def handle_input(self, evt, state):
        if state.value == self.p_num:
            if evt.type == pygame.KEYDOWN:
                if evt.key == self.keybinds["Down"]:
                    self.__class__.__name__.sounds["Down"].play()
                elif evt.key == self.keybinds["Left"]:
                    self.__class__.__name__.sounds["Left"].play()
                elif evt.key == self.keybinds["Right"]:
                    self.__class__.__name__.sounds["Right"].play()
                elif evt.key == self.keybinds["Up"]:
                    self.__class__.__name__.sounds["Up"].play()
        else:
            pass


class Ye(Player):
    ye_img = pygame.image.load("images\\Ye.png")
    sounds = {"Down": pygame.mixer.Sound("sounds\\testdown.ogg"), "Left": pygame.mixer.Sound("sounds\\testleft.ogg"),
              "Right": pygame.mixer.Sound("sounds\\testright.ogg.ogg"), "Up": pygame.mixer.Sound("sounds\\testup.ogg")}

    def __init__(self, player_num):
        super().__init__(player_num)
        self.img = Ye.ye_img
        self.keybinds = {"Down": pygame.K_s, "Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w}
        self.img_pos = self.img.get_width() // 2


class Drake(Player):
    drizzy_img = pygame.image.load("images\\Drake.png")

    def __init__(self, player_num):
        super().__init__(player_num)
        self.img = Drake.drizzy_img


yeezy = Ye(1)
print(yeezy.__class__.__name__)



