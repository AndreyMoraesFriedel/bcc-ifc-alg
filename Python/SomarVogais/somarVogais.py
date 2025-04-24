# Obter a string solicitada (palavra)
palavra = input("")

# Quebrar a string em letras (letras)
letras = list(palavra)

# Criar a variavel acumuladora da vogal a (qa = 0)
qa = 0
# Similar ao anterior (qe = 0)
qe = 0
# (qi = 0)
qi = 0
# (qo = 0)
qo = 0
# (qu = 0)
qu = 0

# Criar uma variavel de indice para loop (p)
p = 0
# Percorrer cada letra da palavra (indice = p)
while p < len(letras):
   # Se letras[p] é vogal a, incrementa qa
   if letras[p].lower() == "a":
       qa += 1
   # Se letras[p] é vogal e, incrementa qe
   if letras[p].lower() == "e":
       qe+=1
   # Se letras[p] é vogal i, incrementa qi
   if letras[p].lower() == "i":
       qi+=1
   # Se letras[p] é vogal o, incrementa qo
   if letras[p].lower() == "o":
       qo+=1
   # Se letras[p] é vogal u, incrementa qu
   if letras[p].lower() == "u":
       qu+=1
   # incrementa p
   p += 1

# Mostrar as variaveis das vogais acumuladoras
print(f"a={qa}, e={qe}, i={qi}, o={qo}, u={qu}")