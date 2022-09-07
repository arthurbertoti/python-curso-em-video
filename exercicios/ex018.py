import math
ang = float(input("Digite o ângulo que você deseja:"))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
cos = math.cos(math.radians(ang))
print("O seno, cosseno, tangente do ângulo {} são respectivamente\n{}\n{}\n{}".format(ang,sen,cos,tan))