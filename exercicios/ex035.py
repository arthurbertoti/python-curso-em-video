print("Digite três retas para descobrir se elas podem ou não formar um triângulo")
a = float(input("Digite o valor da primeira reta (em metros): "))
b = float(input("Digite o valor da segunda reta (em metros): "))
c = float(input("Digite o valor da terceira reta (em metros): "))
abmenor = (a + b) - c
acmenor = (a + c) - b
bcmenor = (b + c) - a
if abmenor > 0 and acmenor > 0 and bcmenor > 0:
    print("É possível fazer um ângulo com essas retas!")
else:
    print("Não é possível fazer triâgulo com essas retas!")
