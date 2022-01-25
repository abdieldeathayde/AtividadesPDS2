from encodings import utf_8
import json

print("Questionário \n")

acertos = 0

print("Qual a raiz quadrada de 81?\n")
raizQuadrada = input("""A: 5\nB: 3\nC: 7\nD: 9\n
Digite sua resposta:\n""").upper()
#print(type(raizQuadrada))
if raizQuadrada == '9' or raizQuadrada == 'D':
    print("Parabéns")
    acertos += 1
else:
    print("Não foi dessa vez :(")
    
print("Qual o maior osso do corpo humano?\n")
maiorOsso = input("""A: Martelo\nB: Estribo\nC: Fêmur\nD: Tíbia\n
Digite sua resposta:\n""").upper()
if maiorOsso == 'Fêmur' or maiorOsso == 'C':
    print("Parabéns")
    acertos += 1
else:
    print("Não foi dessa vez :(")
    
    
print("Qual 'a resposta para a pergunta fundamental sobre a vida, o universo e tudo mais'?\n")
guiaDoMochileiro = input("""A: 32\nB: 'Paz universal'\nC: 42\nD: 'só sei que nada sei'\n
Digite sua resposta:\n""").upper()
if guiaDoMochileiro == '42' or guiaDoMochileiro == 'C':
    print("Parabéns")
    acertos += 1
else:
    print("Não foi dessa vez :(")
    

print("O que é algoritmo?\n")
algoritmo = input("""A: Instruções\nB: Receito de bolo\nC: passo a passo\nD: Sequência finita de ações executáveis\n
Digite sua resposta:\n""").upper()
if algoritmo == 'Sequência finita de ações executáveis' or algoritmo == 'D':
    print("Parabéns")
    acertos += 1
else:
    print("Não foi dessa vez :(")
    
    
print("Quando a internet foi criada?\n")
internet = input("""A: 2000 A.C.\nB: 1969\nC: 2014\nD: 2050\n
Digite sua resposta:\n""").upper()
if internet == '1969' or internet == 'B':
    print("Parabéns")
    acertos += 1
else:
    print("Não foi dessa vez :(")
    
print(f"Relatório: \n Acertos: {(acertos * 100) / 5}%")
print(f"Erros: {((5 - acertos) * 100) / 5}")
relatorio = f"Relatório: Acertos: {(acertos * 100) / 5}% Erros: {((5 - acertos) * 100) / 5}"
with open('relatorio.txt', 'w', encoding='utf8') as file:
    json.dump(relatorio, file, indent=2, ensure_ascii=False)
