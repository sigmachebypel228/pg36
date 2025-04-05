import pygame

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Рисование прямоугольников")
clock = pygame.time.Clock()  # Для управления частотой кадров

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Начальные значения
drawing_rect = False  # Флаг для рисования прямоугольника
start_pos = None  # Начало прямоугольника
rect_color = RED  # Цвет прямоугольника
fill_rect = False  # Флаг для заливки прямоугольника

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing_rect = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing_rect = False
            end_pos = event.pos

            # Рисуем прямоугольник после отпускания кнопки мыши
            rect_width = end_pos[0] - start_pos[0]
            rect_height = end_pos[1] - start_pos[1]
            rect = pygame.Rect(start_pos[0], start_pos[1], rect_width, rect_height)
            pygame.draw.rect(screen, rect_color, rect, width=1 if not fill_rect else 0)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            fill_rect = not fill_rect  # Переключение между контурным и заливочным режимом

    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка текущего состояния прямоугольника
    if drawing_rect:
        current_pos = pygame.mouse.get_pos()
        rect_width = current_pos[0] - start_pos[0]
        rect_height = current_pos[1] - start_pos[1]
        rect = pygame.Rect(start_pos[0], start_pos[1], rect_width, rect_height)
        pygame.draw.rect(screen, rect_color, rect, width=1 if not fill_rect else 0)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров до 60 FPS
    clock.tick(60)

# Завершение работы
pygame.quit()