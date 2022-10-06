#Se importa lo necesario.
import re
#Se crea una función.
def comprobarContrasena(password):
#Se define las variables a utilizar
    largo = False
    mayus = False
    numer = False
    espe = True
#Se comprueba si la contraseña posee 8 o más dígitos.
    if len(password) >= 8:
        largo = True
#Se recorre toda la contraseña para validar que posea al menos una mayúscula.        
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
#Se recorre toda la contraseña para validar que posea al menos un número.
        if password[i].isnumeric():
            numer = True
#Se recorre toda la contraseña para validar que posea al menos un caracter especial.
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(password) == None):
        espe = False
#Se realizan validaciones y se notifica al usuario lo que se requiere.
    if largo == True:
        print("Tu contraseña posee al menos ocho dígitos")
    else:
        print("Muy corta mínimo 8 carácteres")        
    if espe == True:
        print("Tu contraseña posee al menos un caracter especial")
    else:
        print("Falta  al menos un caracter especial [@_!#$%^&*()<>?/\|}{~:]")

    if mayus == True:
        print("Tu contraseña posee al menos una mayúscula.")
    else:
        print("Falta al menos una mayúscula.")
    if numer == True:
        print("Tu contraseña posee al menos un número.")
    else:
        print("Falta al menos un número.")
#Se valida que la contraseña sea robusta.
    if largo and mayus and numer and espe:
        return True
    else:
        return False
#Se emula un do_while.
while True:
#Se solicita la contraseña al usuario.
	password = input("Ingrese contraseña\na comprobar: ")
#Se utiliza la funcion y se notifica al usuario.	
	verificacion = comprobarContrasena(password)
	if verificacion:
			print("La contraseña es segura.")
			break
	else:
    		print("La contraseña NO es segura.")
