import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlack')
        
        layout = [
            [sg.Text("Nome:", size=(5, 0)), sg.Input(size=(20, 0), key='nome')],
            [sg.Text("Idade:", size=(5, 0)), sg.Input(size=(20, 0), key='idade')],
            [sg.Text("Quais desses emails você usa?")],
            [sg.Checkbox("Gmail", key='gmail'), sg.Checkbox("Outlook", key='outlook'), sg.Checkbox("Yahoo", key='yahoo')],
            [sg.Text("Aceita cartão?")],
            [sg.Radio("Sim", 'cartoes', key='simAceitaCartao'), sg.Radio("Não", 'cartoes', key='naoAceitaCartao')],
            [sg.Text("Velocidade:")],
            [sg.Text("0"), sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(24, 20), key='velocidade'), sg.Text("255")],
            [sg.Button("Enviar")],
            [sg.Output(size=(36, 20))]
        ]
        
        self.janela = sg.Window("Sussy.py", layout, size=(300,400))
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            usa_gmail = self.values['gmail']
            usa_outlook = self.values['outlook']
            usa_yahoo = self.values['yahoo']
            cartao = self.values['simAceitaCartao']
            velocidade = self.values['velocidade']
            
            print(f"\nNome: {nome}")
            print(f"Idade: {idade}")
            print(f"Usa GMail? {usa_gmail}")
            print(f"Usa Outlook? {usa_outlook}")
            print(f"Usa Yahoo? {usa_yahoo}")
            print(f"Aceita cartão? {cartao}")
            print(f"Velocidade: {velocidade}")
        

# Programa principal
tela = TelaPython()

tela.Iniciar()
