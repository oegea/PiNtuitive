import tkinter as tk
import pyautogui  # Import pyautogui to send keyboard events to the operating system

class Keyboard:
    def __init__(self, root):
        self.root = root
        self.keyboard_window = None
        self.keyboard_open = False
        self.symbol_layout = False  # Variable to track the current layout
        self.caps_lock = False  # Variable to track the state of Caps Lock

    def open_keyboard(self):
        self.keyboard_open = True
        self.keyboard_window = tk.Toplevel(self.root)
        self.keyboard_window.title("Keyboard")
        self.keyboard_window.geometry(f"{self.root.winfo_screenwidth()}x250+0+{self.root.winfo_screenheight()-300}")
        self.keyboard_window.overrideredirect(True)

        self.keyboard_frame = tk.Frame(self.keyboard_window, bg='black')
        self.keyboard_frame.pack(expand=True, fill='both')

        self.display_keyboard()

    def display_keyboard(self):
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()

        if self.symbol_layout:
            # Define the symbol keyboard layout
            keys = [
                ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
                ['-', '_', '=', '+', '[', ']', '{', '}', ';', '/'],
                ['QWERTY', 'Space', 'Enter', 'Delete']
            ]
        else:
            # Define the QWERTY keyboard layout
            keys = [
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                ['Caps', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.'],
                ['Symbols', 'Space', 'Enter', 'Delete']
            ]

        row_sizes = [5, 5, 5, 10]
        special_keys = {'Space': 20, 'Enter': 10, 'Delete': 10}

        for row_index, row in enumerate(keys):
            key_frame = tk.Frame(self.keyboard_frame, bg='black')
            key_frame.pack(side='top', pady=5)
            for key in row:
                width = special_keys.get(key, row_sizes[row_index])
                
                # Set the background color for Caps Lock based on its state
                bg_color = 'white' if key == 'Caps' and self.caps_lock else 'black'
                fg_color = 'black' if key == 'Caps' and self.caps_lock else 'white'
                
                btn = tk.Button(key_frame, text=key, command=lambda k=key: self.press_key(k), width=width, height=2, bg=bg_color, fg=fg_color, relief='flat', padx=5, pady=5)
                btn.pack(side='left', padx=5)

    def press_key(self, key):
        if key == "Space":
            pyautogui.write(' ')
        elif key == "Delete":
            pyautogui.press('backspace')
        elif key == "Enter":
            pyautogui.press('enter')
        elif key == "Symbols":
            self.symbol_layout = True
            self.display_keyboard()
        elif key == "QWERTY":
            self.symbol_layout = False
            self.display_keyboard()
        elif key == "Caps":
            self.caps_lock = not self.caps_lock  # Toggle Caps Lock state
            self.display_keyboard()  # Refresh keyboard to reflect Caps Lock state
        else:
            if self.caps_lock and key.isalpha():  # Check if Caps Lock is active and key is a letter
                pyautogui.write(key.upper())
            else:
                pyautogui.write(key)

    def close_keyboard(self):
        if self.keyboard_window:
            self.keyboard_window.destroy()
        self.keyboard_open = False

# Sample usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    keyboard = Keyboard(root)
    
    open_button = tk.Button(root, text="Open Keyboard", command=keyboard.open_keyboard)
    open_button.pack(pady=20)
    
    close_button = tk.Button(root, text="Close Keyboard", command=keyboard.close_keyboard)
    close_button.pack(pady=20)
    
    root.mainloop()