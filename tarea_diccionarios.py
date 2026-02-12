# Tarea: Trabajando con Diccionarios

# 1. Crear un Diccionario:
# Crea un diccionario llamado 'informacion_personal' con información ficticia.
informacion_personal = {
    "nombre": "Sofia García",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Diseñadora Gráfica"
}

# 2. Acceder y Modificar Valores:
# Accede al valor asociado a la clave "ciudad" y modifícalo.
informacion_personal["ciudad"] = "Barcelona"

# Agrega una nueva clave-valor para representar un dato adicional.
informacion_personal["telefono"] = "987-654-3210"

# 3. Verificar Existencia de Claves:
# Verifica si la clave "email" existe. Si no, agrégala con un valor ficticio.
if "email" not in informacion_personal:
    informacion_personal["email"] = "sofia.garcia@email.com"

# 4. Eliminar una Clave:
# Elimina la clave "profesion" del diccionario.
del informacion_personal["profesion"]

# 5. Imprimir el Diccionario Final:
# Imprime el diccionario resultante después de todas las operaciones.
print(informacion_personal)