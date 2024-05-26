class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

        self.acordado = False

    
    def falar(self):
        if self.acordado:
            print(f" {self.nome} esta falando")
        else:
            print(f" {self.nome} nao pode falar")

    def pararDeFalar(self):
        if self.acordado:
            print(f" {self.nome} parou de falar")
        else:
            print(f" {self.nome} ja nao estava falando")

    def comer(self):
        if self.acordado:
            print(f" {self.nome} esta comendo")
        else:
            print(f" {self.nome} nao pode pode comer")

    def pararDeComer(self):
        if self.acordado:
            print(f" {self.nome} parou de comer")
        else:
            print(f" {self.nome} ja nao estava comendo")

    def dormir(self):
        if self.acordado:
            print(f" {self.nome} esta dormindo")
            self.acordado = False
        else:
            print(f" {self.nome} ja estava dormindo")
        

    def acordar(self):
        if self.acordado:
            print(f" {self.nome} esta acordado")
        else:
            print(f" {self.nome} acordou")
            self.acordado = True


