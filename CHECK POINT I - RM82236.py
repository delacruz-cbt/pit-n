emailList = ['jaqueline@fiap.com.br', 'pedro@fiap.com.br', 'clara@fiap.com.br', 'alice@fiap.com.br', 'joao@fiap.com.br', 'miguel@fiap.com.br', 'enzo@fiap.com.br', 'gabriel@fiap.com.br', 'arthur@fiap.com.br', 'heitor@fiap.com.br', 'ana@fiap.com.br', 'helena@fiap.com.br', 'beisola@fiap.com.br', 'luiza@fiap.com.br', 'adalto@fiap.com.br', 'abraao@fiap.com.br', 'abacuque@fiap.com.br', 'erminia@fiap.com.br', 'sheila@fiap.com.br', 'fabiola@fiap.com.br', 'tiazinha@fiap.com.br', 'aecio@fiap.com.br', 'agostinho@fiap.com.br', 'isabel@fiap.com.br', 'alberico@fiap.com.br', 'baltasar@fiap.com.br', 'bernardinho@fiap.com.br', 'beijamin@fiap.com.br', 'custodio@fiap.com.br', 'camila@fiap.com.br', 'cleiton@fiap.com.br']

print ('.-ʕ￫ᴥ￩ʔ  BEM VINDO A VALIDAÇÃO PUG BEAR ʕ￫ᴥ￩ʔ -.')

cont = input('Deseja realizar uma consulta ? S OU N \n'.upper())

for c in cont:

    c =+ 0

    if (cont == 'S'):

        inpt = input('Digite o EMAIL para localizar \n Email: ')

        if inpt in emailList:
            print ('Dado catalogado | Número de consultas realizadas ', c)
        else:
            print ('Dado não encontrado | Número de consultas realizadas ', c)

    elif (cont == 'N'):
        print('.-ʕ￫ᴥ￩ʔ AGRADECEMOS A VISITA ʕ￫ᴥ￩ʔ -.')

    else:
        print('.-ʕ￫ᴥ￩ʔ INFELICIDADE ʕ￫ᴥ￩ʔ -.')

    condc = input('Deseja realizar mais uma consulta ? S OU N \n'.upper())

    while condc == 'S':
                    
        c =+ 0

        if (cont == 'S'):

            inpt = input('Digite o EMAIL para localizar \n Email: ')

            if inpt in emailList:
                print ('Dado catalogado | Número de consultas realizadas ', c)
            else:
                print ('Dado não encontrado | Número de consultas realizadas ', c)

        elif (cont == 'N'):
            print('.-ʕ￫ᴥ￩ʔ AGRADECEMOS A VISITA ʕ￫ᴥ￩ʔ -.')

        else:
            print('.-ʕ￫ᴥ￩ʔ INFELICIDADE ʕ￫ᴥ￩ʔ -.')

        condc = input('Deseja realizar mais uma consulta ? S OU N \n'.upper())
