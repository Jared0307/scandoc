import subprocess
import sys

# Función para instalar paquetes si no están disponibles
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Verificar e instalar las bibliotecas necesarias
required_libraries = [
    "requests",
    "jinja2",
    "json"
]

for lib in required_libraries:
    try:
        __import__(lib)
        print(f"Librería {lib} encontrada.")
    except ImportError:
        print(f"Librería {lib} no encontrada. Instalando...")
        install(lib)

import json
import requests
from jinja2 import Template

# Banner con colores personalizados
BANNER = """
___________________________________________________________________

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
___________________________________________________________________
"""

# Función para imprimir el banner con colores personalizados
def print_colored_banner(banner, warning):
    # Verde brillante para el banner principal
    print("\033[1;32m" + banner + "\033[0m")
    # Blanco para el texto de advertencia
    print("\033[1;37m" + warning + "\033[0m")

# Función para obtener datos de Censys
def get_censys_data(ip, api_id, api_secret):
    CENSYS_API_URL = f"https://search.censys.io/api/v2/hosts/{ip}"

    try:
        response = requests.get(CENSYS_API_URL, auth=(api_id, api_secret))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error en la solicitud a Censys: {err}")
        return None

# Función para generar el informe HTML
def generate_html_report(data):
    # Abre el archivo de plantilla HTML
    with open("template.html", "r", encoding="utf-8") as file:
        template_content = file.read()

    # Renderiza la plantilla con los datos estructurados
    template = Template(template_content)
    html_output = template.render(data=data)

    # Guarda el resultado en un archivo HTML
    with open("informe.html", "w", encoding="utf-8") as file:
        file.write(html_output)

    print("Informe HTML generado correctamente.")


# Función para estructurar los datos de Censys para la plantilla
def format_censys_data(data):
    formatted_data = {
        "ip": data["ip"],
        "location": data["location"],
        "autonomous_system": data["autonomous_system"],
        "services": []
    }

    for service in data["services"]:
        formatted_service = {
            "service_name": service["service_name"],
            "port": service["port"],
            "transport_protocol": service["transport_protocol"],
            "banner": service.get("banner", ""),
            "labels": service["labels"]
        }
        formatted_data["services"].append(formatted_service)

    formatted_data["whois"] = data.get("whois", {})
    formatted_data["last_updated_at"] = data.get("last_updated_at", "")

    return formatted_data


# Función principal
def main():
    print_colored_banner(BANNER, WARNING)
    print("Obtén tu API Key de Censys en: https://censys.io/account/api")
    ip = input("Introduce la IP a escanear: ")
    api_id = input("Introduce tu Censys API ID: ")
    api_secret = input("Introduce tu Censys API Secret: ")

    # Obtiene los datos de Censys
    censys_data = get_censys_data(ip, api_id, api_secret)

    if censys_data:
        # Imprime los datos en formato JSON
        json_data = json.dumps(censys_data, indent=4)
        print("Datos en texto claro:")
        print(json_data)

        # Genera el informe HTML con los datos obtenidos
        generate_html_report(censys_data)
    else:
        print("No se pudo obtener datos de Censys.")

if __name__ == "__main__":
    main()
