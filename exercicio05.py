print("Academia New Corpore\n")
Esporte = input("Esporte: ").title()
categoria01 = float(input("Natação 01: "))
categoria02 = float(input("Corrida 02: "))
categoria03 = float(input("Ciclismo 03: "))
esporte = (categoria01 + categoria02 + categoria03) 
if esporte < 10:
    categoria = "Mirim"
elif esporte <= 14:
    categoria = "infantil"
elif esporte >14:
    categoria = "juvenil"
print("\nResultado:\n")
print(f"Nome: {nome}")
print(f"Prova o1: {prova01:.1f}".replace(".",","))
print(f"Prova o1: {prova02:.1f}".replace(".",","))
print(f"Prova o1: {prova03:.1f}".replace(".",","))
print(f"Média: {media:.1f}".replace(".",","))
print(f"Situação: {situacao.upper()}")