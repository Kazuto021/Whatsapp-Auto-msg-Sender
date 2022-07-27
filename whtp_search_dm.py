import pyautogui as pag
import time as t 
import re 

#--------------------------- Searching through the chats using PhoneNumber as primary key------------------------------------------------
def file_split():
    f =open("D:\Intern Web dev\Seldom India\Python\PyAutoGUI\\test.txt",'r') 
    dict={}
    for i in f:
        # li=i.split(":|")
        li=re.split(":|\n",i)
        dict[li[0]]=li[1]

    return dict

def auto_send(text,times):
    for i in range(times):
        pag.typewrite(text)
        pag.press("enter")
        
def search_msg(text,times):
    dict=file_split()
    t.sleep(5)
    ready=pag.prompt("are you ready?")
    if ready.lower()=="yes" or "haan":
        for i in dict:
            pag.press("tab",4)
            pag.typewrite(dict[i],interval=.100)
            pag.press("Enter")
            auto_send(text,times)
            pag.press("tab")
        
__inp__ = pag.prompt("Enter the Text and times to repeat respectively.(Pls use \',\' to separate each field.)\n")
li= str(__inp__).split(",")
text=li[0]
times = int(li[1])
search_msg(text,times)
