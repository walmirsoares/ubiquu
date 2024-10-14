from decimal import Decimal
from controller import AreaPlantioController, CulturaController, ExportacaoController
from model.AreaPlantio import AreaPlantio
from utils import Util
from utils.Util import exibirMenuArray
from view import AreaPlantioView, SensorView, SimulacaoView

def menuPrincipal():

    opcoes = [
        "1 - Áreas de Plantio",
        "2 - Sensores",
        "3 - Simulações",
        "4 - Exportar para arquivo",
        "5 - Sair"
    ];
    
    while True:
    
        exibirMenuArray(opcoes);
        escolhaOpcaoMenuPrincipal = Util.obterEntradaMenu("Escolha uma das opções:", [1, 2, 3, 4, 5]);
        
        if escolhaOpcaoMenuPrincipal == 1:
            AreaPlantioView.menuAreaPlantio();

        elif escolhaOpcaoMenuPrincipal == 2:
            SensorView.menuSensor();

        elif escolhaOpcaoMenuPrincipal == 3:
            SimulacaoView.formSimulacao();

        elif escolhaOpcaoMenuPrincipal == 4:
            ExportacaoController.exportarParaArquivo();

        elif escolhaOpcaoMenuPrincipal == 5:
            print("Sair");
            exit(0);