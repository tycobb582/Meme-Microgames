import pygame.image
import pygame.mixer
from states import FnFStates
pygame.init()


class Player:
    def __init__(self):
        self.keybinds = {}
        self.img_pos = (0, 0)
        self.img = None
        self.img_dim = (0, 0)
        self.cur_time = 0
        self.recording = {}
        self.score = 0

    def draw(self, win):
        win.blit(self.img, (self.img_pos[0], self.img_pos[1], self.img_dim[0], self.img_dim[1]))


class Ye(Player):
    ye_faces = {"Down": pygame.image.load("images\\Kanye (Down).png"), "Left": pygame.image.load("images\\Kanye (Left).png"),
                "Right": pygame.image.load("images\\Kanye (Right).png"), "Up": pygame.image.load("images\\Kanye (Up).png"),
                "Idle": pygame.image.load("images\\Kanye (Idle).png")}
    sounds = {"Down": pygame.mixer.Sound("sounds\\Kanye (Down).ogg"), "Left": pygame.mixer.Sound("sounds\\Kanye (Left).ogg"),
              "Right": pygame.mixer.Sound("sounds\\Kanye (Right).ogg"), "Up": pygame.mixer.Sound("sounds\\Kanye (Up).ogg")}

    def __init__(self, win_dim):
        super().__init__()
        self.img = Ye.ye_faces["Idle"]
        self.img_dim = (self.img.get_width(), self.img.get_height())
        self.keybinds = {"Down": pygame.K_s, "Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w}
        self.img_pos = (win_dim[0] * 0.1, win_dim[1] * 0.45)

    def update(self, state):
        if state == FnFStates.IDLE:
            self.img = Ye.ye_faces["Idle"]

    def handle_input(self, evt, state, dt):
        self.cur_time += dt
        if state == FnFStates.P1_PLAY or state == FnFStates.P1_RECORD:
            if evt.type == pygame.KEYDOWN:
                if evt.key == self.keybinds["Down"]:
                    self.recording[self.cur_time] = "Down"
                    self.img = Ye.ye_faces["Down"]
                    Ye.sounds["Down"].play()
                elif evt.key == self.keybinds["Left"]:
                    self.recording[self.cur_time] = "Left"
                    self.img = Ye.ye_faces["Left"]
                    Ye.sounds["Left"].play()
                elif evt.key == self.keybinds["Right"]:
                    self.recording[self.cur_time] = "Right"
                    self.img = Ye.ye_faces["Right"]
                    Ye.sounds["Right"].play()
                elif evt.key == self.keybinds["Up"]:
                    self.recording[self.cur_time] = "Up"
                    self.img = Ye.ye_faces["Up"]
                    Ye.sounds["Up"].play()
        else:
            pass


class Drake(Player):
    drizzy_faces = {"Down": pygame.image.load("images\\Drake (Down).png"),
                "Left": pygame.image.load("images\\Drake (Left).png"),
                "Right": pygame.image.load("images\\Drake (Right).png"),
                "Up": pygame.image.load("images\\Drake (Up).png"),
                "Idle": pygame.image.load("images\\Drake (Idle).png")}
    sounds = {"Down": pygame.mixer.Sound("sounds\\Drake (Down).ogg"), "Left": pygame.mixer.Sound("sounds\\Drake (Left).ogg"),
              "Right": pygame.mixer.Sound("sounds\\Drake (Right).ogg"), "Up": pygame.mixer.Sound("sounds\\Drake (Up).ogg")}

    def __init__(self, win_dim):
        super().__init__()
        self.img = Drake.drizzy_faces["Idle"]
        self.img_dim = (self.img.get_width(), self.img.get_height())
        self.keybinds = {"Down": pygame.K_DOWN, "Left": pygame.K_LEFT, "Right": pygame.K_RIGHT, "Up": pygame.K_UP}
        self.img_pos = (win_dim[0] * 0.9 - self.img_dim[0], win_dim[1] * 0.45)

    def update(self, state):
        if state == FnFStates.IDLE:
            self.img = Drake.drizzy_faces["Idle"]

    def handle_input(self, evt, state, dt):
        self.cur_time += dt
        if state == FnFStates.P2_PLAY or state == FnFStates.P2_RECORD:
            if evt.type == pygame.KEYDOWN:
                if evt.key == self.keybinds["Down"]:
                    self.recording[self.cur_time] = "Down"
                    self.img = Drake.drizzy_faces["Down"]
                    Drake.sounds["Down"].play()
                elif evt.key == self.keybinds["Left"]:
                    self.recording[self.cur_time] = "Left"
                    self.img = Drake.drizzy_faces["Left"]
                    Drake.sounds["Left"].play()
                elif evt.key == self.keybinds["Right"]:
                    self.recording[self.cur_time] = "Right"
                    self.img = Drake.drizzy_faces["Right"]
                    Drake.sounds["Right"].play()
                elif evt.key == self.keybinds["Up"]:
                    self.recording[self.cur_time] = "Up"
                    self.img = Drake.drizzy_faces["Up"]
                    Drake.sounds["Up"].play()
        else:
            pass





