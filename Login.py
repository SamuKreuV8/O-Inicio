from PySimpleGUI import PySimpleGUI as sg
def janelaLogin():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuário'), sg.Input(key = 'Usuário', size=(20,1))],
        [sg.Text('Senha'), sg.Input(key = 'Senha', password_char = '*', size=(20,1))],
        [sg.Checkbox('Salvar login?')],
        [sg.Button('Entrar')]
    ]
    return sg.Window('Login', layout=layout, finalize = True)

def janelaSusLogin():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Logado com sucesso')],
        [sg.Button('Ok')] 
    ]
    return sg.Window('Sucesso', layout=layout, finalize = True)


janela1, janela2 = janelaLogin(), None

while True:
    window, evento, valores = sg.read_all_windows()
    if window == janela1 and evento  == sg.WINDOW_CLOSED:
        break
    if window == janela1 and evento == 'Entrar':
        janela2 = janelaSusLogin()
        janela1.hide()
        window2, evento2 = sg.read_all_windows()
        if window2 == janela2 and evento2 == 'Ok':
            break