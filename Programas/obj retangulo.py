from dataclasses import dataclass

@dataclass
class Retangulo:
    base: int
    altura: int
    
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)
        
ret = Retangulo(5, 7) # retangulo 5x7

print(ret.base)
print(ret.altura)

print(ret.area())
print
(ret.perimetro())