from pattern.text.es import parse, split, lexicon, spelling
import PySimpleGUI as sg
import os.path
import json
#from Puntuaciones import listaPuntuacionesAltas as listaP

sg.theme("Dark Amber")


def esValida(palabra, *dif):
    palabra = parse(palabra).split('/')
    if palabra[1] in dif:
        if palabra[1] == 'NN':
            if (not palabra[0] in spelling) or (not palabra[0] in lexicon):
                print('\n nono square', palabra[1], ' \n')
                return False
        print('\n yes', palabra[1], '\n')
        return True
    print('\n nono square', palabra[1], ' \n')
    return False


def Crearmenu():
    layoutM = [
        [sg.T("ScrabbleAR", size=(16, 1), justification="center",
              font=("Times New Roman", 25))],
        [sg.T("       Bienvenido a ScrabbleAR!, el juego donde      ")],
        [sg.T("           hay que armar palabras para ganar         ")],
        [sg.B("Iniciar nuevo juego", size=(17, 1), key="inicio"),
         sg.B("Configuracion", size=(17, 1), key="config")],
        [sg.B("Puntuaciones", size=(17, 1), key="puntos"),
         sg.B("Salir", size=(17, 1), key="exit")]
    ]

    if(os.path.isfile("Guardado.json")):
        layoutM += [[sg.B("Continuar partida", size=(36, 1), key="continue")]]

    window = sg.Window("ScrabbleAR - Menu", layoutM, finalize=True)

    return window


def Menu():
    menu = Crearmenu()
    while True:
        event, value = menu.read()

        if event == "Iniciar nuevo Juego" or "Continuar partida":
            if(event == "Continuar partida"):
                print("")
                # cargar ajustes por default
            menu.close()
            # IniciarJuego?
        if event == "Puntuaciones":
            # listaP()
            print("")
        if event == "Configuracion":
            print("")
            #event,ajustes = crear_ventana_config().read()
        else:
            break
    menu.close()


Menu()
