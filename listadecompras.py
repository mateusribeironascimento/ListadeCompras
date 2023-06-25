print('-' * 30)
print(f'{"Lista de Compras":^30}')
lista = []
while True:
    print('-' * 30)
    opção = input('Você deseja:'
                  '\n[1] Inserir'
                  '\n[2] Apagar'
                  '\n[3] Listar'
                  '\n[4] Sair   '
                  '\n--> Opção: ')
    print('-' * 30)
    if opção == '1':
        inserir = input('Que item deseja inserir? ')
        lista.append(inserir)
        print(f'{inserir} foi adicionado no carrinho.')
    elif opção == '2':
        try:
            apagar = input('Digite o número do item que deseja apagar: ')
            apagar2 = int(apagar)
            if apagar2 <= len(lista):
                print(f'{lista[apagar2]} foi removido do carrinho.')
                lista.pop(apagar2)
            else:
                print('Esse item não tem na lista.')
        except:
            print('Opção inválida')
            continue
    elif opção == '3':
        print('Carrinho de compras:')
        for i, n in enumerate(lista):
            print(i, ' - ', n)
    elif opção == '4':
        print('Obrigado por usar nosso programa! :D')
        break
    else:
        print('Opção inválida, tente novamente.')
        continue
