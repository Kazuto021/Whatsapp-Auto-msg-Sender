import pyautogui as pag
import time as t 

# ---------------------------- dming the users through the order they appeared in the current state of chat-------------
# def repeat(text,times):
#     for j in range(times):
#         pag.typewrite(text,0.030)
#         pag.typewrite("\n")
    
# def auto_send(user_count,text,times):
#     t.sleep(5)
#     state= str(pag.prompt("Are you ready?"))
#     if state.lower()=="yes": 
#         for i in range(1,user_count+1):
#             if i ==1:
#                 tabs = 4+i
#                 pag.press("tab",presses=tabs)
#                 pag.press('down',presses=i)
#                 pag.press('enter')
#                 repeat(text,times)
#             elif i>1:
#                 tabs=5+i
#                 pag.press("tab",presses=tabs)
#                 pag.press('down',presses=i)
#                 pag.press('enter')
#                 repeat(text,times)
                
# __inp__ = pag.prompt("Enter the Text, Number of users, and times to repeat respectively.(Pls use \',\' to separate each field.)\n")

# li= str(__inp__).split(",")
# text=li[0]
# user_count = int(li[1])
# times=int(li[2])
# auto_send(user_count,text,times)


