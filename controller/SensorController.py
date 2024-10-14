from model.Sensor import Sensor
from model.TipoSensor import TipoSensor
from utils import Util

sensores = {};
def inserirSensor(tipoSensor, latitude, longitude, areaPlantio):
    novoSensor = Sensor(codigo=len(sensores) + 1, tipo=tipoSensor, latitude=latitude, longitude=longitude, areaPlantio=areaPlantio);
    sensores.update({novoSensor.codigo : novoSensor});
    return novoSensor;
    
def exibirSensores():
    return sensores;
    
def obterTiposSensor():
    tiposSensor = {};
    tiposSensor.update({1 : TipoSensor(1, "Temperatura", "Graus Celsius")});
    tiposSensor.update({2 : TipoSensor(2, "Umidade do Ar", "Percentual")});
    tiposSensor.update({3 : TipoSensor(3, "Umidade do Solo", "Percentual")});
    tiposSensor.update({4 : TipoSensor(4, "Pressão Atmosférica", "Pascal")});
    tiposSensor.update({5 : TipoSensor(5, "Luminosidade", "Percentual")});
    return tiposSensor;

def obterSensores():
    return sensores;
