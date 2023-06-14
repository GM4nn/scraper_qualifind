
# Scraper


Prueba tecnica de Qualifinds




Para ejecutar el proyecto
---------
Para ejecutar el proyecto se debe ejecutar los siguientes comandos situados en la raiz del proyecto


- ``docker build -t scraper_quafilind .``

- ``docker run --name scraper_qua_container -p 8080:80 scraper_quafilind``

## Librerias usadas

Lista de librerias:
- fastapi==0.95.0
- pydantic==1.10.7
- uvicorn==0.21.1
- requests==2.28.2
- beautifulsoup4==4.12.2
- selenium==4.10.0
- chromedriver-autoinstaller==0.4.0
## Notas

Observaciones:

- Se hizo uso de requests para realizar la peticion al endpoint que consumia la plataforma de walmart
- Se hizo uso de selenium para la obtencion de productos por url 
- Debido a que la plataforma de jumbo para obtener productos por url solo traia de a 8, se hizo uso de selenium para asegurar de que se devolviera todos los datos
- PLUS: en el endpoint para obtener productos por url se añadio un parametro llamado "page" el cual se puede ingresar el numero de pagina que desea llamar de la paginacion para la obtencion de los datos, ejemplo de cuerpo de peticion:
    ```
    {
        "url": "https://www.tiendasjumbo.co/tecnologia/informatica/computadores-portatiles",
        "page": 2
    }
    ```

- Se hizo uso de dos time.sleep de 5 segundos debido a que se dificulto realizar un tiempo de espera adecuado a la hora de realizar un scroll hacia abajo y dar click con selenium para obtener la pagina requerida
- En el dockerfile se observa una serie de comandos para instalar el google chrome como tambien su driver para hacer uso de selenium

Documentacion:

- Swagger: http://localhost:8080/docs
- Redoc: http://localhost:8080/redoc
