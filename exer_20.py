nome = input("Nome do cliente: ")
categoria = input("Categoria (A, B, C ou D): ")
total = float(input("Total comprado: R$ "))

if categoria == "A":
    final = total - total * 0.08
elif categoria == "B":
    final = total - total * 0.06
elif categoria == "C":
    final = total - total * 0.04
elif categoria == "D":
    final = total - total * 0.02

if categoria == "A" or categoria == "B" or categoria == "C" or categoria == "D":
    print("Cliente: %s" % nome)
    print("Categoria: %s" % categoria)
    print("Total a pagar: R$ %.3f" % final)
else:
    print("Categoria inexistente!");
