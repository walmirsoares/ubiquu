import json
from controller import AreaPlantioController


def exportarParaArquivo():
    
    conteudo = AreaPlantioController.obterAreasPlantio();
    
    toExport = [];
    for areaPlantio in conteudo:
        toExport.append(areaPlantio);
    
    
    with open("export.json", "w") as outfile: 
        json.dump(toExport, outfile);
        
    input("pressione qualquer tecla para continuar");