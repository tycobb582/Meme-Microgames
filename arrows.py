import pygame.image


class Arrow:
    down_img = pygame.image.load("images\\down_f.png")
    left_img = pygame.image.load("images\\left_f.png")
    right_img = pygame.image.load("images\\right_f.png")
    up_img = pygame.image.load("images\\up_f.png")

    def __init__(self, arrow_type, time, player_pos, win_y, turn_time):
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
        self.y = win_y * time + (player_pos[1] - 200)
        self.scroll_rate = 600

    def update(self, dt):
        self.y -= self.scroll_rate * dt

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
