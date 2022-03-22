## Adivina adivinador....
import random
numero_aleatorio = random.randrange(100)     ##Ahora es entre 0..100
gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 99")
intento = 1
while intento < 6 and not gane:              ## Cambia para que sen 5 intentos
    numero_ingresado = int(input('Ingresa tu número: '))  ##se cambia numeroIngresado a numero_ingresado para cumplir con las convenciones adoptadas
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))