import PySimpleGUI as sg
import random
import os

dir_senhas = os.environ['USERPROFILE'] + r'\Password_Generator'

if not os.path.exists(dir_senhas):
    os.mkdir(dir_senhas)
else:
    pass

class PassGen:
    def __init__(self):
        # Criacao do layout da interface
        sg.theme('Topanga')
        layout = [
            [sg.Text('Site/Software:', font=('Times New Roman', 14)),
             sg.Input(key='site', font=('Times New Roman', 14), expand_x=True, text_color='#FFFFFF')],
            [sg.Text('Email/Usuário:', font=('Times New Roman', 14)),
             sg.Input(key='user', font=('Times New Roman', 14), expand_x=True, text_color='#FFFFFF')],
            [sg.Text('Quantidades de Caracteres:', font=('Times New Roman', 14)),
             sg.Combo(values=list(range(31)),default_value=1, key='total_chars',font=('Times New Roman', 14, 'bold'))],
            [sg.Output(font=('Times New Roman', 14, 'bold'), expand_x=True, text_color='#FFFFFF', key='display')],
            [sg.Button('Gerar Senha', key='gerar', font=('Times New Roman', 11, 'bold')), sg.Stretch(), sg.Button('Fechar Aplicativo', button_color=['#FFFFFF', '#CC0000' ], key='cancel', font=('Times New Roman', 11, 'bold'))]
        ]
        # Criacao da janela
        self.janela =  sg.Window('Password Generator', icon='icon.ico',layout=layout, auto_size_text=True, auto_size_buttons=True, finalize=True, resizable=True, grab_anywhere=True)
    # Looping de eventos
    def Iniciar(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == 'gerar':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
            if eventos == sg.WINDOW_CLOSED or eventos == 'cancel':
                break

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open(f'{dir_senhas}\senhas.txt', 'a', newline=None) as arquivo:
            arquivo.write(f' | Site: {valores["site"]} / Usuário: {valores["user"]} / Nova Senha: {nova_senha}')
            sg.popup(f'Cheque na pasta--> {dir_senhas}',title='Senha salva com sucesso!', auto_close_duration=5, icon='icon.ico', grab_anywhere=True)

gen = PassGen()
gen.Iniciar()