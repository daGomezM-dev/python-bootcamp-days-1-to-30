"""
PyPi: Python Package Index
    Software developed and shared by developers to the python community
    It's like App Store for developers
    URL: https://pypi.org

    COMO INSTALAR PAQUETES:
El encargado de ir a esa "tienda", descargar el paquete y meterlo en tu proyecto es 
una herramienta que ya viene preinstalada en tu entorno: pip (Python Package Installer).

Como ahora tienes tu entorno virtual (.venv) perfectamente configurado, cualquier cosa que 
instales se guardará exclusivamente en la carpeta lib de tu burbuja. Tu Mac seguirá impecable por fuera.

    1- Verifica tu terminal: Abre la terminal integrada de VS Code. Fíjate que al principio de la línea de 
    comandos aparezca el texto (.venv). Esto es tu confirmación visual de que la terminal está dentro de la 
    burbuja y no apuntando a tu sistema global.

    2- Descarga el paquete: Supongamos que quieres instalar un paquete muy útil llamado prettytable 
    (sirve para dibujar tablas visuales directamente en la consola). Escribe este comando y pulsa Enter:
        pip install prettytable

    3- Importa y usa el paquete: Vuelve a tu archivo main.py. Ahora que el paquete está en tu disco duro, 
    tienes que decirle a tu código que lo traiga para poder usarlo, exactamente con la misma sintaxis que 
    usaste para importar librerías internas como random o turtle.

    
    TIPS EXTRA: 
¿COMO SE QUE HAY EN MI BURBUJA? 
Si en algún momento no recuerdas qué paquetes tienes instalados en tu proyecto, simplemente escribe 
    pip list
en la terminal. Te devolverá un inventario completo de todo lo que hay dentro de tu .venv junto con sus 
versiones exactas.

ACTUALIZAR PAQUETES
Si necesitas la última versión de un paquete que ya tienes, el comando es
    pip install --upgrade nombre_del_paquete.

DESINSTALAR
Si has metido un paquete por error o ya no lo necesitas, puedes sacarlo de la burbuja fácilmente con
    pip uninstall nombre_del_paquete.

"""

from prettytable import PrettyTable

# Creamos un objeto a partir del molde (Clase) que acabamos de descargar
table = PrettyTable()

# Usamos los métodos del objeto para añadir datos
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Lo alineo a la izquierda en vez de al centro (modificacion de atributo)
table.align = "l"
print(table)
