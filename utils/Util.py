from decimal import Decimal
import subprocess
import platform

def exibirMenuArray(array):
    for item in array:
        print(f"{item}");

def exibirMenuDictionary(dictionary):
    for key in dictionary.keys():
        print(f"{key} - {dictionary.get(key)}");

        
def obterEntradaMenu(rotulo, arrayOpcoesValidas):
    
    entradaValida = False;
    
    while not entradaValida:
        
        try:
            entradaMenu = int(input(rotulo));
            for opcao in arrayOpcoesValidas:
                if  entradaMenu == int(opcao):
                    return entradaMenu;            
            print(f"A opção informada [{entradaMenu}] não é válida, por favor, informe uma das opções apresenteadas {arrayOpcoesValidas}");            
        except:
            print(f"A opção informada não é válida, por favor, informe uma das opções apresenteadas {arrayOpcoesValidas}");

def obterEntradaNumerica(rotulo):
    entradaValida = False;    
    while not entradaValida:
        try:
            entrada = Decimal(input(rotulo));
            return entrada;
        except:
            print("O valor informado deve ser um número. Por favor, tente novamente.");
 
def limparTela():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True);

        