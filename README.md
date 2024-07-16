### Automated Vulnerabilities Report Generator (AVRG)

Este proyecto es un script Python diseñado para automatizar la recolección de información de servicios de red utilizando la API de Censys. El script realiza escaneos de IP y recopila datos detallados sobre servicios, software asociado, ubicación geográfica, y más, proporcionando un informe detallado en formato HTML.

**Características principales**

- **Escaneo de IP Automatizado:** Utiliza la API de Censys para obtener información detallada sobre servicios expuestos en direcciones IP específicas.
- **Generación de Informes en HTML:** Crea informes detallados en formato HTML, incluyendo detalles como banners de servicio, versiones de software, y métodos de descubrimiento.
- **Inclusión de Información Geográfica y de Red:** Muestra datos sobre ubicación geográfica, información de AS (Sistema Autónomo), y detalles WHOIS de la organización propietaria de la dirección IP.
- **Búsqueda de CVEs:** Incluye enlaces directos para buscar exploits relacionados con los servicios y software identificados en el informe, facilitando la investigación de posibles vulnerabilidades.

### Uso

Clonación del Repositorio:

- git clone git@github.com:Jared0307/scandoc.git
- cd scandoc

Configuración de la API de Censys:

- Crea una cuenta en Censys si aún no tienes una.
- Obtén tus credenciales de API desde tu cuenta de Censys.

Asegúrate de tener Python 3.x instalado.

Ejecuta el script: 

- python scandoc-v5.py

**Generación de Informes:** El script generará automáticamente un informe en formato HTML en el directorio especificado, detallando los servicios encontrados y otra información relevante. En el informe generado, encontrarás enlaces directos para buscar exploits relacionados con los servicios y software identificados.

### Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `Jinja2`

### Ejecución
![image](https://github.com/user-attachments/assets/853926d8-bdd6-4033-a8f9-7c0ea3c7ce4d)
### Reporte
![image](https://github.com/user-attachments/assets/bc0df527-0def-4056-a541-1eaa6c37fc93)
### Links directos a exploits
![image](https://github.com/user-attachments/assets/c1dc832a-27b2-44c3-ba53-f51ea6c2838f)

### Contribución

Si deseas contribuir a este proyecto, siéntete libre de bifurcarlo y enviar solicitudes de extracción. Cualquier mejora en la generación de informes, corrección de errores o adición de nuevas características es bienvenida.

