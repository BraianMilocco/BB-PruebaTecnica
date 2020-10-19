## Aclaración
    Se encuentran tres versiones del programa
    -V_0.1 (primera versión)
    -V_1.0 (segunda versión con código optimizado)
    -V_1.1 (segunda versión con agregado de parámetros para poder recuperar información de parámetros para hacerlo más genérico)

    Los comandos son para sistemas Linux
## Recomendación
    trabajar dentro de un virtualenv nombrado venv (que ya se encuentra en el .gitignore) 

## Requisitos
    python3
    pip
    virtualenv

## Dependencias
    Para instalar dependencias se recomienda

```bash
pip install -r requirements.txt
```

## Ejecutar
    En caso de que no funcione por algún problema de permisos ejecutar en la carpeta correspondiente
```bash
chmod +x netflix_scraping.py
```
    (el script imprime el json en pantalla, en caso de querer recuperar la información en un archivo agregar al final un:
     > nombre_archivo.json
    )

    Ir a la carpeta de la versión 
### V_0.1
```bash
 python3 ./netflix_scraping.py
```

### V_1.0
```bash
 python3 ./netflix_scraping.py
```
### V_1.1
Para ver los datos de series ya precargadas para buscar:
```bash
 python3 ./netflix_scraping.py --series
```
Para ver de donde sale el numero de la serie que quiero buscar:
```bash
 python3 ./netflix_scraping.py --ayuda
```

Para buscar una serie particular
```bash
 python3 ./netflix_scraping.py numeroserie 
```



