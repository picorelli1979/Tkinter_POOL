from tkinter import *

#-- CRIAÇÃO DA JANELA 
janela=Tk()
janela.title('BANCO DE DADOS DE FUNCIONARIOS') # -- TITULO DA JANELA
janela.geometry('500x800+200+200') # -- DIMENSÃO DA JANELA PRINCIPAL
janela['bg'] = 'black' # -- COR DE FUNDO OU BACKGROUND

#-- CRIAÇÃO DO CAMPO INICIAL: 
tela = Label(janela, text='=============//  BANCO DE DADOS  //=============', bg='gray',fg='white', font= 40, width=50, height=2, border=5)
tela.grid(row= 0, column= 0, columnspan= 5, padx= 10, pady=30)

#-- CRIAÇÃO DO MENU COM AS OPÇÕES: 
list_box = Listbox(janela, bg= 'gray',fg='white',font= 5, width= 50, height= 6)
list_box.grid(row= 2, column= 0, padx=10, pady=20)

list_box.insert(0, '1. INCLUIR  FUNCIONARIO')

list_box.insert(1, '2. ALTERAR  FUNCIONARIO')

list_box.insert(2, '3. EXCLUIR  FUNCIONARIO')

list_box.insert(3, '4. CONSULTAR 1 FUNCIONARIO')

list_box.insert(4, '5. CONSULTAR QUADRO GERAL DE FUNCIONARIO')

list_box.insert(5, '6. SAIR DO SISTEMA')

#-- CRIAÇÃO DO BOTÃO QUE VAI PEGAR A ESCOLHA DA OPÇÕES: 

def Pegar_texto():
    Lb3['text'] = (list_box.get(ACTIVE))
       
bt= Button(janela, text='CARREGAR',background= 'blue', fg='white', border= 10, command = Pegar_texto)
bt.grid(row= 40, column= 0, padx= 20, pady=10)

#-- CRIAÇÃO DO CAMPO QUE SAIRA OS DADOS DOS FUNCIONARIOS
Lb3 = Label(janela, text='', background='gray', font= 5 ,width= 50, height= 6, fg= 'white')
Lb3.grid(row=50 , column= 0, padx= 10, pady=10)

#-- CRIAÇÃO DO BOTÃO QUE VAI DELETAR AS INFORMAÇÕES NO CAMPO DE DADOS 
def Deletar_texto():
    Lb3['text'] = ''

bt_del= Button(janela, text='LIMPAR DADOS', background= 'red', fg='white', border= 10, command= Deletar_texto)
bt_del.grid(row= 60, column= 0, padx= 10, pady= 10) 

#-- AQUI É O CAMPO DO RODAPÉ DO SISTEMA 
tela2 = Label(janela, text='============& Dev Fabricio Paim &=============', bg='gray',fg='white', font= 40, width=50, height=2, border=5)
tela2.grid(row= 70, column= 0, columnspan= 5, padx= 10, pady=10)


# COMANDO PARA RODAR A JANELA DO TKINTER 
janela.mainloop()

