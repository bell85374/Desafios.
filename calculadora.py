import math

historial = []

def calculadora():

    while True:

        print("\nCALCULADORA")
        print("1 Sumar")
        print("2 Restar")
        print("3 Multiplicar")
        print("4 Dividir")
        print("5 Potencia")
        print("6 Modulo")
        print("7 Raiz cuadrada")
        print("8 Ver historial")
        print("9 Limpiar historial")
        print("0 Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "0":
            print("Fin del programa")
            break

        if opcion == "8":
            print("\nHISTORIAL")

            if not historial:
                print("No hay operaciones")
            else:
                for h in historial:
                    print(h)

            continue

        if opcion == "9":
            historial.clear()
            print("Historial borrado")
            continue

        if opcion == "7":

            num = float(input("Numero: "))

            if num < 0:
                print("No se puede calcular raiz de numero negativo")
                continue

            resultado = math.sqrt(num)

            operacion = f"√{num:g} = {resultado:g}"
            historial.append(operacion)

            print("Resultado:", f"{resultado:g}")
            continue

        num1 = float(input("Primer numero: "))
        num2 = float(input("Segundo numero: "))

        if opcion == "1":
            resultado = num1 + num2
            operacion = f"{num1:g} + {num2:g} = {resultado:g}"

        elif opcion == "2":
            resultado = num1 - num2
            operacion = f"{num1:g} - {num2:g} = {resultado:g}"

        elif opcion == "3":
            resultado = num1 * num2
            operacion = f"{num1:g} * {num2:g} = {resultado:g}"

        elif opcion == "4":

            if num2 == 0:
                print("No se puede dividir entre 0")
                continue

            resultado = num1 / num2
            operacion = f"{num1:g} / {num2:g} = {resultado:g}"

        elif opcion == "5":
            resultado = num1 ** num2
            operacion = f"{num1:g} ^ {num2:g} = {resultado:g}"

        elif opcion == "6":
            resultado = num1 % num2
            operacion = f"{num1:g} % {num2:g} = {resultado:g}"

        else:
            print("Opcion invalida")
            continue

        historial.append(operacion)
        print("Resultado:", f"{resultado:g}")


calculadora()