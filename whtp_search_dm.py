import pyautogui as pag
import time as t 
import re 

#--------------------------- Searching through the chats using PhoneNumber as primary key------------------------------------------------
def file_split():
    f =open("D:\\project\\Whatsapp-Auto-msg-Sender\\test.txt",'r') 
    dict={}
    for i in f:
        # li=i.split(":|")
        li=re.split(":|\n",i)
        dict[li[0]]=li[1]
    f.close()
    return dict

def auto_send(text,times):
    for i in range(times):
        pag.typewrite("> ",interval=0.4)
        pag.typewrite(text,interval=1)
        pag.press("Enter")
        
def search_msg(text,times):
    dict=file_split()
    t.sleep(5)
    ready=pag.prompt("are you ready?")
    if ready.lower()=="yes" or "haan":
        for i in dict:
            # pag.press("tab",8)
            pag.hotkey("ctrl","f")
            pag.typewrite(dict[i],interval=0.2)
            pag.press("tab")
            pag.press("Enter")
            auto_send(text,times)
            # pag.press("tab")
        
__inp__ = pag.prompt("Enter the Text and times to repeat respectively.(Pls use \',\' to separate each field.)\n")
li= str(__inp__).split(",")
text=li[0]
times = int(li[1])
search_msg(text,times)

