from pynput.keyboard import Key, Controller
import pyperclip
import pyautogui
import sys
import os
import time

keyboardController = Controller()

def fetch_phrase(phrase, configuration):

    for i in range(len(phrase)+2):
        keyboardController.press(Key.backspace)
        keyboardController.release(Key.backspace)

    if phrase in configuration['CONFIGURATION'].keys():
        pyperclip.copy(configuration['CONFIGURATION'][phrase])
        keyboardController.press(Key.ctrl)
        keyboardController.press('v')
        keyboardController.release('v')
        keyboardController.release(Key.ctrl)

    elif phrase == 'quit':
        time.sleep(1)
        pyautogui.alert('Program will be shut down after clicking OK...', title='TextMotes')
        sys.exit(0)

    elif phrase == 'restart':
        time.sleep(1)
        pyautogui.alert('Program will be restarted after clicking OK...', title='TextMotes')
        program_name = ''
        for i in sys.argv[0][::-1]:
            if i != '\\': program_name += i
            else: break
        os.system('start ' + program_name[::-1])
        sys.exit(0)
        
    elif phrase == 'emotes':
        time.sleep(1)
        summary = ''
        for i in configuration['CONFIGURATION'].keys():
            summary = summary + ';' + i + '; > ' + configuration['CONFIGURATION'][i] + '\n'
        pyautogui.alert('List of all configured emotes in config.ini:\n\n' + summary + '\n;quit; > quit the program\n;restart; > restart the program and reload configuration', title='TextMotes')
