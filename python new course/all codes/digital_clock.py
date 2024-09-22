import tkinter as tk
from time import strftime
from datetime import date

display = tk.Tk()
display.title("Digital_Clock by R0#@n")
display.config(bg="Black")

date_data = tk.Label(display,font=('Arial, 30'), background='Black', foreground='Light Blue')
date_data.pack(pady= 20)
date_data.pack(padx= 20)

time_data = tk.Label(display, font= ("ds-digital",80, "bold"), background= "Black", foreground="Yellow")
time_data.pack(pady=5)
time_data.pack(padx=20)


def Display_Time():
    time = strftime('%H:%M:%S %p')
    time_data.config(text=time)
    time_data.after(1000,Display_Time)

def Display_Date():
    today_date = date.today()
    formatted_date = today_date.strftime('%B %d ,%Y')
    date_data.config(text= formatted_date)


Display_Date()
Display_Time()

display.mainloop()
