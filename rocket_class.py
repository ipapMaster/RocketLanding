from constants import *
from tkinter import Canvas


class RocketGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Посади ракету')
        self.root.resizable(False, False)

        # Добавляем холст
        self.canvas = Canvas(root,
                             width=WIDTH,
                             height=HEIGHT,
                             bg='#1a1a2e')
        self.canvas.pack()

        # Добавим землю
        self.canvas.create_rectangle(
            0, HEIGHT - 20,
            WIDTH, HEIGHT,
            fill='#16a085'
        )

        self.rocket = self.canvas.create_rectangle(
            WIDTH // 2 - 10, 50,
            WIDTH // 2 + 10, 90,
            fill='#e74c3c'
        )

        # Добавим физику
        self.y = 50  # Текущая координата верхней точки ракеты
        self.velocity = 0.0  # Скорость падения (изначально стоим)

        # Игровой цикл
        self.update_game()

    # Главный цикл игры
    def update_game(self):
        self.velocity += GRAVITY  # Увеличиваем скорость падения
        self.y += self.velocity  # Изменяем координату Y для ракеты
        self.canvas.move(self.rocket, 0, self.velocity)

        # Вызываем update_game каждые 20 миллисекунд
        self.root.after(20, self.update_game)
