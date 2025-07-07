import os

folder = "2. Programacion_Intermedia"
os.makedirs(folder, exist_ok=True)

for i in range(1, 18):
    filename = f"{folder}/02_{i:02d}.py"
    with open(filename, "w") as f:
        f.write("# Archivo generado automáticamente\n")