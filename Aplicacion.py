from tkinter import *
from tkinter import ttk, font,messagebox
class Aplicacion():
    __ventana=None
    __precioSinIva=None
    __iva=None
    __precioConIva=None
    __ivaLabel=None
    __precioConIvaLabel=None
    __entrada1=None
    __tipoIva=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Cálculo de IVA')
        self.__ventana.resizable(0,0)
        self.__precioSinIva =DoubleVar()
        self.__iva =DoubleVar()
        self.__precioConIva=StringVar()
        self.__tipoIva=DoubleVar()
        contenedor = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10,10)).grid(column=0,row=0)
        precioSinIvaLavel=ttk.Label(contenedor, text="Precio sin IVA").grid(column=0, row=0)
        self.__entrada1=ttk.Entry(contenedor, textvariable=self.__precioSinIva)
        self.__entrada1.grid(padx=10,pady=10,column=1, row=0,sticky='EW')
        separador1=ttk.Separator(contenedor, orient=HORIZONTAL).grid(column=0, row=1,columnspan=2,sticky='EW')
        ttk.Radiobutton(contenedor, text='IVA 21 %', value=21, variable=self.__tipoIva).grid(padx=15,pady=10,column=0,row=2, columnspan=1, sticky='w')
        ttk.Radiobutton(contenedor, text='IVA 10.5 %', value=10.5, variable=self.__tipoIva).grid(padx=15,pady=10,column=0,row=3, columnspan=1, sticky='w')
        separador2=ttk.Separator(contenedor, orient=HORIZONTAL).grid(column=0, row=4,columnspan=2,sticky='EW')
        ivaLabel=ttk.Label(contenedor, text="IVA").grid(column=0, row=5)
        ivaVLabel=ttk.Label(contenedor, textvariable=self.__iva, borderwidth=1, relief="solid",padding=(0,5)).grid(padx=10,pady=10,column=1, row=5,sticky='EW')
        precioCIvaLabel=ttk.Label(contenedor, text="Precio con IVA", padding=(5,5)).grid(column=0, row=6)
        precioCIvaVLabel=ttk.Label(contenedor, textvariable=self.__precioConIva, borderwidth=1, relief="solid",padding=(0,5)).grid(padx=10,pady=10,column=1, row=6, sticky='EW')
        separador3=ttk.Separator(contenedor, orient=HORIZONTAL).grid(column=0, row=7,columnspan=2,sticky='EW')
        boton1=ttk.Button(contenedor,text="Calcular",padding=(15,5), command=self.calcular).grid(padx=10,pady=10,column=0, row=8,sticky='EW')
        boton2=ttk.Button(contenedor, text="Salir",padding=(15,5), command=quit).grid(padx=10,pady=10,column=1, row=8,sticky='E')
        self.__precioSinIva.set('')
        self.__iva.set('')
        self.__precioConIva.set('')
        self.__entrada1.focus()
        self.__tipoIva.set(21)
        self.__ventana.mainloop()
    def calcular(self):
        try:
            precioBase=float(self.__entrada1.get())
            porcentaje=float(self.__tipoIva.get())
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico y se permite el caracter punto "."')
            self.__precioSinIva.set('')
            self.__iva.set('')
            self.__precioConIva.set('')
            self.__entrada1.focus()
        else:
            iva=(precioBase*porcentaje)/100
            self.__iva.set(iva)     
            self.__precioConIva.set(precioBase+iva)     