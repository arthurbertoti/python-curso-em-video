'''x = str(input("Em que cidade você nasceu? ")).strip()
print(x[:5].upper()=="SANTO")
'''
x = input("Como é o nome da sua cidade? ")
x = x.lower()
x = x.title()
x = x.strip()
print("Santo" in x)
