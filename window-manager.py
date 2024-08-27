# This only works with X11 window manager
import os
import time
import subprocess

def get_window_id_list():
    try:
        # Get all current windows
        windows = subprocess.check_output(['wmctrl', '-l']).decode('utf-8').splitlines()
        return [line.split()[0] for line in windows]
    except subprocess.CalledProcessError:
        return []

def is_bar_window(window_id):
    try:
        # Check if the window is the own bar.py process
        pid = subprocess.check_output(['wmctrl', '-lp']).decode('utf-8')
        if window_id in pid:
            pid = [line.split()[2] for line in pid.splitlines() if window_id in line][0]
            # Check if the process is bar.py
            command = subprocess.check_output(['ps', '-p', pid, '-o', 'cmd=']).decode('utf-8').strip()
            return "bar.py" in command
    except subprocess.CalledProcessError:
        return False
    return False

def is_onboard_window(window_id):
    try:
        # Get windows class
        window_class = subprocess.check_output(['xprop', '-id', window_id, 'WM_CLASS']).decode('utf-8')
        if "Onboard" in window_class:
            return True
    except subprocess.CalledProcessError:
        return False
    return False

def is_window_maximizable(window_id):
    try:
        # Check if the window allows maximize actions
        allowed_actions = subprocess.check_output(['xprop', '-id', window_id, '_NET_WM_ALLOWED_ACTIONS']).decode('utf-8')
        # Check if the window is a normal window
        window_type = subprocess.check_output(['xprop', '-id', window_id, '_NET_WM_WINDOW_TYPE']).decode('utf-8')

        if ('_NET_WM_ACTION_MAXIMIZE_HORZ' in allowed_actions and 
            '_NET_WM_ACTION_MAXIMIZE_VERT' in allowed_actions and 
            '_NET_WM_WINDOW_TYPE_NORMAL' in window_type):
            return True
    except subprocess.CalledProcessError:
        return False
    return False

def adjust_window(window_id):
    try:
        if not is_bar_window(window_id) and not is_onboard_window(window_id) and is_window_maximizable(window_id):
            # Maximize the window in kiosk mode
            os.system(f'wmctrl -ir {window_id} -b remove,modal')
            os.system(f'wmctrl -ir {window_id} -b remove,sticky')
            os.system(f'wmctrl -ir {window_id} -b remove,maximized_vert,maximized_horz')
            os.system(f'wmctrl -ir {window_id} -b remove,above')
            os.system(f'wmctrl -ir {window_id} -b remove,below')
            os.system(f'wmctrl -ir {window_id} -b add,fullscreen')
    except Exception as e:
        print(f"Error al ajustar la ventana {window_id}: {e}")

def main():
    while True:
        window_ids = get_window_id_list()

        for window_id in window_ids:
            adjust_window(window_id)

        time.sleep(1)

if __name__ == "__main__":
    main()

