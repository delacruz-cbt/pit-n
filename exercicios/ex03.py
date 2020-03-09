user = input("Informe seu nível de acesso \n").upper()
genre = input("Informe seu gênero: M = masculino ou F = feminino \n").upper()
 
if user != ADM or user != USR or user != GUEST:
    print("Olá visitante")
elif genre != M or genre != F:
    input("Informe apenas M ou F \n").upper()
else:
    if user == ADM and genre == F:
        print("Olá administradora")
    elif user == ADM and genre == M:
        print ("Olá administrador")
    elif user == USR and genre == M:
        print ("Olá usuário")
    else:
        print ("Olá usuária")
