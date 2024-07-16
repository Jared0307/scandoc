### Automated Vulnerabilities Report Generator (AVRG)

Este proyecto es un script Python diseñado para automatizar la recolección de información de servicios de red utilizando la API de Censys. El script realiza escaneos de IP y recopila datos detallados sobre servicios, software asociado, ubicación geográfica, y más, proporcionando un informe detallado en formato HTML.

**Características principales**

- **Escaneo de IP Automatizado:** Utiliza la API de Censys para obtener información detallada sobre servicios expuestos en direcciones IP específicas.
- **Generación de Informes en HTML:** Crea informes detallados en formato HTML, incluyendo detalles como banners de servicio, versiones de software, y métodos de descubrimiento.
- **Inclusión de Información Geográfica y de Red:** Muestra datos sobre ubicación geográfica, información de AS (Sistema Autónomo), y detalles WHOIS de la organización propietaria de la dirección IP.
- **Búsqueda de CVEs:** Incluye enlaces directos para buscar exploits relacionados con los servicios y software identificados en el informe, facilitando la investigación de posibles vulnerabilidades.

### Uso

**Configuración:** Asegúrate de tener las credenciales de API de Censys configuradas correctamente en el script.
**Ejecución:** Ejecuta el script Python `scandoc-v5.py`, especificando las direcciones IP objetivo.
**Generación de Informes:** El script generará automáticamente un informe en formato HTML en el directorio especificado, detallando los servicios encontrados y otra información relevante.

### Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `Jinja2`

![image](https://github.com/user-attachments/assets/ccb17dcc-a5dd-4f14-adf7-5c3062125bf0)

![image](https://github.com/user-attachments/assets/bc0df527-0def-4056-a541-1eaa6c37fc93)

![image](https://github.com/user-attachments/assets/c1dc832a-27b2-44c3-ba53-f51ea6c2838f)

### Contribución

Si deseas contribuir a este proyecto, siéntete libre de bifurcarlo y enviar solicitudes de extracción. Cualquier mejora en la generación de informes, corrección de errores o adición de nuevas características es bienvenida.

