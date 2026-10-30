Conceito = int(input("Letra: A - B - C - D - F ")).upper
match Conceito:
    case "A":
        print("Excelente")
    case "B":
        print("Bom")
    case "C":
        print("Rgular")
    case "D":
        print("Ruim")
    case "F":
        print("REPROVADO")
    case _:
        print("Opção Inválida. Escolha entre A - B - C - D - F")
  