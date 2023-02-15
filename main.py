#Import the required Libraries
from tkinter import Label,Tk,Toplevel
import pygame, time, keyboard, ctypes
from random import randint
from pynput.keyboard import Key,Controller

user32= ctypes.windll.user32

list=[
    "“Success is not final; failure is not fatal: It is the courage to continue that counts.” — Winston S. Churchill",
    "“It is better to fail in originality than to succeed in imitation.” — Herman Melville",
    "“The road to success and the road to failure are almost exactly the same.” — Colin R. Davis",
    "“Success usually comes to those who are too busy looking for it.” — Henry David Thoreau",
    "“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie",
    "“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers",
    "“Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.” —John Wooden",
    "“I never dreamed about success. I worked for it.” —Estée Lauder",
    "“Success is getting what you want, happiness is wanting what you get.” ―W. P. Kinsella",
    "“The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.” — Winston Churchill",
    "“Don’t let yesterday take up too much of today.” — Will Rogers",
    "“You learn more from failure than from success. Don’t let it stop you. Failure builds character.” — Unknown",
    "“If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you.” — Steve Jobs",
    "“Experience is a hard teacher because she gives the test first, the lesson afterwards.” ―Vernon Sanders Law",
    "“To know how much there is to know is the beginning of learning to live.” —Dorothy West",
    "“Goal setting is the secret to a compelling future.” — Tony Robbins",
]

def on_closing():
    sound.play()
    top= Toplevel()
    top.wm_attributes("-topmost", 1)
    top.configure(bg='white')
    x = randint(10,900)
    y = randint(10,700)
    top.geometry("+%d+%d" %(x,y))
    top.geometry("900x50")
    top.title("Information")
    Label(top, text= list[randint(0,len(list)-1)], font=('Arial 12 italic'), bg='white').place(x=450,y=25, anchor='center')
    k.press(Key.media_volume_up)
    time.sleep(0.5)
    k.release(Key.media_volume_up)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
sound=pygame.mixer.Sound("sound.wav")
k=Controller()

for i in range(0,randint(4,12)) :
    keyboard.wait('space')

win = Tk()
win.wm_attributes("-topmost", 1)
win.geometry("1000x300")
win.title("Goofist")
win.configure(bg='blue')
Label(win, text= "You've been goofed !", font=('Arial 72 bold'), bg='blue', fg='#fff').place(x=500,y=150, anchor="center")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)

k.press(Key.media_volume_up)
time.sleep(0.5)
k.release(Key.media_volume_up)


win.protocol("WM_DELETE_WINDOW", on_closing)

win.mainloop()

pygame.display.flip()