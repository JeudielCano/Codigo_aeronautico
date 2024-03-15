aeroCodigo = [['A', 'ALFA'], ['B', 'BRAVO'], ['C', 'CHARLIE'], ['D', 'DELTA'], ['E', 'ECHO'], ['F', 'FOXTROT'], 
          ['G', 'GOLF'], ['H', 'HOTEL'], ['I', 'INDIA'], ['J', 'JULIETT'], ['K', 'KILO'], ['L', 'LIMA'], 
          ['M', 'MIKE'], ['N', 'NOVEMBER'], ['O', 'OSCAR'], ['P', 'PAPA'], ['Q', 'QUEBEC'], ['R', 'ROMEO'], 
          ['S', 'SIERRA'], ['T', 'TANGO'], ['U', 'UNIFORM'], ['V', 'VICTOR'], ['W', 'WHISKEY'], ['X', 'XRAY'], 
          ['Y', 'YANKEE'], ['Z', 'ZULU']]

# Función para buscar el codigo de lo que hayamos ingresado dentro de la lista codigo
def buscar(letra): #Def se utiliza para crear o definir una funcion
    for codigo in aeroCodigo:
        if codigo[0] == letra:
            return codigo[1]
    

# Solicitar al usuario que ingrese el código
entrada = input("Ingrese el código: ").upper() #El método devuelve una cadena donde todos los caracteres están en mayúsculas
#ignora las minisculas y los numeros

# Lista para almacenar el codigo de la lsita que corresponda a cada letra
codigoYfrase = []

# Convertir cada letra del código ingresado a su código aronautico y agregarlo a la lista
for letra in entrada:
    codigoYfrase.append(buscar(letra))
    #El método anexa un elemento al final de la lista

# Unir los códigos en una sola cadena con espacios entre ellos utilizando el join que significa unir.
Resultado = " ".join(codigoYfrase)

# Mostrar el código extendido
print("Código extendido:")
print(Resultado)