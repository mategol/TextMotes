from pynput import keyboard
from pynput.keyboard import Key, Controller
from resources.phrase_fetcher import *
import pyperclip
import configparser
import sys
import pyautogui
import time
import os

phrase_buffer = ''
fence = True
configuration = configparser.ConfigParser()

if 'config.ini' in os.listdir('.'):
    configuration.read('config.ini', encoding='utf-8')
else:
    pyautogui.alert('Failed to detect configuration file. Generating new one with default settings', title="TextMotes")
    configuration['CONFIGURATION'] = {'updown': '🙃', 'heart': '❤', 'smile': '🙂', 'proud': '😁', 'wink': '😉', 'angel': '😇', 'think': '🤔', 'throw': '🤮', 'cowboy': '🤠', 'like': '👍', 'sleep': '😴', 'fright': '😬', 'shh': '🤫', 'faceless': '😶', 'swag': '😎', 'susp': '🧐', 'tear': '😢', 'sad': '😕', 'angry': '😡', 'skull': '💀', 'love': '😍', 'tong': '😛', 'cry': '😭', 'party': '🥳'}
    with open('config.ini', 'w', encoding='utf-8') as config_file:
        configuration.write(config_file)

if 'quit' in configuration['CONFIGURATION'].keys() or 'restart' in configuration['CONFIGURATION'].keys() or 'emotes' in configuration['CONFIGURATION'].keys():
    pyautogui.alert('You named an emote with restricted phrase. Restricted phrases are:\n- quit\n- restart\n-emotes', title='TextMotes - shutting down')
    sys.exit(0)

def on_press(key):
    global phrase_buffer, fence
    if str(key) != 'Key.space':
        if str(key)[:4] != 'Key.':
            if str(key).replace("'", '') == ';' and fence == True:
                fence = False
            elif str(key).replace("'", '') == ';' and fence == False:
                fetch_phrase(phrase_buffer, configuration)
                phrase_buffer, fence = '', True
            elif fence == False:
                phrase_buffer += str(key).replace("'", '')
            else:
                phrase_buffer = ''
        elif str(key) != 'Key.shift':
            if str(key) == 'Key.backspace' and fence == False:
                phrase_buffer = phrase_buffer[:-1]
            else:
                phrase_buffer, fence = '', True
    else:
        phrase_buffer, fence = '', True

pyautogui.alert('PROGRAM   S T A R T E D\n\nType ;quit; anywhere to exit the program in any moment.', title='TextMotes')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

listener = keyboard.Listener(on_press=on_press)
listener.start()