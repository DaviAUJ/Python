import pyautogui as auto
import keyboard
import time
import random

songs = ["All I Need", "Creep", "2 + 2 = 5", "Sit Down. Stand Up", "Ful Stop"]

time.sleep(5)

while not keyboard.is_pressed("alt"):
    chosenSong = random.choice(songs)
    
    auto.typewrite(f".sb {chosenSong} Radiohead")
    auto.press("Enter")
    time.sleep(31)
    