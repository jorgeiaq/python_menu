print("bienvenido")

exercises1 = int(input("ingrese un numero del 40 al 42 para ejercutar un taller: "))

selected_workshop == 41:
        if exercises1 == 1:
            #ejercicio 1
            base = float(input("ingrese la base del triangulo"))
            height = float(input("ingrese la altura del triangulo"))
            area = (base * height) / 2
            print("el area del triangulo es:", area)

        elif exercises1 == 2:
            #ejercicio 2
            num1 = float(input("ingrese un numero"))
            num2 = float(input("ingrese otro numero"))
            operation= num1 + num2
            print("el resultado de la operacion es", num1, "y", num2, "es:", operation)

        elif exercises1 == 3:
            # ejercicio 3
            num = float(input("ingrese un numero cualquiera"))
            result = num ** 2
            print("el resultado es", num, "es", result)

        elif exercises1 == 4:
            # ejercicio 4
            addition = 1234 + 532
            print("la suma da como resultado:", addition)

        elif exercises1 == 5:
            # ejercicio 5
            subtraction = 1234 - 532
            print("el resultado es:", subtraction)

        elif exercises1 == 6:
            # ejercicio 6
            multiplication = 1234 * 532
            print("el resultado es:", multiplication)

        elif exercises1 == 7:
            # ejercicio 7
            division = 1234 / 532
            print("la division da como resultado:", division)

        elif exercises1 == 8:
            # ejercicio 8
            num1 = 1234
            num2 = 532
            module = num1 % num2
            print("el modulo es:", module)

        elif exercises1 == 9:
            # 1 euro equivale 1,10 dolares
            euro = float(input("ingrese la cantidad a convertir"))
            dollar = 1.10
            change = euro * dollar
            print("su cambio es:", change)

        elif exercises1 == 10:
            # ejercicio 10
            height = float(input("ingrese el valor"))
            width = float(input("ingrese la anchura"))
            area = height * width
            print("el area del rectangulo es:" + str(area))

        elif exercises1 == 11:
            # ejercicio 11
            side = float(input("el lado del cuadrado es"))
            area = side ** 2
            perimeter = 4 * side
            print("el area del cuadrado es:", area)
            print("el perimetro es:", perimeter)
            print("el lado es:", side)

        elif exercises1 == 12:
            # ejercicio 12
            import math
            radio = float(input("ingrese el valor"))
            height = float(input("ingrese el valor"))
            volume = math.pi * radio**2 * height 
            area = 2 * math.pi * radio * height + 2 * math.pi * radio**2
            print("el volumen del cilindro es:", volume)
            print("el area es:", area)

        elif exercises1 == 13:
            # ejercicio 13
            import math
            radio = float(input("ingrese el radio de la circunferencia"))
            length = 2 * math.pi * radio 
            area = math.pi * radio ** 2
            enrolled_area =(math.pi * radio ** 2) / 2
            print("el area es:", area)
            print("la longitud:", length)
            print("el area del circulo inscrito es:", enrolled_area)

        elif exercises1 == 14:
            # ejercicio 14
            num1 = float(input("ingrese un numero"))
            num2 = float(input("ingrese otro numero"))
            num3 = float(input("ingrese otro numero"))
            prom = (num1 + num2 +num3) / 3
            print("el promedio de los numeros es:", prom)

selected_workshop = 42:
        elif exercises2 == 15:
            print("Ingresa un número")
            number = int(input("Ingrese un número para saber si es positivo o negativo: "))

        if number >= 0:
            print("El número es positivo:", number)
        else:
            print("El número es negativo:", number)

        elif exercises2 == 16:
            # Ejercicio 2: Número mayor y menor
            print("Bienvenido al programa")
            number1 = int(input("Ingrese el primer número: "))
            other = int(input("Ingrese otro número: "))

        if number1 > other:
            elderly = number1
            minor = other
        else:
            elderly = other
            minor = number1

            print("El número mayor es:", elderly)
            print("El número menor es:", minor)

        elif exercises2 == 17:
            # Ejercicio 3: Número mayor y menor de tres números
            print("Ingrese tres números")
            number1 = int(input("Digite el primer número: "))
            number2 = int(input("Digite un segundo número: "))
            number3 = int(input("Digite un último número: "))

        if number1 > number2 and number1 > number3:
            elderly = number1
        elif number2 > number3 and number2 > number1:
            elderly = number2
        else:
            elderly = number3

        if number1 < number2 and number1 < number3:
            minor = number1
        elif number2 < number1 and number2 < number3:
            minor = number2
        else:
            minor = number3

            print("El número mayor es:", elderly)
            print("El número menor es:", minor)

        elif exercises2 == 18:
            # Ejercicio 4: Sueldo de empleados con horas extra
            print("Bienvenido")
            name = input("Ingrese su nombre: ")
            hours = float(input("Ingrese las horas trabajadas: "))

            value_hours = 4
            extra_value = value_hours * 2

        if hours <= 48:
            salary = hours * value_hours
            print("El empleado", name, "tiene un sueldo de:", salary)
        else:
            extra_hours = hours - 48
            extra_salary = extra_hours * extra_value
            total_salary = 48 * value_hours + extra_salary
            print("El empleado", name, "tiene un sueldo con horas extras de:", total_salary)

        elif exercises2 == 19:
            # ejercicio 5 suma o resta

            print("BIENVENIDO ingresa lo que se te solicita")
            # variables de suma y resta
            a = float(input("ingresa un numero: "))
            b = float(input("ingresa un numero para la letra b: "))

        if a < b:
            subtraction = a - b
            print("el resultado es:", subtraction)

        elif a > b:
            addition = a + b
            print("el resultado de la suma es:", addition) 
        elif exercises2 == 20:
            # ejercicio 6 cociente de 2 numeros

            print("bienvenido")

            A = int(input("ingresa un numero: "))
            B = int(input("ingresa otro numero: "))



        if A > 0 and B > 0:
            quotient = A // B
            print("la operacion da como resultado: ", quotient)
        else:
            print("la division es imposible")
        elif exercises2 == 21:
            # ejercicio 7 triangulo equilatero

            print("ingrese lo solicitado para determinar si el triangulo es equilatero o no")
            # variables side para los lados del triangulo
            side1 = int(input("ingrese el lado 1 del triangulo: "))
            side2 = int(input("ingrese el lado 2 del triangulo: "))
            side3 = int(input("ingrese el ultimo lado del triangulo: "))

            # proceso para determinar si el triangulo es equilatero

        if side1 == side2 and side2 == side3:
            print("los tres datos son iguales esto significa que el triangulo es equilatero.")
        else:
            print("no es equilatero.")
        elif exercises2 == 22:
            # ejercicio 8 suma o multiplicacion de dos numeros

            print("ingrese lo solicitado")
            # inicio
            a = int(input("ingrese un numero para a: "))
            b = int(input("ingrese un numero para b: "))

            # proceso
            addition = a + b
            if a > 0 and b > 0:
            print("devido a que los dos numeros son positivos entonces se sumaran: ", addition)
            elif a < -1 and b < -1:
            multiplication = -a * (-b)
            print("en este caso se multiplicara: ", multiplication)
        elif exercises2 == 23:
            # incicio del programa
            print("ingresa tu dia nacimiento correspondiente a este se le dara su signo zodiacal.")
            # variables day y month para el ejercicio
            day = int(input("ingrese su dia de nacimiento: "))
            month = int(input("ingresa tu mes de nacimiento: "))

        if month == 3 and day >= 21 or month == 4 and day <= 19:
            print("tu signo es aries.")
        elif month == 4 and day >= 20 or month == 5 and day <= 20:
            print("tu signo es tauro.")
        elif month == 5 and day >= 21 or month == 6 and day <= 20:
            print("tu signo es geminis.")
        elif month == 6 and day >= 21 or month == 7 and day <= 22:
            print("tu signo es cancer.")
        elif month == 7 and day >= 23 or month == 8 and day <= 22:
            print("tu signo es leo.")
        elif month == 8 and day >= 23 or month == 9 and day <= 22:
            print("tu signo es virgo.")
        elif month == 9 and day >= 23 or month == 10 and day <= 22:
            print("tu signo es libra.")
        elif month == 10 and day >= 23 or month == 11 and day <= 21:
            print("tu signo es escorpio.")
        elif month == 11 and day >= 22 or month == 12 and day <= 21:
            print("tu signo es sagitario.")
        elif month == 12 and day >= 22 or month == 1 and day <= 19:
            print("tu signo es capricornio.")
        elif month == 1 and day >= 20 or month == 2 and day <= 18:
            print("tu signo es acuario.")
        elif month == 2 and day >= 19 or month == 3 and day <= 20:
            print("tu signo es picis.")

        elif exercises2 == 24:
            # ejercicio 10 perimetro y area 

            print("ingrese los valores.")

            base = int(input("ingrese la base del cuadrilatero: "))
            heigth = int(input("ingrese la altura del cuadrilatero: "))



        if base == heigth:
            print("el cuadrilatero es un cuadrado.")
            side1 = int(input("ingrese el lado 1:"))
            side2 = int(input("ingrese el segundo lado:"))
            perimeter1 = 4 * base
            print("el perimetro es:", perimeter1)
            surface1 = side1 * side2
            print("la superfifice es:", surface1)
        else:
            print("el cuadrilatero es un rectangulo.")
            perimeter2 = 2 * (base + heigth)
            print("el perimetro es:", perimeter2)
            surface2 = base * heigth
            print("la superficie es:", surface2)
        elif exercises2 == 25:
            # ejercicio 11 descuentos de productos

            # inicio
            print("BIENVENIDO")

            buys = int(input("ingrese el valor de sus compra para el descuento: "))

            # desarrollo del ejercicio 

            if buys <= 100:
            discount1 = 5
            amount_n1 = buys * (discount1 / 100)
            price_f1 = buys - amount_n1
            print("el precio fue de: ", price_f1)
            print("el descuento en pesos es de: ", amount_n1)
        if buys >= 100 and buys <= 200:
            discount2 = 10
            amount_n2 = buys * (discount2 / 100)
            price_f2 = buys - amount_n2
            print("el precio en pesos es de: ", price_f2)
            print("el descuento es de: ", amount_n2)
        else:
            discount3 = 15
            amount_n3 = buys * (discount3 / 100)
            price_f3 = buys - amount_n3
            print("el precio total en pesos fue de: ", price_f3)
            print("el descuento es de: ", amount_n3)
        elif exercises2 == 26:
            # ejercicio 12 año bisiesto

            print("BIENVENIDO")

            february = int(input("ingrese un dia del mes de febrero: "))

        if february <= 28:
            print("el año es normal")
        elif february == 29:
            print("el año es bisiesto")

    selected_workshop = 43:
            exercises3 = int(input("Ingrese el número del ejercicio (26-31): "))

        if exercises3 == 27:
            print("bienvenido al programa, a continuacion se imprimira los multiplos de 3 del 1 al 100")
        for number in range (3, 100, 3):
            print("-", number)
        elif exercises3 == 28:
            print("bienvenido al programa")
        for odd in range(1, 100, 2):
            print("-",odd)
        elif exercises3 == 29:
            print("bienvenido")
            print("numeros pares del 1 al 100")
        for pair in range(2, 100, 2):
            print("-", pair)
        elif exercises3 == 30:
            print("bienvenido")
        for one in[1,2,3]:
            print("-", one)
        elif exercises3 == 31:
            print("bienvenido")
            print("numeros del 10 al 1")
        for number10 in range(10 ,0 , -1):
            print("-", number10) 
        elif exercises3 == 32:
            print("bienvenido")
            print("cuadrados del 1 al 30")
            limit = 30
        for c in range(1, limit):
            square = c * c
        if square <= limit:
            print("-", square)
        elif exercises3 == 33:
            print("bienvenido")
            print("suma de los cuadrados del 1 al 100")
            addition = 0
        for f in range(1, 101):
            operation = f * f
            addition += operation
            print("-", operation)

            print("la suma final da como resultado:", addition)
        elif exercises3 == 34:
            print("bienvenido")
            print("numero factorial del numero ingresado por teclado")
            number3 = int(input("ingrese un numero: "))
            factorial = 1
        for z in range(1, number3 + 1):
            factorial *= z
            print("el factorial es:", factorial)
        elif exercises3 == 35:
            print("bienvenido")
            print("conversion de grados fahrenheit a celcius")

        while True:
            fahrenheit = float(input("ingrese una temperatura para converir a celsius: "))

        if fahrenheit == 999:
            print("el programa ha finalizado.")
        break

            celsius = 5/9 * (fahrenheit - 32)

            print("la temperatura en grados celcius es de:", celsius)
        elif exercises3 == 36:
            print("bienvenido")
            print("numeros primos hasta un numero ingresado por el usuario")
            number45 = int(input("ingrese un numero: "))

        for number32 in range(2, number45 + 1):
            number_primo = True
        for division in range(2, int(number32**0.5) + 1):
        if number32 % division == 0:
            number_primo = False
        break

        if number_primo:
            print(number32)
        elif exercises3 == 37:
            print("bienvenido")
            print("tabla de multiplicacion")

            multiplication = int(input("ingrese un numero del 1 al 10: "))
            print("la tabla de multiplicacion que escogio es:", multiplication)
        if multiplication == 1:
        for q in range(1, 11):
            resultd1 = multiplication * q
            print(multiplication, "x", q, "=", resultd1)

        elif multiplication == 2:
        for w in range(1, 11):
            resultd2 = multiplication * w
            print(multiplication, "x", w, "=", resultd2)

        elif multiplication == 3:
        for e in range(1, 11):
            resultd3 = multiplication * e
            print(multiplication, "x", e, "=", resultd3)

        elif multiplication == 4:
        for r in range(1, 11):
            resultd4 = multiplication * r
            print(multiplication, "x", r, "=", resultd4)

        elif multiplication == 5:
        for t in range(1, 11):
            resultd5 = multiplication * t
            print(multiplication, "x", t, "=", resultd5)

        elif multiplication == 6:
        for y in range(1, 11):
            resultd6 = multiplication * y
            print(multiplication, "x", y, "=", resultd6)

        elif multiplication == 7:
        for u in range(1, 11):
            resultd7 = multiplication * u
            print(multiplication, "x", u, "=", resultd7)

        elif multiplication == 8:
        for i in range(1, 11):
            resultd8 = multiplication * i
            print(multiplication, "x", i, "=", resultd8)

        elif multiplication == 9:
        for p in range(1, 11):
            resultd9 = multiplication * p
            print(multiplication, "x", p, "=", resultd9)

        elif multiplication == 10:
        for d in range(1, 11):
            resultd10 = multiplication * d
            print(multiplication, "x", d, "=", resultd10)

        else:
            print("ingrese un numero del 1 al 10")
        elif exercises3 == 38:
            print("bienvenido")

            addition = 0
            total = 0


        while True:
            number99 = int(input("ingrese un numero al azar: "))
            number98 = int(input("ingrese un numero al azar: "))

        if number99 == 0 or number98 == 0:
            print("finalizo ejecucion")
        break

            total = number98 + number99
            addition += 1
        if addition >= 0:
            average = total / addition
            print("el promedio de la suma de los numeros es:", average)
        else:
            print("ingrese un numero positivo")
        elif exercises3 == 39:
            print("bienvenido")
            number19 = int(input("ingrese un numero: "))
            number16 = int(input("ingrese un numero: "))

        if number19 >= number16:
            print("el primer numero ingresado debeser menor que el primero")
        else:
        for number in range(number19, number16 + 1):
            print("-", number)
        elif exercises3 == 40:
            print("bienvenido")

            number = int(input("ingrese un numero: "))
            number2 = int(input("ingrese un numero: "))


        for y in range(number + 1):
        for t in range(y, number2 + 1):
            print(f"{y}-{t}")

            selected_workshop >= 44 or <= 99:
        print("finaliza sesion")
        break