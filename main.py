import requests
import config
import json
from random import randint
import pyperclip
from pynput import keyboard

headers = {"Authorization": f"Bearer {config.api_key}"}
the_one_list = requests.get("https://the-one-api.dev/v2/quote", headers=headers).json()

print('Ready')

#on keystroke run below
# Keyboard shortcut
combination = {keyboard.Key.shift, keyboard.Key.cmd, 
               keyboard.KeyCode(char="6"), keyboard.KeyCode(char="9")}

# The currently active modifiers
current = set()
combo_pressed = False

def on_press(key):
    global combo_pressed
    if key in combination:
        current.add(key)
        if all(k in current for k in combination):
            print('All modifiers active')
            combo_pressed = True
            random_number = randint(0, 999)
            dialog = the_one_list['docs'][random_number]['dialog']
            pyperclip.copy(f"{dialog}")
            #listener.stop()


def on_release(key):
    global combo_pressed
    try:
        current.remove(key)
    except KeyError:
        pass
    if len(current) == 0 and combo_pressed:
        print('coppied')
        combo_pressed = False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()