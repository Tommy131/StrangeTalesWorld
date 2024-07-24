'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-21 02:08:40
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-23 00:46:12
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# test.py

import pygame
import sys

class Entity:
    def __init__(self, image_paths, frame_rate):
        self.animations = {key: [pygame.image.load(path) for path in paths] for key, paths in image_paths.items()}
        self.current_state = 'idle'
        self.frame_index = 0
        self.frame_rate = frame_rate
        self.clock = pygame.time.Clock()
        self.facing_left = False

    def update_animation(self):
        self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_state])

    def get_current_image(self):
        image = self.animations[self.current_state][self.frame_index]
        if self.current_state in ['jump', 'crouch'] and self.facing_left:
            return pygame.transform.flip(image, True, False)
        elif self.facing_left:
            return pygame.transform.flip(image, True, False)
        return image

    def set_state(self, state):
        self.current_state = state

    def handle_input(self, keys):
        raise NotImplementedError("Subclasses must implement this method.")

    def draw(self, screen, position):
        current_image = self.get_current_image()
        screen.blit(current_image, position)


class Player(Entity):
    def __init__(self, image_paths, frame_rate):
        super().__init__(image_paths, frame_rate)
        self.last_direction = 'right'

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.facing_left = True
            self.last_direction = 'left'
            self.set_state('run')
        elif keys[pygame.K_RIGHT]:
            self.facing_left = False
            self.last_direction = 'right'
            self.set_state('run')
        elif keys[pygame.K_UP]:
            self.set_state('jump')
        elif keys[pygame.K_DOWN]:
            self.set_state('crouch')
        elif keys[pygame.K_SPACE]:
            self.set_state('attack1')
        else:
            self.set_state('idle')
            self.facing_left = self.last_direction == 'left'

# main.py
def load_images():
    assets_path = 'assets/images/player/'
    # 定义动画帧路径
    image_paths = {
        'idle': [f'{assets_path}adventurer-idle-{i:02d}.png' for i in range(4)] + [f'{assets_path}adventurer-idle-2-{i:02d}.png' for i in range(4)],
        'run': [f'{assets_path}adventurer-run-{i:02d}.png' for i in range(6)],
        'jump': [f'{assets_path}adventurer-jump-{i:02d}.png' for i in range(4)],
        'attack1': [f'{assets_path}adventurer-attack1-{i:02d}.png' for i in range(5)],
        'attack2': [f'{assets_path}adventurer-attack2-{i:02d}.png' for i in range(6)],
        'attack3': [f'{assets_path}adventurer-attack3-{i:02d}.png' for i in range(6)],
        'crouch': [f'{assets_path}adventurer-crouch-{i:02d}.png' for i in range(4)],
        'die': [f'{assets_path}adventurer-die-{i:02d}.png' for i in range(7)],
        'hurt': [f'{assets_path}adventurer-hurt-{i:02d}.png' for i in range(3)],
        'slide': [f'{assets_path}adventurer-slide-{i:02d}.png' for i in range(2)],
        'smrslt': [f'{assets_path}adventurer-smrslt-{i:02d}.png' for i in range(4)]
    }
    return image_paths

def main():
    pygame.init()
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Game Character Animation")

    frame_rate = 10
    image_paths = load_images()
    player = Player(image_paths, frame_rate)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.update_animation()

        screen.fill((0, 0, 0))  # 清屏
        player.draw(screen, (window_size[0] // 2, window_size[1] // 2))
        pygame.display.flip()
        player.clock.tick(frame_rate)

if __name__ == "__main__":
    main()
