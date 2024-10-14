from decimal import Decimal
from controller import AreaPlantioController, CulturaController
from model.AreaPlantio import AreaPlantio
from utils import Util
from utils.Util import exibirMenuArray, exibirMenuDictionary, obterEntradaMenu, obterEntradaNumerica
from view import View

areaPlantioController = AreaPlantioController;


def menuAreaPlantio():
        
    escolhaOpcaoMenu = 0;
    
    opcoes = [
        "1 - Inserir Áreas de Plantio",
        "2 - Exibir Áreas de Plantio",
        "3 - Menu Principal"
    ];
    
    while True:
    
        exibirMenuArray(opcoes);
        escolhaOpcaoMenu = Util.obterEntradaMenu("Escolha uma das opções:", [1, 2, 3]);
        
        if escolhaOpcaoMenu == 1:
            formInserirAreaPlantio();
        elif escolhaOpcaoMenu == 2:
            formExibirAreasPlantioAdicionadas();
        elif escolhaOpcaoMenu == 3:
            View.menuPrincipal();

def formInserirAreaPlantio():
    
    nomeAreaPlantio = input("Adicione um nome à área de plantio: ");

    culturas = CulturaController.obterCulturas();
    exibirMenuDictionary(culturas);
    escolhaCultura = obterEntradaMenu("Escolha uma das culturas: ", culturas.keys());
    
    area = Decimal(obterEntradaNumerica("Adicione uma área: "));
    latitude = Decimal(obterEntradaNumerica("Adicione a latitude de localização: "));
    longitude = Decimal(obterEntradaNumerica("Adicione a longitude de localização: "));
    
    novaAreaPlantio = AreaPlantio(codigo=0, nome=nomeAreaPlantio, cultura=culturas.get(escolhaCultura), latitude=latitude, longitude=longitude, area=area);
    areaPlantioController.inserirAreaPlantio(novaAreaPlantio);
    
def formExibirAreasPlantioAdicionadas():
    exibirMenuDictionary(areaPlantioController.obterAreasPlantio());
    input("pressione qualquer tecla para continuar...");
