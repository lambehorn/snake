import tkinter as tk

def play_with_friend():
    pass

def play_vs_computer():
    pass

def open_settings():
    pass

def quit_app():
    tk.messagebox.showinfo("Выход", "Приложение закроется")
    root.destroy()

root = tk.Tk()
root.title("Змейка — Меню")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#FFE5EA")

# Заголовок
tk.Label(root, text="ИГРА ЗМЕЙКА", font=("Press Start 2P", 20, "bold"), 
         fg="#E381B1", bg="#FFE5EA").pack(pady=30)
tk.Label(root, text="на двоих", font=("Candara", 14, 'bold'), 
         fg="#E381B1", bg="#FFE5EA").pack()

# Кнопки
tk.Button(root, text="С другом", font=("Candara", 12, 'bold'), width=25, height=2,
          command=play_with_friend, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Против компьютера", font=("Candara", 12, 'bold'), width=25, height=2,
          command=play_vs_computer, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Настройки", font=("Candara", 12, 'bold'), width=25, height=2,
          command=open_settings, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Выход", font=("Candara", 12, 'bold'), width=25, height=2,
          command=quit_app, bg="#FFE5EA", fg="#E381B1").pack(pady=8)

root.mainloop()
