from tkinter import Tk, Entry, Label, IntVar, Checkbutton, Button, messagebox
from math import pow


def change_metric_display():
    if scale_choice.get() == 0:
        temperature_label['text'] = 'Temperatura (°C)'
        speed_label['text'] = 'Velocidade do Vento (Km/h)'
    else:
        temperature_label['text'] = 'Temperatura (°F)'
        speed_label['text'] = 'Velocidade do Vento (mph)'


def calculate_index():
    if scale_choice.get() == 0:
        t = float(temperature_entry.get())
        v = float(speed_entry.get())

        if t > 10:
            messagebox.showwarning('AVISO', "A fórmula só é efetiva para valores menores que 10°C!")
            return False
        if v < 0:
            messagebox.showwarning('AVISO', "Não existe velocidade negativa!")
            return False
        
        wind_chill_standard_formula(t, v)

    else:
        t = float(temperature_entry.get())
        v = float(speed_entry.get())

        if t > 50:
            messagebox.showwarning('AVISO', "A fórmula só é efetiva para valores menores que 50°F!")
            return False
        if v < 0:
            messagebox.showwarning('AVISO', "Não existe velocidade negativa!")
            return False
        
        wind_chill_american_formula(t, v)


def wind_chill_standard_formula(t, v):
    wci = 13.12 + 0.6215*t - 11.37*pow(v, 0.16) + 0.3965*t*pow(v, 0.16)
    wci = int(wci)

    if wci > -10:
        message = """ Ainda está tranquilo, basta se vestir\nbem para não pegar nenhum resfriado. """
    elif wci > -25:
        message = """ Um pouco frio, risco de hipotermia caso você fique muito\ntempo sem uma proteção adequada. """
    elif wci > -45:
        message = """ Clima Antártico. Cerca de 30 minutos sem proteção\ne você já pode encomendar seu caixão. """
    elif wci > -60:
        message = """ O que quer que você faça, não tire seu casaco.\nCinco minutinhos e você vira presunto. """
    else:
        message = """ Fuja. Corra. Se aqueça. Caso contrário, sua pele\npode congelar antes mesmo que você perceba. """
    
    result_window(wci, message, '°C')


def wind_chill_american_formula(t, v):
    wci = 35.74 + 0.6215*t - 35.75*pow(v, 0.16) + 0.4275*t*pow(v, 0.16)
    wci = int(wci)

    if wci > 15:
        message = """ Ainda está tranquilo, basta se vestir\nbem para não pegar nenhum resfriado. """
    elif wci > -15:
        message = """ Um pouco frio, risco de hipotermia caso você fique muito\ntempo sem uma proteção adequada. """
    elif wci > -50:
        message = """ Clima Antártico. Cerca de 30 minutos sem proteção\ne você já pode encomendar seu caixão. """
    elif wci > -75:
        message = """ O que quer que você faça, não tire seu casaco.\nCinco minutinhos e você vira presunto. """
    else:
        message = """ Fuja. Corra. Se aqueça. Caso contrário, sua pele\npode congelar antes mesmo que você perceba. """
    
    result_window(wci, message, '°F')


def result_window(temperature, message, metric):
    new_window = Tk()
    new_window.resizable(False, False)
    new_window.title("Resultado")

    Label(new_window, text=f'A sensação térmica será de {temperature}{metric}.',
          font=('Laksaman', 16), padx=5).pack()
    Label(new_window, text=message,font=('Laksaman', 16), padx=5).pack(pady=20)

    new_window.mainloop()


window = Tk()
window.resizable(False, False)
window.title("Calculador de Sensação Térmica")

temperature_label = Label(window, text='Temperatura (°C)', font=('Laksaman', 16),
                          padx=10, pady=20)
temperature_label.pack()

temperature_entry = Entry(window, font=('Laksaman', 14), justify=['center'])
temperature_entry.pack()

speed_label = Label(window, text='Velocidade do Vento (Km/h)', font=('Laksaman', 16),
                    padx=10, pady=20)
speed_label.pack()

speed_entry = Entry(window, font=('Laksaman', 14), justify=['center'])
speed_entry.pack()

Button(window, text='CALCULAR', font=('Laksaman', 16),
       command=calculate_index).pack(pady=10)

scale_choice = IntVar()
Checkbutton(window, text='Usar escala americana',
            font=('Laksaman', 12), variable=scale_choice,
            command=change_metric_display, pady=10).pack()

window.mainloop()