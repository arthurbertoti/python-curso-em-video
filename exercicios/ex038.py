from time import sleep
print("\033[1;32;40mDigite dois números, e lhe mostrarei qual deles é maior!\033[m")
sleep(2.5)
a = float(input("\033[1;34;40mDigite o primeiro número:\033[m "))
b = float(input("\033[1;34;40mDigite o segundo número:\033[m "))
print("ANALIZANDO...")
sleep(3)
if a > b:
    print("\033[1;32;40mO número {} é maior que o número {}!\033[m".format(a,b))
elif b > a:
    print("\033[1;32;40mO número {} é maior que o número {}!\033[m".format(b,a))
else:
    print("\033[1;32;40mOs números {} e {} tem o mesmo valor!\033[m".format(a,b))