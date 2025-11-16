import csv
import io

# Supongamos que esta es tu cadena CSV
csv_string = "nombre,edad,ciudad \n Juan,28,Buenos Aires \n María,22,Córdoba \n Pedro,35,Rosario"

# Utilizamos io.StringIO para tratar la cadena como un archivo
csv_file = io.StringIO(csv_string)

with open('archivo.csv', 'a') as archivo:
    # Agrega una línea al archivo
    archivo.write(csv_string)

# Leemos el contenido del "archivo" CSV
reader = csv.reader(csv_file)

# Convertimos el contenido en una lista de listas
data = list(reader)

# Mostramos el contenido
for row in data:
    print(row)
