import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from functions import *

#============================================================================================
lista_tipos_select = ['Fonte CIP', 'Fonte Direta', 'Fonte Utilities']

lista_nomes = []
lista_cnpjs = []
lista_mIDs = []
lista_tipos = []

lista_emails = []
lista_emails_cc = []

lista_emails_added = []

# ========================================== [GUI] ==================================================
window = tk.Tk()
window.minsize(760, 400)
window.maxsize(760, 500)
window.rowconfigure([0,1,2], weight=1)
try:
    icon = tk.PhotoImage(file = 'img.gif')
    window.iconphoto(False, icon)
except:
    pass

# EMPRESA -----------------------
frame_empresa = Frame(window)
title_empresa = Label(frame_empresa, text = 'Empresa')
title_empresa.grid(row = 0, column = 0, stick= 'W', padx = 10)

frame_nome = Frame(frame_empresa)
nome_label = Label(frame_nome, text = 'Nome')
nome_label.grid(row= 0 , column = 0, stick = 'W')
nome_entry = Entry(frame_nome, width=50)
nome_entry.grid(row= 1 , column = 0, stick = 'WE')

frame_cnpj = Frame(frame_empresa)
cnpj_label = Label(frame_cnpj, text = 'CNPJ')
cnpj_label.grid(row = 0, column = 0, stick = 'w')
cnpj_entry = Entry(frame_cnpj, width=18)
cnpj_entry.grid(row = 1, column = 0, stick = 'we')

frame_mID = Frame(frame_empresa)
mID_label = Label(frame_mID, text = 'Member ID')
mID_label.grid(row = 0, column = 0, stick='w')
mID_entry = Entry(frame_mID, width=10)
mID_entry.grid(row = 1, column = 0, stick='we')

frame_type = Frame(frame_empresa)
type_label = Label(frame_type, text = 'Tipo')
type_label.grid(row = 0, column = 0, stick='w')
type_lista = ttk.Combobox(frame_type, values = lista_tipos_select)
type_lista.grid(row = 1, column = 0, stick='we')

def add_fonte():
    nome = nome_entry.get()
    cnpj = cnpj_entry.get()
    mID = mID_entry.get()
    tipo = type_lista.get()

    nome = nome.replace('–', '-').strip() #corrige traço
    if len(nome) < 1:
        showinfo('ERRO',  'Nome fonte vazio')
        return
    cnpj = cnpj.replace('.', '').replace('-', '').replace(' ', '').replace('/','') # remove espaço, ponto, barra e traço
    if len(cnpj) < 1:
        showinfo('ERRO',  'CNPJ vazio')
        return
    if not(cnpj.isnumeric()):
        showinfo('ERRO',  'CNPJ não numérico')
        return
    if len(cnpj) < 14:
        showinfo('ERRO',  'CNPJ inválido')
        return
    mID = mID.strip()
    if len(mID) != 5:
        showinfo('ERRO',  'member ID inválido')
        return
    if not(tipo in lista_tipos_select):
        showinfo('ERRO',  'Tipo de fonte inválido')
        return
    
    lista_nomes.append(nome)
    lista_cnpjs.append(cnpj)
    lista_mIDs.append(mID)
    lista_tipos.append(tipo)

    empresas_added_lista['values'] = lista_nomes

    nome_entry.delete(0, END)
    cnpj_entry.delete(0, END)
    mID_entry.delete(0, END)
    type_lista.delete(0, END)


add_botao_empresa = Button(frame_empresa, text='Add', command=add_fonte)

frame_empresas_added = Frame(frame_empresa)
empresas_added = Label(frame_empresas_added, text='Empresas adicionadas')
empresas_added.grid(row=0, column = 0, stick='w')
empresas_added_lista = ttk.Combobox(frame_empresas_added, values = lista_nomes, width= 30)
empresas_added_lista.grid(row=1, column =0, stick='w', padx=5)

def remove_empresa():
    empresa = empresas_added_lista.get()
    if empresa == '':
        showinfo('ERRO', 'Nenhum empresa selecionada')
    index_fonte = lista_nomes.index(empresa)
    del lista_nomes[index_fonte]
    del lista_cnpjs[index_fonte]
    del lista_mIDs[index_fonte]
    del lista_tipos[index_fonte]
    empresas_added_lista['values'] = lista_nomes
    empresas_added_lista.delete(0, END)


botao_remove_empresa = Button(frame_empresas_added, text='remove', command=remove_empresa)
botao_remove_empresa.grid(row=1, column = 1, sticky='w')


frame_nome.grid(row = 1, column = 0, padx= 10, stick = 'we')
frame_cnpj.grid(row = 1, column = 1, padx= 10, stick = 'we')
frame_mID.grid(row=1, column = 2, padx= 10, stick = 'we')
frame_type.grid(row=1, column= 3, padx=10, stick = 'we')
add_botao_empresa.grid(row = 1, column = 4, padx=10, stick='S')
frame_empresas_added.grid(row=2, column=0, pady=10, padx=10, stick='w')


#EMAILS -----------------------
frame_email = Frame(window)
title_email = Label(frame_email, text = 'Emails')
title_email.grid(row=0, column=0, pady=10, padx=10, sticky='w')



frame_endereco = Frame(frame_email)
enedereco_label = Label(frame_endereco, text = 'Endereço email')
enedereco_label.grid(row=0, column=0, stick = 'W')
endereco_entry = Entry(frame_endereco, width=40)
endereco_entry.grid(row=1, column=0, stick='we')


frame_email_type = Frame(frame_email)
email_type_label = Label(frame_email_type, text = 'To/CC')
email_type_label.grid(row = 0, column = 0, stick='w')
email_type_lista = ttk.Combobox(frame_email_type, values = ['To', 'CC'], width = 5)
email_type_lista.grid(row = 1, column = 0, stick='we')


def add_email():
    email = endereco_entry.get()
    to_cc = email_type_lista.get()
    
    email = email.strip()
    if len(email) < 1:
        showinfo('ERRO',  'Email vazio')
        return
    if not(to_cc in ['To', 'CC']):
        showinfo('ERRO',  'Tipo de email inválido')
        return
    
    if to_cc == 'To':
        lista_emails.append(email)
        lista_emails_added.append(email)
    if to_cc == 'CC':
        lista_emails_cc.append(email)
        lista_emails_added.append(email + ' (CC)')
    emails_added_lista['values'] = lista_emails_added
    
    endereco_entry.delete(0,END)
    email_type_lista.delete(0,END)

add_botao_email = Button(frame_email, text='Add', anchor='e', command=add_email)


frame_emails_added =Frame(frame_email)
emails_added = Label(frame_emails_added, text = 'Emails adicionados')
emails_added.grid(row = 0, column = 0, stick='w')
emails_added_lista = ttk.Combobox(frame_emails_added, values = lista_emails_added, width=25 )
emails_added_lista.grid(row = 1, column = 0, stick='we')

def remove_email():
    email = emails_added_lista.get()
    if email == '':
        showinfo('ERRO',  'Nenhum email selecionado')
        return
    if email in lista_emails:
        del lista_emails[lista_emails.index(email)]
    elif email[:-5] in lista_emails_cc:
        del lista_emails_cc[lista_emails_cc.index(email[:-5])]

    lista_emails_added.remove(email)
    emails_added_lista['values'] = lista_emails_added
    emails_added_lista.delete(0, END)


botao_remove_email = Button(frame_emails_added, text='remove', command=remove_email)
botao_remove_email.grid(row = 1, column = 1, stick='sw', padx = 5)


frame_endereco.grid(row=1, column= 0, padx=10, stick='we')
frame_email_type.grid(row=1, column= 1, padx=10, stick='we')
add_botao_email.grid(row = 1, column = 2, stick = 'se')
frame_emails_added.grid(row=2, column=0, pady=10, padx=10, stick='w')

#ENVIAR ---------------------------
def enviar_email():
    if len(lista_nomes) < 1:
        showinfo('ERRO', 'Não foram adicionadas empresas')
    if len(lista_emails) < 1:
        showinfo('ERRO', 'Não foram adicionadas emails')
    
    enviar_email_add_fonte(lista_nomes, lista_cnpjs, lista_mIDs, lista_tipos, lista_emails, lista_emails_cc)
    print(lista_nomes)
    print(lista_cnpjs)
    print(lista_mIDs)
    print(lista_tipos)

    print(lista_emails)
    print(lista_emails_cc)
    pass

enviar_botao = Button(window, text = 'Enviar', command=enviar_email, width = '15', height= '2')

frame_empresa.grid(row=0, column =0, pady = 10, stick = 'we')
frame_email.grid(row=1, column =0, pady = 10, stick = 'we')
enviar_botao.grid(row=2, column =0, pady = 10, padx= 10, stick = 'se')

window.mainloop()