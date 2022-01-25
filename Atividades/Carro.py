class Carro():
    def __init__(self):
        self.marca = "Volkswagen"
        self.modelo = "Gol"
        self.ano = 2000
        self.valor = 12000
    
CarroMiguel = Carro()
CarroMiguel.marca = "Fiesta"
CarroMiguel.modelo = "EcoSport"
CarroMiguel.ano = 2007
CarroMiguel.valor = 45000

CarroBid = Carro()
CarroBid.marca = "Chevrolet"
CarroBid.modelo = "Onix"
CarroBid.ano = 2009
CarroBid.valor = 23000

CarroHisa = Carro()
CarroHisa.marca = "Citroën"
CarroHisa.modelo = "C3"
CarroHisa.ano = 2004
CarroHisa.valor = 30000


print(CarroMiguel.marca)
print(CarroHisa.marca)
print(CarroBid.marca)