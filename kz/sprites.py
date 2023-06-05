import pygame


class Transport(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(x, y))
        # добавляем в группу
        self.add(group)
        self.speed = 2

    def update(self, W):
        if W > self.rect.x > -self.rect.width:
            self.rect.x -= self.speed
        else:
            # теперь не перебрасываем влево,
            # а удаляем из всех групп
            self.kill()


class Passenger(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, path, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image_path = path
        self.rect = self.image.get_rect(center=(x, y))
        # добавляем в группу
        self.add(group)
        self.speed = 1

    def update(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()

    def get_path(self):
        return self.image_path
