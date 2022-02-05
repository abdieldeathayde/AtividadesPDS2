def olamundo():
    print("Olá mundo")
#olamundo()

def mostraNumero():
    numero = int(input('Digite um numero: '))
    print(f"o numero informado foi {numero}")
#mostraNumero()

def soma():
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero'))
    somar = a + b 
    print(f"A soma foi: {somar}")
#soma()

def mostraMedia():
    print('Digite 4 notas: ')
    notas = []
    
    for i in range(4):
        #print('digite a nota ')
        nota = float(input(f'Digite a nota {i+1} : \n'))
        notas.append(nota)
    
    media = sum(notas)
    media = media / 4
    
    print(f'A média é: {media}')
    
#mostraMedia()
#questao 5
def conversorDeUnidade():
    metros = float(input('Digite a distancia em metros'))
    
    centimetro = metros * 100
    
    print(f"{metros} metros em centimetros são: {centimetro} centímetros")
    
#conversorDeUnidade()

#questao 6 
def calculaAreaCirculo():
    raio = float(input('Digite o raio da circunferencia'))
    area = 3.14159 * (raio * raio)
    print(f"A area é: {area}")
#calculaAreaCirculo()

def calculaAreaQuadrado():
    # base = float(input('Digite o tamanho da base do quadrado: \n'))
    # altura = float(input('Digite a altura do quadrado: \n'))
    lado = float(input('Digite o tamanho de um dos lados \n'))
    area = lado * lado
    
    dobroDaArea = area * 2
    
    print(f'A área é: {area} e o dobro dela é: {dobroDaArea}!')
    
#calculaAreaQuadrado()

#questao 8 :
def calcula_salario():
    valorHoraTrabalhada = float(input('Digite o valor da hora trabalhada: \n'))
    numeroHorasTrabalhadasNoMes = int(input('Digite o numero de horas trabalhadas: \n'))
    salario = valorHoraTrabalhada * numeroHorasTrabalhadasNoMes
    
    print(f"O Seu salário é: {salario}")
    
#calcula_salario()

#questao 9:

def conversor_temperatura():
    grausFahrenheit = float(input('Digite a temperatura em graus Fahrenheit: \n'))
conversor_temperatura()