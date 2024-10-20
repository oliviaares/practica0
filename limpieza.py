import re

# Leer el contenido del archivo requirements.txt
with open('requirements.txt', 'r') as f:
    lines = f.readlines()

# Filtrar líneas que contienen rutas locales (file://) y mantener solo las líneas con el formato correcto
clean_lines = [re.sub(r'\s*@.*', '', line) for line in lines]

# Escribir el nuevo archivo requirements.txt limpio
with open('requirements.txt', 'w') as f:
    f.writelines(clean_lines)

print("requirements.txt limpio creado con éxito.")

