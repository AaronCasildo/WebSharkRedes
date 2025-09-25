# 🌐 TCPDUMP Network Analysis Tool
<img width="547" height="250" alt="image" src="https://github.com/user-attachments/assets/eec1c9e7-009b-412e-b08e-fed8abf4667b" />

Una herramienta interactiva en Python para análisis y captura de tráfico de red usando `tcpdump`. Perfecta para administradores de sistemas, profesionales de seguridad y estudiantes de redes.

## 🚀 Características

- **Interfaz de menú intuitiva** - Navegación fácil con opciones numeradas
- **Múltiples métodos de captura** - TCP, UDP, ICMP y más protocolos
- **Filtrado avanzado** - Por IP, puerto, tamaño de paquete y rangos de red
- **Exportación a PCAP** - Guarda capturas para análisis posterior con Wireshark
- **Análisis en tiempo real** - Monitoreo live del tráfico de red
- **Filtros especializados** - Para tráfico web (puertos 80/443) y más

## Funcionalidades Principales

| Opción | Descripción |
|--------|-------------|
| **1** | Mostrar interfaces de red disponibles |
| **2** | Capturar número específico de paquetes |
| **3** | Seleccionar interfaz específica |
| **4** | Filtrar por protocolo (TCP/UDP/ICMP) |
| **5** | Mostrar paquetes en formato ASCII |
| **6** | Capturar con timestamp completo |
| **7** | Guardar en archivo .pcap |
| **8** | Filtrar por IP o rango de red |
| **9** | Filtrar por puerto específico |
| **10** | Captura dirigida (IP + Puerto) |
| **11** | Tráfico web (puertos 80/443) |
| **12** | Filtrar por tamaño de paquete |

## 📋 Requisitos Previos
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/23ffb807-1f3a-4fd1-9fd1-66a39bd0dcb0" />

- **Sistema Operativo**: Linux/Unix (Ubuntu, Debian, CentOS, etc.)
- **Python**: 3.6 o superior
- **Permisos**: Usuario con acceso sudo
- **Dependencias**: tcpdump instalado

### Instalación de tcpdump

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install tcpdump

# CentOS/RHEL
sudo yum install tcpdump

# Fedora
sudo dnf install tcpdump
```

## 🔧 Instalación y Uso

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/AaronCasildo/WebSharkRedes.git
   cd WebSharkRedes
   ```

2. **Ejecuta la herramienta**:
   ```bash
   python3 tcp_shark.py
   ```

3. **Selecciona una opción** del menú interactivo

## 💡 Ejemplos de Uso

### Capturar tráfico HTTP/HTTPS
```bash
# Selecciona la opción 11 en el menú
# Ingresa la IP destino: 192.168.1.100
```

### Analizar paquetes grandes
```bash
# Selecciona la opción 12 en el menú  
# Ingresa el tamaño: 1500
```

### Guardar captura para Wireshark
```bash
# Selecciona la opción 7 en el menú
# Ingresa el nombre: mi_captura
# Resultado: mi_captura.pcap
```

## 📖 Guía de Comandos tcpdump

El repositorio incluye una **guía completa** con todos los comandos tcpdump más utilizados:

- Filtrado por protocolos
- Captura por interfaces
- Filtros de red y puertos
- Opciones de formato y salida
- Ejemplos prácticos

## 🛡️ Casos de Uso
<img width="1854" height="639" alt="image" src="https://github.com/user-attachments/assets/e638cfd7-92fb-4b66-967c-e4b21cee2923" />

### Administración de Sistemas
- Monitoreo de tráfico de red
- Diagnóstico de conectividad
- Análisis de rendimiento

### Seguridad Informática
- Detección de tráfico sospechoso
- Análisis forense de red
- Monitoreo de intrusiones

### Desarrollo y Testing
- Debug de aplicaciones de red
- Análisis de APIs REST
- Testing de conectividad

## ⚠️ Consideraciones de Seguridad

- **Permisos**: Requiere privilegios de administrador (sudo)
- **Privacidad**: Respeta las políticas de privacidad de tu organización
- **Legal**: Usa solo en redes donde tengas autorización
- **Datos**: Los archivos .pcap pueden contener información sensible

---

**⭐ Si te parece útil esta herramienta, ¡no olvides darle una estrella al repositorio!**
