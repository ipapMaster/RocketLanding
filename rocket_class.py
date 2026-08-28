from constants import *
from tkinter import Canvas


class RocketGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Посади ракету')

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
