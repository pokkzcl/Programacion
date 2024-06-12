class Mascota:
    def __init__(self, nombre, tipo, dueño):
        self.nombre = nombre 
        self.tipo = tipo
        self.dueño = dueño
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nTipo: {self.tipo}\nDueño: {self.dueño}"