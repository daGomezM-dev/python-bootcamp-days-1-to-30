"""
Cuando instalas Python en tu Mac, se instala a nivel Global (para todo el ordenador). 
Sin embargo, cuando los programadores hacemos proyectos, no queremos que las librerías de un 
proyecto se mezclen con las de otro.
Para evitar ese caos, creamos Entornos Virtuales (la carpeta oculta llamada .venv que ves en tu explorador).

Una burbuja (.venv) es, literalmente, una carpeta que coge el motor Global de Python que le digas en 
ese momento, lo clona, y lo aísla.

CREACIÓN: 
1- En el panel izquierdo de VS Code (el Explorador), haz clic derecho sobre la carpeta .venv y dale a Eliminar (Delete/Move to Trash).
2- Presiona Cmd + Shift + P para abrir la paleta de comandos.
3- Escribe Python: Create Environment (Crear Entorno) y haz clic ahí.
4- Selecciona la opción Venv.
5- Te aparecerá la lista de tus intérpretes (la misma que me mandaste en la foto). Selecciona tu Python nuevo (el Global o el de Homebrew, el que prefieras mantener).

"""