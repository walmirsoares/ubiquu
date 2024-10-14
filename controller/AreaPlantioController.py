# Culturas
import model as model

areasPlantio = {};

def inserirAreaPlantio(areaPlantio):
    novoItem = len(areasPlantio) + 1;
    areaPlantio.codigo = novoItem;
    areasPlantio.update({novoItem : areaPlantio});
    return areaPlantio;

def obterAreasPlantio():
    return areasPlantio;