import json
import model.Cultura

class AreaPlantio:
    
    sensores = {};
    
    def __init__(self, codigo, nome, cultura, area, latitude, longitude):
        self.codigo = codigo;
        self.nome = nome;
        self.cultura = cultura;
        self.area = area;
        self.latitude = latitude;
        self.longitude = longitude
        
    def __str__(self):
        
        sensorAsStr = "";
        for sensor in self.sensores.values():
            sensorAsStr = sensorAsStr + sensor.tipo.nome + " - ";
        
        return f"({self.codigo}) ({self.nome}) ({self.cultura.nome}) ({sensorAsStr})"
    
    def addSensor(self, sensor):
        self.sensores.update({sensor.codigo : sensor});
        
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True)        