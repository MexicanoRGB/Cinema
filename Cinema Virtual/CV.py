#project: Mivie Theater v1.0
#Author: MM
#v1.0
import os

print('********************************************************')
print('*************Bem vindo Ao Cinema Virtual****************')
print('********************************************************')

a2 = 0
a = 60
listaFilmes = []

while True:

    print('1.Adicionar Filme')
    print('2.Remover Filme')
    print('3.Buscar Filme')
    print('4.Editar Filme')
    print('5.Vender Ingresso')
    print('6.Listar Filmes')
    print('7.Sair')

    Opcao = int(input('Opção: '))
    if Opcao == 1:
        print('Qual Filme deseja adicionar?')
    filme = input().upper().strip()
    listaFilmes.append(filme)
    if Opcao == 2:
        print('Qual Filme deseja Remover?')
    filme = input().upper().strip()
    listaFilmes.remove(filme)
    if Opcao == 3:
        print('Qual Filme deseja Buscar?')
        filme = input().upper().strip()
        for item in listaFilmes:
            if filme == item:
                print('filme:',item)
    if Opcao == 4:
        print('Qual ingresso deseja?')
        filme = input().upper().strip()
    if Opcao == 5:
        print('Qual ingresso deseja vender?')
        qtdIngresso = int(input())
        if qtdIngresso > a2:
            print('Não é possivel')
        else:
            print('Quantos ingressos quer comprar?:')
            a2 = a2 - qtdIngresso
            print('Restam', a2, 'Ingressos')
            
    if Opcao == 6:
        print('Lista dos filmes adicionados:', item)

    if Opcao == 7:
        print('Saindo...')
        break

    input()
    os.system('cls')