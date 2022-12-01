# pacrcial_2
from tkinter import *
from tkinter import messagebox
import random
import numpy as np


def matriz():
    return matriz 

    
    

# variables globales 



#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("PARCIAL_2")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")


#frame de graficacion


x = StringVar()
#--------------------
#frame entrada datos
#--------------------




frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "MATRIZ ")
titulo.config(bg = "white", fg = "blue", font = ("Arial",16))
titulo.place(x = 20, y = 10)

# Etiqueta para x
lb_numero = Label(frame_entrada, text = "tamano = ")
lb_numero.config(bg="white", fg="blue", font=("Arial",16))
lb_numero.place(x=100, y=50)

lb_buscar = Label(frame_entrada, text = "Buscar= ")
lb_buscar.config(bg="white", fg="black", font=("Arial",16))
lb_buscar.place(x=100, y=50)


# Entry para x
entry_numero= Entry(frame_entrada, textvariable=x)
entry_numero.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_numero.focus_set()
entry_numero.place(x=300, y=50, width=115, height=30)


fr_graficaion=Frame(ventana_principal)
fr_graficaion.config(bg="white",width=300, height=300)
fr_graficaion.pack(fill=BOTH ,padx=10, pady=10)

c=Canvas(fr_graficaion, width=200, height=200)
c.place(x=10 , y=10)


polil=c.create_polygon(0,0, 0,200, 200,200 , 200,0,  fill="grey" , outline="white", width=1)

lineal2=c.create_line(60,0  ,   60,200,fill="black")
lineal=c.create_line(180,0 , 180,200,fill="black")
lineal=c.create_line(0,100 , 300,100,fill="black")
lineal=c.create_line(0,200 , 300,200,fill="black")



matriz= np.random.randint(10, size=(3,3)) 



print(matriz) 


#--------------------
#frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "white", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 260)

# Boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=matriz)
bt_sumar.place(x=45, y=45, width=100, height=30)


# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.place(x=10, y = 390)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",14))
t_resultados.place(x=10,y=10, width=460, height= 80)

ventana_principal.mainloop()
                 
                  
