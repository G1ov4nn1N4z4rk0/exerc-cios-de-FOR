# -*- coding: utf-8 -*-
"""for1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MQdlCSx9WLyfDPWjod_p_zdVvrxyPFiA
"""

m = [1,3,5,8]

m [0],m [-1] = m[-1], m[0]

print(m)

produtos = {
'camiseta': (25.00, 10),
'calça': (45.00, 5),
'sapato': (60.00, 3),
'boné': (15.00, 8)
}
pmax = float(input("entre com valor maximo"))
for produto in produtos:
  preco = produtos[produto][0]
  if preco <= pmax:
    print(produto,preco)

"""Em uma competição de ginástica, cada atleta recebe votos de
sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica
sendo a média dos votos restantes. Você deve fazer um programa
que receba o nome do ginasta e as notas dos sete jurados
alcançadas pelo atleta em sua apresentação e depois informe a sua
média, conforme a descrição acima informada (retirar o melhor e o
pior salto e depois calcular a média com as notas restantes). As
notas não são informadas em ordem crescente ou decrescente.
"""

ginasta = input("digite o nome do ginasta? ")

for quant in range(7):
  notas = input("digite as notas do ginasta? ")
  print(notas)
  if notas <= 0:
    break
notas.remove(max(notas)),notas.remove(min(notas))


media = sum(notas)/len(notas)
print(f"o {ginasta} recebeu uma media de notas de {media} ")