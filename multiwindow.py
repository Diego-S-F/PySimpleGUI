# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 08:37:15 2021

@author: Diego_SF
"""

import PySimpleGUI as sg

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Button('Ventana 2', key="Launch 2"), sg.Button('Exit', key='Exit')]]

win1 = sg.Window('Window 1', layout)

win2_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
    win1['-OUTPUT-'].update(vals1[0])
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break
    if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        layout2 = [
                    [sg.Text("Datos")],
                    [sg.Text("Dato1: ")],
                    [sg.Input(size=(30, 1), key="-dato_1-")],
                    [sg.Text("dat2: ")],
                    [sg.Input(size=(30, 1), key="-dato_2-")],
                    [sg.B("Cancelar", key="-cancelar-"), sg.B("Guardar", key="-guardar_datos-") ]
                    ]
        win2 = sg.Window('Window 2', layout2)
    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Exit' or ev2 == "-cancelar-" or ev2 == "-guardar_datos-" :
            win2_active  = False
            win2.close()
win1.close()