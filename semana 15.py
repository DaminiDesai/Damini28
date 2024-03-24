# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Damini",
    "edad": 19,
    "ciudad": "Quito",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "Estudiante"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0986926635"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)

