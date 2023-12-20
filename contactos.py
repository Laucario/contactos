import tkinter as tkinter
from tkinter import ttk

contactos = [] #creamos una lista

def Agregar_Contactos(): #creamos la funcion de agregar contactos definiendo las variables de nombre y telefono
    nombre = CajaNombre.get()
    telefono = CajaTelefono.get()
    contacto = {"nombre": nombre, "telefono": telefono}
    contactos.append(contacto)#obtenemos lo ingresaddo en los entry, lo añadimos a la lista con append y lo insertamos con insert
    treeview.insert("", tkinter.END, text=nombre, values=(telefono))

def Eliminar_Contactos(): #definimos la funcion eliminar contactos, la cual va a borrar una tarea seleccionada
    seleccion = treeview.selection() #definimos que la seleccion sea una marca del treeview
    for contacto in seleccion: 
        treeview.delete(contacto) #mientras haya algo marcado, se borra

def salir(): #se defina la funcion salir que a cerrar la ventana 
    ventana.quit()

ventana = tkinter.Tk()
ventana.title("Lista de Contactos") #se define la ventana y el nombre de la ventana

treeview = ttk.Treeview(columns=('Telefono')) #se forman las columnas ademas de la columna "#0"

treeview.heading ('#0', text='Nombre')
treeview.heading ('Telefono', text='Telefono') #damos valores a las columnas

etiqueta = tkinter.Label(ventana, text= "Nombre") #usando label se crea el texto que va a motrar
etiqueta.pack(pady=10) #se empaqueta y se da forma del label

CajaNombre = tkinter.Entry(ventana)
CajaNombre.pack() #se crea una caja de texto vacía que agregue el valor nombre al diccionario y se empaqueta

etiqueta = tkinter.Label(ventana, text= "Telefono")
etiqueta.pack(pady=10) #lo mismo que en el label se nombre pero esta vez en número

CajaTelefono = tkinter.Entry(ventana)
CajaTelefono.pack() #se crea una caja de texto vacía como en nombre pero de número

Boton_Agregar = tkinter.Button(ventana, text="Agregar contacto", bg="blue", command=Agregar_Contactos)
Boton_Agregar.pack(pady=15)
Boton_Eliminar = tkinter.Button(ventana, text="Eliminar contacto", bg="brown", command=Eliminar_Contactos)
Boton_Eliminar.pack(pady=15) #se crean y empaquetan los botones, con nombre y comando que realizan
Boton_Salir = tkinter.Button(ventana, text="Salir", bg="red", command=salir)
Boton_Salir.pack(pady=15)

treeview.pack() #se da la forma al treeview


ventana.mainloop() #corre y repite el programa indefinidamente
