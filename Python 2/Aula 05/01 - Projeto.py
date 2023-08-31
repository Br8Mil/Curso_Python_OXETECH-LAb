
#Minha versão

import PySimpleGUI as sg
from dados import cotar

sg.theme('DarkAmber')

interface = [
[sg.Text('User')],
[sg.Input(key='user')],
[sg.Text('Password')],
[sg.Input(key='pass')],
[sg.Button('Login'), sg.Button('Register New User')],
[sg.Text('', key= 'message')],
]

interface_register = [
[sg.Text('E-mail')],
[sg.Input(key='new_email')],
[sg.Text('User')],
[sg.Input(key='new_user')],
[sg.Text('Pass')],
[sg.Input(key='new_pass')],
[sg.Button('Register'), sg.Button('Back')],
[sg.Text('', key= 'message2')],
]

interface_cotacao = [
[sg.Text('Welcome to the Quotation Screen')],
[sg.Text('Enter Start Date, Year-Month-Day')],
[sg.Input(key='starter_YMD')],
[sg.Text('Provide End Date, Year-Month-Day')],
[sg.Input(key='end_YMD')],
[sg.Text('Enter the ticker')],
[sg.Input(key='ticker_1')],
[sg.Button('Quote'), sg.Button('Back')],
]

window = sg.Window('Log in', layout=interface)
window_reg = sg.Window('Register', layout=interface_register)
window_cot = sg.Window('Cotação', layout=interface_cotacao)

user_correct = ['Rodrigo', 'Juan']
pass_correct = ['12345', '5190']
email = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        user_login = values['user']
        pass_login = values['pass']
        if user_login in user_correct and pass_login in pass_correct:
            window['message'].update('Successful Login.')
            event, values = window_cot.read()
            if event == sg.WIN_CLOSED:
                sg.Close()
            elif event == 'Quote':
                ticker_input = values['ticker_1']
                start_input = values['starter_YMD']
                end_input = values['end_YMD']
                cotar(ticker_input, start_input, end_input)
            elif event == 'Back':
                sg.Close()
        else:
            window['message'].update('username or password is invalid.')
    elif event == 'Register New User':
        event, values = window_reg.read()
        newemail = values['new_email']
        newuser = values['new_user']
        newpass = values['new_pass']
        if event == 'Register':
            user_correct.append(newuser)
            pass_correct.append(newpass)
            email.append(newemail)
            window_reg['message2'].update('Successfully Registered User.')
        elif event == 'Back':
            sg.Close()