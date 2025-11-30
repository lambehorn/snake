import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
import random

# Глобальные настройки
settings = {
    "speed": "Средняя"
}

def play_with_friend():
    open_game_window(mode="friend")

def play_vs_computer():
    open_game_window(mode="computer")

def quit_app():
    if messagebox.askokcancel("Выход"):
        root.destroy()

class Snake:
    def __init__(self, start_pos, direction, color):
        self.body = [start_pos]
        self.direction = direction
        self.next_direction = direction
        self.color = color
        self.score = 0

    def move(self):
        dx, dy = self.next_direction
        head_x, head_y = self.body[0]
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        self.direction = self.next_direction

    def grow(self):
        self.score += 1

    def shrink(self):
        if len(self.body) > 1:
            self.body.pop()

def open_game_window(mode="friend"):
    game_window = tk.Toplevel(root)
    game_window.title("Игра — Змейка")
    game_window.geometry("600x500")
    game_window.resizable(False, False)
    game_window.configure(bg="#FFE5EA")

    # Заголовок
    canvas_title = tk.Canvas(game_window, width=600, height=60, bg="#FFE5EA", highlightthickness=0)
    canvas_title.pack(pady=5)

    title_text = "ИГРА ЗМЕЙКА"
    x, y = 300, 30
    for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
        canvas_title.create_text(x+dx, y+dy, text=title_text,
                                font=("Press Start 2P", 20, "bold"),
                                fill="#E381B1",
                                anchor="center")
    canvas_title.create_text(x, y, text=title_text,
                            font=("Press Start 2P", 20, "bold"),
                            fill="#E381B1",
                            anchor="center")

    # Игровое поле в клетку
    field_width = 400
    field_height = 300
    cell_size = 20
    cols = field_width // cell_size
    rows = field_height // cell_size

    canvas_field = tk.Canvas(
        game_window,
        width=field_width,
        height=field_height,
        bg="#FFF0F5",
        highlightbackground="#E381B1",
        highlightthickness=2
    )
    canvas_field.pack(pady=10)

    for x in range(0, field_width + 1, cell_size):
        canvas_field.create_line(x, 0, x, field_height, fill="#E381B1", width=1)
    for y in range(0, field_height + 1, cell_size):
        canvas_field.create_line(0, y, field_width, y, fill="#E381B1", width=1)

    # Счёт
    score_frame = tk.Frame(game_window, bg="#FFE5EA")
    score_frame.pack(pady=10)

    score_label1 = tk.Label(score_frame, text="Счёт игрока 1:", font=("Candara", 14, 'bold'), 
             fg="#E381B1", bg="#FFE5EA")
    score_label1.grid(row=0, column=0, padx=15)
    score_value1 = tk.Label(score_frame, text="0", font=("Candara", 18, 'bold'), 
             fg="#E381B1", bg="#FFE5EA", width=4)
    score_value1.grid(row=0, column=1)

    score_label2 = tk.Label(score_frame, text="Счёт игрока 2:", font=("Candara", 14, 'bold'), 
             fg="#E381B1", bg="#FFE5EA")
    score_label2.grid(row=1, column=0, padx=15)
    score_value2 = tk.Label(score_frame, text="0", font=("Candara", 18, 'bold'), 
             fg="#E381B1", bg="#FFE5EA", width=4)
    score_value2.grid(row=1, column=1)

    # Инициализация игры
    if mode == "friend":
        snake1 = Snake((5, rows // 2), (1, 0), "#FF6B9D")
        snake2 = Snake((cols - 6, rows // 2), (-1, 0), "#4ECDC4")
        snakes = [snake1, snake2]
    else:
        snake1 = Snake((5, rows // 2), (1, 0), "#FF6B9D")
        snakes = [snake1]
        # Скрываем счет второго игрока в режиме против компьютера
        score_label2.grid_remove()
        score_value2.grid_remove()

    food = None

    def reset_game():
        """Перезапускает игру после столкновения"""
        nonlocal food
        # Сбрасываем змейки в начальное положение
        if mode == "friend":
            snake1.body = [(5, rows // 2)]
            snake1.direction = (1, 0)
            snake1.next_direction = (1, 0)
            snake1.score = 0
            snake2.body = [(cols - 6, rows // 2)]
            snake2.direction = (-1, 0)
            snake2.next_direction = (-1, 0)
            snake2.score = 0
        else:
            snake1.body = [(5, rows // 2)]
            snake1.direction = (1, 0)
            snake1.next_direction = (1, 0)
            snake1.score = 0
        
        # Сбрасываем счет на экране
        score_value1.config(text="0")
        if len(snakes) > 1:
            score_value2.config(text="0")
        
        # Размещаем новую еду
        place_food()
        
        # Перерисовываем игру
        draw_game()

    def place_food():
        nonlocal food
        while True:
            x = random.randint(0, cols - 1)
            y = random.randint(0, rows - 1)
            pos = (x, y)
            occupied = False
            for snake in snakes:
                if pos in snake.body:
                    occupied = True
                    break
            if not occupied:
                food = pos
                break

    place_food()

    def get_speed_delay():
        speed_map = {"Медленная": 200, "Средняя": 150, "Быстрая": 100}
        return speed_map.get(settings["speed"], 150)

    def draw_game():
        canvas_field.delete("snake")
        canvas_field.delete("food")
        
        # Рисуем змейки
        for snake in snakes:
            for i, (x, y) in enumerate(snake.body):
                x1 = x * cell_size
                y1 = y * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                if i == 0:
                    canvas_field.create_rectangle(x1+2, y1+2, x2-2, y2-2, 
                                                fill=snake.color, outline=snake.color, tags="snake")
                else:
                    canvas_field.create_oval(x1+2, y1+2, x2-2, y2-2, 
                                           fill=snake.color, outline=snake.color, tags="snake")
        
        # Рисуем еду
        if food:
            fx, fy = food
            fx1 = fx * cell_size
            fy1 = fy * cell_size
            fx2 = fx1 + cell_size
            fy2 = fy1 + cell_size
            canvas_field.create_oval(fx1+3, fy1+3, fx2-3, fy2-3, 
                                   fill="#FFD700", outline="#FFD700", tags="food")

    def check_collision(snake):
        head_x, head_y = snake.body[0]
        
        # Столкновение со стенами
        if head_x < 0 or head_x >= cols or head_y < 0 or head_y >= rows:
            return True
        
        # Столкновение с собой
        if snake.body[0] in snake.body[1:]:
            return True
        
        # Столкновение с другой змейкой
        for other_snake in snakes:
            if other_snake != snake and snake.body[0] in other_snake.body:
                return True
        
        return False

    def game_loop():
        nonlocal food
        
        # Двигаем змейки
        collision_occurred = False
        for snake in snakes:
            snake.move()
            
            # Проверяем столкновения
            if check_collision(snake):
                collision_occurred = True
                break
            
            # Проверяем еду
            if snake.body[0] == food:
                snake.grow()
                place_food()
                # Обновляем счет
                if snake == snake1:
                    score_value1.config(text=str(snake1.score))
                if len(snakes) > 1 and snake == snake2:
                    score_value2.config(text=str(snake2.score))
            else:
                snake.shrink()
        
        # Если было столкновение, перезапускаем игру
        if collision_occurred:
            reset_game()
        
        draw_game()
        game_window.after(get_speed_delay(), game_loop)

    # Управление клавишами
    def on_key_press(event):
        key = event.keysym.lower()
        
        # Управление для первой змейки (WASD)
        if key == 'w' and snake1.direction != (0, 1):
            snake1.next_direction = (0, -1)
        elif key == 's' and snake1.direction != (0, -1):
            snake1.next_direction = (0, 1)
        elif key == 'a' and snake1.direction != (1, 0):
            snake1.next_direction = (-1, 0)
        elif key == 'd' and snake1.direction != (-1, 0):
            snake1.next_direction = (1, 0)
        
        # Управление для второй змейки (стрелки)
        if len(snakes) > 1:
            if key == 'up' and snake2.direction != (0, 1):
                snake2.next_direction = (0, -1)
            elif key == 'down' and snake2.direction != (0, -1):
                snake2.next_direction = (0, 1)
            elif key == 'left' and snake2.direction != (1, 0):
                snake2.next_direction = (-1, 0)
            elif key == 'right' and snake2.direction != (-1, 0):
                snake2.next_direction = (1, 0)

    game_window.bind('<KeyPress>', on_key_press)
    game_window.focus_set()

    # Начальная отрисовка
    draw_game()
    
    # Запуск игрового цикла
    game_window.after(get_speed_delay(), game_loop)

    tk.Button(game_window, text="← Назад в меню", font=("Candara", 12, 'bold'),
              command=game_window.destroy, bg="#E381B1", fg="white", width=20).pack(pady=15)

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Настройки")
    settings_window.geometry("300x200")
    settings_window.resizable(False, False)
    settings_window.grab_set()
    settings_window.configure(bg="#E381B1")
    tk.Label(settings_window, bg="#E381B1", text="Скорость игры:", 
             font=("Candara", 20, 'bold')).pack(pady=10)

    speed_var = tk.StringVar(value=settings["speed"])
    speeds = ["Медленная", "Средняя", "Быстрая"]
    for speed in speeds:
        tk.Radiobutton(
            settings_window,
            text=speed,
            variable=speed_var,
            value=speed,
            bg="#E381B1",
            font=("Press Start 2P", 11)
        ).pack(anchor="w", padx=50)

    def save_and_close():
        settings["speed"] = speed_var.get()
        settings_window.destroy()

    tk.Button(
        settings_window,
        text="Сохранить",
        font=("Candara", 12),
        bg="#FFE5EA",
        fg="black",
        command=save_and_close
    ).pack(pady=15)

# Главное меню
root = tk.Tk()
root.title("Змейка — Меню")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#FFE5EA")

canvas = Canvas(root, width=400, height=60, bg="#FFE5EA", highlightthickness=0)
canvas.pack(pady=1)

text = "ИГРА ЗМЕЙКА"
x, y = 200, 50
for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
    canvas.create_text(x+dx, y+dy, text=text, 
                     font=("Press Start 2P", 22, "bold"),
                     fill="#E381B1", anchor="center")
canvas.create_text(x, y, text=text,
                  font=("Press Start 2P", 22, "bold"),
                  fill="#E381B1", anchor="center")

tk.Label(root, fg="#E381B1", bg="#FFE5EA", text="на двоих", 
         font=("Candara", 14, 'bold')).pack(pady=0)

tk.Button(root, text="С другом", font=("Candara", 12, 'bold'), width=25, height=2,
          command=play_with_friend, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Против компьютера", font=("Candara", 12, 'bold'), width=25, height=2,
          command=play_vs_computer, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Настройки", font=("Candara", 12, 'bold'), width=25, height=2,
          command=open_settings, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Выход", font=("Candara", 12, 'bold'), width=25, height=2,
          command=quit_app, bg="#FFE5EA", fg="#E381B1").pack(pady=8)

root.mainloop()
