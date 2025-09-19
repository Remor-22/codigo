def main():
    try:
        num1 = float(input("ingresa el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))
        
        medio = (num1 + num2) / 2
        print(f"El numero del medio entre {num1} Y {num2} es: {medio}")

    except ValueError:
        print("Error: Debes ingresar numeros validos.")

if __name__ == "__main__":
    main()