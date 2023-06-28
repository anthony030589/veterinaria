import tkinter as tk
#contructor Frame#
class Frame(tk.Frame):
    def __init__(self, ventanaHistoriaM):
        super().__init__(ventanaHistoriaM, width=1200, height=620)
        self.ventanaHistoriaM = ventanaHistoriaM
        self.pack()
        self.config(bg='#CDD8FF')
        self.etiquetasMascota()
    
    def etiquetasMascota(self):
        #Etiquetas#
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblNumeroChip = tk.Label(self, text='Numero MicroChip: ')
        self.lblNumeroChip.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblNumeroChip.grid(column=0, row=1, padx=10, pady=5)

        self.lblSexo = tk.Label(self, text='Sexo: ')
        self.lblSexo.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblSexo.grid(column=0, row=2, padx=10, pady=5)

        self.lblTamano = tk.Label(self, text='Tamaño: ')
        self.lblTamano.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblTamano.grid(column=0, row=3, padx=10, pady=5)

        self.lblEspecie = tk.Label(self, text='Especie: ')
        self.lblEspecie.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblEspecie.grid(column=0, row=4, padx=10, pady=5)

        self.lblRaza = tk.Label(self, text='Raza: ')
        self.lblRaza.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblRaza.grid(column=0, row=5, padx=10, pady=5)

        self.lblColor = tk.Label(self, text='Color: ')
        self.lblColor.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblColor.grid(column=0, row=6, padx=10, pady=5)

        self.lblEddad = tk.Label(self, text='Edad: ')
        self.lblEddad.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblEddad.grid(column=0, row=7, padx=10, pady=5)

        self.lblFechaNacimiento = tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFechaNacimiento.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblFechaNacimiento.grid(column=0, row=8, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0, row=9, padx=10, pady=5)


        #Entry#
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=40, font=('ARIAL',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svNumeroChip = tk.StringVar()
        self.entryNumeroChip = tk.Entry(self, textvariable=self.svNumeroChip)
        self.entryNumeroChip.config(width=40, font=('ARIAL',15))
        self.entryNumeroChip.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svSexo = tk.StringVar()
        self.entrySexo = tk.Entry(self, textvariable=self.svSexo)
        self.entrySexo.config(width=40, font=('ARIAL',15))
        self.entrySexo.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svTamano = tk.StringVar()
        self.entryTamano = tk.Entry(self, textvariable=self.svTamano)
        self.entryTamano.config(width=40, font=('ARIAL',15))
        self.entryTamano.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEspecie = tk.StringVar()
        self.entryEspecie = tk.Entry(self, textvariable=self.svEspecie)
        self.entryEspecie.config(width=40, font=('ARIAL',15))
        self.entryEspecie.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svRaza = tk.StringVar()
        self.entryRaza = tk.Entry(self, textvariable=self.svRaza)
        self.entryRaza.config(width=40, font=('ARIAL',15))
        self.entryRaza.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svColor = tk.StringVar()
        self.entryColor = tk.Entry(self, textvariable=self.svColor)
        self.entryColor.config(width=40, font=('ARIAL',15))
        self.entryColor.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=40, font=('ARIAL',15))
        self.entryEdad.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svFechaNacimiento = tk.StringVar()
        self.entryFechaNacimiento = tk.Entry(self, textvariable=self.svFechaNacimiento)
        self.entryFechaNacimiento.config(width=40, font=('ARIAL',15))
        self.entryFechaNacimiento.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=40, font=('ARIAL',15))
        self.entryAntecedentes.grid(column=1, row=9, padx=10, pady=5, columnspan=2)

        #Botones#
        self.btnNuevo = tk.Button(self, text='Nuevo')
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=10, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar')
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=10, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar')
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#B00000', cursor='hand2', activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=10, padx=10, pady=5)