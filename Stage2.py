import tkinter as tk
import time,datetime

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Время до начала курса")
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
            """ Функция вычисляет разницу между датой начала курса и текущей датой и выводит ее на виджет
                В случае, если текущая дата больше даты начала курса, выводит сообщение, что курс уже начался """
        courseStarts = datetime.datetime(2018, 10, 10, 18, 20, 00, 000000)
        now = datetime.datetime.now()
        delta = courseStarts - now
        days = delta.days
        hours = (delta.seconds%86400)//3600
        minutes = ((delta.seconds%86400)%3600)//60
        seconds = ((delta.seconds%86400)%3600)%60
        if courseStarts > now:
            message = "До начала курса осталось: {} дней {} часов {} минут {} секунд"
        else:
            message = "Курс уже начался"
        self.label.configure(text=message.format(days,hours,minutes,seconds))
        self.root.after(1000, self.update_clock)

app=App()
  
