class Televisao(): 
    tamanho = "42'"
    marca = "Philco"
    
tv = Televisao()
print(tv.tamanho)
print(tv.marca)

class Carro():
    def __init__(self):
        
        self.marca = "Gol"
        self.modelo = "horizon"
        self.ano = 2000
        self.valor = 28000
        
carroBid = Carro()
carroBid.marca = "Fiesta"
carroBid.modelo = "Hatch"
carroBid.ano = 2014
carroBid.valor = 33900

CarroPai = Carro()
CarroPai.marca = "Ford"
CarroPai.modelo = "Ecosport"
CarroPai.ano = 2007
CarroPai.valor = 31900

CarroHisa = Carro()
CarroHisa.marca = "Citroën"
CarroHisa.modelo = "C3"
CarroHisa.ano = 2014
CarroHisa.valor = 25500
