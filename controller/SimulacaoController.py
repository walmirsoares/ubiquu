from controller import AreaPlantioController, CulturaController, SensorController
from model.AreaPlantio import AreaPlantio
from model.Sensor import Sensor


def gerarSimulacao():
    
    # culturas
    culturas = CulturaController.obterCulturas();
    
    # criando área de plantio
    areaPlantio = AreaPlantio(
        area=100, 
        codigo=0, 
        nome="teste", 
        cultura=culturas.get(1),
        latitude=100,
        longitude=100
    );
    areaPlantio = AreaPlantioController.inserirAreaPlantio(areaPlantio);
    
    # adicionando sensores à área de plantio
    adicionarSensores(areaPlantio);
    
    input("Pressione qualquer tecla para continuar...");
    

def adicionarSensores(areaPlantio):
        
    # obtendo tipos de sensores
    tiposSensores = SensorController.obterTiposSensor();
        
    for tipoSensor in tiposSensores.values():    
        sensor = SensorController.inserirSensor(
            tipoSensor = tipoSensor,
            latitude=100,
            longitude=100,
            areaPlantio=areaPlantio
        );
        areaPlantio.addSensor(sensor);