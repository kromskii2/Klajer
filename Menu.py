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
