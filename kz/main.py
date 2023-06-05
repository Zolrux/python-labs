import pygame
import sys
from random import randint
from sprites import Passenger, Transport
import time

pygame.init()

# Начальные значения

info = {"score": 0,
        "is_increase_score": True,
        "game_run": True,
        "road_move": 0,
        "road_move_step": 1,
        "transports_speed": 2
       }

WIDTH = 700
HEIGHT = 400

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра такси")

FPS = 60
clock = pygame.time.Clock()

# ЦВЕТА (RGB)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Пути к изображениям
transport_path = ("textures/car1.png", "textures/car2.png",
                  "textures/car3.png", "textures/car4.png",
                  "textures/bike.png")
passengers_path = ("textures/passenger_true.png", "textures/passenger_false.png")

def game_render():
    global road, taxi, taxi_rect
    # Создаем дорогу и основную машину (такси)
    road = pygame.image.load("textures/road.jpg").convert()
    road = pygame.transform.scale(road, (road.get_width() * 2, HEIGHT))
    taxi = pygame.image.load("textures/main_car.png").convert_alpha()
    taxi = pygame.transform.scale(
        taxi, (taxi.get_width() // 6, taxi.get_height() // 6))
    taxi_rect = taxi.get_rect(topleft=(0, HEIGHT // 2))
    # pygame.draw.rect(taxi, RED, taxi.get_rect(), 1)

game_render()

# Последнее время спавна пассажира
last_spawn_passenger = time.time()

# Константы
ROAD_TOP_POS = (HEIGHT - 160) - (taxi.get_height() // 2)
ROAD_BOTTOM_POS = ROAD_TOP_POS + 85
taxi_speed = 3

# pygame.draw.rect(window, (255, 0, 0), (0, ROAD_TOP_POS + 40, WIDTH, 130), 2)

# Формируем готовые изображения траснпорта
transport_surf = []
# Формируем готовые изображения пассажиров
passengers_surf = []

# Функции

def colide_passenger():
    for passenger in passengers:
        if passenger.rect.collidepoint(taxi_rect.midright):
            image_path = passenger.get_path().split("/")[-1]
            if "true" in image_path:
                info["score"] += 10
                info["is_increase_score"] = True
                passenger.kill()
            else:
                game_over()


def colide_transport():
    for transport in transports:
        if transport.rect.collidepoint(taxi_rect.midright):
            game_over()


def colide_transport_with_passenger():
    for passenger in passengers:
        for transport in transports:
            if passenger.rect.colliderect(transport.rect):
                passenger.kill()


# По умолчанию скорость автомобилей = 2
def spawn_transport(transports, speed=2):
    rand_transport = transport_surf[randint(0, len(transport_surf) - 1)]
    transport = Transport(WIDTH,
        randint(int(ROAD_TOP_POS), int(ROAD_BOTTOM_POS) + 20),
        rand_transport,
        transports)
    transport.speed = speed


def spawn_passenger(passengers):
    passenger_lst = passengers_surf[randint(0, len(passengers_surf) - 1)]
    image_path, rand_passenger = passenger_lst
    Passenger(WIDTH,
              randint(int(ROAD_TOP_POS), int(ROAD_BOTTOM_POS) + 50),
              rand_passenger,
              image_path,
              passengers)


def score():
    # Распологаем количество очков
    f = pygame.font.Font(None, 24)
    score_text = f.render(f"Очки: {info['score']}", True, WHITE, BLACK)
    score_pos = score_text.get_rect(topleft=(30, 20))
    window.blit(score_text, score_pos)


def game_over():
    # Распологаем результаты (очки и таймер кнопки для запуска игры)
    f = pygame.font.Font(None, 48)
    game_over_text = f.render("GAME OVER", True, RED)
    game_over_pos = game_over_text.get_rect(center=(WIDTH // 2, 50))
    result_text = f.render(f"Очки: {info['score']}", True, WHITE)
    result_pos = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    modal = pygame.Surface((WIDTH, HEIGHT))
    modal.fill(BLACK)

    # Изображение кнопки рестарта
    restart_btn = pygame.image.load("textures/restart_button.png").convert_alpha()
    restart_btn = pygame.transform.scale(
        restart_btn, (restart_btn.get_width() // 5, restart_btn.get_height() // 5))
    restart_btn_rect = restart_btn.get_rect(center=(WIDTH // 2, HEIGHT - 150))

    modal.blit(game_over_text, game_over_pos)
    modal.blit(result_text, result_pos)
    modal.blit(restart_btn, restart_btn_rect)
    window.blit(modal, (0, 0))
    info["game_run"] = False

    # Отлавливаем нажатие кнопки рестарт
    while not info["game_run"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn_rect.collidepoint(event.pos):
                    # Возращаем начальные значение при рестарте
                    info["game_run"] = True
                    info["score"] = 0
                    info["road_move"] = 0
                    info["road_move_step"] = 1
                    info["transports_speed"] = 2
                    passengers.empty()
                    transports.empty()
                    # Рендерим заново дорогу, такси
                    game_render()

        pygame.display.update()
        clock.tick(FPS)


def play(last_spawn_passenger):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == TRANSPORT_EVENT:
                # Каждые 50 очков увеличиваем скорость машин (кроме такси)
                if info["score"] % 10 == 0 and info["score"]:
                    info["transports_speed"] += 0.5
                spawn_transport(transports, info["transports_speed"])
                TRANSPORT_SPAWN_TIME = randint(5000, 10000)
                pygame.time.set_timer(TRANSPORT_EVENT, TRANSPORT_SPAWN_TIME)

        if info["game_run"]:
            window.blit(road, (info["road_move"], 0))  # (Фон который мы видим)
            window.blit(road, (WIDTH + info["road_move"], 0))  # (Фон который мы еще не видим)

            # Проверка времени и создание пассажира
            current_time = time.time()
            # Время спавна пассажира от 7 до 10 секунд
            if current_time - last_spawn_passenger >= randint(7, 10):
                spawn_passenger(passengers)
                last_spawn_passenger = current_time

            if info["road_move"] <= -WIDTH:
                window.blit(road, (0, 0))
                info["road_move"] = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if taxi_rect.y > ROAD_TOP_POS:
                    taxi_rect.y -= taxi_speed

            elif keys[pygame.K_DOWN]:
                if taxi_rect.y < ROAD_BOTTOM_POS:
                    taxi_rect.y += taxi_speed

            transports.draw(window)
            passengers.draw(window)
            colide_passenger()
            colide_transport()
            # При достижении 50 очков машины ( кроме такси ) и
            # пассажири начнут сталкиваться
            if info["score"] % 50 == 0 and info["score"]:
                colide_transport_with_passenger()
            # Каждые 50 очков увеличиваем скорость объектов
            if info["score"] % 50 == 0 \
                    and info["score"] \
                    and info["is_increase_score"]:
                # Увеличиваем скорость на 1
                info["road_move_step"] += 1
                # Для того чтобы увеличить скорость только один раз
                # при увеличении очков
                info["is_increase_score"] = False
            info["road_move"] -= info["road_move_step"]
            window.blit(taxi, taxi_rect)
            score()

            transports.update(WIDTH)
            passengers.update()
        else:
            game_over()

        pygame.display.update()
        clock.tick(FPS)


for i in range(len(transport_path)):
    transport = pygame.image.load(transport_path[i]).convert_alpha()
    transport = pygame.transform.flip(transport, True, False)
    # Уменьшаем картинку в 4 раза
    transport = pygame.transform.scale(
        transport, (transport.get_width() // 6, transport.get_height() // 6))
    # pygame.draw.rect(transport, RED, transport.get_rect(), 1)
    transport_surf.append(transport)


for i in range(len(passengers_path)):
    passengers_surf.append([])
    # Помещаем путь картинки
    passengers_surf[i].append(passengers_path[i])
    passenger = pygame.image.load(passengers_path[i]).convert_alpha()
    # Уменьшаем картинку в 10 раз
    passenger = pygame.transform.scale(
        passenger, (passenger.get_width() // 10, passenger.get_height() // 10))
    # pygame.draw.rect(passenger, RED, passenger.get_rect(), 1)
    # Помещаем пассажира (спрайт)
    passengers_surf[i].append(passenger)

# Создаем группу спрайтов для взаимодействия с ними
transports = pygame.sprite.Group()
passengers = pygame.sprite.Group()

TRANSPORT_EVENT = pygame.USEREVENT
TRANSPORT_SPAWN_TIME = randint(5000, 10000)
# Устанавливаем время появление транспорта (от 5 до 10 секунд)
pygame.time.set_timer(TRANSPORT_EVENT, TRANSPORT_SPAWN_TIME)

# Начало работы
play(last_spawn_passenger)