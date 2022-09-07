print("Olá \nMundo!")
n1 = int(input("Digite um número: "))
n2 = float(input("digite outro número: "))
s = n1 + n2
print("A soma desses números é {}".format(s), end=", ")
d = n1 / n2
print(f"E a divisão de {n1} e {n2} é {d:.3f}")

""":.xf= mostrar apenas x casas flutuantes
end= no fim deste linha oq estiver entre "" será lido e então passado para a próxima linha do programa, ao invés de pular uma linha
\n quebra a linha
para considerar apenas a primeira letra como resposta, digite [0]  no final da linha"""