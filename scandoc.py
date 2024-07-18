import subprocess
import sys
import os

# Establecer la codificación de la consola a UTF-8
os.environ["PYTHONIOENCODING"] = "utf-8"
# Función para instalar paquetes si no están disponibles
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Verificar e instalar las bibliotecas necesarias
required_libraries = ["socket", "censys", "json", "jinja2"]

for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        print(f"Librería {lib} no encontrada. Instalando...")
        install(lib)

import json
import socket
from jinja2 import Template

# Banner con colores personalizados
BANNER = """

  ██████  ▄████▄   ▄▄▄       ███▄    █ ▓█████▄  ▒█████   ▄████▄       
▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▒██▀ ▀█       
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▒▓█    ▄      
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒▓▓▄ ▄██▒     
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░ ████▓▒░▒ ▓███▀ ░     
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░     
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░  ▒        
░  ░  ░  ░          ░   ▒      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░             
      ░  ░ ░            ░  ░         ░    ░        ░ ░  ░ ░           
         ░                              ░               ░             
"""
WARNING = """
El autor de este script no se responsabiliza 
por cualquier uso indebido o ilegal de la herramienta.
"""

# Función para imprimir el banner con colores personalizados
def print_colored_banner(BANNER, WARNING):
    print("\033[1;32m" + BANNER + "\033[0m")
    print("\033[1;37m" + WARNING + "\033[0m")

# Función para obtener la dirección IP de una URL
def obtener_direccion_ip(url):
    try:
        direccion_ip = socket.gethostbyname(url)
        return direccion_ip
    except socket.gaierror:
        return None

def ejecutar_censys_search(ip):
    try:
        # Asegurarse de que la configuración se haya realizado correctamente
        config_command = "censys config"
        subprocess.run(config_command, shell=True, check=True)
        
        # Comando para ejecutar la búsqueda en Censys
        comando = ["censys", "view", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        
        if resultado.returncode == 0:
            print("Búsqueda en Censys exitosa.")
            return json.loads(resultado.stdout.strip())
        else:
            print(f"Error en la búsqueda de Censys. Código de retorno {resultado.returncode}")
            print(f"Mensaje de error: {resultado.stderr}")
            return None
    except Exception as e:
        print(f"Error al ejecutar el comando censys: {e}")
        return None

# Función para guardar JSON en un archivo
def guardar_json(json_data, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(json_data, file, indent=4)
        print(f"JSON guardado exitosamente en {file_name}")
    except Exception as e:
        print(f"Error al guardar JSON: {e}")

def renderizar_html(json_data, template_file, output_file):
    try:
        with open(template_file, 'r') as file:
            template_content = file.read()
            template = Template(template_content)

        # Renderizar el template con los datos del JSON
        rendered_html = template.render(data=json_data)

        with open(output_file, 'w') as file:
            file.write(rendered_html)

        print(f"HTML generado exitosamente en {output_file}")
    except Exception as e:
        print(f"Error al renderizar HTML: {e}")

# Ejecutar el script
if __name__ == "__main__":
    print_colored_banner(BANNER, WARNING)
    print("Obtén tu API Key de Censys en: https://censys.io/account/api")
    print("____________________________________________________________")
    
    url = input("Por favor, ingresa la URL para obtener su dirección IP: ")
    ip = obtener_direccion_ip(url)

    if ip:
        json_data = ejecutar_censys_search(ip)

        if json_data:
            guardar_json(json_data, 'datos_censys.json')

            # Renderizar HTML con Jinja2 basado en los atributos disponibles en el JSON
            template_file = 'template.html'
            output_file = 'informe.html'
            renderizar_html(json_data, template_file, output_file)
    else:
        print(f"No se pudo obtener la dirección IP de {url}")
