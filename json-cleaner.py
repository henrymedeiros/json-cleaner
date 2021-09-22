import functions
while(True):
    try:
        functions.print_menu()
        option = int(input("Opcao: "))
        if(option==1):
            filename = input('Digite o nome do arquivo (apenas o nome, sem extensão): ')
            functions.clear_json(filename)
        elif(option==2):
            filename = input('Digite o nome do arquivo (apenas o nome, sem extensão): ')
            functions.nullify_json(filename)
        elif(option==3):
           functions. help_info()
        elif(option==0):
            break
    except:
        print('ERRO - Digite um valor válido!')

