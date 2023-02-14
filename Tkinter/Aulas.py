from tkinter import *
from tkinter import ttk

### AULA 2 ### (Janela básica)
## Abre a janela
janela = Tk()
## Define o titulo da janela
janela.title('Aulas Tkinter')
## Configurar o tamanho da janela
janela.geometry('300x250')
## Alterando a cor de fundo da janela
#janela.config(bg='blue')
## Alterando o icone da janela
janela.iconphoto(False,PhotoImage(file='D:\Rafael\Documents\Codigos\Python\Tkinter\logo.png'))
## Tornando a janela nãp redimensionável
janela.resizable(width=False,height=False)

### AULA 3 ### (Label)
## Criação do label
#label_1 = Label(janela,width=10,height=2,text='Label 1:',font=('Arial 15'),fg='white',bg='blue')
#label_1.grid(row=0,column=0,pady=10)

#Label_2 = Label(janela,width=10,height=2,text='Label 2:',font=('Arial 15 bold'),fg='gray',bg='blue')
#Label_2.grid(row=1,column=0,pady=10)

#label_3 = Label(janela,width=10,height=2,text='Label 3:',font=('Arial 15 bold italic'),fg='red',bg='blue')
#label_3.grid(row=2,column=0,pady=10)
# Resumo da caracteristicas
'''
LABEL
Font é a fonte do gtextop de dentro da label
fg é a cor do texto
bg é a cor do background

GRID
row é a linha
column é a a coluna
pady é o espaçamento
'''

### AULA 4 ### (Gerenciamento de geometria)
## Place() - Usa parametros de x e y para gerenciar os widgets
#ttk.Label(janela, width=20, text='Place').place(x=150, y=10)

## Pack() - Usa direções para gerenciar os widgets (RIGHT,LEFT,TOP,BOTTOM) - Menos usado - Obs: Se usar Pack não é possível usar o grid
#ttk.Label(janela, width=20, text='Pack 1').pack(side=BOTTOM)
#ttk.Label(janela, width=20, text='Pack 2').pack(side=BOTTOM)
#ttk.Label(janela, width=20, text='Pack 3').pack(side=BOTTOM)

## Grid() - Gerencia as posições comomse fosse uma planilha de excel, usando parametros rows(Linhas) e columns(Colunas)
#Label_0 = Label(janela,width=15,height=5,justify=CENTER,text='Linha: 0 Coluna: 0')
#Label_0.grid(row=0,column=0)
#Label_1 = Label(janela,width=15,height=5,justify=CENTER,text='Linha: 1 Coluna: 1')
#Label_1.grid(row=1,column=1)
#Label_2 = Label(janela,width=15,height=5,justify=CENTER,text='Linha: 2 Coluna: 2')
#Label_2.grid(row=2,column=2)
#Label_3 = Label(janela,width=15,height=5,justify=CENTER,text='Linha: 3 Coluna: 3')
#Label_3.grid(row=3,column=3)

### Aula 5 ### (Botão)
## Criação + função teste (HelloWord)

""" global cont
cont = 0

def HelloWord():
    global cont
    texto_1 = 'Hello World! (1)'
    texto_2 = 'Hello World! (2)'

    if(cont%2==0):
        resultado = texto_2 + f' contador: {cont}'
        label['text'] = resultado
        label['fg'] = 'blue'
    else:
        resultado = texto_1 + f'contador: {cont}'
        label['text'] = resultado
        label['fg'] = 'white'
    
    cont+=1

label = Label(janela,height=2,text='O texto será apresentado aqui',relief=FLAT,fg='white',bg='black')
label.pack()

botao = Button(janela,command=HelloWord,width=10,height=1,text='Botão',relief='flat',fg='white',bg='black')
botao.pack()

botao_1 = Button(janela,command=HelloWord,width=10,height=1,text='Botão',relief='raised',fg='white',bg='black')
botao_1.pack()

botao_2 = Button(janela,command=HelloWord,width=10,height=1,text='Botão',relief='sunken',fg='white',bg='black')
botao_2.pack()

botao_3 = Button(janela,command=HelloWord,width=10,height=1,text='Botão',relief='groove',fg='white',bg='black')
botao_3.pack()

botao_4 = Button(janela,command=HelloWord,width=10,height=1,text='Botão',relief='ridge',fg='white',bg='black')
botao_4.pack()
"""
### AULA 6 ### (Entry)
## Criação (Réplica de fomulário) 

#Nome---------
label_nome = Label(janela, width=20, text='Nome:',anchor=W)
label_nome.grid(row=0,column=0,padx=10,pady=5,sticky=NSEW)
entry_nome = Entry(janela,width=10,font=('Arial 10 italic'))
entry_nome.grid(row=0,column=1,padx=10,pady=5)

#Idade---------
label_idade = Label(janela, width=20, text='Idade:',anchor=W)
label_idade.grid(row=1,column=0,padx=10,pady=5,sticky=NSEW)
entry_idade = Entry(janela,width=10,font=('Arial 10 italic'))
entry_idade.grid(row=1,column=1,padx=10,pady=5)

#País---------
label_pais = Label(janela, width=20, text='País:',anchor=W)
label_pais.grid(row=2,column=0,padx=10,pady=5,sticky=NSEW)
entry_pais = Entry(janela,width=10,font=('Arial 10 italic'))
entry_pais.grid(row=2,column=1,padx=10,pady=5)

# Respostas---------
label_respostas = Label(janela,width=20,text='Respostas abaixo',font=('Arial 10'))
label_respostas.grid(row=4,column=0)

def inserir():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_respostas['text'] = 'Respostas abaixo:\n' + 'Nome: ' + nome + '\n' + 'Idade: ' + idade + ' anos\n' + 'País: ' + pais
    entry_nome.delete(0,END)
    entry_idade.delete(0,END)
    entry_pais.delete(0,END)


botao = Button(janela,command=inserir,text='Inserir')
botao.grid(row=3,column=1)


janela.mainloop()