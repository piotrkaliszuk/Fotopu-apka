from tkinter import *
import datetime
from subprocess import call
import subprocess, sys
from testtt import kamera
from ROI import wykrywacz_ruchu
from ROIStatic import wykrywacz_ruchu_statyczny

screen = Tk()
screen.geometry("500x380")
screen.title("Kamera")
now = datetime.datetime.now()
dt = now.strftime("%m/%d/%Y")
Label(text="").pack()
Label(text =
      f'Widok kamery', font = ('Calibri',13)).pack()
Label(text = "").pack()
Label(text="").pack()
#def kamera1():
    #kamera()
def wykrywacz():
    wykrywacz_ruchu()
def wykrywacz_statyczny():
    wykrywacz_ruchu_statyczny()
def wylacz():
    screen.destroy()
def biblioteka():
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, '/home/piotrek/PycharmProjects/pythonProject2/Zrzuty'])
Button(text='Włącz wykrywacz ruchu statyczny', height='2', width='30', command=wykrywacz_statyczny).pack()
Button(text ='Włącz wykrywacz ruchu',height = '2',width = '30',command = wykrywacz).pack()
Button(text ='Pokaż biblioteke',height = '2',width = '30',command = biblioteka).pack()
Button(text ='Wyjście',height = '2',width = '30',command = wylacz).pack()
Label(text="").pack()
Label(text="").pack()
Label(text=f'{dt}', bg='grey',width = '300',height = '2', font=('Calibri', 13)).pack()
#Label(text=f'Wciśnij "SPACE" aby wykonać zrzut ekranu lub "ESC" aby wyjść', bg='grey', width='300', height='2', font=('Calibri', 8)).pack()

screen.mainloop()


