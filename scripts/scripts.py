import serial
import serial.tools
import serial.tools.list_ports
import csv
import io


def list_ports() -> list:
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.name)

    return ports


def save_csv(data: list, filename: str):
    with open(str, 'a') as archivo:
        # Agrega una línea al archivo
        archivo.write(data)
