from tkinter import *
from tkinter import ttk

def Janela_inicial():
    # Construção da janela
    Inicio = Tk()
    Inicio.title('')
    Inicio.geometry('200x150')
    Inicio.resizable(width=False,height=False)
    
    # Label do titulo
    Label_titulo = Label(Inicio,text='Informações iniciais')
    Label_titulo.grid(row=0,column=0,padx=10,pady=5,columnspan=2)
    
    # Informações para o cronômetro
    label_horas = Label(Inicio,text='Horas:',anchor=E)
    label_horas.grid(row=1,column=0)
    entry_horas = Entry(Inicio,width=10)
    entry_horas.grid(row=1,column=1)

    label_minutos = Label(Inicio,text='Minutos:',anchor=W)
    label_minutos.grid(row=2,column=0)
    entry_minutos = Entry(Inicio,width=10)
    entry_minutos.grid(row=2,column=1)

    label_segundos = Label(Inicio,text='Segundos:',anchor=W)
    label_segundos.grid(row=3,column=0)
    entry_segundos = Entry(Inicio,width=10)
    entry_segundos.grid(row=3,column=1)

    # Função de inserir valores
    def inserir():
        global hora,minuto,segundo
        hora = int(entry_horas.get())
        minuto = int(entry_minutos.get())
        segundo = int(entry_segundos.get())
        Inicio.destroy()

    # Botão para inserir os valores
    btn = Button(Inicio,command=inserir,text='Inserir valores')
    btn.grid(row=4,column=1)
    Inicio.mainloop()

def cronometro():
    # Construção da janela
    cronometro = Tk()
    cronometro.title('Cronômetro')
    cronometro.geometry('275x100')
    cronometro.config(bg='black')
    cronometro.resizable(width=False,height=False)
    
    # Label do titulo
    Label_titulo = Label(cronometro,text='Cronômetro',fg='white',bg='black')
    Label_titulo.grid(row=0,column=0)

    # Contador
    label_hora = Label(cronometro,text=f'{hora}:{minuto}:{segundo}',font=('Arial 25'),fg='blue',bg='black')
    label_hora.grid(row=1,column=1,columnspan = 3)

    btn_iniciar = Button(cronometro,text='Iniciar',relief=RAISED,fg='white',bg='black')
    btn_pausar = Button(cronometro,text='Pausar',relief=RAISED,fg='white',bg='black')
    btn_reiniciar = Button(cronometro,text='Reiniciar',relief=RAISED,fg='white',bg='black')
    btn_iniciar.grid(row=2,column=1)
    btn_pausar.grid(row=2,column=2)
    btn_reiniciar.grid(row=2,column=3)


    cronometro.mainloop()


Janela_inicial()
cronometro()

