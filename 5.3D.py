import tkinter as tk
import tkinter.messagebox as tkmb
import RPi.GPIO as GPIO
import time

# set up the board
GPIO.setmode(GPIO.BCM)

# set up the pin(s)
GPIO.setup(14, GPIO.OUT) #red

# Function for a Dash or Dot 'Blink'
def blink_dotdash(dotdash):
   # turn on
   GPIO.output(14, GPIO.HIGH)
   # keep on for a dot/dash
   time.sleep(dotdash)
   # turn off
   GPIO.output(14, GPIO.LOW)
   
def blinkChar(strChar, dot, dash, compSpace, charSpace):   
    if (strChar.lower() == 'a'):
        blink_dotdash(dot)
        time.sleep(compSpace)       
        blink_dotdash(dash)
    elif (strChar.lower() == 'b'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)  
    elif (strChar.lower() == 'c'):
        blink_dotdash(dash) 
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'd'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'e'):
        blink_dotdash(dot)
    elif (strChar.lower() == 'f'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'g'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'h'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'i'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'j'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'k'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'l'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'm'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'n'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'o'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'p'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 'q'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'r'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)  
    elif (strChar.lower() == 's'):
        blink_dotdash(dot) 
        time.sleep(compSpace)
        blink_dotdash(dot) 
        time.sleep(compSpace)
        blink_dotdash(dot)
    elif (strChar.lower() == 't'):
        blink_dotdash(dash)
    elif (strChar.lower() == 'u'):
        blink_dotdash(dot) 
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'v'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'w'):
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'x'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'y'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
    elif (strChar.lower() == 'z'):
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dash)
        time.sleep(compSpace)
        blink_dotdash(dot)
        time.sleep(compSpace)
        blink_dotdash(dot)
    else:
        time.sleep(charSpace)
def blink():
    # set up the variables for Morse code
    morseUnit = 1
    dot = 1 * morseUnit
    dash = 3 * morseUnit

    compSpace = 1 * morseUnit # The space between the components of one character is one unit
    charSpace = 3 * morseUnit # The space between characters is three units
    wordSpace = 7 * morseUnit # The space between words is seven units

    x = entry_box.get()
    
    if len(x) == 0:
        tkmb.showerror(title=None, message='no characters entered')
    elif len(x) > 12:
        tkmb.showerror(title=None, message='too many characters entered\n maximum numbers of 12 characters')
    elif x.replace(' ','').isalpha() == False:
        tkmb.showerror(title=None, message='non alpha characters entered')        
    else:
        for i in range(len(x)):
            blinkChar(x[i], dot, dash, compSpace, charSpace)
            if x[i] == ' ':
                time.sleep(wordSpace - charSpace)
            elif i < len(x):
                time.sleep(charSpace)
            else:
                time.sleep(wordSpace)
    
def system_exit():
    GPIO.output(14, GPIO.LOW)
    window.destroy()

## GUI Definitions ##
window = tk.Tk()
window.title("Morse GUI")

v = tk.IntVar()
    
frame_a = tk.Frame(master=window, height = 10)
frame_a.pack(fill = tk.BOTH, side = tk.TOP, expand = True)

label_a = tk.Label(text = 'Enter a word\n(maximum 12 characters)', fg='white', bg='SlateGray3', width=20, height=3)
label_a.pack(fill = tk.X, side = tk.TOP, expand = True, padx = 10, pady = 5)

entry_box = tk.Entry (window)
entry_box.pack()

blinkbutton = tk.Button(text = 'Blink Word', command = blink)
blinkbutton.pack(pady = 2)

exitbutton = tk.Button(text = 'Exit', width = 20, command = system_exit)
exitbutton.pack(fill = tk.X, side = tk.BOTTOM, padx = 10, pady = 5, expand = True)

window.mainloop()

GPIO.cleanup()