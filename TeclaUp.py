#investigar como leer un caracter del teclado:
#si deseas leer solo un carácter desde el teclado en python puedes hacerlo utilizando la funcion input() junto con indexación para obtener el primer caracter.

#escribir un programa que corra un bucle infinito leyendo e imprimiendo la teclas y solo termnara cuando se precione la tecla ↑ indicada como UP.

from readchar import readkey, key

def check_for_up_key():
    #funcion para verificar si ha presionado la tecla de felcha arriba 
    while True: 
        k = readkey()
        if k == key.UP: 
            print("se preciono la tecla ↑. Saliendo del bucle.") 
            break  

#iniciar el bucle para verificar la tecla de flecha arriba 
check_for_up_key()