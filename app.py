#função para pedir as notas do aluno;
def pedirNotas():
    nota1 = input("Digite a primeira nota: ");
    while True:
        try:
            nota1 = float(nota1);
            # caso o usuário digite uma nota menor que 10 e maior que 0
            if nota1 < 0 or nota1 > 10:
                nota1 = input("A primeira nota deve estar entre 0 e 10: ");
                continue;
            break;
        # caso o usuário digite um valor invalido;
        except ValueError:
            nota1 = input("Digite a primeira nota corretamente: ");
        
    nota2 = input("Digite a segunda nota: ");
    while True:
        try:
            nota2 = float(nota2);
            # caso o usuário digite uma nota menor que 10 e maior que 0
            if nota2 < 0 or nota2 > 10:
                nota2 = input("A segunda nota deve estar entre 0 e 10: ");
                continue;
            break;
        # caso o usuário digite um valor invalido;
        except ValueError:
            nota2 = input("Digite a segunda nota corretamente: "); 

    nota3 = input("Digite a terceira nota: ");
    while True:
        try:
            nota3 = float(nota3);
            # caso o usuário digite uma nota menor que 10 e maior que 0
            if nota3 < 0 or nota3 > 10:
                nota3 = input("A terceira nota deve estar entre 0 e 10");
                continue;
            break;
        # caso o usuário digite um valor invalido;
        except ValueError:
            nota3 = input("Digite a terceira nota corretamente: ");

    nota4 = input("Digite a quarta nota: ");
    while True:
        try:
            nota4 = float(nota4);
            # caso o usuário digite uma nota menor que 10 e maior que 0
            if nota4 < 0 or nota4 > 10:
                nota4 = input("a quarta nota deve estar entre 0 e 10: ");
                continue;
            break;
        # caso o usuário digite um valor invalido;
        except ValueError:
            nota4 = input("Digite a quarta nota corretamente: ");
            
    media = (nota1 + nota2 + nota3 + nota4) / 4;

    return media;



# função que recupera o valor da média calculado e verifica se o aluno foi aprovado ou reprovado;
def restuladoMedia(media):
    # caso o aluno reprove direto (nota menor que 3);
    if(media < 3):
        print(f"O aluno foi reprovado com média: {media}");
    # caso o aluno vá para a final
    elif(media < 7 and media >= 3):
            print(f"A média do aluno foi: {media}")
            notaFinal = (input("Digite a nota final do aluno: ")); 
            while True:
                try:
                    notaFinal = float(notaFinal);
                    # caso o usuário digite uma nota menor que 10 e maior que 0
                    if notaFinal < 0 or notaFinal > 10:
                        notaFinal = input("A nota final deve estar entre 0 e 10: ");
                        continue;
                    break;
                # caso o usuário digite um valor invalido;
                except ValueError:
                    notaFinal = input("Digite a nota final corretamente: ");         
            if(notaFinal >= 5):
                    print(f"O aluno foi aprovado com nota final de: {notaFinal}");
            else:
                    print(f"O aluno foi reprovado com nota final de: {notaFinal}");
    # caso o aluno seja aprovado direto por média;
    else:
        print(f"O aluno foi aprovado com media: {media}");

#MENU PARA CALCULAR AS NOTAS
#criação de uma flag  que irá controlar a entrada e saida do sistema do usuário;
flagMenu = True;
#enquanto a variavel "flagMenu" for True o sistema irá rodar;
while flagMenu == True:
    opcao = input("Digite 1 para calcular uma nota ou 2 para sair do sistema: ");
    match opcao:
        case "1": 
            resultado = pedirNotas()
            restuladoMedia(resultado);
        
        case "2": 
            print("saindo...");
            #muda o valor da variavel "flagMenu" para false para que o sistema saia do loop;
            flagMenu = False;
        #caso padrão caso o usuário não digite nenhum dos casos;
        case _:
            print("Digite um número valido!");
