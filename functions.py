import json

def print_menu():
    print('MENU PRINCIPAL')
    print('1) Limpar valores')
    print('2) Nulificar valores')
    print('3) Ajuda')
    print('0) Sair')

def help_info():
    print("FUNCIONALIDADES")
    print("1) Todos os valores no seu arquivo 'json' terão seus valores definidos para os parâmetros escolhidos. Caso nenhum parâmetro for definido os dados terão um valor padrão")
    print("2) Todos os valores no seu arquivo 'json' vão ser definidos como 'null'")
    print("3) Informações do programa")
    print("0) Finaliza o programa")


def clear_json(filename):
    try:
        file = open(f'{filename}.json')
        data = json.load(file)
        cleared_data = {}
        for key,value in data.items():
            if type(value) is int:
                cleared_data[key] = 0
            elif type(value) is float:
                cleared_data[key] = 0.0
            elif type(value) is str:
                cleared_data[key] = ""
            elif type(value) is list:
                cleared_data[key] = []
            elif type(value) is dict:
                cleared_data[key] = {}
            
        with open(f'{filename}_cleared.json', 'w') as outfile:
                json.dump(cleared_data, outfile)
    except:
        print('Ocorreu um erro!')


def nullify_json(filename):
    try:
        file = open(f'{filename}.json')
        data = json.load(file)
        null_data = {}
        
        for key in data.keys():
            null_data[key] = None

        with open(f'{filename}_nullified.json', 'w') as outfile:
            json.dump(null_data, outfile)
        
    except Exception as e: 
        print(e)