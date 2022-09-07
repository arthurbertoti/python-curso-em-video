print("\033[1;34;40mMostrarei se você esta aprovado, reprovado, ou de recuperação de acordo com duas notas suas!\033[m")
x = float(input("\033[1;34;40mDigite aqui a sua primeira nota:\033[m "))
y = float(input("\033[1;34;40mDigite aqui a sua segunda nota:\033[m "))
media = (x + y) / 2
if media < 5:
    print("\033[1;31;40mVocê está de reprovado! A sua média é de {}!\033[m".format(media))
elif 5 <= media < 6.9:
    print("\033[1;33;40mVocê está de recuperação! A sua média foi de {}!\033[m".format(media))
else:
    print("\033[1;32;40mVocê está aprovado! A sua média foi {}!\033[m".format(media))
