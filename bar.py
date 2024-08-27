import tkinter as tk
import os

class AutoHideBar:
    def __init__(self, root):
        self.root = root
        self.hidden = False
        self.timer = None
        self.bar_height = 50 
        
        # Window configuration
        self.root.overrideredirect(True)
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.bar_height}+0+{self.root.winfo_screenheight()-self.bar_height}")
        self.root.attributes("-topmost", True)
        self.root.configure(bg='black')
        
        # bar canvas
        self.canvas = tk.Canvas(root, width=self.root.winfo_screenwidth(), height=50, bg='black', highlightthickness=0)
        self.canvas.pack(expand=True, fill='both')
        
        # Draw a close button
        x_center = self.root.winfo_screenwidth() // 2
        self.canvas.create_line(x_center - 10, 15, x_center + 10, 35, fill="white", width=4)
        self.canvas.create_line(x_center + 10, 15, x_center - 10, 35, fill="white", width=4)
        
        # Add cose event
        self.canvas.bind('<Button-1>', lambda e: self.close_all_windows(), add="+")
        
        # Button to open the keyboard
        self.keyboard_button = tk.Button(root, text="⌨️", command=self.open_keyboard, bg='black', fg='white', borderwidth=0, font=('Arial', 20))
        self.keyboard_button.place(x=self.root.winfo_screenwidth() - 60, y=0, width=60, height=50)
        
        # Reset timer
        self.reset_timer()

        # Start checking mouse position
        self.root.after(100, self.check_mouse_position)
        
    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.timer = self.root.after(15000, self.hide_bar)  # Hide the bar after 15 seconds of inactivity
        print("Timer reset")

    def hide_bar(self):
        print("Hiding bar")
        self.hidden = True
        self.root.withdraw()  # Hide the window

    def show_bar(self):
        print("Showing bar")
        self.hidden = False
        self.root.deiconify()  # Show the window
        self.reset_timer()

    def check_mouse_position(self):
        x, y = self.root.winfo_pointerxy()
        screen_height = self.root.winfo_screenheight()
        
        # If mouse is at the bottom, show the bar
        if self.hidden and y >= screen_height - self.bar_height:
            print("Mouse detected at the bottom, showing bar")
            self.show_bar()

        self.root.after(100, self.check_mouse_position)

    def close_all_windows(self):
        # Close all windows but the bar
        current_pid = os.getpid()
        windows = os.popen('wmctrl -lp').readlines()
        for window in windows:
            if str(current_pid) not in window:
                window_id = window.split()[0]
                os.system(f'wmctrl -ic {window_id}')
    
    def open_keyboard(self):
        # Open keyboard. This doesn't work as expected, needs refinement
        os.system("matchbox-keyboard &")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoHideBar(root)
    root.mainloop()

