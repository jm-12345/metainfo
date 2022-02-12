import os
"""
Black="\[\033[0;30m\]"        # Black
Red="\[\033[0;31m\]"          # Red
Green="\[\033[0;32m\]"        # Green
Yellow="\[\033[0;33m\]"       # Yellow
Blue="\[\033[0;34m\]"         # Blue
Purple="\[\033[0;35m\]"       # Purple
Cyan="\[\033[0;36m\]"         # Cyan
White="\[\033[0;37m\]"        # White
"""
nombreimg_modificar="---"
tag="Comment"
comment="---"
def limpiar():
    os.system("clear")
def actualizar():
    os.system("pkg update -y && pkg upgrade -y")

def instalar():
    os.system("pkg install exiftool")
    os.system("pkg install perl")

limpiar()

print("\033[0;35m"+"""

███╗░░░███╗███████╗████████╗░█████╗░██╗███╗░░██╗███████╗░█████╗░
████╗░████║██╔════╝╚══██╔══╝██╔══██╗██║████╗░██║██╔════╝██╔══██╗
██╔████╔██║█████╗░░░░░██║░░░███████║██║██╔██╗██║█████╗░░██║░░██║
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║██║╚████║██╔══╝░░██║░░██║
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
Version-1.0
""")
   
print("\033[0;33m"+"""

   1) Sacar metadatos de archivos         3) Borrar todos los metadatos de un archivo

   2) Modificar metadatos de archivos     4) Instalar repositorios (Usar en la primera ejecucion)

   0) Salir
   """)
   
num=input("\033[0;34m"+"""
 Seleccione la herramienta: """)
limpiar()

if num =="1":
    print("\033[0;35m"+"""


╔═══╗
║╔═╗║
║╚══╦══╦══╦══╦═╗
╚══╗║╔╗║╔═╣╔╗║╔╝
║╚═╝║╔╗║╚═╣╔╗║║
╚═══╩╝╚╩══╩╝╚╩╝
╔═╗╔═╗──╔╗─────╔╗──╔╗
║║╚╝║║─╔╝╚╗────║║─╔╝╚╗
║╔╗╔╗╠═╩╗╔╬══╦═╝╠═╩╗╔╬══╦══╗
║║║║║║║═╣║║╔╗║╔╗║╔╗║║║╔╗║══╣
║║║║║║║═╣╚╣╔╗║╚╝║╔╗║╚╣╚╝╠══║
╚╝╚╝╚╩══╩═╩╝╚╩══╩╝╚╩═╩══╩══╝ """)
    print("\033[0;34m")
    nombreimg_extraer=input("Introduzca la el nombre del archivo: ")

    limpiar()

    print("\033[0;32m\]")
    os.system("exiftool -S "+nombreimg_extraer)

elif num=="2":
    print("\033[0;33m")
    print("""
Modificar metadatos
------------------------

Nombre archivo - """+nombreimg_modificar+""" 

Etiqueta/Tag - """+tag+"""

Comentario - """+comment)

    print("\033[0;34m")
    nombreimg_modificar=input("""
Introduzca el nombre del archivo: """)

    limpiar()

    print("\033[0;33m")
    print("""
Modificar metadatos
------------------------

Nombre archivo - """+nombreimg_modificar+"""

Etiqueta/Tag - """+tag+"""

Comentario - """+comment)

    print("\033[0;34m")    
    comment=input("""
Introduce el comentario: """)

    limpiar()

    print("\033[0;33m")
    print("""
Modificar metadatos
------------------------

Nombre archivo - """+nombreimg_modificar+"""

Etiqueta/Tag - """+tag+"""

Comentario - """+comment)

    print("\033[0;34m")
    input("""
Pulsa enter para continuar
""")

    os.system("exiftool -"+tag+"='"+comment+"' "+nombreimg_modificar)

    y_n=input("""
¿Quieres guardar una copia original de la foto?(y/n)

""")
    
    if y_n=="y":
        os.system(f"mv {nombreimg_modificar}_original fotos_originales")
        print("\033[0;32m")
        ruta_origin=os.popen("pwd").read()
        print(f"""
La foto ha sido guardada correctamente en {ruta_origin}""")

    elif y_n=="n":
        os.system(f"rm {nombreimg_modificar}")
        print("\033[0;31m")
        print("""
La foto original se ha boreado""")

elif num =="3":
    print("""

╔══╗
║╔╗║
║╚╝╚╦══╦═╦═╦══╦═╗
║╔═╗║╔╗║╔╣╔╣╔╗║╔╝
║╚═╝║╚╝║║║║║╔╗║║
╚═══╩══╩╝╚╝╚╝╚╩╝
╔═╗╔═╗──╔╗─────╔╗──╔╗
║║╚╝║║─╔╝╚╗────║║─╔╝╚╗
║╔╗╔╗╠═╩╗╔╬══╦═╝╠═╩╗╔╬══╦══╗
║║║║║║║═╣║║╔╗║╔╗║╔╗║║║╔╗║══╣
║║║║║║║═╣╚╣╔╗║╚╝║╔╗║╚╣╚╝╠══║
╚╝╚╝╚╩══╩═╩╝╚╩══╩╝╚╩═╩══╩══╝
""")
    
    print("\033[0;31m")
    print("""SE BORRARAN TODOS LOS METADATOS
            """)
    print("\033[0;34m")
    nombreimg_borrar=input("Introduce el nombe del archivo: ")
    
    os.system("exiftool -all="+ nombreimg_borrar)

elif num =="4":

    actualizar()
    instalar()
    actualizar()
    
elif num =="0":
    print("")
else:
    print("\033[0;31m"+"""
 Error - Opcion invalida""")
