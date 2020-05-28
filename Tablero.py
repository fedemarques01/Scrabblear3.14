import PySimpleGUI as sg
from datetime import datetime as datetime
import json

sg.theme("Topanga")
def crearTablero():
    col = fil = 15 
    """
    col,fil y fichas son constantes que se usan a la hora de definir las proporciones del tablero y las fiachas por estante de jugador
    BackT es el tablero pero en back end, usado a la hora de ver el contenido de las casillas 
    y es actualizado cuando se verifica una palabra
    """

    fichas = 7 
    backT = [["" for i in range(col)] for i in range(fil)]
    #ColM es la columna donde se encuentra la informacion de la partida junto a otros comentarios y los botones para terminar y guardar la partida
    colM = [
        [sg.B("Guardar",size=(13,1),key="-save-")],
        [sg.B("Terminar",size=(13,1),key="Exit")],
        [sg.Frame(layout=[[sg.Text("Ponga una ficha en ST para comenzar la partida",size=(13,10),key="-comment-")]],
        title="Comentarios",title_color="Yellow",background_color="Black",key="-block-")],
        [sg.Text("Dificultad: ",key="-dif-")],
        [sg.Text("Tu puntaje: 0",key="-pJug-")],
        [sg.Text("Puntaje CPU: 0",key="-pCPU-")]
    ]
    #col board es la columna donde esta el atril del cpu y el tablero, generados de esta forma para que quede una columna al lado de la otra
    colBoard = [[sg.Text("CPU:")]]

    colBoard += [[sg.B("?",size=(2,1),pad=(0,0),disabled=True) for i in range(fichas)]for j in range(1)]

    colBoard += [[sg.Text("")]]

    colBoard += [[sg.B("",size=(3,1), key =(m,n),pad=(0,0)) for m in range(col)] for n in range(fil)]

    #ColPlayer es la columna donde estan las fichas del jugador
    colPlayer = [[sg.B("",size=(3,1),key = str(k) , pad=(0,0)) for k in range(fichas)]for l in range(1)] 

    #layout del tablero, junta todas las columnas y añade el resto de los botones
    frontT = [
        [sg.Column(colM),
        sg.Column(colBoard)],
    [sg.Text("")],
    [sg.Text("Tus fichas:"), sg.Column(colPlayer),
    sg.B("Comprobar",key="-fin-",size=(10,1)),sg.B("Pasar",key="-cambiar-",size=(10,1)),
    sg.B("Deshacer",key="-back-",size=(10,1))]
    ]

    tablero = sg.Window("ScrabbleAR - Juego",frontT,finalize=True)

    return tablero,backT
#carga todos los botones del tablero, el ya guardado en caso de una partida guardada o el 
def cargarTablero(tablero,board,tabla):
    
    if(tabla == None):
        triple_letter = [(1,5),(1,9),(5,1),(5,5),(5,9),(5,13),(9,1),(9,5),(9,9),(9,13),(13,5),(13,9)]
        double_letter = [(0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,9),(14,3),(14,11)]
        double_word = [(1,1),(2,2),(3,3),(4,4),(1,13),(2,12),(3,11),(4,10),(13,1),(12,2),(11,3),(10,4),(10,10),(11,11),(12,12),(13,13)]
        triple_word = [(0,0),(0,7),(0,14),(7,0),(7,14),(14,0),(14,7),(14,14)]
        start_button = (7,7)   

        for x in triple_letter:
            tablero.FindElement(x).update("Lx3",button_color=("#D4D4D4","#8A1111"))
            board[x[0]][x[1]] = "Lx3"
        for x in double_letter:
            tablero.FindElement(x).update("Lx2",button_color=("#D4D4D4","#79118A"))
            board[x[0]][x[1]] = "Lx2"
        for x in double_word:
            tablero.FindElement(x).update("Px2",button_color=("#D4D4D4","#8A1155"))
            board[x[0]][x[1]] = "Px2"
        for x in triple_word:
            tablero.FindElement(x).update("Px3",button_color=("#D4D4D4","#0F6F6C"))
            board[x[0]][x[1]] = "Px3"
        tablero.FindElement(start_button).update("St",button_color=("#D4D4D4","#928900"))
    else:
        backT = tabla
        for i in range(len(tabla)):
            for j in range(len(tabla[i])):
                if(tabla[i][j] == ""):
                    continue
                

    return tablero,backT



#carga todos los ajustes de la partida(puntaje,dificultad,botones especiales,bolsa)
def cargarPartida(tablero,backT,datos):

    return tablero,backT

def Jugar(settings,event):

    tablero,backT = crearTablero()
    #creo un diccionario con los datos de la partida instanciando un tablero vacio por defecto
    datos = {"tablero": None} 
    print("me mori")
    if(event == "continue"):
        arch = open("Guardado.json","r")
        datos.update(json.load(arch))#si existe una partida guardada datos tendra el backT de la partida anterior en tablero, y los settings de la partida anterior
    else:
        datos.update(settings)#sino datos tendra los settings que elijio el jugador o los por defecto

    tablero,backT = cargarPartida(tablero,backT,datos)        
    event, _ = tablero.read()

if __name__ == "__main__":
    Jugar()