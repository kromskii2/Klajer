import tkinter as tk
import webbrowser

class RoundedMenuApp:
    def __init__(self, width, height, corner_radius):
        self.width = width
        self.height = height
        self.corner_radius = corner_radius

        self.root = tk.Tk()
        self.root.title("Klajer")  # Изменено название приложения

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

    def open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com/")

    def run(self):
        self.root.mainloop()


# Create and run the application
app = RoundedMenuApp(width=646, height=396, corner_radius=30)
app.run()
