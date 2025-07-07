import os

# Ruta base del repositorio (ajústala si ejecutas el script desde otra ubicación)
base_path = 'domina-python-manipulacion-datos-pandas'
carpeta_nueva = '3. Programacion_Avanzada'
ruta_completa = os.path.join(base_path, carpeta_nueva)

# Crear la carpeta si no existe
os.makedirs(ruta_completa, exist_ok=True)

# Crear los archivos 03_01.py a 03_08.py
for i in range(1, 9):
    nombre_archivo = f'03_{i:02}.py'
    ruta_archivo = os.path.join(ruta_completa, nombre_archivo)
    with open(ruta_archivo, 'w') as f:
        f.write(f'# Archivo: {nombre_archivo}\n# Script de Programación Avanzada #{i}\n')

print(f'✓ Carpeta "{carpeta_nueva}" y archivos creados correctamente en:\n{ruta_completa}')
