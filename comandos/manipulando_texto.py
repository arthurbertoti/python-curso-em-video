"""  FATIAMENTO


uma frase comum, ou apenas uma letra, são uma str para python.
para salvar qualquer dado no computador em um eu uso o =(recebe)o fazer isso com uma string o computador salva cada caractér e espaço da mesma maneira:

EX:  frase = "Curso em Vídeo"


o pc recebe assim:
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í] [d] [e] [o]
Com a seguinte contagem dos caractéres
 0   1   2   3   4   5   6   7   8   9  10  11  12  13






Para manipular os textos, eu posso utilizar []
EX:
print(frase[6])
seria impresso: "e"


print(frase[3:13])
seria impresso: "so em víde"

OBSERVAÇÂO: esta lista imprimi da primeira letra marcada até uma antes do sinal de parar (neste caso, o último ser impresso foi "e"


print(frase[2:12:2])
seria impresso: "roe í"

OBSERVAÇÃO: o último número na lista ("2") mostra em qual o espaço entre os caractéres que serão imprimidos


print(frase[:6])
seria impresso: "Curso "

OBSERVAÇÃO: já que não tem nada no número que era para iniciar, imprimi-se desde o primero caractér


print(frase[4::3])
seria impresso: "omío"

OBSERVAÇÃO: já que não tem final, vai daquele caractér marcado (4) até o último

print(frase[-5])
seria impresso: "V"


print(frase[-5:])
seria impresso "Vídeo"


PARA TER A FRASE AO CONTRÁRIO

print(frase[::-1]
seria impresso: oedíV me osruC





Para ter informar sobre a str eu posso comandos



EX:

len()
Mostra quantos caractéres tem
Como usar: len(frase)
resposta: 14


.count()
conta quantas vezes aparece uma str
Como usar: frase.count("o")
resposta: 2
como usar(2): frase.count("o",0,12)
resposta: 1
explicação: tem como delimitar eu quero que o programa procuta por uma str


.find()
procura na str algo específico
como usar: frase.find("deo")
resposta: 11
explicação: mostra onde começa o que o programa encontrou
ATENÇÂO: se der "-1", isto que tu procurou não tem na str


in
responde com True e False, se tem ou não na str algo
como usar: "Curso" in frase
resposta: True





Para transformar algo em uma/alguma str:



.replace()
muda algo na str em relação às palavras e espaços específicos
como usar: frase.replace("Python", "JAVA")
resposta: Curso em JAVA


.upper()
Torna todas as letras da str maiúsculas
como usar: frase.upper()
resposta: CURSO EM VÍDEO PYTHON


.lower()
torna todas as letras da str minúsculas
como usar: frase.lower()
resposta: curso em vídeo python


.capitalize()
Deixa a primeira letra da str em maiúcula enquanto deixa todas as outras em minúscula
como usar: frase.capitalize()
resposta: Curso em vídeo python


.title()
deixa a primeira letra de cada palavra maúscula enquato todas as outras ficam minúsculas
como usar: frase.title()
resposta: Curso Em Vídeo Python


.strip()
Caso haja espaço inúteis antes ou depois da str, eles serão removidos
como usar: frase.strip()
resposta: Curso em vídeo Python


.rtrip()
Retira os espaços inúteis à direita da str
como usar: frase.rstrip()
resposta: Curso em Vídeo Python


.lstrip()
Retira os espaços inúteis à esquerda da str
como usar: frase.lstrip()
resposta: Curso em Vídeo Python





DIVISÃO


.split()
Divide str em lista, cada palavra recebe uma nova indexação, seus próprios "números"
como usar: frase.split()
resposta:['Curso', 'em', 'Vídeo', 'Python']



JUNÇÃO


"".join()
junta as palavras com o que estiver nas""
Como usar: " ".join(frase)
Resposta: Curso em Vídeo Python


"""