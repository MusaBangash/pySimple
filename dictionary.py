from tkinter.tix import WINDOW
import PySimpleGUI as sg
import json
sg.SetOptions(font=("Verdana 16"))

layout=[
    
    [sg.Text("Enter Word"),sg.InputText(size=(24,14),key="-W-"),sg.Button("Go")],
    [sg.Multiline(size=(50,25),disabled=True,key="-OUT-")]
]

#Window

window=sg.Window("Dictionary",layout)

#event values loop

while True:
    
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='Go':
        
        w=values['-W-'].lower()
        total=[]
        with open("dict.json",'r') as f:
            data=json.load(f)
            for i,j in data.items():
                if i==w:
                    total.append(j)
        if len(total)>0:
            
            window['-OUT-'].update(total)
        else:
            window['-OUT-'].update('Nothing found!')
                    


#close
window.close()