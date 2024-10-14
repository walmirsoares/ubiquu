# Culturas
import model as model

def obterCulturas():
    MILHO   = model.Cultura.Cultura(1, "Milho");
    SOJA    = model.Cultura.Cultura(2, "Soja");
    culturas = {};
    culturas.update({MILHO.codigo:MILHO});
    culturas.update({SOJA.codigo:SOJA});
    return culturas;