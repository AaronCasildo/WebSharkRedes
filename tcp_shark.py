import subprocess
import sys

def bienvenida():
    subprocess.run(["clear"])  # Se limpia la pantalla.
    print('Bienvenido al menú de configuración de red con TCPDUMP')
    print('Seleccione una opción:\n')

def menu():
    subprocess.run(["clear"])  # Se limpia la pantalla.
    print('1 - Mostrar interfaces de red disponibles')
    print('2 - Capturar un número específico de paquetes y guardarlos en un archivo')
    print('3 - Seleccionar una interfaz específica para capturar paquetes')
    print('4 - Capturar paquetes específicos (TCP, UDP, ICMP, etc.)')
    print('5 - Mostrar solo paquetes en ASCII')
    print('6 - Capturar con fecha y hora')
    print('7 - Guardar la captura en un archivo .pcap y mostrar el número de paquetes capturados')
    print('8 - Filtrar por dirección IP o rango de red (mostrando IP y puerto)')
    print('9 - Filtrar por puerto / tipo de puerto / rango de puertos')
    print('10 - Capturar paquetes con destino a una IP y puerto específico')
    print('11 - Capturar paquetes con IP destino específica y puerto 80 o 443')
    print('12 - Capturar tráfico filtrando por tamaño del paquete')
    print('\n00 - Salir')

    return int(input('Ingrese una opción: '))  # Se solicita ingresar una opción.

def process1():
    subprocess.run(["clear"])
    subprocess.run(["tcpdump", "-D"])
    input('\nPresione Enter para regresar al menú principal...')
    
def process2():
    packets = input('Ingrese el número de paquetes a capturar: ')
    file = input('Ingrese el nombre del archivo (Sin extensión): ')
    subprocess.run(["tcpdump", "-c", packets, "-w", file + ".pcap"])
    input('\nPresione Enter para regresar al menú principal...')

def process3():
    interface = input('Ingrese el nombre de la interfaz: ')
    subprocess.run(["tcpdump", "-i", interface])
    input('\nPresione Enter para regresar al menú principal...')

def process4():
    interface = input('Ingrese el nombre de la interfaz: ')
    protocol = input('Ingrese el protocolo a capturar (tcp, udp, icmp, etc.): ')
    subprocess.run(["tcpdump", "-i", interface, protocol])
    input('\nPresione Enter para regresar al menú principal...')

def process5():
    subprocess.run(["tcpdump", "-A"])
    input('\nPresione Enter para regresar al menú principal...')

def process6():
    subprocess.run(["tcpdump", "-tttt"])
    input('\nPresione Enter para regresar al menú principal...')

def process7():
    file = input('Ingrese el nombre del archivo para guardar la captura: ')
    subprocess.run(["tcpdump", "-w", file + ".pcap"])
    input('\nPresione Enter para regresar al menú principal...')

def process8():
    ip = input('Ingrese la dirección IP o el rango de red: ')
    subprocess.run(["tcpdump", "host", ip])
    input('\nPresione Enter para regresar al menú principal...')

def process9():
    port = input('Ingrese el puerto o rango de puertos: ')
    subprocess.run(["tcpdump", "port", port])
    input('\nPresione Enter para regresar al menú principal...')

def process10():
    ip = input('Ingrese la IP de destino: ')
    port = input('Ingrese el puerto de destino: ')
    subprocess.run(["tcpdump", "dst", ip, "and", "port", port])
    input('\nPresione Enter para regresar al menú principal...')

def process11():
    ip = input('Ingrese la IP destino: ')
    subprocess.run(["tcpdump", "dst", ip, "and", "(port 80 or port 443)"])
    input('\nPresione Enter para regresar al menú principal...')

def process12():
    size = input('Ingrese el tamaño del paquete en bytes: ')
    subprocess.run(["tcpdump", "greater", size])
    input('\nPresione Enter para regresar al menú principal...')

def exit_program():
    print('Saliendo...')
    sys.exit()

funciones = {
    1: process1,
    2: process2,
    3: process3,
    4: process4,
    5: process5,
    6: process6,
    7: process7,
    8: process8,
    9: process9,
    10: process10,
    11: process11,
    12: process12,
    00: exit_program
}

def main():
    bienvenida()
    while True:
        x = menu()
        if x in funciones:
            funciones[x]()
        else:
            print('Opción no válida. Intente de nuevo.')
            input('\nPresione Enter para continuar...')

if __name__ == "__main__":
    main()
