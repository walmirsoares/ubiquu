class TipoSensor:
        
    def __init__(self, codigo, nome, unidadeMedida):
        self.codigo = codigo;
        self.nome = nome;
        self.unidadeMedida = unidadeMedida;
        
    def __str__(self):
        return f"{self.codigo} ({self.unidadeMedida})"