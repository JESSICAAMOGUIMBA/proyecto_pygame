from tkinter import *
import os
ventana=Tk()

ventana.title("PLAY DUNCKHUNT!!!")
ventana=Frame (height=400,width=400)
ventana.pack(padx=5,pady=5)
ventana.configure(background="pink")

anchoBoton=25
altoBoton=2

boton1=Button(ventana,text="JUGADOR 1",width=anchoBoton,height=altoBoton,background="#91F467",command=lambda:os.system("proyecto_duckhunt.py")).place(x=20,y=20)
boton2=Button(ventana,text="JUGADOR 2",width=anchoBoton,height=altoBoton,background="#91F467",command=lambda:os.system("proyecto_duckhunt.py")).place(x=20,y=120)
boton4=Button(ventana,text="Salir",width=anchoBoton,height=altoBoton,background="#91F467",command=ventana.quit).place(x=20,y=220)

mainloop( )
