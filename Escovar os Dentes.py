eye = None
can_standUp = None
can_brush = None
stand_up = None

open = True
closed = False

# ----------------------------------------------------- #

print("Você ainda não pode escovar os dentes")
print()

# ----------------------------------------------------- #

pergunta = str(input("Você está dormindo? [sim/não]: ")).capitalize()
if pergunta == "Sim":
    acordado = False
elif pergunta == "Nao":
    acordado = True
else:
    print("Resposta Inválida")
    exit()

print()

# ----------------------------------------------------- #

while acordado == False:
    resposta = str(input("Continuar Dormindo? [sim/não]: ")).capitalize()
    if resposta == "Não":
        acordado = True
        print()
        print("Você está acordado agora")
    elif resposta == "Sim":
        continue
    else:
        print("Resposta Inválida")
        continue

print()

# ----------------------------------------------------- #

if acordado == True:
    can_standUp = True
else:
    can_standUp = False

if acordado == True:
    can_brush = True
else:
    can_brush = False

if acordado == True:
    can_standUp = True
else:
    can_standUp = False

# ----------------------------------------------------- #

while can_standUp == True:
    print("Você pode se levantar agora")
    resposta2 = str(input("Deseja se levantar? [sim/não]: ")).capitalize()
    if resposta2 == "Sim":
        stand_up = True
        print()
        print("Vocês está em pé")
        break
    elif resposta2 == "Não":
        print()
        continue
    else:
        print("Resposta Inválida")
        continue

# ----------------------------------------------------- #

if can_brush == True:
    can_brush = "Você pode escovar os dentes agora"
else:
    can_brush = "Você não pode escovar os dentes"

if acordado == True:
    acordado = "Vocês está acordado agora"

print(can_brush)

