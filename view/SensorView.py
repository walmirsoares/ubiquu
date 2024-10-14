from decimal import Decimal
from controller import AreaPlantioController, SensorController
from utils import Util
from utils.Util import exibirMenuArray, exibirMenuDictionary, obterEntradaMenu, obterEntradaNumerica
from view import View

areaPlantioController = AreaPlantioController;

def menuSensor():
        
    escolhaOpcaoMenu = 0;
    
    opcoes = [
        "1 - Inserir Sensores",
        "2 - Exibir Sensores",
        "3 - Voltar ao Menu Principal"
    ];
    
    while True:
    
        exibirMenuArray(opcoes);
        escolhaOpcaoMenu = Util.obterEntradaMenu("Escolha uma das opções:", [1, 2, 3]);
        
        if escolhaOpcaoMenu == 1:
            formInserirSensor();
        elif escolhaOpcaoMenu == 2:
            formExibirSensoresAdicionados();
        elif escolhaOpcaoMenu == 3:
            View.menuPrincipal();

def formInserirSensor():

    # tipo do sensor
    tiposSensor = SensorController.obterTiposSensor();
    Util.exibirMenuDictionary(tiposSensor);
    escolhaTipoSensor = obterEntradaMenu("Escolha o tipo do sensor: ", tiposSensor.keys());
    
    # latitude
    latitude = Decimal(obterEntradaNumerica("Adicione a latitude de localização: "));
    
    # longitude
    longitude = Decimal(obterEntradaNumerica("Adicione a longitude de localização: "));
    
    # área de plantio
    areasPlantio = AreaPlantioController.obterAreasPlantio();
    Util.exibirMenuDictionary(areasPlantio);
    escolhaAreaPlantio = obterEntradaMenu("Escolha uma área de plantio: ", areasPlantio.keys());
    
    # inserindo novo sensor
    SensorController.inserirSensor(
        tipoSensor=tiposSensor.get(escolhaTipoSensor), 
        longitude=longitude, 
        latitude=latitude, 
        areaPlantio=areasPlantio.get(escolhaAreaPlantio)
    );
    
def formExibirSensoresAdicionados():
    exibirMenuDictionary(SensorController.obterSensores());
    input("pressione qualquer tecla para continuar...");