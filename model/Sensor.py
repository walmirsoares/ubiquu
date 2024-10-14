class Sensor:
        
    def __init__(self, codigo, tipo, latitude, longitude, areaPlantio):
        self.codigo = codigo;
        self.tipo = tipo;
        self.latitude = latitude;
        self.longitude = longitude;        
        self.areaPlantio = areaPlantio;
        
    def __str__(self):
        return f"{self.codigo} ({self.tipo.nome})"