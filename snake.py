import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas

# Глобальные настройки
settings = {
    "speed": "Средне"
}

def play_with_friend():
    open_game_window()

def play_vs_computer():
    open_game_window()

def quit_app():
    if messagebox.askokcancel("Выход"):
        root.destroy()

def open_game_window():
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

    tk.Label(score_frame, text="Счёт игрока 1:", font=("Candara", 14, 'bold'), 
             fg="#E381B1", bg="#FFE5EA").grid(row=0, column=0, padx=15)
    tk.Label(score_frame, text="0", font=("Candara", 18, 'bold'), 
             fg="#E381B1", bg="#FFE5EA", width=4).grid(row=0, column=1)

    tk.Label(score_frame, text="Счёт игрока 2:", font=("Candara", 14, 'bold'), 
             fg="#E381B1", bg="#FFE5EA").grid(row=1, column=0, padx=15)
    tk.Label(score_frame, text="0", font=("Candara", 18, 'bold'), 
             fg="#E381B1", bg="#FFE5EA", width=4).grid(row=1, column=1)

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
