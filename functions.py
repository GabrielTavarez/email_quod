import win32com.client as win32
from texto_email import *
from tkinter.messagebox import showinfo
def enviar_email_add_fonte(lista_nomes, lista_cnpjs, lista_mIDs, lista_tipos, lista_emails, lista_emails_cc):
    outlook = win32.Dispatch('outlook.application')

    recipients = ''
    for email in lista_emails:
        recipients += email+';'

    recipients_cc = ''
    for email in lista_emails_cc:
        recipients_cc += email+';'

    for i in range(len(lista_nomes)):
        mail = outlook.CreateItem(0)
        mail.To = recipients
        mail.CC = recipients_cc
        mail.Subject = f'Inclusão de Fonte - {lista_cnpjs[i]}'
        body_email = get_body(lista_nomes[i], lista_cnpjs[i], lista_mIDs[i], lista_tipos[i])
        mail.Body = body_email
        try:
            mail.Send()
        except:
            showinfo('ERRO', 'Falha ao enviar emails (provavelmente email inválido)')
        
    