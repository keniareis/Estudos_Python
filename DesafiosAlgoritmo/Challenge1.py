"""Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias."""

cigarroDia = int(input("Quantos cigarros você fuma por dia?  "))
anosFumado = int(input("Há quantos anos você fuma?  "))

#calcula o total de cigarros fumados
cigarroFumado =  365 * cigarroDia*anosFumado

#Calcula o tempo de vida perdido em minutos
tempo = cigarroFumado * 10

#converto os minutos para dias
diaVida = (tempo)/(60*24)

print(f'Voce já fumou {cigarroFumado:.2f} cigarros e perdeu {diaVida:.2f} dias de vida')
