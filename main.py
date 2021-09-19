import pygame
import player
import states

win_dim = (800, 600)
fs = False  # Fullscreen
win = pygame.display.set_mode(win_dim, pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
done = False
game_state = states.FnFStates.P1_RECORD
p1 = player.Ye(win_dim)
p2 = player.Drake(win_dim)
players = [p1, p2]
turn_clock = 3
font = pygame.font.SysFont("Arial", 24)
last_turn = None
hollow_arrows = {"Down": pygame.image.load("images\\down_h.png"), "Left": pygame.image.load("images\\left_h.png.png"),
                 "Right": pygame.image.load("images\\right_h.png"), "Up": pygame.image.load("images\\up_h.png")}
filled_arrows = {"Down": pygame.image.load("images\\down_f.png"), "Left": pygame.image.load("images\\left_f.png.png"),
                 "Right": pygame.image.load("images\\right_f.png"), "Up": pygame.image.load("images\\up_f.png")}


def score_check(p1, p2, state):
    if state == states.FnFStates.P2_PLAY:
        for time in p1.recording:
            for time2 in p2.recording:
                if time - 0.15 <= time2 <= time + 0.15:
                    # Perfect!
                    if p1.recording[time] == p2.recording[time2]:
                        # Same note
                        p2.score += 1
                        break
                    else:
                        p1.score += 1
                        break
                elif time - 0.25 <= time2 <= time + 0.25:
                    # Good!
                    if p1.recording[time] == p2.recording[time2]:
                        # Same note
                        p2.score += 0.75
                        break
                    else:
                        p1.score += 1
                        break
                elif time - 0.35 <= time2 <= time + 0.35:
                    # Okay!
                    if p1.recording[time] == p2.recording[time2]:
                        # Same note
                        p2.score += 0.5
                        break
                    else:
                        p1.score += 1
                        break
    elif state == states.FnFStates.P1_PLAY:
        for time in p2.recording:
            for time2 in p1.recording:
                if time - 0.15 <= time2 <= time + 0.15:
                    # Perfect!
                    if p2.recording[time] == p1.recording[time2]:
                        # Same note
                        p1.score += 1
                        break
                    else:
                        p2.score += 1
                        break
                elif time - 0.25 <= time2 <= time + 0.25:
                    # Good!
                    if p2.recording[time] == p1.recording[time2]:
                        # Same note
                        p1.score += 0.75
                        break
                    else:
                        p2.score += 1
                        break
                elif time - 0.35 <= time2 <= time + 0.35:
                    # Okay!
                    if p2.recording[time] == p1.recording[time2]:
                        # Same note
                        p1.score += 0.5
                        break
                    else:
                        p2.score += 1
                        break


while not done:
    # Update
    delta_time = clock.tick() / 1000
    turn_clock -= delta_time
    if turn_clock <= 0:
        if game_state == states.FnFStates.P1_RECORD:
            game_state = states.FnFStates.P2_PLAY
            turn_clock = 3
        elif game_state == states.FnFStates.P2_PLAY:
            score_check(p1, p2, game_state)
            game_state = states.FnFStates.IDLE
            last_turn = states.FnFStates.P1_RECORD
            turn_clock = 4
        elif game_state == states.FnFStates.P2_RECORD:
            game_state = states.FnFStates.P1_PLAY
            turn_clock = 3
        elif game_state == states.FnFStates.P1_PLAY:
            score_check(p1, p2, game_state)
            game_state = states.FnFStates.IDLE
            last_turn = states.FnFStates.P2_RECORD
            turn_clock = 4
        elif game_state == states.FnFStates.IDLE:
            for player in players:
                player.cur_time = 0
                player.recording = {}
            if last_turn == states.FnFStates.P1_RECORD:
                game_state = states.FnFStates.P2_RECORD
            else:
                game_state = states.FnFStates.P1_RECORD
            turn_clock = 3

    # Input
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    elif event.type == pygame.QUIT:
        done = True
    if game_state == states.FnFStates.P1_RECORD or game_state == states.FnFStates.P1_PLAY:
        p1.handle_input(event, game_state, delta_time)
    elif game_state != states.FnFStates.IDLE:
        p2.handle_input(event, game_state, delta_time)

    # Draw
    win.fill((0, 0, 0))
    for player in players:
        player.draw(win)
        temp = font.render(str(player.score), False, (175, 175, 175))
        win.blit(temp, (player.img_pos[0] + player.img_dim[0] // 2, player.img_pos[1] + 200))
    for arrow in hollow_arrows:
        if arrow == "Down":
            for player in players:
                win.blit(arrow, (player.img_pos[0] - 50, player.img_pos[1] - 100))
    if game_state == states.FnFStates.P1_RECORD or game_state == states.FnFStates.P2_RECORD:
        temp = font.render("Record!   " + str(round(turn_clock, 3)), False, (255, 255, 0))
    elif game_state == states.FnFStates.P1_PLAY or game_state == states.FnFStates.P2_PLAY:
        temp = font.render("Play!   " + str(round(turn_clock, 3)), False, (255, 255, 0))
    else:
        temp = font.render("Cool it!   " + str(round(turn_clock, 3)), False, (255, 255, 0))
    win.blit(temp, (win_dim[0] // 2 - 80, win_dim[1] * 0.1))
    pygame.display.flip()

pygame.quit()