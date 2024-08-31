import tkinter as tk
import os
import subprocess

# Where is stored the PiNtuitiveUI executable
app_image_path = os.path.abspath("./ui/dist/PiNtuitiveUI.AppImage")
ui_window_name = "PiNtuitive UI"

from keyboard import Keyboard

class AutoHideBar:
    def __init__(self, root):
        self.root = root
        self.hidden = False
        self.timer = None
        self.bar_height = 50 
        self.keyboard = Keyboard(root)  # Create a keyboard instance
        
        # Window configuration
        self.root.overrideredirect(True)
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.bar_height}+0+{self.root.winfo_screenheight()-self.bar_height}")
        self.root.attributes("-topmost", True)
        self.root.configure(bg='black')
        
        # Bar canvas
        self.canvas = tk.Canvas(root, width=self.root.winfo_screenwidth(), height=50, bg='black', highlightthickness=0)
        self.canvas.pack(expand=True, fill='both')
        
        # Draw a close button (X)
        x_center = self.root.winfo_screenwidth() // 2
        self.close_button = self.canvas.create_line(x_center - 10, 15, x_center + 10, 35, fill="white", width=4)
        self.close_button_2 = self.canvas.create_line(x_center + 10, 15, x_center - 10, 35, fill="white", width=4)
        
        # Bind close event only to the close button
        self.canvas.tag_bind(self.close_button, '<Button-1>', lambda e: self.close_all_windows())
        self.canvas.tag_bind(self.close_button_2, '<Button-1>', lambda e: self.close_all_windows())

        # Button to open/close the keyboard
        self.keyboard_button = tk.Button(root, text="⌨️", command=self.toggle_keyboard, bg='black', fg='white', borderwidth=0, font=('Arial', 20))
        self.keyboard_button.place(x=self.root.winfo_screenwidth() - 60, y=0, width=60, height=50)
        
        # Reset timer
        self.reset_timer()

        # Start checking mouse position
        self.root.after(100, self.check_mouse_position)

        self.execute_ui()

    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        # Reset the timer only if the keyboard is not open
        if not self.keyboard.keyboard_open:
            self.timer = self.root.after(15000, self.hide_bar)  # Hide the bar after 15 seconds of inactivity
        print("Timer reset")

    def hide_bar(self):
        if not self.keyboard.keyboard_open:  # Only hide the bar if the keyboard is not open
            print("Hiding bar")
            self.hidden = True
            self.root.withdraw()  # Hide the window
        else:
            print("Keyboard is open, not hiding the bar")

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
        self.keyboard.close_keyboard()
        current_pid = os.getpid()
        
        windows = self.get_all_windows()
        for window in windows:
            self.maybe_close_window(window, current_pid)
        
        self.execute_ui()

    def get_all_windows(self):
        """Get all open windows."""
        windows = os.popen('wmctrl -lp').readlines()
        return windows

    def maybe_close_window(self, window, current_pid):
        """Close the window if it doesn't belong to the current process or PiNtuitiveUI.AppImage."""
        window_fields = window.split()
        window_pid = window_fields[2]
        window_name = ' '.join(window_fields[4:])

        # Do not close the window if its name contains ui_window_name
        if ui_window_name in window_name:
            print(f"Skipping window: {window_name} with ID: {window_fields[0]}")
            return

        # Check if the window_pid belongs to the current process or PiNtuitiveUI.AppImage
        if str(current_pid) not in window:
            window_id = window_fields[0]
            print(f"Closing window with ID: {window_id}, PID: {window_pid}, Name: {window_name}")
            os.system(f'wmctrl -ic {window_id}')

    def execute_ui(self):
        print(f"Checking if {app_image_path} exists and is not running...")
        if os.path.exists(app_image_path):
            try:
                process_check = subprocess.run(['pgrep', '-f', 'PiNtuitiveUI.AppImage'], stdout=subprocess.PIPE)
                if not process_check.stdout:
                    print("AppImage not running. Attempting to launch...")
                    subprocess.Popen([app_image_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    print("AppImage is already running.")
            except Exception as e:
                print(f"Error while trying to execute the application: {e}")
        else:
            print(f"AppImage not found at {app_image_path}")

    def toggle_keyboard(self):
        """Open or close the virtual keyboard."""
        if self.keyboard.keyboard_open:
            self.keyboard.close_keyboard()
            self.reset_timer() 
        else:
            self.keyboard.open_keyboard()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoHideBar(root)
    root.mainloop()
