from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


import shutil, os


def abreFichero():


    fichero = filedialog.askopenfilename(title="Abrir")

    vrutavideo.set(fichero)

def enviaVideo():

    try:
        #shutil.copy(vrutavideo.get(), r"\\10.8.65.29\TECNICOS\TELEDERMA\video.mp4" )
        shutil.copy(vrutavideo.get(), r"\\10.8.65.80\videos\video.mp4" )

        messagebox.showinfo("Aviso", "Video Enviado")
        #showinfo(title="Aviso", message="VIDEO ENVIADO")
    except:
        messagebox.showinfo("Aviso", "Error en eNVIO")
        #showinfo(title="Aviso", message="VIDEO ENVIADO")

raiz = Tk()

raiz.title("Pantallas Salud")
raiz.geometry('300x100+350+150')

miFrame = Frame(raiz)
miFrame.pack()

etiqueta = Label(miFrame, text="Seleccionar Video :")
etiqueta.grid(row=0, column=0)

boton = Button(miFrame, text="Buscar Video", command=abreFichero)
boton.grid(row=1, column=0)

vrutavideo = StringVar()

rutafichero = Label(miFrame, textvariable=vrutavideo)
rutafichero.grid(row=2, column=0)

botonEnviar = Button(miFrame, text="Enviar Video", command=enviaVideo)
botonEnviar.grid(row=3, column=0)





raiz.mainloop()