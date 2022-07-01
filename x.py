while(True):
    nome = input("Digite o nome:")
    if nome == "0":
        break
    nota = int(input("Digite a nota:"))
    if nota < 5:
        nota = 6 
    if nota > 10:
        nota = 10
    f = open('dados.txt', "a")
    f.write(f"{nome};{nota}\n")
    f.close()