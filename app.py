def pedirNotas():
    nota1 = input("Digite a primeira nota: ")
    while True:
        try:
            nota1 = float(nota1)
            if nota1 < 0 or nota1 > 10:
                nota1 = input("A primeira nota deve estar entre 0 e 10: ")
                continue
            break
        except ValueError:
            nota1 = input("Digite a primeira nota corretamente: ")
        
    nota2 = input("Digite a segunda nota: ")
    while True:
        try:
            nota2 = float(nota2)
            if nota2 < 0 or nota2 > 10:
                nota2 = input("A segunda nota deve estar entre 0 e 10: ")
                continue
            break
        except ValueError:
            nota2 = input("Digite a segunda nota corretamente: ")  # ← Corrigido!

    nota3 = input("Digite a terceira nota: ")
    while True:
        try:
            nota3 = float(nota3)
            if nota3 < 0 or nota3 > 10:
                nota3 = input("A terceira nota deve estar entre 0 e 10")
                continue
            break
        except ValueError:
            nota3 = input("Digite a terceira nota corretamente: ")

    nota4 = input("Digite a quarta nota: ")
    while True:
        try:
            nota4 = float(nota4)
            if nota4 < 0 or nota4 > 10:
                nota4 = input("a quarta nota deve estar entre 0 e 10: ")
                continue 
            break
        except ValueError:
            nota4 = input("Digite a quarta nota corretamente: ")
            
    media = (nota1 + nota2 + nota3 + nota4) / 4

    return media



#CALCULAR A MÉDIA(FEITO!)
def restuladoMedia(media):
    if(media < 3):
        print(f"O aluno foi reprovado com média: {media}");
    elif(media < 7 and media >= 3):
            notaFinal = (input("Digite a nota final do aluno: ")); 
            while True:
                try:
                    notaFinal = float(notaFinal);
                    if notaFinal < 0 or notaFinal > 10:
                        notaFinal = input("Anota final deve estar entre 0 e 10: ");
                        continue;
                    break;
                except ValueError:
                    notaFinal = input("Digite a nota final corretamente: ");         
            if(notaFinal >= 5):
                    print(f"O aluno foi aprovado pela nota final com nota: {notaFinal}");
            else:
                    print(f"Reprovado com nota final de: {notaFinal}");
    else:
        print(f"O aluno foi aprovado com media: {media}");



#MENU PARA CALCULAR AS NOTAS
flagMenu = True;
while flagMenu == True:
    opcao = input("Digite 1 para calculas uma nota ou 2 para sair do sistema: ");
    match opcao:
        case "1": 
            resultado = pedirNotas()
            restuladoMedia(resultado);
        
        case "2": 
            print("saindo...");
            flagMenu = False;
        case _:
            print("Digite um número valido!");