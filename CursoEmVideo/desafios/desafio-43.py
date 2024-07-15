peso = float(input('digite o seu peso: '))
altura = float(input('digite sua altura:'))
imc = peso // (altura*altura)

if imc <= 18.5:
    print('você esta abaixo do peso')
elif imc <= 25:
    print('você esta no peso ideal')
elif imc <= 30:
    print('você esta no sobrepeso')
elif imc <= 40:
    print('você esta com obesidade')
elif imc > 40:
    print('você esta com obesidade morbida')