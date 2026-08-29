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
                             bg=DARK_SKY)
        self.canvas.pack()

        # Добавим землю
        self.canvas.create_rectangle(
            0, HEIGHT - 20,
            WIDTH, HEIGHT,
            fill=TERRAIN
        )

        # Сама ракета
        self.rocket = self.canvas.create_rectangle(
            WIDTH // 2 - 10, 50,
            WIDTH // 2 + 10, 90,
            fill=RED
        )

        # Добавим физику
        self.y = 50  # Текущая координата верхней точки ракеты
        self.velocity = 0.0  # Скорость падения (изначально стоим)

        # Состояние двигателя
        self.is_engine_on = False

        # Игра запущена? Игровой цикл активен?
        self.is_game_run = True

        # Параметры текста
        self.text_status = self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            anchor='center', fill='yellow',
            font=('Arial', 16)
        )

        # Слушаем клавиатуру
        self.root.bind('<KeyPress-Up>', self.engine_on)
        self.root.bind('<KeyRelease-Up>', self.engine_off)

        # Игровой цикл
        self.update_game()

    # Главный цикл игры
    def update_game(self):
        if not self.is_game_run:
            return

        if self.is_engine_on:
            self.velocity -= THRUST
        else:
            self.velocity += GRAVITY  # Увеличиваем скорость падения

        self.y += self.velocity  # Изменяем координату Y для ракеты
        self.canvas.move(self.rocket, 0, self.velocity)

        # Проверка столкновения с землёй
        rocket_bottom = self.y + 40

        if rocket_bottom >= HEIGHT - 20:
            self.is_game_run = False  # Стоп-игра
            self.check_landing()  # Проверяем скорость встречи с землёй
            return

        # Вызываем update_game каждые 20 миллисекунд
        self.root.after(20, self.update_game)

    def engine_on(self, event):
        if self.is_game_run:  # Двигатель работает пока игра активна
            self.is_engine_on = True
        # print(f'Имя клавиши: {event.keysym}')
        # print(f'Код клавиши: {event.keycode}')

    def engine_off(self, event):
        self.is_engine_on = False

    def check_landing(self):
        if self.velocity <= SAFE_SPEED:
            self.canvas.itemconfig(
                self.text_status,
                text=f'Успешная посадка:\n Скорость: {self.velocity:.2f}',
                fill=GREEN
            )
        else:
            self.canvas.itemconfig(
                self.rocket, fill='black'
            )  # Успешная посадка
            self.canvas.itemconfig(
                self.text_status,
                text=f'Крушение:\n Скорость высока: {self.velocity:.2f}',
                fill=RED
            )  # Ракета почернела - сгорела
