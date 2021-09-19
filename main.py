import pygame
import player
import states
pygame.mixer.init()


def score_check(p1, p2, state):
    perfect = 0.2
    good = 0.35
    ok = 0.45
    if state == states.FnFStates.P2_PLAY:
        for time in p1.recording:
            for time2 in p2.recording:
                if time - perfect <= time2 <= time + perfect:
                    # Perfect!
                    if p1.recording[time] == p2.recording[time2]:
                        # Same note
                        p2.score += 1
                        break
                    else:
                        p1.score += 1
                        break
                elif time - good <= time2 <= time + good:
                    # Good!
                    if p1.recording[time] == p2.recording[time2]:
                        # Same note
                        p2.score += 0.75
                        break
                    else:
                        p1.score += 1
                        break
                elif time - ok <= time2 <= time + ok:
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
                if time - perfect <= time2 <= time + perfect:
                    # Perfect!
                    if p2.recording[time] == p1.recording[time2]:
                        # Same note
                        p1.score += 1
                        break
                    else:
                        p2.score += 1
                        break
                elif time - good <= time2 <= time + good:
                    # Good!
                    if p2.recording[time] == p1.recording[time2]:
                        # Same note
                        p1.score += 0.75
                        break
                    else:
                        p2.score += 1
                        break
                elif time - ok <= time2 <= time + ok:
                    # Okay!
                    if p2.recording[time] == p1.recording[time2]:
                        # Same note
                        p1.score += 0.5
                        break
                    else:
                        p2.score += 1
                        break


win_dim = (800, 600)
fs = False  # Fullscreen
win = pygame.display.set_mode(win_dim, pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
done = False
game_state = states.FnFStates.IDLE
p1 = player.Ye(win_dim)
p2 = player.Drake(win_dim)
players = [p1, p2]
bpm = 100
interim_time = 1 / (bpm / 60) * 4
loop_time = 1 / (bpm / 60) * 16
turn_clock = interim_time
font = pygame.font.SysFont("Arial", 24)
last_turn = states.FnFStates.P2_RECORD
hollow_arrows = {"Down": pygame.image.load("images\\down_h.png"), "Left": pygame.image.load("images\\left_h.png"),
                 "Right": pygame.image.load("images\\right_h.png"), "Up": pygame.image.load("images\\up_h.png")}
arrow_y_align = 200
notes = []
prev_notes = 0
winning_score = 30
winner = None
beats = {"Cool Loop": "sounds\\loop1coolname.ogg", "Kickoff": "sounds\\kickoff.ogg"}
pygame.mixer.music.load(beats["Kickoff"])
pygame.mixer.music.play()

while not done:
    # Update
    delta_time = clock.tick() / 1000
    turn_clock -= delta_time
    if turn_clock <= 0:
        if p1.score >= 30 or p2.score >= 30:
            if p1.score > p2.score:
                game_state = states.FnFStates.P1_WIN
                winner = p1.__class__.__name__
            elif p2.score > p1.score:
                game_state = states.FnFStates.P2_WIN
                winner = p2.__class__.__name__
            else:
                pass
        elif game_state == states.FnFStates.P1_RECORD:
            pygame.mixer.music.play()
            game_state = states.FnFStates.P2_PLAY
            turn_clock = loop_time
            pygame.mixer.music.load(beats["Cool Loop"])
            pygame.mixer.music.play()
        elif game_state == states.FnFStates.P2_PLAY:
            score_check(p1, p2, game_state)
            game_state = states.FnFStates.IDLE
            last_turn = states.FnFStates.P1_RECORD
            turn_clock = interim_time
            pygame.mixer.music.load(beats["Kickoff"])
            pygame.mixer.music.play()
        elif game_state == states.FnFStates.P2_RECORD:
            game_state = states.FnFStates.P1_PLAY
            turn_clock = loop_time
            pygame.mixer.music.load(beats["Cool Loop"])
            pygame.mixer.music.play()
        elif game_state == states.FnFStates.P1_PLAY:
            score_check(p1, p2, game_state)
            game_state = states.FnFStates.IDLE
            last_turn = states.FnFStates.P2_RECORD
            turn_clock = interim_time
            pygame.mixer.music.load(beats["Kickoff"])
            pygame.mixer.music.play()
        elif game_state == states.FnFStates.IDLE:
            for player in players:
                player.cur_time = 0
                player.recording = {}
            if last_turn == states.FnFStates.P1_RECORD:
                game_state = states.FnFStates.P2_RECORD
            else:
                game_state = states.FnFStates.P1_RECORD
            turn_clock = loop_time
            pygame.mixer.music.load(beats["Cool Loop"])
            pygame.mixer.music.play()

    for arrow in notes:
        arrow.update(delta_time)
        if arrow.y <= -48:
            notes.remove(arrow)

    # Input
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    elif event.type == pygame.QUIT:
        done = True
    if game_state == states.FnFStates.P1_RECORD or game_state == states.FnFStates.P1_PLAY:
        notes = p1.handle_input(event, game_state, delta_time, loop_time, p2.img_pos, notes)
    elif game_state == states.FnFStates.P2_RECORD or game_state == states.FnFStates.P2_PLAY:
        notes = p2.handle_input(event, game_state, delta_time, loop_time, p2.img_pos, notes)

    # Draw
    win.fill((0, 0, 0))
    for player in players:
        player.draw(win)
        temp = font.render(str(player.score), False, (175, 175, 175))
        win.blit(temp, (player.img_pos[0] + player.img_dim[0] // 2, player.img_pos[1] + 200))
    for arrow in hollow_arrows:
        if arrow == "Down":
            for player in players:
                win.blit(hollow_arrows[arrow], (player.img_pos[0] + 10, player.img_pos[1] - arrow_y_align))
        elif arrow == "Left":
            for player in players:
                win.blit(hollow_arrows[arrow], (player.img_pos[0] - 50, player.img_pos[1] - arrow_y_align))
        elif arrow == "Right":
            for player in players:
                win.blit(hollow_arrows[arrow], (player.img_pos[0] + 70, player.img_pos[1] - arrow_y_align))
        elif arrow == "Up":
            for player in players:
                win.blit(hollow_arrows[arrow], (player.img_pos[0] + 130, player.img_pos[1] - arrow_y_align))
    for arrow in notes:
        arrow.draw(win)
    if game_state == states.FnFStates.P1_RECORD or game_state == states.FnFStates.P2_RECORD:
        temp = font.render("Record!   " + str(round(turn_clock, 3)), False, (255, 255, 0))
    elif game_state == states.FnFStates.P1_PLAY or game_state == states.FnFStates.P2_PLAY:
        temp = font.render("Play!   " + str(round(turn_clock, 3)), False, (255, 255, 0))
    elif game_state == states.FnFStates.IDLE:
        temp = font.render("Cool it!   " + str(round(turn_clock, 3)), False, (255, 255, 0))
    else:
        temp = font.render(winner + " Wins!", False, (0, 255, 0))
    win.blit(temp, (win_dim[0] // 2 - int(temp.get_width()) // 2, win_dim[1] * 0.1))
    pygame.display.flip()

pygame.quit()