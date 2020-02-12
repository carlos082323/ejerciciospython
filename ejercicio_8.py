edad = int(input("Digite su edad: "))
print(edad**2)

if edad>=18 and edad<=25:
    print("Tienes entre 18 y 25")
    if(edad>20):
        print("Tienes mas de 20")
        #hola
elif edad>25:
    print("Tiene mas de 25")
else:
    print("Eres menor de edad")
