#Nuevas Tecnologías de Programación
#Paulo Enrique Toro Valderrama (71370437)
#2021/09/18 - 11:15h.


# 1. Crear una lista con 5 municipios del departamento de Antioquia. Luego, recorrer esta lista y mostrar cada ciudad excepto una de ellas (cualquiera)

""" municipios = ["Medellín", "Envigado", "Itagüi", "Bello", "LaEstrella"]

for mpio in municipios:
    if mpio == "Medellín":
        pass
    else:
        print(mpio) """

# 2. Generar una lista con los 10 primeros de la siguiente sucesión: 7,11,15,19,23...

""" contador = 1
numeroi = 7
LosDiezPrimerosNumeros = []
LosDiezPrimerosNumeros.append(numeroi)
while(contador<10): 
    numeroi += 4
    LosDiezPrimerosNumeros.append(numeroi)
    contador+=1
print(LosDiezPrimerosNumeros) """

# 3. Generar un diccionario con los datos de un departamento de Colombia(código,nombre, poblacion, municipios (3municipios). Luego, mostrar este diccionario,solo con el segundo municipio.

""" Antioquia = {
    "Código" : "cod01",
    "Nombre" : "Antioquia",
    "Capital" : "Medellín",
    "Población" : "6407000(2018)",
    "Municipios" : ["Bello", "Itagüi", "Envigado"]
}

print(Antioquia["Municipios"][1]) """

# 4. Generar los archivos necesarios para generar las clases: "Inmueble(Padre)", Oficina", "Casa" con base en el diagrama.

class Inmueble:
    def __init__(self, codigo, direccion, telefono):
        self.__codigo = codigo
        self.__direccion = direccion
        self.__telefono = telefono
    
    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, telefono):
        self.__telefono = telefono

    def radicar(self,codigo) : type(None)

    def arrendar(self):
        print(f"Arrendando el Inmueble con el código {self.__codigo}...")

#Subclase
class Oficina(Inmueble):
    def __init__(self, codigo, direccion, telefono, salaAsamblea):
        super().__init__(codigo, direccion, telefono)
        self.__salaAsamblea = salaAsamblea      
        
    def getSalaAsamblea(self):
        return self.__salaAsamblea
    
    def setSalaASamblea(self, salaAsamblea):
        self.__salaAsamblea = salaAsamblea

    def instalarInternet(self):
        return f"El internet está siendo instalado en la {self.__salaAsamblea}..."

#Subclase
class Casa(Inmueble):
    def __init__(self, codigo, direccion, telefono, nroHabitaciones):
        super().__init__(codigo, direccion, telefono)
        self.__nroHabitaciones = nroHabitaciones      
        
    def getNroHabitaciones(self):
        return self.__nroHabitaciones
    
    def setNroHabitaciones(self, nroHabitaciones):
        self.__nroHabitaciones = nroHabitaciones

    def repararJardin(self):
        return f"El jardín está siendo reparado y hay {self.getNroHabitaciones()}"

inmueble1 = Inmueble("Cod01", "Calle77#45-33", "6045678789")
print(inmueble1.arrendar())

oficina1 = Oficina("Cod01", "Calle77#45-33", "6045678789", "Sala3")
sala = oficina1.getSalaAsamblea()
print(oficina1.instalarInternet())
print(oficina1.getSalaAsamblea())
print(oficina1.getDireccion())

oficina1.setSalaASamblea("Sala45")
print(oficina1.getSalaAsamblea())

casa1 = Casa("Cod02", "Calle79#43-77", "6045622112", 5)
print("La casa tiene " + str(casa1.getNroHabitaciones()) + " habitaciones")
print(casa1.getCodigo())
