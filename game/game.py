import random

"""Module providing a function to create game with python."""
import pygame
import game.screens as screens
from game.colors import WHITE, BLACK, RED, GREEN, GRAY
from itertools import cycle


def my_crosshair(crosshair_img):
    """Function draws the crosshair."""
    pygame.draw.circle(crosshair_img, WHITE, (10, 10), 10, 2)
    pygame.draw.line(crosshair_img, WHITE, (0, 10), (20, 10), 2)
    pygame.draw.line(crosshair_img, WHITE, (10, 0), (10, 20), 2)


def hunt_game_start(surface):
    """Function starts the game."""
    width, height = surface.get_width(), surface.get_height()
    pygame.display.set_caption("Duck Shooting Game")

    # Load duck GIF
    duck_frames = []

    try:
        duck_gif = pygame.image.load("./assets/duck.gif")
        # TODO fix duck gif to animated
        for frame_number in range(duck_gif.get_width() // duck_gif.get_height()):
            frame_surf = pygame.Surface(
                (duck_gif.get_height(), duck_gif.get_height()), pygame.SRCALPHA
            )
            frame_surf.blit(
                duck_gif,
                (0, 0),
                (
                    frame_number * duck_gif.get_height(),
                    0,
                    duck_gif.get_height(),
                    duck_gif.get_height(),
                ),
            )
            duck_frames.append(frame_surf)
    except pygame.error:
        print("Error loading the duck GIF. Using a default surface instead.")
        default_duck = pygame.Surface((50, 50))
        default_duck.fill(RED)
        duck_frames = [default_duck]

    if not duck_frames:
        print("No frames were extracted from the GIF. Using a default surface instead.")
        default_duck = pygame.Surface((50, 50))
        default_duck.fill(RED)
        duck_frames = [default_duck]

    duck_cycle = cycle(duck_frames)
    duck_img = next(duck_cycle)
    duck_rect = duck_img.get_rect()
    duck_speed = 3
    # Crosshair
    crosshair_img = pygame.Surface((20, 20), pygame.SRCALPHA)
    my_crosshair(crosshair_img)
    crosshair_rect = crosshair_img.get_rect()
    pygame.mouse.set_visible(False)

    # Fonts
    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 72)

    # Buttons
    button_width, button_height = 200, 50
    button_y = height - button_height - 20
    play_again_button = pygame.Rect(
        (width // 2 - button_width - 10), button_y, button_width, button_height
    )
    exit_button = pygame.Rect((width // 2 + 10), button_y, button_width, button_height)

    def draw_button(surface, text, rect, color):
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, WHITE, rect, 2)
        text_surf = font.render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)

    def reset_game():
        global score, ammo, duck_x, duck_y, duck_dx, change_direction_counter, game_over
        score = 0
        ammo = 10
        duck_x, duck_y = reset_duck()
        duck_dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
        change_direction_counter = 0
        game_over = False

    def reset_duck():
        return random.randint(0, width - duck_rect.width), height

    # Game variables
    score = 0
    ammo = 10

    # Duck position and movement
    duck_x, duck_y = reset_duck()
    duck_dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
    change_direction_counter = 0

    # Game state
    game_over = False
    stage = 1
    # Main game loop
    # TODO implement class
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    if play_again_button.collidepoint(event.pos):
                        reset_game()
                    elif exit_button.collidepoint(event.pos):
                        screens.main_menu_screen(surface=surface, score=score)
                elif not game_over and ammo > 0:
                    ammo -= 1
                    if duck_rect.collidepoint(event.pos):
                        score += 1
                        if score // stage >= stage + 5:
                            print(score)
                            print(stage)
                            stage += 1
                            duck_speed += 1
                        ammo += 2
                        duck_x, duck_y = reset_duck()
                        duck_dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
                        change_direction_counter = 0
                if ammo == 0:
                    game_over = True

        if not game_over:
            # Move the duck
            duck_x += duck_dx
            duck_y -= duck_speed

            duck_rect.x = int(duck_x)
            duck_rect.y = int(duck_y)
            duck_img = next(duck_cycle)

            # Sudden changes in path
            change_direction_counter += 1
            if change_direction_counter >= random.randint(30, 90):
                duck_dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
                change_direction_counter = 0

            # Keep duck within surface bounds horizontally
            if duck_rect.left < 0 or duck_rect.right > width:
                duck_dx *= -1

            # Deduct point if duck leaves the top of the surface
            #
            if duck_rect.bottom < 0:
                score = max(0, score - 1)
                duck_x, duck_y = reset_duck()
                duck_dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
                change_direction_counter = 0

            # Reset duck position if it goes off-surface at the bottom never happens!
            if duck_rect.top > height:
                duck_x, duck_y = reset_duck()
                duck_dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
                change_direction_counter = 0

        # Update crosshair position fixed
        crosshair_rect.center = pygame.mouse.get_pos()

        # Draw everything
        surface.fill(BLACK)
        # create a surface object, image is drawn on it.
        imp = pygame.image.load("./assets/stage.png").convert()

        # Using blit to copy content from one surface to other
        surface.blit(imp, (0, 0))
        if not game_over:
            surface.blit(duck_img, duck_rect)
        surface.blit(crosshair_img, crosshair_rect)

        # Draw score and ammo
        score_text = font.render(f"Score: {score}", True, WHITE)
        ammo_text = font.render(f"Ammo: {ammo}", True, WHITE)
        surface.blit(score_text, (10, 10))
        surface.blit(ammo_text, (width - 120, 10))
        surface.blit(duck_img, duck_rect)

        # Game end surface
        if game_over:
            if score == 0:
                game_over_text = big_font.render("Game Over!", True, RED)
            else:
                game_over_text = big_font.render("Victory!", True, GREEN)

            final_score_text = font.render(f"You Got {score} Duck!", True, WHITE)

            surface.blit(
                game_over_text,
                (width // 2 - game_over_text.get_width() // 2, height // 2 - 50),
            )
            surface.blit(
                final_score_text,
                (width // 2 - final_score_text.get_width() // 2, height // 2 + 50),
            )
            pygame.mouse.set_visible(True)
            # TODO remove crosshair
            draw_button(surface, "Play Again", play_again_button, GRAY)
            draw_button(surface, "Main Menu", exit_button, GRAY)

        pygame.display.flip()
        clock.tick(60)
