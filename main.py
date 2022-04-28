#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as tm
import tkinter.filedialog as tf

ARQUIVO = None

def novo():
    global ARQUIVO
    ARQUIVO = None
    textBox.delete(1.0,'end')

def abrir():
    global ARQUIVO
    ARQUIVO = tf.askopenfilename(defaultextension = '.txt',
    filetypes = [('Todos os Arquivos','*.*'),
            ('Arquivos de texto','*.txt')])
    textBox.delete(1.0, 'end')
    leitura = open(ARQUIVO, 'r')
    textBox.insert(1.0, ARQUIVO.read())
    leitura.close()

def salvar():
    global ARQUIVO
    if ARQUIVO is None:
        ARQUIVO = tf.asksaveasfilename(initialfile = 'arquivo.txt',
        defaultextension = '.txt',
        filetypes = [('Todos os Arquivos','*.*'),
        ('Arquivos de Texto','*.txt')])
    escreve = open(ARQUIVO,'w')
    escreve.write(textBox.get(1.0,'end'))
    escreve.close()

def cortar():
    textBox.event_generate('<<Cut>>')

def copiar():
    textBox.event_generate('<<Copy>>')

def colar():
    textBox.event_generate('<<Paste>>')

def sobre():
    tm.showinfo('Sobre',
        'Autor: \nRodrigo Nery')

root = tk.Tk()
textBox = tk.Text(root)
scrollBar = tk.Scrollbar(textBox)
textBox.grid(sticky = tk.N + tk.E + tk.S + tk.W)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

menu_barra = tk.Menu(root)
menu_arquivo = tk.Menu(menu_barra)
menu_editar = tk.Menu(menu_barra)
menu_ajuda = tk.Menu(menu_barra)

menu_arquivo.add_command(label = 'Novo',
        command = novo)
menu_arquivo.add_command(label = 'Abrir',
        command = abrir)
menu_arquivo.add_command(label = 'Salvar',
        command = salvar)
menu_arquivo.add_command(label = 'Sair',
        command = root.destroy)
menu_editar.add_command(label = 'Cortar',
        command = cortar)
menu_editar.add_command(label = 'Copiar',
        command = copiar)
menu_editar.add_command(label = 'Colar',
        command = colar)
menu_ajuda.add_command(label = 'Sobre',
        command = sobre)

menu_barra.add_cascade(label = 'Arquivo',
        menu = menu_arquivo)
menu_barra.add_cascade(label = 'Editar',
        menu = menu_editar)
menu_barra.add_cascade(label = 'Ajuda',
        menu = menu_ajuda)

root.config(menu = menu_barra)
scrollBar.pack(side = tk.RIGHT, fill = tk.Y)

root.title('Sem título - Bloco de Notas')
root.geometry('600x400')
root.resizable(False, False)
root.iconbitmap(r'/home/rodrigo/notepad.ico')
root.eval('tk::PlaceWindow . center')
root.mainloop()
