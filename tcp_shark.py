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
    print('5 - Capturar paquetes y desplegarlos en ascii')
    print('6 - Capturar paquetes con fecha y hora')
    print('7 - Guardar la captura en un archivo `.pcap` y mostrar el número de paquetes capturados')
    print('\n00 - Salir')

def main():
    while True:
        menu()  # Mostrar menú en cada iteración
        try:
            x = int(input('Ingrese una opción: '))  # Solicitar opción del usuario
            if x in funciones:
                funciones[x]()
            else:
                print('Opción no válida. Intente de nuevo.')
                input('Presione Enter para continuar...')
        except ValueError:
            print('Error: Ingrese un número válido.')
            input('Presione Enter para continuar...')

def process1(): 
    subprocess.run(["clear"])
    subprocess.run(["tcpdump", "-D"])  # Corregido "tpcdump" a "tcpdump"
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
    interface = input('Ingrese el nombre de la interfaz (normalmente se llama enp0s3): ')
    protocol = input('Ingrese el protocolo a capturar (TCP, UDP, ICMP, etc.): ')
    subprocess.run(["tcpdump", "-c 100","-i", interface, protocol])  # Corrección en el comando
    input('\nPresione Enter para regresar al menú principal...')

def process5():
    subprocess.run(["tcpdump", "-c 100", "-A"])
    input('\nPresione Enter para regresar al menú principal...')

def procces6():
    subprocess.run(["tcpdump", "-c 100", "-tttt"])
    input('\nPresione Enter para regresar al menú principal...')    

def procces7(): #pendiente de ser completado
    subprocess.run(["tcpdump", "-c 100", "-w", "captura.pcap"])
    print('Número de paquetes capturados:')  # Se agrega mensaje
    subprocess.run(["tcpdump", "-r", "captura.pcap", "-c", "100"])
    subprocess.run(['tcpdump -r <archivo.pcap> | wc -l'])
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
    6: procces6,
    7: procces7,	
    00: exit_program
}

if __name__ == "__main__":
    bienvenida()
    main()
