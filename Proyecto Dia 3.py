texto = input("Crea un Texto ")
letras = []

texto = texto.lower()



letras.append(input("Coloque la primera letra: ").lower())
letras.append(input("Coloque la segunda letra: ").lower())
letras.append(input("Coloque la tercera letra: ").lower())


print("\n")
print("CANTIDAD DE LETRAS")


cantidad_letras = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras} veces. ")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces. ")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces. ")

print("\n")
print("CANTIDAD DE PALABRAS")


cantidad_de_palabras = texto.split()
print(f"Hemos encontrado {len(cantidad_de_palabras)} palabras")

print("\n")
print("LETRAS DE INICIO Y FIN")
letra_In = texto[0]
letra_fin = texto[-1]
print(f"La primera letra es {letra_In} y la ultima {letra_fin}")

print("\n")
print("TEXTO INVERTIDO")
cantidad_de_palabras.reverse()
texto_invertido = ' '.join(cantidad_de_palabras)
print(f" Si ordenamos tu texto alrevez: {texto_invertido}.\n Seria el resultado")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")

if "python" in texto:
    print("La palabra Python se encuentra en el texto")
else:
    print("La palabra Python no se encuentra en el texto")


#dicPython = "python" in texto
#dic = {True:"si", False:"no"}
#print(f"La palabra 'Python' {dic[dicPython]} se encuentra en el texto")
