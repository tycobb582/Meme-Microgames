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
    ye_img = pygame.image.load("images\\Ye.png")
    sounds = {"Down": pygame.mixer.Sound("sounds\\yeup.ogg"), "Left": pygame.mixer.Sound("sounds\\yeleft.ogg"),
              "Right": pygame.mixer.Sound("sounds\\yeright.ogg"), "Up": pygame.mixer.Sound("sounds\\yeup.ogg")}

    def __init__(self, win_dim):
        super().__init__()
        self.img = Ye.ye_img
        self.img_dim = (self.img.get_width(), self.img.get_height())
        self.img = pygame.transform.scale(self.img, (self.img_dim[0] * 8, self.img_dim[1] * 8))
        self.img_dim = (self.img.get_width(), self.img.get_height())
        self.keybinds = {"Down": pygame.K_s, "Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w}
        self.img_pos = (win_dim[0] * 0.1, win_dim[1] * 0.45)
        self.screen_height = win_dim[1]

    def handle_input(self, evt, state, dt, turn_time, o_pos, notes):
        self.cur_time += dt
        if state == FnFStates.P1_PLAY or state == FnFStates.P1_RECORD:
            if evt.type == pygame.KEYDOWN:
                if evt.key == self.keybinds["Down"]:
                    self.recording[self.cur_time] = "Down"
                    if state == FnFStates.P1_RECORD:
                        notes.append(Arrow("Down", self.cur_time + turn_time, o_pos, self.screen_height))
                    Ye.sounds["Down"].play()
                elif evt.key == self.keybinds["Left"]:
                    self.recording[self.cur_time] = "Left"
                    if state == FnFStates.P1_RECORD:
                        notes.append(Arrow("Left", self.cur_time + turn_time, o_pos, self.screen_height))
                    Ye.sounds["Left"].play()
                elif evt.key == self.keybinds["Right"]:
                    self.recording[self.cur_time] = "Right"
                    if state == FnFStates.P1_RECORD:
                        notes.append(Arrow("Right", self.cur_time + turn_time, o_pos, self.screen_height))
                    Ye.sounds["Right"].play()
                elif evt.key == self.keybinds["Up"]:
                    self.recording[self.cur_time] = "Up"
                    if state == FnFStates.P1_RECORD:
                        notes.append(Arrow("Up", self.cur_time + turn_time, o_pos, self.screen_height))
                    Ye.sounds["Up"].play()
        else:
            pass

        return notes


class Drake(Player):
    drizzy_img = pygame.image.load("images\\Drake.png")
    sounds = {"Down": pygame.mixer.Sound("sounds\\ddown.ogg"), "Left": pygame.mixer.Sound("sounds\\dleft.ogg"),
              "Right": pygame.mixer.Sound("sounds\\dright.ogg"), "Up": pygame.mixer.Sound("sounds\\dup.ogg")}

    def __init__(self, win_dim):
        super().__init__()
        self.img = Drake.drizzy_img
        self.img_dim = (self.img.get_width(), self.img.get_height())
        self.img = pygame.transform.scale(self.img, (self.img_dim[0] * 8, self.img_dim[1] * 8))
        self.img_dim = (self.img.get_width(), self.img.get_height())
        self.keybinds = {"Down": pygame.K_DOWN, "Left": pygame.K_LEFT, "Right": pygame.K_RIGHT, "Up": pygame.K_UP}
        self.img_pos = (win_dim[0] * 0.9 - self.img_dim[0], win_dim[1] * 0.45)
        self.screen_height = win_dim[1]

    def handle_input(self, evt, state, dt, turn_time, o_pos, notes):
        self.cur_time += dt
        if state == FnFStates.P2_PLAY or state == FnFStates.P2_RECORD:
            if evt.type == pygame.KEYDOWN:
                if evt.key == self.keybinds["Down"]:
                    self.recording[self.cur_time] = "Down"
                    if state == FnFStates.P2_RECORD:
                        notes.append(Arrow("Down", self.cur_time + turn_time, o_pos, self.screen_height))
                    Drake.sounds["Down"].play()
                elif evt.key == self.keybinds["Left"]:
                    self.recording[self.cur_time] = "Left"
                    if state == FnFStates.P2_RECORD:
                        notes.append(Arrow("Left", self.cur_time + turn_time, o_pos, self.screen_height))
                    Drake.sounds["Left"].play()
                elif evt.key == self.keybinds["Right"]:
                    self.recording[self.cur_time] = "Right"
                    if state == FnFStates.P2_RECORD:
                        notes.append(Arrow("Left", self.cur_time + turn_time, o_pos, self.screen_height))
                    Drake.sounds["Right"].play()
                elif evt.key == self.keybinds["Up"]:
                    self.recording[self.cur_time] = "Up"
                    if state == FnFStates.P2_RECORD:
                        notes.append(Arrow("Up", self.cur_time + turn_time, o_pos, self.screen_height))
                    Drake.sounds["Up"].play()
        else:
            pass

        return notes


class Arrow:
    down_img = pygame.image.load("images\\down_f.png")
    left_img = pygame.image.load("images\\left_f.png")
    right_img = pygame.image.load("images\\right_f.png")
    up_img = pygame.image.load("images\\up_f.png")

    def __init__(self, arrow_type, time, player_pos, win_y):
        if arrow_type == "Down":
            self.img = Arrow.down_img
            self.x = player_pos[0] + 10
        elif arrow_type == "Left":
            self.img = Arrow.left_img
            self.x = player_pos[0] - 50
        elif arrow_type == "Right":
            self.img = Arrow.right_img
            self.x = player_pos[0] + 70
        elif arrow_type == "Up":
            self.img = Arrow.up_img
            self.x = player_pos[0] + 130
        self.y = (win_y - (player_pos[1] - 200)) * time
        self.scroll_rate = win_y

    def update(self, dt):
        self.y -= self.scroll_rate * dt
        print(self.y)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
